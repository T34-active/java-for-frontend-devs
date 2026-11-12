import type { Theme } from 'vitepress'
import DefaultTheme from 'vitepress/theme'
import TermTip from './components/TermTip.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('Term', TermTip)
    app.component('TermTip', TermTip)
  },
} satisfies Theme
