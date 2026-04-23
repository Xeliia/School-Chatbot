# Technology Stack

**Analysis Date:** 2026-04-23

## Overview
- Monorepo-style project with a Python FastAPI backend and a Svelte/Vite frontend.
- Backend runtime is Python 3.10+ with ASGI serving through Uvicorn.
- Frontend runtime is Node.js 18+ with Vite as dev/build tooling.
- LLM-provider abstraction supports local and cloud OpenAI-compatible endpoints.

## Evidence
- Python dependencies are declared in `requirements.txt` (`fastapi`, `uvicorn`, `httpx`, `pydantic`, `pydantic-settings`, `python-dotenv`, `pyngrok`).
- Frontend dependencies and scripts are declared in `frontend/package.json` (`svelte`, `vite`, Tailwind 4, DaisyUI 5).
- Vite + Svelte integration is configured in `frontend/vite.config.js`.
- PostCSS + Tailwind plugin wiring is configured in `frontend/postcss.config.js`.
- Backend app/runtime entry points are in `backend/main.py` and `backend/run.py`.
- Backend settings model and env loading are in `backend/config.py`.
- Stack prerequisites and run commands are documented in `README.md` and `frontend/README.md`.
- npm lockfile is present at `frontend/package-lock.json`.

## Key Findings
- **Languages**
  - Python: primary backend language (`backend/main.py`, `backend/config.py`, `backend/run.py`).
  - JavaScript + Svelte: primary frontend language (`frontend/src/main.js`, `frontend/src/App.svelte`).
- **Runtime and package managers**
  - Python with pip (`requirements.txt`), no Python lockfile detected.
  - Node.js with npm (`frontend/package.json`, `frontend/package-lock.json`).
- **Frameworks and tooling**
  - Backend: FastAPI + Pydantic Settings + HTTPX + Uvicorn.
  - Frontend: Svelte 5 + Vite 6.
  - Styling: Tailwind CSS 4 + DaisyUI 5 via PostCSS.
- **Configuration model**
  - Backend reads root `.env` through `SettingsConfigDict(env_file=...)` in `backend/config.py`.
  - Frontend consumes `VITE_*` variables in `frontend/src/App.svelte`.
- **Build/dev commands**
  - Frontend uses `npm run dev`, `npm run build`, `npm run preview` (`frontend/package.json`).
  - Backend runs with `python backend/run.py` or `uvicorn` path (`backend/run.py`, `backend/main.py`).

## Risks/Gaps
- No CI pipeline config detected (`.github/workflows/*` not present).
- No containerization/deployment manifests detected (`Dockerfile`, `docker-compose*.yml`, `Procfile`, `vercel.json` absent).
- No test framework dependencies or test files were detected in stack manifests.
- Python dependency versions are range-based without a lockfile, reducing reproducibility.

## Suggested Follow-ups
- Add CI workflow for lint/build/test (GitHub Actions in `.github/workflows/`).
- Introduce Python lockfile strategy (`pip-tools`, Poetry, or equivalent) for reproducible installs.
- Add backend and frontend test harnesses and scripts.
- Add deployment baseline artifacts (container or platform config) aligned to target hosting.

---
*Stack analysis: 2026-04-23*
