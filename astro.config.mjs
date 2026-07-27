import sitemap from '@astrojs/sitemap';
import starlight from '@astrojs/starlight';
import mermaid from 'astro-mermaid';
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
    site: 'https://docs.lexigram.dev',
    output: 'static',
    integrations: [
        mermaid(),
        sitemap(),
        starlight({
            title: 'Lexigram',
            description: 'The async-first, contract-driven Python application framework built for scale. Enforce boundaries, manage dependencies, and build resilient systems with Lexigram.',
            logo: {
                src: './public/logo.png',
            },
            favicon: 'logo.png',
            head: [
                {
                    tag: 'meta',
                    attrs: { property: 'og:image', content: 'https://docs.lexigram.dev/og-image.png' },
                },
                {
                    tag: 'meta',
                    attrs: { name: 'twitter:image', content: 'https://docs.lexigram.dev/og-image.png' },
                },
                {
                    tag: 'meta',
                    attrs: { name: 'twitter:card', content: 'summary_large_image' },
                },
                {
                    tag: 'meta',
                    attrs: { name: 'keywords', content: 'python, framework, async, dependency injection, contract-first, scalable, web development, lexigram' },
                },
            ],
            tagline: 'A modern, async-first Python web framework',
            social: [
                { icon: 'github', label: 'GitHub', href: 'https://github.com/dbtinoy-/lexigram' },
            ],
            editLink: {
                baseUrl: 'https://github.com/dbtinoy-/lexigram/edit/main/',
            },
            customCss: [
                './src/styles/custom.css',
            ],

            components: {
                Head: './src/components/starlight/Head.astro',
                Header: './src/components/starlight/Header.astro',
                Sidebar: './src/components/starlight/Sidebar.astro',
                PageSidebar: './src/components/starlight/PageSidebar.astro',
                TableOfContents: './src/components/starlight/TableOfContents.astro',
            },
            expressiveCode: {
                themes: ['one-dark-pro', 'github-light'],
                styleOverrides: {
                    frames: {
                        frameBoxShadowCssValue: '0 8px 16px rgba(0, 0, 0, 0.3)',
                    }
                }
            },
            sidebar: [
                // Getting Started
                {
                    label: 'GETTING STARTED',
                    items: [
                        { label: 'Installation', slug: 'getting-started/installation' },
                        { label: 'Your First App', slug: 'getting-started/first-app' },
                        { label: 'Project Structure', slug: 'getting-started/project-structure' },
                        { label: 'Core Concepts', slug: 'getting-started/core-concepts' },
                        { label: 'Configuration', slug: 'getting-started/configuration' },
                    ],
                },

                // Ecosystem
                {
                    label: 'ECOSYSTEM',
                    items: [
                        { label: 'Package Overview', slug: 'ecosystem' },
                        { label: 'Adoption Paths', slug: 'ecosystem/adoption-paths' },
                        { label: 'AI Architecture', slug: 'ecosystem/ai-architecture' },
                        { label: 'Choosing Backends', slug: 'ecosystem/choosing-backends' },
                        { label: 'Compatibility', slug: 'ecosystem/compatibility' },
                    ],
                },

                // Fundamentals
                {
                    label: 'FUNDAMENTALS',
                    items: [
                        { label: 'Application Lifecycle', slug: 'fundamentals/application-lifecycle' },
                        { label: 'Architecture', slug: 'fundamentals/architecture' },
                        { label: 'Providers', slug: 'fundamentals/providers' },
                        { label: 'Dependency Injection', slug: 'fundamentals/dependency-injection' },
                        { label: 'Container Protocols', slug: 'fundamentals/container-protocols' },
                        { label: 'Modules', slug: 'fundamentals/modules' },
                        { label: 'Result Pattern', slug: 'fundamentals/result-pattern' },
                        { label: 'YAML Configuration', slug: 'fundamentals/yaml-configuration' },
                    ],
                },

                // Core Packages
                {
                    label: 'FOUNDATION PACKAGES',
                    items: [
                        { label: 'Overview', slug: 'packages' },
                        {
                            label: 'lexigram-foundation',
                            autogenerate: { directory: 'packages/foundation' },
                        },
                        {
                            label: 'lexigram-web',
                            autogenerate: { directory: 'packages/web' },
                        },
                        {
                            label: 'lexigram-data',
                            autogenerate: { directory: 'packages/data' },
                        },
                        {
                            label: 'lexigram-security',
                            autogenerate: { directory: 'packages/security' },
                        },
                        {
                            label: 'lexigram-events',
                            autogenerate: { directory: 'packages/events' },
                        },
                        {
                            label: 'lexigram-infra',
                            autogenerate: { directory: 'packages/infra' },
                        },
                {
                    label: 'lexigram-utilities',
                    autogenerate: { directory: 'packages/utilities' },
                },
                    ],
                },
                // Experimental
                {
                    label: 'EXPERIMENTAL',
                    items: [
                        {
                            label: 'lexigram-experimental',
                            autogenerate: { directory: 'experimental' },
                        },
                    ],
                },
                // Platform
                {
                    label: 'PLATFORM',
                    items: [
                        {
                            label: 'lexigram-ai',
                            autogenerate: { directory: 'platform' },
                        },
                    ],
                },

                // Guides
                {
                    label: 'GUIDES',
                    items: [
                        { label: 'AI Agents', slug: 'guides/ai-agents' },
                        { label: 'AI Feedback', slug: 'guides/ai-feedback' },
                        { label: 'AI Integration', slug: 'guides/ai-integration' },
                        { label: 'AI MCP', slug: 'guides/ai-mcp' },
                        { label: 'AI Memory', slug: 'guides/ai-memory' },
                        { label: 'AI RAG', slug: 'guides/ai-rag' },
                        { label: 'AI Sessions', slug: 'guides/ai-sessions' },
                        { label: 'AI Skills', slug: 'guides/ai-skills' },
                        { label: 'AI Workers', slug: 'guides/ai-workers' },
                        { label: 'Audit Trail', slug: 'guides/audit-trail' },
                        { label: 'Authentication & Authorization', slug: 'guides/authentication' },
                        { label: 'Background Jobs & Tasks', slug: 'guides/background-jobs' },
                        { label: 'Caching', slug: 'guides/caching' },
                        { label: 'CLI Usage', slug: 'guides/cli' },
                        { label: 'Database & Migrations', slug: 'guides/database' },
                        { label: 'Deployment', slug: 'guides/deployment' },
                        { label: 'Event-Driven Architecture', slug: 'guides/event-driven' },
                        { label: 'Feature Flags', slug: 'guides/feature-flags' },
                        { label: 'File Storage', slug: 'guides/file-storage' },
                        { label: 'Graph Databases', slug: 'guides/graph-databases' },
                        { label: 'GraphQL', slug: 'guides/graphql' },
                        { label: 'HTTP Client', slug: 'guides/http-client' },
                        { label: 'Multi-Tenancy', slug: 'guides/multi-tenancy' },
                        { label: 'NoSQL', slug: 'guides/nosql' },
                        { label: 'Notifications', slug: 'guides/notifications' },
                        { label: 'Observability', slug: 'guides/observability' },
                        { label: 'Queue', slug: 'guides/queue' },
                        { label: 'Real-Time', slug: 'guides/real-time' },
                        { label: 'Resilience', slug: 'guides/resilience' },
                        { label: 'Search', slug: 'guides/search' },
                        { label: 'Testing Strategies', slug: 'guides/testing' },
                        { label: 'Vector Stores', slug: 'guides/vector-stores' },
                        { label: 'Webhooks', slug: 'guides/webhooks' },
                        { label: 'Workflows & Sagas', slug: 'guides/workflows-sagas' },
                    ],
                },

                // Reference
                {
                    label: 'REFERENCE',
                    items: [
                        { label: 'Error Codes', slug: 'reference/errors' },
                        { label: 'CLI Commands', slug: 'reference/cli' },
                        { label: 'Environment Variables', slug: 'reference/env-vars' },
                    ],
                },

                // Audit
                {
                    label: 'AUDIT',
                    items: [
                        { label: 'Overview', slug: 'audit' },
                        { label: 'Integrations', slug: 'audit/integrations' },
                        { label: 'Protocols', slug: 'audit/protocols' },
                        { label: 'Security', slug: 'audit/security' },
                        { label: 'Quality Report', slug: 'audit/quality' },
                        { label: 'Rules', slug: 'audit/rules' },
                        { label: 'Test Report', slug: 'audit/tests' },
                    ],
                },

            ],
        }),
    ],
});