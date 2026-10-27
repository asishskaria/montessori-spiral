import contextlib
import importlib.util
import io
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('privacy_check', ROOT / 'tools' / 'privacy_check.py')
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


class PrivacyTests(unittest.TestCase):
    def test_empty_generic_content_is_allowed(self):
        self.assertEqual([], gate.findings('content/spiral.json', b'{"areas": []}'))

    def test_binary_and_source_documents_are_rejected(self):
        self.assertTrue(gate.findings('export.pdf', b'%PDF-1.7'))
        self.assertTrue(gate.findings('content.txt', b'one\x00two'))

    def test_common_identifier_patterns_are_rejected(self):
        samples = ['person' + '@' + 'example.invalid', '212' + '-555' + '-1234', 'Example' + ' Academy']
        for text in samples:
            with self.subTest(kind=samples.index(text)):
                self.assertTrue(gate.findings('draft.txt', text.encode()))

    def test_credentials_are_rejected(self):
        self.assertTrue(gate.findings('config.txt', ('ghp_' + 'a' * 36).encode()))

    def test_private_record_path_is_rejected(self):
        self.assertTrue(gate.findings('records/sample.json', b'{}'))

    def test_local_terms_are_case_insensitive(self):
        with patch.dict(os.environ, {'MONTESSORI_PRIVATE_TERMS': 'synthetic-sentinel'}):
            self.assertTrue(gate.findings('draft.txt', b'SYNTHETIC-SENTINEL'))

    def test_indexed_bytes_are_checked_instead_of_working_copy(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(['git', 'init', '--quiet', str(root)], check=True)
            draft = root / 'draft.txt'
            draft.write_text('person' + '@' + 'example.invalid', encoding='utf-8')
            subprocess.run(['git', '-C', str(root), 'add', 'draft.txt'], check=True)
            draft.write_text('A generic educational description.', encoding='utf-8')
            output = io.StringIO()
            with patch.object(gate, 'ROOT', root), contextlib.redirect_stderr(output):
                self.assertTrue(gate.scan())
            self.assertNotIn('example.invalid', output.getvalue())
            subprocess.run(['git', '-C', str(root), 'add', 'draft.txt'], check=True)
            with patch.object(gate, 'ROOT', root):
                self.assertFalse(gate.scan())


if __name__ == '__main__':
    unittest.main()
