# Codebase Structure

Analysis Date: 2026-04-23

## Overview
- Repository is organized as a two-app workspace: Python backend and Svelte frontend.
- Root-level documentation/config drives both apps, with environment values loaded by backend from the repository root.
- Planning artifacts are kept in `.planning/codebase/` and are separate from runtime code.

## Evidence
- Root project documentation and setup instructions: `README.md`.
- Backend service files: `backend/main.py`, `backend/config.py`, `backend/run.py`, `backend/prompts/`.
- Frontend app files: `frontend/src/main.js`, `frontend/src/App.svelte`, `frontend/src/lib/components/`.
- Frontend build/tooling files: `frontend/package.json`, `frontend/vite.config.js`, `frontend/postcss.config.js`.
- Existing mapping docs directory: `.planning/codebase/`.

## Directory Layout
- `backend/`: FastAPI server, settings, startup entry, and prompt text assets.
- `backend/prompts/`: text prompts selected by backend settings.
- `frontend/`: Vite/Svelte application package.
- `frontend/public/`: static public assets.
- `frontend/src/`: frontend runtime code.
- `frontend/src/lib/components/`: reusable Svelte UI components.
- `frontend/src/lib/assets/`: local image/icon assets used by UI components.
- `.planning/codebase/`: architecture, quality, stack, and concern reference docs.

## Key File Locations
- Entry points
  - `backend/run.py`: backend startup command and uvicorn runtime wiring.
  - `backend/main.py`: API application object and endpoint implementations.
  - `frontend/src/main.js`: frontend mount point attaching app to DOM.
- Configuration
  - `backend/config.py`: all backend runtime settings and backend-specific URL/payload behavior.
  - `frontend/.env.example`: frontend required runtime variables template.
  - `frontend/vite.config.js`: frontend build pipeline plugin config.
- Core logic
  - `frontend/src/App.svelte`: chat request lifecycle, streaming decode, chat history persistence, and panel orchestration.
- Documentation
  - `backend/README.md`: backend usage and endpoint contract.
  - `frontend/README.md`: frontend setup, stack, and feature notes.

## Naming Conventions
- Backend modules use lowercase snake_case filenames (`config.py`, `main.py`, `run.py`).
- Frontend component files use PascalCase (`ChatHeader.svelte`, `HistoryPanel.svelte`).
- Frontend entry/style files use lowercase (`main.js`, `app.css`).
- Prompt assets use lowercase text filenames in `backend/prompts/` (`noa.txt`, `assignment_prompt.txt`).

## Where to Add New Code
- New backend endpoint
  - Route handler: `backend/main.py` (current pattern).
  - Shared setting/URL behavior: `backend/config.py`.
- New frontend UI feature
  - Container state/orchestration: `frontend/src/App.svelte`.
  - New reusable visual component: `frontend/src/lib/components/`.
  - New static image/icon: `frontend/src/lib/assets/` or `frontend/public/` depending on usage pattern.
- New prompt variant
  - Add text file to `backend/prompts/` and reference via `SYSTEM_PROMPT` value.

## Key Findings
- Structure is shallow and approachable, with minimal nesting outside dependency folders.
- Frontend follows a hub-and-spoke structure where `App.svelte` is the hub and component files are spokes.
- Backend currently behaves as a compact service with config and route concerns in two primary files.

## Risks and Gaps
- Lack of backend subpackages (for routes/services/schemas) may slow scaling beyond current endpoint set.
- Single large frontend orchestrator file can become a bottleneck for parallel feature work.
- No dedicated frontend API folder means transport concerns are not isolated from UI state.

## Suggested Follow-ups
- Introduce backend subfolders (`routes`, `services`, `schemas`) under `backend/` when adding non-trivial features.
- Add frontend `src/lib/api/` and `src/lib/state/` folders to separate fetch/stream logic from presentation state.
- Add a lightweight contribution note in root `README.md` documenting where new code belongs by concern.
