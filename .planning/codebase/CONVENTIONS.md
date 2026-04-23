# Coding Conventions

**Analysis Date:** 2026-04-23

## Overview
This codebase is a two-part application: a Python FastAPI backend and a Svelte 5 frontend. Conventions are mostly implicit in source files and README guidance rather than enforced by lint/format tooling.

## Naming Patterns
**Files:**
- Svelte component files use PascalCase names, e.g., `frontend/src/lib/components/ChatInput.svelte`.
- Frontend entry/style files use lowercase names, e.g., `frontend/src/main.js`, `frontend/src/app.css`.
- Backend Python modules use snake_case or lowercase names, e.g., `backend/config.py`, `backend/main.py`, `backend/run.py`.

**Functions:**
- JavaScript and Svelte script functions use camelCase, e.g., `sendMessage`, `saveCurrentChat` in `frontend/src/App.svelte`.
- Python functions use snake_case, e.g., `verify_api_key`, `stream_chat_response` in `backend/main.py`.

**Variables:**
- JavaScript constants often use UPPER_SNAKE_CASE for config constants, e.g., `API_URL`, `HISTORY_KEY` in `frontend/src/App.svelte`.
- JavaScript mutable state uses camelCase with Svelte runes, e.g., `showHistoryPanel`, `abortController` in `frontend/src/App.svelte`.
- Python settings fields use snake_case, e.g., `llm_backend_type`, `frontend_url` in `backend/config.py`.

**Types:**
- Python type hints are consistently used for API contracts and config helper methods, e.g., `list[Message]`, `dict[str, str]` in `backend/main.py` and `backend/config.py`.
- Frontend currently uses JavaScript/Svelte without TypeScript types.

## Code Style
**Formatting:**
- Dedicated formatter configuration files are not detected (`.prettierrc`, `eslint.config.*`, `.eslintrc*` not found).
- Formatting appears manually consistent with 2-space indentation in Svelte and 4-space indentation in Python.

**Linting:**
- Frontend lint tooling scripts are not defined in `frontend/package.json`.
- Python lint config files (e.g., `pyproject.toml`, `ruff.toml`, `setup.cfg`) are not detected in project-owned files.

## Import Organization
**Order:**
1. External framework/runtime imports first (`fastapi`, `httpx`, `pydantic` in `backend/main.py`).
2. Standard library imports are present but not strictly grouped ahead of third-party imports (`json`, `typing` in `backend/main.py`).
3. Internal/local imports after external imports (`from config import ...` in `backend/main.py`, local component imports in `frontend/src/App.svelte`).

**Path Aliases:**
- Path alias configs are not detected (`tsconfig.json`/`jsconfig.json` absent).
- Relative imports are used in frontend and backend modules.

## Error Handling
**Patterns:**
- Backend validates auth/header format and raises `HTTPException` with specific status codes in `backend/main.py`.
- Backend wraps network operations with `try/except` and converts failures to API-friendly error payloads or HTTP errors in `backend/main.py`.
- Frontend uses guarded `try/catch` blocks for `localStorage` read/write fallbacks in `frontend/src/App.svelte`.
- Frontend stream parsing silently skips malformed chunks in `frontend/src/App.svelte`.

## Logging
**Framework:**
- No centralized logging library detected.
- Backend uses lightweight console output (`print`) in `backend/run.py`.

**Patterns:**
- Startup information is printed once at boot in `backend/run.py`.
- Runtime request/exception logs rely on default FastAPI/Uvicorn behavior.

## Comments
**When to Comment:**
- Frontend uses section-style comments to segment large component logic blocks in `frontend/src/App.svelte`.
- Backend uses concise docstrings on helper methods and endpoint utilities in `backend/main.py` and `backend/config.py`.

**JSDoc/TSDoc:**
- JSDoc/TSDoc blocks are not used in frontend component scripts.

## Function Design
**Size:**
- Most backend functions are compact and endpoint-focused, while `frontend/src/App.svelte` contains many responsibilities in a single large script block.

**Parameters:**
- Backend prefers explicit typed parameters and dependency-injected settings objects in route handlers (`Depends(get_settings)` in `backend/main.py`).
- Frontend passes handlers and state through component props in child components like `frontend/src/lib/components/ChatInput.svelte`.

**Return Values:**
- Backend returns structured JSON objects or streaming responses (`StreamingResponse`) in `backend/main.py`.
- Frontend handler functions usually mutate component state and return early for guard conditions.

## Module Design
**Exports:**
- Backend exports settings via `get_settings()` and defines cohesive module-level responsibilities in `backend/config.py` and `backend/main.py`.
- Frontend app entry exports mounted app instance from `frontend/src/main.js`.

**Barrel Files:**
- Barrel index files are not used for frontend components; direct component imports are used in `frontend/src/App.svelte`.

## Evidence
- `backend/main.py`
- `backend/config.py`
- `backend/run.py`
- `frontend/src/App.svelte`
- `frontend/src/main.js`
- `frontend/src/lib/components/ChatInput.svelte`
- `frontend/src/lib/components/ChatMessage.svelte`
- `frontend/package.json`
- `frontend/postcss.config.js`
- `frontend/vite.config.js`

## Key Findings
- Use language-native naming conventions already present: camelCase in frontend code, snake_case in Python backend.
- Keep explicit backend type hints and dependency injection patterns for new API endpoints.
- Continue using sectioned comments/docstrings only where code has non-trivial logic.
- Prefer direct relative imports unless alias support is intentionally added across tooling.

## Risks/Gaps
- No enforced lint/format rules increase risk of style drift across contributors.
- Large monolithic frontend script in `frontend/src/App.svelte` increases review and maintenance complexity.
- Mixed import grouping style in Python may become inconsistent as backend files grow.

## Suggested Follow-ups
- Add explicit lint/format configs and scripts for both stacks (e.g., ESLint/Prettier for frontend, Ruff/Black for backend).
- Split `frontend/src/App.svelte` into feature-focused stores/services/components while preserving current UI behavior.
- Introduce a short contributor style guide in `README.md` and link to config files once tooling is added.

---

*Convention analysis: 2026-04-23*
