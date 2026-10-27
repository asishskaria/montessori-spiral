# Montessori Spiral

An empty framework for Montessori education information supplied by contributors.

No curriculum content, learner records, progress values, or institutional data is included.

## Structure

`content/spiral.json` is the empty content repository. Add only generic educational material explicitly approved for public release. Keep personalized instances in separate private repositories.

## Required setup before any commit

Requires Git and Python 3.10 or newer.

```
python tools/setup_privacy.py
python tools/privacy_check.py --self-test
git add .
python tools/privacy_check.py
git commit
```

The installer enables the tracked pre-commit and pre-push hooks for this checkout. The checker inspects the complete staged snapshot, including filenames. It blocks common personal identifiers, institutional records, private source documents, and secrets. The push hook checks outgoing commit snapshots as well. GitHub Actions repeats the scan on pushes and pull requests.

A hook is local configuration: every new checkout must run setup. Hooks can be bypassed, and automated detection cannot identify every person, institution, or indirect disclosure. Review every diff before committing. Configure repository rules to require the Privacy check before merges once the repository is created.

For additional known names or institution identifiers, set `MONTESSORI_PRIVATE_TERMS` to a semicolon-separated list in your environment. Never store those terms in this public repository. Run the checker with that environment whenever reviewing public changes.

## Contributing

Do not add source exports, learner profiles, observations, assessments, photos, contact details, institution names, classroom identifiers, credentials, or links to private records. Do not use real personal data in tests or examples. See CONTRIBUTING.md for the review process.
