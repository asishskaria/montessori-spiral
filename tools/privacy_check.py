"""Fail-closed public-content gate. Uses Git snapshots, never prints matched data."""
import argparse
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {'.md', '.json', '.py', '.yml', '.yaml', '.html', '.css', '.js', '.ts', '.tsx', '.svg', '.txt'}
SPECIAL = {'.gitignore', '.gitattributes', '.githooks/pre-commit', '.githooks/pre-push'}
RULES = {
    'email address': r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b',
    'phone number': r'(?<!\w)(?:\+\d{1,3}[ .-]?)?(?:\(\d{3}\)|\d{3})[ .-]\d{3}[ .-]\d{4}(?!\w)',
    'government identifier': r'\b\d{3}-\d{2}-\d{4}\b',
    'private record URL': r'transparentclassroom\.com|/children/\d+|/lesson_sets/\d+',
    'personal or institutional field value': r'''["']?(?:student|child|learner|parent|teacher|school|institution|classroom)[ _-]?(?:name|id|address|email|phone)["']?\s*[:=]\s*["']?[^\s"'\[\]{},:][^\r\n,}]*''',
    'birth or residential identifier': r'''["']?(?:date[ _-]?of[ _-]?birth|birth[ _-]?date|dob|home[ _-]?address)["']?\s*[:=]\s*[^\r\n,}]+''',
    'street address': r'\b\d{1,6}\s+(?:[A-Z0-9]+\s+){1,5}(?:Street|Avenue|Road|Lane|Drive|Boulevard|Way)\b',
    'named institution': r'\b(?:[A-Z][a-z]+\s+){1,5}(?:School|Academy|Preschool|Kindergarten|Montessori\sSchool)\b',
    'institution domain': r'https?://[^\s/]+\.(?:edu|k12\.[a-z]{2}\.us)\b',
    'credential': r'(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[A-Z0-9]{16}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)',
    'secret assignment': r'''(?:api[_-]?key|access[_-]?token|password|client[_-]?secret)\s*["']?\s*[:=]\s*["'][A-Za-z0-9_+/.=-]{8,}["']''',
}
PATTERNS = {name: re.compile(pattern, 0 if name == 'named institution' else re.I) for name, pattern in RULES.items()}

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, stderr=subprocess.PIPE)

def findings(path, blob):
    issues = []
    if path not in SPECIAL and Path(path).suffix.lower() not in ALLOWED:
        issues.append('unapproved file type; binary/source documents are not public content')
    if re.search(r'(?:^|/)(?:private|imports|exports|records|roster|observations)(?:/|[._-])', path, re.I):
        issues.append('private-record filename')
    if b'\0' in blob:
        return issues + ['binary content']
    try:
        text = blob.decode('utf-8')
    except UnicodeDecodeError:
        return issues + ['non-UTF-8 content']
    if len(blob) > 1_000_000:
        issues.append('oversized content requires separate review')
    for label, pattern in PATTERNS.items():
        if pattern.search(text) or pattern.search(path):
            issues.append(label)
    for term in filter(None, (s.strip() for s in os.environ.get('MONTESSORI_PRIVATE_TERMS', '').split(';'))):
        if term.casefold() in (path + '\n' + text).casefold():
            issues.append('locally configured private term')
            break
    return issues

def scan(ref=None):
    paths = git('ls-tree', '-r', '--name-only', '-z', ref) if ref else git('ls-files', '--cached', '-z')
    failed = False
    for raw in paths.split(b'\0'):
        if not raw:
            continue
        path = raw.decode('utf-8')
        # git show reads exact indexed/committed bytes, not the working file.
        blob = git('show', f'{ref}:{path}' if ref else f':{path}')
        issues = findings(path, blob)
        if issues:
            failed = True
            # Do not echo paths or matched values: they may themselves identify someone.
            print('BLOCKED file: ' + ', '.join(issues), file=sys.stderr)
    return failed

def self_test():
    cases = [
        ('content.json', ('{"child_' + 'name":"' + 'Example' + '"}').encode()),
        ('lesson.txt', ('person' + '@' + 'example.invalid').encode()),
        ('record.pdf', b'%PDF-1.7'),
        ('notes.txt', ('Example' + ' Academy').encode()),
        ('notes.txt', ('212' + '-555' + '-1234').encode()),
        ('notes.txt', ('https://' + 'www.transparent' + 'classroom.com/s/1').encode()),
        ('notes.txt', ('ghp_' + 'a' * 36).encode()),
    ]
    assert all(findings(path, blob) for path, blob in cases), 'Detection self-test failed'
    assert not findings('content/spiral.json', b'{"areas": []}'), 'Empty content rejected'
    print('Privacy detection self-tests passed.')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--self-test', action='store_true')
    parser.add_argument('--ref')
    parser.add_argument('--pre-push', action='store_true')
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    failed = scan(args.ref)
    if args.pre_push:
        for line in sys.stdin:
            _, local_sha, _, remote_sha = line.split()
            if set(local_sha) == {'0'}:
                continue
            revision = local_sha if set(remote_sha) == {'0'} else f'{remote_sha}..{local_sha}'
            for sha in git('rev-list', revision).decode().splitlines():
                failed = scan(sha) or failed
    if failed:
        print('Remove identifying content before committing or pushing. Do not bypass this check.', file=sys.stderr)
        return 1
    print('Privacy check passed. Manual review is still required for names and indirect identifiers.')
    return 0

if __name__ == '__main__':
    try:
        sys.exit(main())
    except (subprocess.CalledProcessError, UnicodeError, ValueError, AssertionError) as error:
        print('Privacy check could not complete; operation blocked. ' + type(error).__name__, file=sys.stderr)
        sys.exit(1)
