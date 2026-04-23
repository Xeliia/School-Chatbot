import test from 'node:test'
import assert from 'node:assert/strict'

import {
  buildExcludeParam,
  clampSuggestionLimit,
  createSuggestionState,
  onSuggestionClicked,
  onSuggestionsRefreshed,
} from './suggestions.js'

test('clicked suggestion is excluded for immediate next fetch only', () => {
  let state = createSuggestionState()
  state = onSuggestionClicked(state, 'general-location')
  assert.equal(buildExcludeParam(state), 'general-location')

  state = onSuggestionsRefreshed(state)
  assert.equal(buildExcludeParam(state), '')
})

test('last clicked id is retained while immediate exclusion clears after refresh', () => {
  let state = createSuggestionState()
  state = onSuggestionClicked(state, 'academic-strands')
  assert.equal(state.lastClickedId, 'academic-strands')

  state = onSuggestionsRefreshed(state)
  assert.equal(state.immediateExcludeId, null)
  assert.equal(state.lastClickedId, 'academic-strands')
})

test('limit is clamped to 3-4', () => {
  assert.equal(clampSuggestionLimit(1), 3)
  assert.equal(clampSuggestionLimit(3), 3)
  assert.equal(clampSuggestionLimit(4), 4)
  assert.equal(clampSuggestionLimit(99), 4)
})
