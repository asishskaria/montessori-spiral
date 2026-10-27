# Montessori Spiral

An open project to help parents and educators understand the Montessori curriculum, practice supporting it, and keep a record of their own learning.

Start with the [design and handoff notes](docs/README.md). The design is organized around curriculum areas: Practical Life, Sensorial, Language, Mathematics, and cultural subjects. Simple explanations lead into deeper material, sources, adult side quests, and a learning ledger.

**Current state:** design documents, literature findings, an empty curriculum data file, and tested privacy safeguards. The public app and ledger are planned, not implemented. No learner records, progress values, or institution-specific data are included.

## Structure

`content/spiral.json` remains empty until sourced curriculum entries have been reviewed. `docs/` records product, UX, data, security, and implementation decisions. `tests/` checks the privacy gate and documentation links. Keep personalized instances in separate private repositories.

## Required setup before any commit

Requires Git and Python 3.10 or newer.

```
python tools/setup_privacy.py
python tools/privacy_check.py --self-test
python -m unittest discover -s tests -v
git add .
python tools/privacy_check.py
git commit
```

The installer enables the tracked pre-commit and pre-push hooks for this checkout. The checker inspects the complete staged snapshot, including filenames. It blocks common personal identifiers, institutional records, private source documents, and secrets. The push hook checks outgoing commit snapshots as well. GitHub Actions repeats the scan on pushes and pull requests.

A hook is local configuration: every new checkout must run setup. Hooks can be bypassed, and automated detection cannot identify every person, institution, or indirect disclosure. Review every diff before committing. Configure repository rules to require the Privacy check before merges once the repository is created.

For additional known names or institution identifiers, set `MONTESSORI_PRIVATE_TERMS` to a semicolon-separated list in your environment. Never store those terms in this public repository. Run the checker with that environment whenever reviewing public changes.

## Contributing

Do not add source exports, learner profiles, observations, assessments, photos, contact details, institution names, classroom identifiers, credentials, or links to private records. Do not use real personal data in tests or examples. See CONTRIBUTING.md for the review process.
