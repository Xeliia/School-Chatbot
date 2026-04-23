# Requirements

## Phase 01: Dynamic FAQ Suggestion Buttons

- FAQ-01: Display 3-4 quick-reply FAQ buttons above the message input in the chat UI.
- FAQ-02: Suggestions are contextual to SCHA/Noa knowledge categories (general info, admissions, strands, contact, culture) via a curated pool.
- FAQ-03: Clicking a suggestion auto-sends it as a user message and triggers the assistant response flow.
- FAQ-04: Immediate-turn deduplication: clicked suggestion is excluded from the very next suggestion set.
- FAQ-05: Rotation/randomization: each turn serves a randomized subset from remaining items; previously clicked item may reappear after at least one turn.
- FAQ-06: Backend exposes a FastAPI endpoint returning randomized suggestions with server-side filtering support for last-used IDs.
- FAQ-07: Include automated verification for backend logic and frontend suggestion state logic.
