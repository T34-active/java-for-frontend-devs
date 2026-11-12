<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref } from 'vue'
import { withBase } from 'vitepress'
import { module1ById } from '../glossary/module1'

const props = withDefaults(
  defineProps<{
    /** 术语表 id，见 glossary/module1.ts */
    id: string
    /** 覆盖默认展示文案；不传则用词条 label */
    text?: string
    /**
     * 需要加粗时用组件属性，不要写 **&lt;Term /&gt;**：
     * Markdown 的 ** 包不住 Vue 组件，会原样露出星号。
     */
    strong?: boolean
  }>(),
  { strong: false },
)

const term = computed(() => module1ById[props.id])
const label = computed(() => props.text ?? term.value?.label ?? props.id)
const moreHref = computed(() =>
  term.value?.more ? withBase(term.value.more) : undefined,
)
const open = ref(false)
const root = ref<HTMLElement | null>(null)

function toggle(e: MouseEvent) {
  e.preventDefault()
  e.stopPropagation()
  open.value = !open.value
}

function onDocClick(e: MouseEvent) {
  if (!open.value || !root.value) return
  if (!root.value.contains(e.target as Node)) open.value = false
}

function onKey(e: KeyboardEvent) {
  if (e.key === 'Escape') open.value = false
}

onMounted(() => {
  document.addEventListener('click', onDocClick)
  document.addEventListener('keydown', onKey)
})

onBeforeUnmount(() => {
  document.removeEventListener('click', onDocClick)
  document.removeEventListener('keydown', onKey)
})
</script>

<template>
  <span
    v-if="term"
    ref="root"
    class="term-tip"
    :class="{ 'is-open': open }"
  >
    <button
      type="button"
      class="term-tip__trigger"
      :class="{ 'is-strong': strong }"
      :aria-expanded="open"
      :aria-controls="`term-pop-${id}`"
      @click="toggle"
    >
      {{ label }}
    </button>
    <span
      v-show="open"
      :id="`term-pop-${id}`"
      class="term-tip__pop"
      role="dialog"
      :aria-label="term.label"
    >
      <span class="term-tip__title">{{ term.label }}</span>
      <span class="term-tip__def">{{ term.def }}</span>
      <a
        v-if="moreHref"
        class="term-tip__more"
        :href="moreHref"
        @click.stop
      >
        查看相关章节
      </a>
    </span>
  </span>
  <span v-else class="term-tip term-tip--missing" :title="`未知术语 id: ${id}`">
    {{ label }}
  </span>
</template>
