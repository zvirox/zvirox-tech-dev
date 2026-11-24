---
layout: default
title: Net Watch Pro
description: Private Linux network speed monitor and per-app bandwidth tracker powered by Rust, Aya eBPF, and local SQLite storage.
permalink: /projects/nwp/
redirect_from:
  - /projects/net-watch-pro/
image: /assets/images/logos/net-watch-pro.png
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Net Watch Pro",
  "operatingSystem": "Linux",
  "applicationCategory": "NetworkingApplication",
  "description": "Private, local-first Linux network speed monitor and per-app data tracker using kernel Aya eBPF probes and local SQLite persistence.",
  "url": "https://zvirox.in/projects/nwp/",
  "downloadUrl": "https://zvirox.in/downloads/nwp/",
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

    {% assign nwp_tags = "Rust,Aya eBPF,Tauri 2,React 19,SQLite,Linux" | split: "," %}
    {% include projects/project-hero.html app_id="nwp" tags=nwp_tags %}

    <div class="zv-post-content zv-project-content">
      <h2>Overview</h2>
      <p>
        Standard Linux desktop speed indicators only show combined interface totals. When a background build, container image pull, or browser tab saturates your connection, they rarely identify which binary owns the traffic.
      </p>
      <p>
        <strong>Net Watch Pro</strong> pairs a lightweight background collector (<code>netwatchd</code>) using Linux Aya eBPF socket counters with an unprivileged Tauri desktop UI. It tracks live Mbps throughput, attributes traffic per process, and keeps 90 days of hourly and daily totals in SQLite on your disk. It is strictly a read-only monitor and never intercepts or slows down packets.
      </p>

      <h2>Key Capabilities</h2>
      <ul>
        <li><strong>Real-Time 1 Hz Sparklines:</strong> Smooth upload and download meters over 60-second windows with selectable Mbps and MB/s units.</li>
        <li><strong>Per-Application Attribution:</strong> Aya eBPF kernel probes link socket byte counts directly to running Linux processes, with clean interface fallback on older kernels.</li>
        <li><strong>Privilege-Split Security:</strong> Kernel inspection runs inside <code>netwatchd</code> while the Tauri UI runs completely unprivileged, communicating via a peer-credential Unix socket.</li>
        <li><strong>Active Connection Inspector:</strong> Browse live remote IP endpoints, destination ports, and protocols grouped by executable name.</li>
        <li><strong>90-Day SQLite Retention:</strong> Query hourly, daily, and weekly historical traffic locally with zero outbound telemetry.</li>
        <li><strong>Starship Socket Bridge:</strong> Exposes read-only bandwidth queries over <code>nwp.sock</code> so Starship Control can summarize what is hogging your link.</li>
      </ul>

      <h2>Privilege-Separated eBPF Architecture</h2>
      <p>
        By keeping kernel probe attachment isolated in <code>netwatchd</code> and storing aggregates in WAL-mode SQLite, desktop UI memory stays light and never runs as root.
      </p>

      <div class="zv-teardown-schematic" aria-label="Net Watch Pro Architecture">
        <div class="zv-teardown-header">
          <div class="zv-teardown-title-wrap">
            <span class="zv-teardown-category">eBPF telemetry pipeline</span>
            <span class="zv-teardown-subtitle">Aya eBPF Kernel Counters · netwatchd Daemon · Unprivileged UI</span>
          </div>
          <span class="zv-teardown-shield">READ-ONLY · ZERO CLOUD</span>
        </div>
        <div class="zv-teardown-body">
          <svg class="zv-teardown-svg" viewBox="0 0 840 260" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="20" y="24" width="230" height="206" rx="8" fill="#0B0C0E" stroke="#38B6F0" stroke-opacity="0.5" stroke-width="1.5"/>
            <rect x="20" y="24" width="230" height="32" rx="8" fill="#14161D"/>
            <text x="135" y="44" font-family="monospace" font-size="11" font-weight="600" fill="#F5F5F6" text-anchor="middle">1. LINUX KERNEL SPACE</text>
            <rect x="35" y="72" width="200" height="62" rx="5" fill="#111213" stroke="#2C2E33"/>
            <text x="48" y="94" font-family="sans-serif" font-size="12" font-weight="600" fill="#F5F5F6">Aya eBPF Byte Probes</text>
            <text x="48" y="114" font-family="monospace" font-size="9.5" fill="#38B6F0">Read-only socket map counters</text>
            <rect x="35" y="148" width="200" height="62" rx="5" fill="#111213" stroke="#2C2E33"/>
            <text x="48" y="170" font-family="sans-serif" font-size="12" font-weight="600" fill="#F5F5F6">Process PID Mapping</text>
            <text x="48" y="190" font-family="monospace" font-size="9.5" fill="#8A8B91">Fallback: /proc/net interface</text>

            <path d="M 250,125 L 305,125" stroke="#38B6F0" stroke-width="2"/>
            <polygon points="310,125 300,120 300,130" fill="#38B6F0"/>

            <rect x="310" y="24" width="235" height="206" rx="8" fill="#0B0C0E" stroke="#3355FF" stroke-opacity="0.5" stroke-width="1.5"/>
            <rect x="310" y="24" width="235" height="32" rx="8" fill="#14161D"/>
            <text x="427" y="44" font-family="monospace" font-size="11" font-weight="600" fill="#F5F5F6" text-anchor="middle">2. NETWATCHD DAEMON</text>
            <rect x="325" y="72" width="205" height="62" rx="5" fill="#111213" stroke="#2C2E33"/>
            <text x="338" y="94" font-family="sans-serif" font-size="12" font-weight="600" fill="#F5F5F6">Tokio 1 Hz Aggregator</text>
            <text x="338" y="114" font-family="monospace" font-size="9.5" fill="#22C55E">Hourly &amp; daily SQLite rollups</text>
            <rect x="325" y="148" width="205" height="62" rx="5" fill="#111213" stroke="#2C2E33"/>
            <text x="338" y="170" font-family="sans-serif" font-size="12" font-weight="600" fill="#F5F5F6">Peer-Cred Unix Socket</text>
            <text x="338" y="190" font-family="monospace" font-size="9.5" fill="#3355FF">Zero network API listeners</text>

            <path d="M 545,125 L 595,125" stroke="#3355FF" stroke-width="2"/>
            <polygon points="600,125 590,120 590,130" fill="#3355FF"/>

            <rect x="600" y="24" width="220" height="206" rx="8" fill="#0B0C0E" stroke="#2C2E33" stroke-width="1.5"/>
            <rect x="600" y="24" width="220" height="32" rx="8" fill="#14161D"/>
            <text x="710" y="44" font-family="monospace" font-size="11" font-weight="600" fill="#F5F5F6" text-anchor="middle">3. DESKTOP CLIENT</text>
            <rect x="615" y="72" width="190" height="62" rx="5" fill="#111213" stroke="#2C2E33"/>
            <text x="628" y="94" font-family="sans-serif" font-size="12" font-weight="600" fill="#F5F5F6">React 19 + ECharts</text>
            <text x="628" y="114" font-family="monospace" font-size="9.5" fill="#8A8B91">Unprivileged tray &amp; graphs</text>
            <rect x="615" y="148" width="190" height="62" rx="5" fill="#111213" stroke="#2C2E33"/>
            <text x="628" y="170" font-family="sans-serif" font-size="12" font-weight="600" fill="#F5F5F6">Starship HUD Bridge</text>
            <text x="628" y="190" font-family="monospace" font-size="9.5" fill="#7C5CE6">nwp.sock bandwidth tools</text>
          </svg>
        </div>
      </div>

      <h2>License &amp; Downloads</h2>
      <p>
        Net Watch Pro is licensed under <a href="https://www.gnu.org/licenses/agpl-3.0.html" target="_blank" rel="noopener noreferrer">AGPL-3.0</a> with an offline Pro key option. Download verified Linux installers from the <a href="{{ '/downloads/nwp/' | relative_url }}">Net Watch Pro Downloads page</a>.
      </p>
    </div>

    <div class="zv-project-navigation">
      <a href="{{ '/projects/atp/' | relative_url }}" class="zv-project-back" style="margin-bottom:0;">&larr; Agentic Tuneup Pro</a>
      <a href="{{ '/projects/ytf/' | relative_url }}" class="zv-project-text-link">Next: Your TV Friend &rarr;</a>
    </div>
  </article>
</div>
