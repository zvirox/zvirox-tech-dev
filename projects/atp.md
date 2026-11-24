---
layout: default
title: Agentic Tuneup Pro
description: Safety-first Linux disk cleaner, unified package manager, and health monitor with SHA-256 reversible quarantine.
permalink: /projects/atp/
redirect_from:
  - /projects/agentic-tuneup-pro/
image: /assets/images/logos/agentic-tuneup-pro.png
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Agentic Tuneup Pro",
  "operatingSystem": "Linux",
  "applicationCategory": "UtilitiesApplication",
  "description": "Safety-first Linux disk cleaner, package manager, and system health monitor backed by a two-phase reversible SHA-256 quarantine vault.",
  "url": "https://zvirox.in/projects/atp/",
  "downloadUrl": "https://zvirox.in/downloads/atp/",
  "license": "https://www.gnu.org/licenses/agpl-3.0.html",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD"
  },
  "author": {
    "@type": "Person",
    "name": "Prakashpuri Gauswami",
    "url": "https://zvirox.in/about/"
  }
}
</script>

<div class="zv-container">
  <article class="zv-post zv-project-page">
    <a class="zv-project-back" href="{{ '/projects/' | relative_url }}">&larr; All projects</a>

    {% assign atp_tags = "Rust,Tauri 2,React 19,SHA-256 Vault,Linux,MCP" | split: "," %}
    {% include projects/project-hero.html app_id="atp" tags=atp_tags %}

    <div class="zv-post-content zv-project-content">
      <h2>Overview</h2>
      <p>
        Standard Linux cleanup scripts delete files right away using shell wildcards. One wrong path wipe can erase active build environments or break packages with zero undo path.
      </p>
      <p>
        <strong>Agentic Tuneup Pro</strong> scans browser caches, system logs, Python venvs, <code>node_modules/</code>, and Rust <code>target/</code> directories in parallel, moving selected items into a reversible SHA-256 quarantine vault before permanent deletion. If any app still expects a cached file, you can restore it byte-for-byte with original permissions.
      </p>

      <h2>Key Features</h2>
      <ul>
        <li><strong>Two-Phase Reversible Quarantine:</strong> Cleaned artifacts move into an indexed local vault with retention timers and SHA-256 verification before permanent purge.</li>
        <li><strong>Hard Protected System Paths:</strong> Kernel-checked rules permanently lock out <code>/etc</code>, <code>/boot</code>, <code>/usr</code>, SSH keys, and keyrings from deletion targets.</li>
        <li><strong>Zero-Shell Execution:</strong> System scanners and cleanups run via native Rust OS syscalls without spawning <code>sh -c</code>, eliminating path expansion injection risks.</li>
        <li><strong>Unified Linux Package View:</strong> Inspect <code>apt</code>, <code>dnf</code>, <code>pacman</code>, and Flatpak apps alongside unused orphan dependencies in one interface.</li>
        <li><strong>Slowdown Diagnostics:</strong> Correlates CPU thermal throttling, memory pressure, and heavy background processes in real-time 1 Hz charts.</li>
        <li><strong>Starship Control Integration:</strong> Connects over <code>SO_PEERCRED</code> local sockets so Starship Control can query system stats or request gated cleanups.</li>
      </ul>

      <h2>Quarantine Safety Model</h2>
      <p>
        Privileged operations run through an explicit helper boundary (<code>atpd-helper</code>) only when removing system packages or editing root-owned directories, keeping the Tauri interface unprivileged.
      </p>

      <div class="zv-teardown-schematic" aria-label="Agentic Tuneup Pro Architecture">
        <div class="zv-teardown-header">
          <div class="zv-teardown-title-wrap">
            <span class="zv-teardown-category">Safety pipeline</span>
            <span class="zv-teardown-subtitle">Parallel Rust Scanner · Allowlist Filter · Reversible Vault</span>
          </div>
          <span class="zv-teardown-shield">REVERSIBLE QUARANTINE</span>
        </div>
        <div class="zv-teardown-body">
          <svg class="zv-teardown-svg" viewBox="0 0 840 280" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="20" y="24" width="235" height="224" rx="8" fill="#0B0C0E" stroke="#22C55E" stroke-opacity="0.45" stroke-width="1.5"/>
            <rect x="20" y="24" width="235" height="32" rx="8" fill="#14161D"/>
            <text x="137" y="44" font-family="monospace" font-size="11" font-weight="600" fill="#F5F5F6" text-anchor="middle">1. PARALLEL SCANNER</text>
            <rect x="35" y="72" width="205" height="46" rx="5" fill="#111213" stroke="#2C2E33"/>
            <text x="48" y="92" font-family="sans-serif" font-size="12" font-weight="600" fill="#F5F5F6">Developer &amp; Browser Targets</text>
            <text x="48" y="108" font-family="monospace" font-size="9.5" fill="#8A8B91">target/ · node_modules · cache</text>
            <rect x="35" y="130" width="205" height="46" rx="5" fill="#111213" stroke="#F43F5E" stroke-opacity="0.45"/>
            <text x="48" y="150" font-family="sans-serif" font-size="12" font-weight="600" fill="#F5F5F6">Hard Protected Guard</text>
            <text x="48" y="166" font-family="monospace" font-size="9.5" fill="#F43F5E">Blocks /etc /boot ~/.ssh /usr</text>
            <rect x="35" y="188" width="205" height="44" rx="5" fill="#111213" stroke="#2C2E33"/>
            <text x="137" y="214" font-family="monospace" font-size="10" fill="#38B6F0" text-anchor="middle">Direct Rust syscalls (no sh)</text>

            <path d="M 255,136 L 305,136" stroke="#22C55E" stroke-width="2"/>
            <polygon points="310,136 300,131 300,141" fill="#22C55E"/>

            <rect x="310" y="24" width="230" height="224" rx="8" fill="#0B0C0E" stroke="#3355FF" stroke-opacity="0.5" stroke-width="1.5"/>
            <rect x="310" y="24" width="230" height="32" rx="8" fill="#14161D"/>
            <text x="425" y="44" font-family="monospace" font-size="11" font-weight="600" fill="#F5F5F6" text-anchor="middle">2. QUARANTINE VAULT</text>
            <rect x="325" y="72" width="200" height="58" rx="5" fill="#111213" stroke="#2C2E33"/>
            <text x="338" y="92" font-family="sans-serif" font-size="12" font-weight="600" fill="#F5F5F6">Phase 1: Isolate + Hash</text>
            <text x="338" y="110" font-family="monospace" font-size="9.5" fill="#22C55E">SHA-256 + original chmod/uid</text>
            <rect x="325" y="144" width="200" height="86" rx="5" fill="#111213" stroke="#2C2E33"/>
            <text x="338" y="166" font-family="sans-serif" font-size="12" font-weight="600" fill="#F5F5F6">1-Click Bitwise Restore</text>
            <text x="338" y="186" font-family="monospace" font-size="9.5" fill="#8A8B91">Or approved Phase 2 Purge</text>
            <text x="338" y="206" font-family="monospace" font-size="9.5" fill="#38B6F0">Verifies digest before unlink</text>

            <path d="M 540,136 L 590,136" stroke="#38B6F0" stroke-width="2"/>
            <polygon points="595,136 585,131 585,141" fill="#38B6F0"/>

            <rect x="595" y="24" width="225" height="224" rx="8" fill="#0B0C0E" stroke="#2C2E33" stroke-width="1.5"/>
            <rect x="595" y="24" width="225" height="32" rx="8" fill="#14161D"/>
            <text x="707" y="44" font-family="monospace" font-size="11" font-weight="600" fill="#F5F5F6" text-anchor="middle">3. SYSTEM TELEMETRY</text>
            <rect x="610" y="72" width="195" height="50" rx="5" fill="#111213" stroke="#2C2E33"/>
            <text x="622" y="92" font-family="sans-serif" font-size="12" font-weight="600" fill="#F5F5F6">Apache ECharts 1 Hz</text>
            <text x="622" y="109" font-family="monospace" font-size="9.5" fill="#8A8B91">CPU · RAM · Temp · Disk I/O</text>
            <rect x="610" y="134" width="195" height="96" rx="5" fill="#111213" stroke="#2C2E33"/>
            <text x="622" y="156" font-family="sans-serif" font-size="12" font-weight="600" fill="#F5F5F6">Package Explorer</text>
            <text x="622" y="176" font-family="monospace" font-size="9.5" fill="#A1A3AB">apt · dnf · pacman · Flatpak</text>
            <text x="622" y="198" font-family="monospace" font-size="9.5" fill="#7C5CE6">atp.sock -> Starship HUD</text>
          </svg>
        </div>
      </div>

      <h2>License &amp; Downloads</h2>
      <p>
        Agentic Tuneup Pro is licensed under <a href="https://www.gnu.org/licenses/agpl-3.0.html" target="_blank" rel="noopener noreferrer">AGPL-3.0</a>. Download verified Linux installers from the <a href="{{ '/downloads/atp/' | relative_url }}">Agentic Tuneup Pro Downloads page</a>.
      </p>
    </div>

    <div class="zv-project-navigation">
      <a href="{{ '/projects/alp/' | relative_url }}" class="zv-project-back" style="margin-bottom:0;">&larr; Audio Labs Pro</a>
      <a href="{{ '/projects/nwp/' | relative_url }}" class="zv-project-text-link">Next: Net Watch Pro &rarr;</a>
    </div>
  </article>
</div>
