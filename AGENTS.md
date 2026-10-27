# Instructions for AI and human contributors

Read README.md, docs/README.md, docs/DECISIONS.md, and docs/ROADMAP.md before changing the project. The repository is the durable handoff, not a transcript of a conversation.

## Public boundary

- This repository is public. Include only reusable code, generic educational content, and design documentation.
- Never copy child records, institution-specific information, private repository references, local absolute paths, exports, photos, credentials, or personal observations here. This includes issues, pull request bodies, test fixtures, commit messages, and logs.
- Public literature citations are allowed. Personal examples must not be drawn from real records. Prefer empty examples and generated test sentinels.
- When working with a private instance, copy approved generic changes from public to private. Never synchronize private directories back into this repository.
- Enable the hooks with tools/setup_privacy.py. Run tests and the privacy checker before EVERY commit. Never use --no-verify or disable the checker to force a commit.
- Configure any known sensitive terms outside version control through MONTESSORI_PRIVATE_TERMS. Never commit that environment value.
- The checker is heuristic. Review the full diff, filenames, new dependencies, and outgoing history manually as well.

## Product and content

- Curriculum areas are the primary navigation. General principles support the activity explanations.
- Preserve beginner and deeper-reading paths. Do not assume that every reader is a trained educator.
- Cite the source for educational claims. Distinguish source summaries, editorial suggestions, and reviewed presentations.
- Do not invent child ages, progress, lesson dates, developmental scores, compulsory sequences, or mastery predictions.
- Ledger corrections add linked entries; they do not silently rewrite history. A local ledger is not tamper-proof.
- Browser-local notes must never be submitted to GitHub or another service automatically.
- No analytics, remote fonts, or third-party scripts by default. New external services and hosting decisions need an explicit design decision.

## Coordination

Use a codex/ branch for parallel implementation. Keep each task bounded by a feature or file area. Read current git status before edits; preserve another contributor's work. Write a short handoff with changed files, verification, unresolved issues, and the next action. Never claim tests passed or a deployment exists without evidence.

Push small, useful, tested increments as requested by the maintainer. Check remote changes before pushing; never force-push shared history. Use a pull request when branch protection or overlapping work calls for review. Do not message other chats or people without the maintainer's authorization.

Update docs/DECISIONS.md when a settled decision changes, and docs/ROADMAP.md when an item is actually delivered. Mark proposals as proposals. Avoid duplicating this project's plan in an AI-specific hidden file.
