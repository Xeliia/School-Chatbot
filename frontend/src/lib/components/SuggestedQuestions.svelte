<script>
  import { cubicIn, cubicOut } from 'svelte/easing'
  import { fly } from 'svelte/transition'

  let {
    suggestions = [],
    visible = true,
    loading = false,
    onSelect,
  } = $props()
</script>

{#if suggestions.length > 0}
  {#if visible}
    <div
      class="px-5 pt-3 pb-1 border-t border-nord-5 bg-white overflow-hidden"
      in:fly={{ y: 10, duration: 85, delay: 0, opacity: 1, easing: cubicOut }}
      out:fly={{ y: 10, duration: 75, delay: 0, opacity: 1, easing: cubicIn }}
    >
      <div class="flex flex-wrap gap-2">
        {#each suggestions as suggestion (suggestion.id)}
          <button
            class="rounded-full px-3.5 py-1.5 text-xs md:text-sm border transition-all duration-150
              border-nord-4 bg-nord-6 text-nord-0 hover:bg-nord-5 hover:border-nord-8/40
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
{/if}
