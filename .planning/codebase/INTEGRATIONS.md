# External Integrations

**Analysis Date:** 2026-04-23

## Overview
- Backend acts as an API gateway between the frontend UI and configurable LLM providers.
- Integration model is OpenAI-compatible across local (Ollama/llama.cpp) and cloud (Gemini/OpenAI) services.
- Frontend-to-backend calls are authenticated with a shared Bearer API key.

## Evidence
- LLM backend enum and defaults are defined in `backend/config.py` (`OLLAMA`, `LLAMACPP`, `GEMINI`, `OPENAI`, `OPENAI_COMPATIBLE`).
- Default provider URLs are in `backend/config.py` (`http://localhost:11434`, `https://generativelanguage.googleapis.com/v1beta/openai`, `https://api.openai.com/v1`).
- LLM HTTP integration is implemented via `httpx.AsyncClient` in `backend/main.py`.
- Chat relay endpoint is `POST /chat` in `backend/main.py`.
- Model discovery relay endpoint is `GET /models` in `backend/main.py`.
- Frontend API base and key usage are in `frontend/src/App.svelte` (`VITE_API_URL`, `VITE_API_KEY`, `Authorization: Bearer ...`).
- Backend env template is in `.env.example`; frontend env template is in `frontend/.env.example`.
- CORS settings are applied via `CORSMiddleware` in `backend/main.py` using `frontend_url` from `backend/config.py`.

## Key Findings
- **APIs & External services**
  - LLM providers: Ollama, llama.cpp, Google Gemini, OpenAI, OpenAI-compatible APIs.
  - Integration style: backend sends OpenAI-style `/chat/completions` and `/models` requests with provider-specific URL mapping.
  - Network client: `httpx` async streaming and non-streaming requests in `backend/main.py`.
- **Authentication & identity**
  - App-level auth: custom Bearer token check via `verify_api_key` dependency in `backend/main.py`.
  - Provider auth: optional `LLM_API_KEY` sent as Bearer token for cloud backends in `backend/config.py`.
- **Data storage and state**
  - Backend persistence: not detected (no DB client or ORM usage in backend files).
  - Frontend state/history: local browser storage, described in `frontend/README.md`.
- **Monitoring and observability**
  - Error handling is HTTPException- and stream-message-based in `backend/main.py`.
  - No dedicated logging/metrics/tracing integration detected.
- **CI/CD and hosting**
  - Hosting/deployment platform config not detected in repository.
  - CI automation not detected (`.github/workflows/*` missing).
- **Webhooks/callbacks**
  - Incoming webhooks: not detected.
  - Outgoing callbacks/webhooks: not detected.

## Risks/Gaps
- Broad CORS configuration includes `"*"` in allowed origins in `backend/main.py`, which is permissive for non-local deployments.
- Frontend fallback API key (`changeme`) in `frontend/src/App.svelte` can cause weak default security if copied to production.
- No rate limiting, request quota control, or abuse prevention detected on chat endpoints.
- No integration health probes for upstream LLM providers beyond runtime request failures.
- No centralized secrets management documented beyond local `.env` files.

## Suggested Follow-ups
- Restrict CORS origins to explicit frontend domains in non-dev environments.
- Enforce non-default API key policy and startup validation for production.
- Add structured logging and basic metrics around provider latency/error rate.
- Add optional retries/circuit-breaker logic for upstream LLM calls.
- Add CI checks for integration smoke tests (`/health`, `/models`, auth-required `/chat`).
- Define deployment target and environment-secret strategy (platform secret store).

---
*Integration audit: 2026-04-23*
