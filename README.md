<p align="center">
  <a href="https://zvirox.in">
    <img src="assets/images/zvirox-logo.png" alt="Zvirox Logo" width="280" height="104">
  </a>
</p>

<h1 align="center">Zvirox Web (<code>zvirox-tech-dev</code>)</h1>

<p align="center">
  <b>Official Website &amp; Technical Documentation Hub for <a href="https://zvirox.in">zvirox.in</a></b>
  <br>
  <i>Cyber Defender · Privacy-First · Linux &amp; Android TV Open-Source Software</i>
</p>

<p align="center">
  <a href="https://zvirox.in"><img src="https://img.shields.io/website?url=https%3A%2F%2Fzvirox.in&label=zvirox.in&style=flat-square&labelColor=111213" alt="Site Status"></a>
  <a href="https://zvirox.in/downloads/"><img src="https://img.shields.io/badge/downloads-7%20apps-3355FF?style=flat-square&labelColor=111213" alt="Downloads Hub"></a>
  <a href="https://github.com/zvirox"><img src="https://img.shields.io/badge/maintainer-@zvirox-3355FF?style=flat-square&labelColor=111213" alt="Maintainer"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-10b981?style=flat-square&labelColor=111213" alt="License: MIT"></a>
</p>

> The official website, release directory, and engineering documentation hub for **[Zvirox](https://zvirox.in)** — showcasing 7 open-source Linux and Android TV tools built by **Prakashpuri Gauswami** (`@zvirox`).

---

## 🚀 Overview

`zvirox-tech-dev` powers [zvirox.in](https://zvirox.in), presenting seven local-first open-source applications, a live categorized [Downloads Directory](https://zvirox.in/downloads/) (updated daily at 06:00 AM IST), and systems engineering guides:

| App | Category | Current Release | Pages | License |
| :--- | :--- | :--- | :--- | :--- |
| **Starship Control** (`sc`) | Linux Desktop | `v0.1.0-beta.1` (Beta) | [Project](https://zvirox.in/projects/sc/) · [Downloads](https://zvirox.in/downloads/sc/) | Apache-2.0 |
| **Screen Studio Pro** (`ssp`) | Linux Desktop | `v0.1.0-beta.1` (Beta) | [Project](https://zvirox.in/projects/ssp/) · [Downloads](https://zvirox.in/downloads/ssp/) | MIT |
| **Easy Edits Pro** (`eep`) | Linux Desktop | `v0.1.3-beta.3` (Beta) | [Project](https://zvirox.in/projects/eep/) · [Downloads](https://zvirox.in/downloads/eep/) | AGPL-3.0 + Commercial |
| **Audio Labs Pro** (`alp`) | Linux Desktop | `v0.1.0-beta.1` (Beta) | [Project](https://zvirox.in/projects/alp/) · [Downloads](https://zvirox.in/downloads/alp/) | Apache-2.0 |
| **Agentic Tuneup Pro** (`atp`) | Linux Desktop | `v0.1.0-beta.1` (Beta) | [Project](https://zvirox.in/projects/atp/) · [Downloads](https://zvirox.in/downloads/atp/) | AGPL-3.0 |
| **Net Watch Pro** (`nwp`) | Linux Desktop | `v0.9.2-beta.5` (Beta) | [Project](https://zvirox.in/projects/nwp/) · [Downloads](https://zvirox.in/downloads/nwp/) | AGPL-3.0 |
| **Your TV Friend** (`ytf`) | Android TV | `v0.0.3` (Stable) | [Project](https://zvirox.in/projects/ytf/) · [Downloads](https://zvirox.in/downloads/ytf/) | MIT |

---

## 🛠️ Architecture & Tech Stack

- **Static Site Generator:** [Jekyll 4](https://jekyllrb.com/) hosted on **GitHub Pages**
- **Domain:** Custom apex domain `zvirox.in` with HTTPS enforced via GitHub Pages
- **Design System:** Linear Matte Dark aesthetic (`#050505` void canvas, `#111213` surface, `#3355FF` Cobalt accent, `1px` crisp borders) with high-contrast Light mode toggle (`#F3F4F6` / `#FFFFFF`)
- **Automated Release Sync:** `.github/workflows/update-downloads.yml` runs daily at 06:00 AM IST (`30 0 * * *` UTC) to refresh `_data/release_manifest.json` with SHA-256 checksums for `.deb`, `.rpm`, `.pkg.tar.zst`, and `.apk` assets
- **Styling:** Custom SCSS (`assets/css/style.scss`) compiled via Dart Sass with `@media (prefers-reduced-motion)` compliance
- **Privacy-First:** Zero third-party analytics, zero ad beacons, zero telemetry. Browser `localStorage` is used exclusively for theme preference (`zvirox-theme: dark | light`).
- **Jekyll Plugins:**
  - `jekyll-feed` — Atom RSS feed generation (`/feed.xml`)
  - `jekyll-sitemap` — Automated root sitemap (`/sitemap.xml`)
  - `jekyll-seo-tag` — Open Graph, Twitter Cards, and schema markup
  - `jekyll-redirect-from` — Server-side redirect handling for clean canonical URLs

---

## 📁 Repository Structure

```text
zvirox-tech-dev/
├── _config.yml               # Jekyll site configuration & plugin definitions
├── CNAME                     # Custom apex domain configuration (zvirox.in)
├── robots.txt                # Search engine crawler directives & sitemap pointers
├── index.md                  # Homepage: Linear hero stage, 7-project cards, Why Zvirox
├── about.md                  # Maintainer profile (Prakashpuri Gauswami / @zvirox)
├── contact.md                # Contact channels, GitHub issue trackers & security policy
├── licensing.md              # Per-project licenses & AGPL-3.0 commercial dual-licensing
├── privacy.md                # Truthful per-application privacy statement (DPDP Act 2023)
├── terms.md                  # Plain-language website terms of service & trademark policy
├── cookies.md                # Transparent cookie statement (localStorage theme only)
├── llms.txt                  # Structured catalog for AI assistants & crawlers
├── .github/workflows/
│   └── update-downloads.yml  # Daily 06:00 AM IST release manifest sync
├── _data/
│   ├── download_products.json # Release rules (.deb, .rpm, .pkg.tar.zst, .apk)
│   └── release_manifest.json  # Generated live release versions, checksums & channels
├── sitemap/
│   └── index.html            # User-facing HTML visual directory
├── downloads/
│   ├── index.md              # Categorized Downloads Hub (Linux Apps & Android Apps)
│   ├── sc.md                 # Starship Control downloads
│   ├── ssp.md                # Screen Studio Pro downloads
│   ├── eep.md                # Easy Edits Pro downloads
│   ├── alp.md                # Audio Labs Pro downloads
│   ├── atp.md                # Agentic Tuneup Pro downloads
│   ├── nwp.md                # Net Watch Pro downloads
│   └── ytf.md                # Your TV Friend downloads
├── projects/
│   ├── index.md              # Projects portfolio showcase
│   ├── sc.md                 # Starship Control project page
│   ├── ssp.md                # Screen Studio Pro project page
│   ├── eep.md                # Easy Edits Pro project page
│   ├── alp.md                # Audio Labs Pro project page
│   ├── atp.md                # Agentic Tuneup Pro project page
│   ├── nwp.md                # Net Watch Pro project page
│   └── ytf.md                # Your TV Friend project page
├── guides/
│   └── index.md              # Technical guides hub & topic explorer
├── categories/
│   ├── index.md              # All categories directory
│   ├── voice-audio-ai/       # Voice & Audio AI guides
│   ├── ai/                   # AI & coding agents guides
│   ├── networking/           # Network protocols & architecture
│   ├── linux/                # Linux systems & administration
│   ├── cybersecurity/        # Defensive security fundamentals
│   ├── it/                   # IT infrastructure & troubleshooting
│   └── development/          # Software development notes
├── _posts/                   # Published technical guides & architectural articles
├── _includes/
│   ├── downloads/            # Download directory cards, release badges & history
│   └── projects/             # Interactive Linear motion stages & hero headers
├── _layouts/
│   ├── default.html          # Global layout (header, mobile drawer, 4-column footer)
│   ├── post.html             # Article layout with dynamic table of contents
│   └── category.html         # Category archive layout
└── assets/
    ├── css/style.scss        # Master stylesheet & Linear Matte tokens
    └── images/
        ├── logos/            # Resized 256x256 PNG logos for all 6 Linux apps
        └── projects/eep/     # Article feature diagrams & screenshots
```

---

## 🔍 Google Search Console & SEO

This website generates a single authoritative XML sitemap via `jekyll-sitemap`, structured for **Google Search Console** and Bing Webmaster Tools:

- **Submission URL:** `https://zvirox.in/sitemap.xml`
- **Visual Directory:** `https://zvirox.in/sitemap/`

The old `/sitemap/sitemap.xml` path is retired and returns 404 — do not submit it. `robots.txt` and `llms.txt` advertise only `/sitemap.xml`.

### Features:
- 100% canonical HTTPS endpoints with accurate W3C `lastmod` timestamps.
- Zero broken links, zero 404s, and zero redirected URLs.
- Legacy URLs (`/articles/` and `/voice%20ai/`) seamlessly forward to canonical endpoints via `jekyll-redirect-from` and meta-refresh fallbacks.
- Open Graph and Schema.org metadata verified via `jekyll-seo-tag`.

---

## 💻 Local Development

### 1. Clone the Repository
```bash
git clone git@github.com:zvirox/zvirox-tech-dev.git
cd zvirox-tech-dev
```

### 2. Compile Stylesheet (Dart Sass)
```bash
npx --yes sass assets/css/style.scss assets/css/style.css
```

### 3. Build & Run Locally (Jekyll)
If Ruby and Bundler are installed:
```bash
bundle install
bundle exec jekyll serve --livereload
```
Preview at `http://localhost:4000/`.

---

## 📜 Licensing

- **Website Source & Content:** Copyright © 2026 Prakashpuri Gauswami. Released under the [MIT License](LICENSE).
- **Associated Software Repositories:**
  - [Starship Control](https://github.com/zvirox/starship-control): Apache License 2.0 ([Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)).
  - [Screen Studio Pro](https://github.com/zvirox/screen-studio-pro): MIT License ([MIT](https://opensource.org/licenses/MIT)).
  - [Easy Edits Pro](https://github.com/zvirox/easy-edits-pro): GNU Affero General Public License v3.0 ([AGPL-3.0](https://www.gnu.org/licenses/agpl-3.0.html)) + Commercial License available on request.
  - [Audio Labs Pro](https://github.com/zvirox/audio-labs-pro): Apache License 2.0 ([Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)).
  - [Agentic Tuneup Pro](https://github.com/zvirox/agentic-tuneup-pro): GNU Affero General Public License v3.0 ([AGPL-3.0](https://www.gnu.org/licenses/agpl-3.0.html)).
  - [Net Watch Pro](https://github.com/zvirox/net-watch-pro): GNU Affero General Public License v3.0 ([AGPL-3.0](https://www.gnu.org/licenses/agpl-3.0.html)).
  - [Your TV Friend](https://github.com/zvirox/your-tv-friend): MIT License ([MIT](https://opensource.org/licenses/MIT)).

For complete details, visit the [Licensing Page](https://zvirox.in/licensing/).

---

## 👤 Maintainer Verification

- **Maintainer:** Prakashpuri Gauswami (`@zvirox`)
- **Role:** Cybersecurity Analyst & Builder
- **Location:** Patan, Gujarat, India
- **Official Domain:** [zvirox.in](https://zvirox.in)
- **Email:** [info@zvirox.in](mailto:info@zvirox.in)
- **GitHub:** [@zvirox](https://github.com/zvirox)
