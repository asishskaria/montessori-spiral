# Experience design

Status: proposed interaction design. No screens described here are implemented yet.

## Main navigation

| Destination | Reader's question | First-release behavior |
| --- | --- | --- |
| Curriculum | What are the areas and how do activities connect? | Browse area cards, strands, activities, and source-backed connections. |
| Side quests | How can I understand and support this work? | Short adult learning tasks connected to an area or activity. |
| My ledger | What have I learned, questioned, or revised? | Dated local entries, filters, linked corrections, export and restore. |
| Sources | Where does this explanation come from? | References, source type, review status, and content version. |

The homepage leads with the curriculum areas. Use a readable list or card view as the default; an interactive map is an additional view, with keyboard-accessible equivalents.

## Progressive depth

Every activity page offers three levels without requiring an account:

1. Start here: plain-language purpose, key terms, and the activity's place in its area.
2. Understand more: material, adult preparation, what to notice, related work, and why the connections matter.
3. Examine the evidence: citations, source-specific sequence information, uncertainties, review status, and correction history.

Do not hide important safety or scope information behind the deeper-reading control. Home extensions must be labeled separately from formal classroom presentations.

## Activity page

Header: title, area, strand, developmental context, content status, source version.

Body: purpose; description; what a prepared adult should understand; relevant materials; possible connections; source references. A detailed presentation is shown only when appropriately sourced and reviewed. Avoid invented instruction steps to fill an empty card.

Actions: save a learning note; start a related side quest; ask a question; propose a correction. Each action should preserve the activity ID and content version in the resulting ledger event.

## Adult side quests

Each quest follows learn -> try or observe -> explain -> reflect. The quest belongs to the adult, not the child. Completion means the adult recorded the task; it does not measure teaching skill or child mastery.

Example task shapes, authored for this product rather than quoted from a curriculum:

- Read an activity's purpose, then explain it in your own words.
- Compare two related activities and identify what changes in their demands.
- Review an accessible setup and identify one change that could support independence.
- Compare an earlier reflection with a source and record what you would now explain differently.

Quests have a duration estimate, learning purpose, source links, reflection prompt, and accessible alternatives. No streak penalties, child rankings, or competitive scoreboards.

## Learning ledger

A chronological list shows entry type, linked area/activity, date, and content version. Available entry types: learning note, question, reflection, quest completion, proposed correction, and follow-up.

An entry detail view shows its text, references, and any linked later entries. Corrections point back to the entry or content revision they address. Display both the original and the new understanding; make the latest view easy to follow.

Users can filter by area, type, date, and unresolved question. Drafts are editable before saving. Saved entries use linked follow-ups rather than silent edits. This is an ordinary versioned journal, not a cryptographically immutable ledger. Users must still be able to delete their local data deliberately.

Export explains that the file may contain personal notes and stays under the user's control. Restore validates the schema, displays a preview, and handles duplicate IDs without duplicating entries. Nothing is transmitted automatically.

## Corrections and shared knowledge

In the first release, a proposed correction is a local ledger event. Sharing it requires a separate explicit action and a sanitized preview. Do not copy a whole ledger into a public issue or pull request.

A later community feature can distinguish submitted, under review, accepted, and declined proposals. Only a reviewed change should alter the published curriculum. Preserve the source, reason, and revision links.

## Accessibility and visual direction

Calm, readable, curriculum-focused. Distinct colors may help identify areas but must not carry meaning alone. Support narrow screens, keyboard navigation, visible focus, reduced motion, and screen-reader labels. Keep source links readable and available without hover. Avoid decorative child profiles or invented learner examples in the public app.
