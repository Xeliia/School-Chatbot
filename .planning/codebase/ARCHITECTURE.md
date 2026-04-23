# Architecture

Analysis Date: 2026-04-23

## Overview
- Overall style: split frontend-backend application with a thin API proxy backend and a UI-centric frontend.
- Backend pattern: FastAPI edge service that validates API key, normalizes settings, then forwards requests to OpenAI-compatible LLM endpoints.
- Frontend pattern: single smart container component controlling chat/session state and delegating rendering to leaf components.

## Evidence
- Backend app bootstrap and route registration live in `backend/main.py`.
- Backend runtime/config composition is centralized in `backend/config.py` and launched via `backend/run.py`.
- Frontend entry mount is in `frontend/src/main.js`.
- Primary UI orchestration, network calls, and local history management are in `frontend/src/App.svelte`.
- UI decomposition into reusable leaf components is under `frontend/src/lib/components/`.
- Styling/theme system is centralized in `frontend/src/app.css` with Tailwind+DaisyUI integration from `frontend/postcss.config.js`.

## Layers
- Presentation Layer
  - Purpose: render chat UI and panel widgets.
  - Location: `frontend/src/lib/components/`.
  - Contains: stateless/presentational Svelte components (`ChatMessage`, `ChatInput`, `HistoryPanel`, cards/modals).
  - Depends on: props/events from `frontend/src/App.svelte`.
- Frontend Application Layer
  - Purpose: own client state, request lifecycle, stream parsing, and persistence.
  - Location: `frontend/src/App.svelte`.
  - Contains: message state, fetch orchestration, abort logic, localStorage history, panel state.
  - Depends on: backend `/chat` endpoint and browser APIs.
- API Layer
  - Purpose: authenticate requests, expose stable endpoints, stream SSE to client.
  - Location: `backend/main.py`.
  - Contains: `/health`, `/chat`, `/models`, `/config` handlers and API-key dependency.
  - Depends on: settings provider in `backend/config.py` and outbound HTTP via httpx.
- Configuration Layer
  - Purpose: resolve environment defaults and backend-specific request shape.
  - Location: `backend/config.py`.
  - Contains: backend enum, default URL/model maps, payload/header builders, system prompt resolver.

## Data Flow
- Chat streaming path
  1. User submits message in `frontend/src/lib/components/ChatInput.svelte`; handler invokes `sendMessage` in `frontend/src/App.svelte`.
  2. `frontend/src/App.svelte` posts to `POST /chat` with bearer token and stream mode.
  3. `backend/main.py` verifies authorization and relays payload to configured LLM endpoint.
  4. Backend yields SSE chunks (`data: {content}`) back to client.
  5. Frontend incrementally parses chunks into paragraph bubbles and updates message list.
- Config resolution path
  1. Backend starts from `backend/run.py`.
  2. `backend/config.py` loads root `.env` through Pydantic settings with backend-type defaults.
  3. `backend/main.py` consumes resolved settings for CORS, endpoint URLs, headers, and prompt text.

## Key Findings
- Architecture is intentionally simple and fast to iterate: one backend module and one frontend orchestration module.
- Frontend business logic is centralized in one file (`frontend/src/App.svelte`), reducing indirection but increasing local complexity.
- Backend integration logic is centralized in settings helpers (`backend/config.py`), making backend switching straightforward.
- Component boundaries in `frontend/src/lib/components/` are mostly presentational and controlled from parent callbacks.

## Risks and Gaps
- CORS currently allows wildcard plus configured origin in `backend/main.py`, which weakens origin restrictions.
- `frontend/src/App.svelte` mixes transport parsing, UX behavior, persistence, and panel state in one unit; change risk grows with features.
- Backend has minimal file-level modularization (`backend/main.py` and `backend/config.py`), limiting separation for future growth.
- No dedicated shared API client module on the frontend; request construction is embedded in `frontend/src/App.svelte`.

## Suggested Follow-ups
- Extract frontend network and stream parsing logic from `frontend/src/App.svelte` into `frontend/src/lib/` services.
- Split backend route handlers and LLM client orchestration into separate modules under `backend/`.
- Tighten CORS policy in `backend/main.py` to explicit allowed origins per environment.
- Add architecture decision notes in `.planning/codebase/` for backend-selection strategy and streaming contract.
