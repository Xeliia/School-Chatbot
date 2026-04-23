export function clampSuggestionLimit(limit = 4) {
  const numeric = Number(limit)
  if (!Number.isFinite(numeric)) return 4
  return Math.max(3, Math.min(4, Math.trunc(numeric)))
}

export function createSuggestionState() {
  return {
    immediateExcludeId: null,
    lastClickedId: null,
  }
}

export function buildExcludeParam(state) {
  const id = state?.immediateExcludeId
  return id ? String(id) : ''
}

export function onSuggestionClicked(state, suggestionId) {
  return {
    immediateExcludeId: suggestionId,
    lastClickedId: suggestionId,
  }
}

export function onSuggestionsRefreshed(state) {
  return {
    ...state,
    immediateExcludeId: null,
  }
}
