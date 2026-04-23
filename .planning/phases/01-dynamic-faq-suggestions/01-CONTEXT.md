# Phase 01: Dynamic FAQ Suggestion Buttons - Context

Gathered: 2026-04-23
Status: Ready for planning
Source: User technical requirement prompt

<domain>
## Phase Boundary

Implement a quick-reply/suggested-question feature in the existing chat experience.
Scope includes backend endpoint support and frontend state/UI wiring for randomized suggestions with immediate-turn deduplication.
</domain>

<decisions>
## Decisions

### Locked Decisions
- D-01: Render quick-reply buttons above the message input field in the current messenger-like chat UI.
- D-02: Show only 3-4 suggestion buttons at a time from a larger FAQ pool (~15-20).
- D-03: Suggestions are SCHA-contextual (general info, admissions, strands, contact, culture).
- D-04: On click, the selected suggestion is sent automatically as the user message.
- D-05: Dedup rule: selected suggestion must not appear in the immediate next returned set.
- D-06: Rotation rule: next sets are randomized from remaining pool; previously clicked item can reappear after at least one turn.
- D-07: Backend should provide randomized suggestions while supporting exclusion of last used question ID(s).

### Claude's Discretion
- Define exact endpoint shape for suggestion retrieval while matching existing FastAPI style.
- Choose internal frontend state shape and helper functions for turn-based exclusion.
- Add lightweight tests using currently available test tooling in repo.
</decisions>

<canonical_refs>
## Canonical References

Downstream agents MUST read these before implementing.

### Existing app behavior
- README.md - setup, env contract, frontend/backend interaction expectations.
- backend/main.py - chat endpoint, auth dependency pattern, FastAPI structure.
- backend/config.py - API key and backend configuration model.
- frontend/src/App.svelte - current chat send flow and where quick replies should integrate.

### Codebase standards and constraints
- .planning/codebase/ARCHITECTURE.md
- .planning/codebase/CONVENTIONS.md
- .planning/codebase/TESTING.md
</canonical_refs>

<specifics>
## Specific Ideas

Seed pool should include prompts like:
- Where is SCHA located?
- What are the SHS strands available?
- How do I enroll online?
- What are the core values of the school?
- What documents do I need for SHS admission?
- What are the registrar's office hours?

Implementation can extend to 15-20 total suggestions while preserving category spread.
</specifics>

<deferred>
## Deferred Ideas

- AI-generated dynamic FAQ authoring from embeddings/vector search.
- Per-user persistent suggestion personalization across sessions.
</deferred>
