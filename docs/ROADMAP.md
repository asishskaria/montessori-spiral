# Implementation roadmap

Ship small, tested increments. A checkbox means verified delivery, not an intention.

- [x] Public/private repository separation established at project level.
- [x] Public privacy scanner, pre-commit hook, and pre-push hook.
- [x] Initial CI privacy check passed.
- [x] Product, curriculum, literature, UX, data, and AI handoff notes.
- [ ] Responsive public app shell and curriculum-area navigation.
- [ ] One source-reviewed activity slice, with sources and beginner/deeper-reading views.
- [ ] Connected activity view with relationship types and accessible list navigation.
- [ ] Browser-local learning ledger with schema validation.
- [ ] Dated notes, questions, reflections, and linked corrections.
- [ ] Ledger export, validated restore, duplicate handling, and deliberate local deletion.
- [ ] Adult side quests with optional ledger reflections.
- [ ] Community correction draft and explicit sanitized sharing preview.
- [ ] Public hosting, deployment tests, and verified public URL.
- [ ] Additional developmental levels and reviewed curriculum coverage.

## First UI increment

Use HTML, CSS, and JavaScript initially; choose a framework only when its benefits justify the complexity. Keep curriculum data separate from UI code. A native mobile app is not required for the first responsive web experience.

Completion criteria: a reader can browse the proposed areas, understand what is and is not available, open sources, and switch reading depth with keyboard or touch. Empty content is honestly labeled. No synthetic learner profile or invented progress is shown.

## Ledger increment

Tests must cover persistence across reload, corrections preserving originals, invalid references, export/restore round trips, duplicate IDs, malformed and oversized imports, storage failure, and HTML/script text remaining inert. Test deletion with a deliberate confirmation and verify that it removes only the selected local data.

## Content increment

Validate stable IDs, referential integrity, HTTPS source links, review status, content versions, and explicit relationship types. A trained reviewer should check detailed presentations before they are described as educator-reviewed.

## Release and coordination

Before each public commit: run unit tests, run privacy self-tests, stage only intended files, run the staged privacy check, and inspect the diff. Never suppress a failing check. Before pushing, inspect outgoing commits and remote changes.

For each handoff record scope, files changed, checks performed, known limitations, and next task. Avoid assigning two contributors simultaneous ownership of the same module. A repository note is not authorization to contact other people or chats.

For deployment, verify that the public build contains only generic content and no local ledger values. Verify base-path routing if hosted under a repository path. Private-instance deployment remains a separate security decision.
