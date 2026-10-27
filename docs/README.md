# Montessori Spiral design and handoff

Status: first design increment, 2026-10-26. These documents describe the intended app. They do not assert that it has been built or hosted.

Read in this order:

1. [Product scope](PRODUCT.md): people, purpose, and curriculum structure.
2. [Literature findings](LITERATURE.md): what the consulted sources support and where interpretation begins.
3. [Experience design](EXPERIENCE.md): navigation, reader depth, side quests, and the ledger.
4. [Data and privacy](DATA-AND-PRIVACY.md): records, corrections, and public/private boundaries.
5. [Decisions](DECISIONS.md): settled choices and open questions.
6. [Implementation roadmap](ROADMAP.md): small increments, tests, and completion criteria.

Contributor instructions are in [AGENTS.md](../AGENTS.md). Current curriculum data is deliberately empty in [spiral.json](../content/spiral.json). Source references and original summaries are recorded here; full third-party books, paid albums, and source documents are not copied into the repository.

## Current handoff

- Implemented: Git privacy hooks, a privacy scanner, CI checks, and design documentation.
- Not implemented: public UI, ledger persistence, curriculum graph, side quests, user accounts, community corrections, or hosting.
- Next concrete task: a responsive curriculum explorer with clearly empty data states, source links, and beginner/deeper-reading views. Build one small, source-reviewed area before expanding coverage.
- A personalized instance is a separate deployment and security boundary. No instance identity or private record is needed to work on this public project.
