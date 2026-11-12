import { defineConfig } from 'vitepress'

/**
 * VitePress 站点配置。
 * srcDir 指向仓库根目录，直接复用各模块下已有的 .md。
 */
export default defineConfig({
  title: 'Java For Frontend Devs',
  description: '前端工程师转 Java 全栈的系统化学习手册',
  lang: 'zh-CN',
  // GitHub Pages 项目站路径：https://t34-active.github.io/java-for-frontend-devs/
  base: '/java-for-frontend-devs/',
  cleanUrls: true,
  // 文档就在仓库根下的各模块目录里
  srcDir: '.',
  srcExclude: [
    '**/node_modules/**',
    '**/target/**',
    // 根目录 README 留给 GitHub；站点首页用 index.md
    'README.md',
  ],
  // 文档里会链到旁边的 Java 源码目录（给 IDE 用），站点内无需当成页面
  ignoreDeadLinks: true,
  lastUpdated: true,
  themeConfig: {
    logo: undefined,
    siteTitle: 'Java For Frontend Devs',
    nav: [
      { text: '首页', link: '/' },
      { text: '模块一 · 核心', link: '/01-Java-Core-And-OOP/' },
      { text: '模块二 · 并发', link: '/02-Concurrency-And-JVM/' },
      { text: '模块三 · Spring', link: '/03-SpringBoot-Ecosystem/' },
      { text: '模块四 · 数据库', link: '/04-Database-And-ORM/' },
      { text: '模块五 · 中间件', link: '/05-Middleware-And-Architecture/' },
    ],
    sidebar: {
      '/01-Java-Core-And-OOP/': [
        {
          text: '模块一 · Java 核心与 OOP',
          collapsed: false,
          items: [
            { text: '模块导读', link: '/01-Java-Core-And-OOP/' },
            { text: '0. 安装 JDK 与工具链', link: '/01-Java-Core-And-OOP/00-install-jdk-and-toolchain' },
            { text: '1. 强类型与基础语法', link: '/01-Java-Core-And-OOP/01-strong-typing-and-basics' },
            { text: '2. 面向对象深挖', link: '/01-Java-Core-And-OOP/02-oop-deep-dive' },
            { text: '3. 集合框架', link: '/01-Java-Core-And-OOP/03-collections-framework' },
            { text: '4. 泛型', link: '/01-Java-Core-And-OOP/04-generics' },
            { text: '5. Stream 与 Lambda', link: '/01-Java-Core-And-OOP/05-stream-and-lambda' },
            { text: '6. 异常体系', link: '/01-Java-Core-And-OOP/06-exception-system' },
          ],
        },
      ],
      '/02-Concurrency-And-JVM/': [
        {
          text: '模块二 · 并发与 JVM',
          items: [
            { text: '模块导读（待生成）', link: '/02-Concurrency-And-JVM/' },
          ],
        },
      ],
      '/03-SpringBoot-Ecosystem/': [
        {
          text: '模块三 · Spring Boot',
          items: [
            { text: '模块导读（待生成）', link: '/03-SpringBoot-Ecosystem/' },
          ],
        },
      ],
      '/04-Database-And-ORM/': [
        {
          text: '模块四 · 数据库与 ORM',
          items: [
            { text: '模块导读（待生成）', link: '/04-Database-And-ORM/' },
          ],
        },
      ],
      '/05-Middleware-And-Architecture/': [
        {
          text: '模块五 · 中间件与架构',
          items: [
            { text: '模块导读（待生成）', link: '/05-Middleware-And-Architecture/' },
          ],
        },
      ],
      '/': [
        {
          text: '学习路线',
          items: [
            { text: '全书总览', link: '/' },
            { text: '0. 安装 JDK 与工具链', link: '/01-Java-Core-And-OOP/00-install-jdk-and-toolchain' },
            { text: '模块一 · Java 核心与 OOP', link: '/01-Java-Core-And-OOP/' },
            { text: '模块二 · 并发与 JVM', link: '/02-Concurrency-And-JVM/' },
            { text: '模块三 · Spring Boot', link: '/03-SpringBoot-Ecosystem/' },
            { text: '模块四 · 数据库与 ORM', link: '/04-Database-And-ORM/' },
            { text: '模块五 · 中间件与架构', link: '/05-Middleware-And-Architecture/' },
          ],
        },
      ],
    },
    search: {
      provider: 'local',
      options: {
        translations: {
          button: { buttonText: '搜索', buttonAriaLabel: '搜索文档' },
          modal: {
            noResultsText: '没有结果',
            resetButtonTitle: '清除',
            footer: { selectText: '选择', navigateText: '切换', closeText: '关闭' },
          },
        },
      },
    },
    outline: {
      label: '本页目录',
      level: [2, 3],
    },
    docFooter: {
      prev: '上一篇',
      next: '下一篇',
    },
    lastUpdated: {
      text: '最后更新',
    },
    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '菜单',
    darkModeSwitchLabel: '主题',
    socialLinks: [
      { icon: 'github', link: 'https://github.com/T34-active/java-for-frontend-devs' },
    ],
  },
})
