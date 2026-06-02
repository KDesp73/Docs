# My Docs

Documentation, notes and tutorials — built with [Astro Starlight](https://starlight.astro.build).

Live site: [docs.kdesp73.org](https://docs.kdesp73.org)

## Setup

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # output in dist/
npm run preview  # preview production build
```

## Project structure

```
src/
├── assets/          # Images referenced from Markdown (optimized by Astro)
├── content/docs/    # Pages and posts (Markdown / MDX)
│   ├── index.mdx    # Home page
│   ├── about.md
│   └── posts/       # Blog posts / notes
├── styles/custom.css
└── content.config.ts
public/
├── assets/          # Static files served at /assets/…
└── CNAME            # Custom domain for GitHub Pages
```

## Adding a post

Create a file in `src/content/docs/posts/`:

```markdown
---
title: My New Post
description: Short summary for SEO and previews.
date: 2026-06-02
tags: [example]
categories: [misc]
---

Your content here…
```

Posts appear automatically in the sidebar under **Posts**.

## Deploy

Pushes to `main` trigger the GitHub Actions workflow in `.github/workflows/deploy.yml`, which builds with Astro and deploys to GitHub Pages.

## License

MIT
