<script>
  let {
    suggestions = [],
    loading = false,
    onSelect,
  } = $props()
</script>

{#if suggestions.length > 0}
  <div class="px-5 pt-3 pb-1 border-t border-nord-5 bg-white">
    <div class="flex flex-wrap gap-2">
      {#each suggestions as suggestion (suggestion.id)}
        <button
          class="rounded-full px-3.5 py-1.5 text-xs md:text-sm border transition-all duration-200
            border-nord-4 bg-nord-6 text-nord-1 hover:border-nord-8/40 hover:bg-nord-5
            disabled:opacity-50 disabled:cursor-not-allowed"
          onclick={() => onSelect?.(suggestion)}
          disabled={loading}
        >
          {suggestion.question}
        </button>
      {/each}
    </div>
  </div>
{/if}
