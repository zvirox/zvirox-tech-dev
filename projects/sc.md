---
layout: default
title: Starship Control
description: Local-first AI cockpit and floating desktop HUD coordinating Zvirox Linux apps over verified local Unix sockets.
permalink: /projects/sc/
redirect_from:
  - /projects/starship-control/
image: /assets/images/logos/starship-control.png
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Starship Control",
  "operatingSystem": "Linux",
  "applicationCategory": "UtilitiesApplication",
  "description": "Local-first AI cockpit and floating desktop command bar that coordinates Zvirox Linux desktop applications over kernel-checked Unix sockets.",
  "url": "https://zvirox.in/projects/sc/",
  "downloadUrl": "https://zvirox.in/downloads/sc/",
  "license": "https://www.apache.org/licenses/LICENSE-2.0",
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

    {% assign sc_tags = "Rust,Tauri 2,React 19,llama.cpp,MCP,Linux" | split: "," %}
    {% include projects/project-hero.html app_id="sc" tags=sc_tags %}

    <div class="zv-post-content zv-project-content">
      <h2>Overview</h2>
      <p>
        Desktop creative tools and system utilities usually live on separate islands. You record a video clip in one app, clean speech in another, cut timelines in a third, and inspect system bottlenecks from a terminal.
      </p>
      <p>
        <strong>Starship Control</strong> links the Zvirox desktop suite inside one local cockpit window and a quick floating HUD (<code>Super+Shift+Space</code>). You type what you need in plain words. The Rust planner inspects which apps are running locally, drafts an explicit step-by-step plan, and pauses for your click before mutating files or settings.
      </p>

      <h2>Core Capabilities</h2>
      <ul>
        <li><strong>Cockpit &amp; Floating HUD:</strong> Manage multi-step projects and local model downloads in the 1200x800 Cockpit, or tap <code>Super+Shift+Space</code> anywhere for a compact command bar.</li>
        <li><strong>Offline GGUF Inference:</strong> Run open language models locally via <code>llama-cpp-2</code> with Vulkan, ROCm, or CPU execution. Optional external API keys work strictly for prompts you choose to send remotely.</li>
        <li><strong>Three-Tier Approval Lock:</strong> Read-only status checks run right away. File edits, cleanup runs, or timeline mutations halt at a signed approval prompt before execution.</li>
        <li><strong>Zero Open Network Ports:</strong> Companion apps expose descriptors under <code>$XDG_DATA_HOME/starship/plugins/</code> and talk over Unix domain sockets validated with Linux <code>SO_PEERCRED</code>.</li>
        <li><strong>Built-in Model Hub:</strong> Pull GGUF weights from Hugging Face with pause/resume support, SHA-256 verification, and hardware resource charts rendered with Apache ECharts.</li>
        <li><strong>Prompt Guardrails:</strong> Window titles and external filenames stay isolated inside <code>&lt;untrusted_context&gt;</code> boundaries so filename strings cannot hijack tool calls.</li>
      </ul>

      <h2>Connected Socket Architecture</h2>
      <p>
        Every companion app works standalone without Starship Control. When both are running on your Linux session, local sockets connect them under your user UID without opening TCP listeners.
      </p>

      <div class="zv-teardown-schematic" aria-label="Starship Control Socket Teardown">
        <div class="zv-teardown-header">
          <div class="zv-teardown-title-wrap">
            <span class="zv-teardown-category">Socket orchestration</span>
            <span class="zv-teardown-subtitle">Rust Planner · SO_PEERCRED Unix Sockets · 5 Companion Bridges</span>
          </div>
          <span class="zv-teardown-shield">LOCAL UID VERIFIED</span>
        </div>
        <div class="zv-teardown-body">
          <svg class="zv-teardown-svg" viewBox="0 0 840 320" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="20" y="20" width="230" height="270" rx="8" fill="#0B0C0E" stroke="#3355FF" stroke-opacity="0.5" stroke-width="1.5"/>
            <rect x="20" y="20" width="230" height="34" rx="8" fill="#14161D"/>
            <text x="135" y="42" font-family="monospace" font-size="11" font-weight="600" fill="#F5F5F6" text-anchor="middle">1. COCKPIT &amp; HUD</text>
            <rect x="35" y="72" width="200" height="54" rx="6" fill="#111213" stroke="#2C2E33"/>
            <text x="48" y="94" font-family="sans-serif" font-size="12" font-weight="600" fill="#F5F5F6">React 19 Interface</text>
            <text x="48" y="112" font-family="monospace" font-size="10" fill="#8A8B91">Super+Shift+Space HUD</text>
            <rect x="35" y="142" width="200" height="58" rx="6" fill="#111213" stroke="#2C2E33"/>
            <text x="48" y="164" font-family="sans-serif" font-size="12" font-weight="600" fill="#F5F5F6">Local GGUF / API Router</text>
            <text x="48" y="182" font-family="monospace" font-size="10" fill="#38B6F0">llama.cpp · Vulkan / ROCm</text>
            <rect x="35" y="216" width="200" height="54" rx="6" fill="#111213" stroke="#2C2E33"/>
            <text x="48" y="238" font-family="sans-serif" font-size="12" font-weight="600" fill="#F5F5F6">SQLite WAL + Secret Store</text>
            <text x="48" y="256" font-family="monospace" font-size="10" fill="#22C55E">Local audit history</text>

            <path d="M 250,155 L 305,155" stroke="#3355FF" stroke-width="2"/>
            <polygon points="310,155 300,150 300,160" fill="#3355FF"/>
            <text x="278" y="142" font-family="monospace" font-size="9" fill="#A1A3AB" text-anchor="middle">Safety Gate</text>

            <rect x="310" y="20" width="230" height="270" rx="8" fill="#0B0C0E" stroke="#2C2E33" stroke-width="1.5"/>
            <rect x="310" y="20" width="230" height="34" rx="8" fill="#14161D"/>
            <text x="425" y="42" font-family="monospace" font-size="11" font-weight="600" fill="#F5F5F6" text-anchor="middle">2. TRUST BOUNDARY</text>
            <rect x="325" y="72" width="200" height="62" rx="6" fill="#111213" stroke="#22C55E" stroke-opacity="0.45"/>
            <text x="338" y="94" font-family="sans-serif" font-size="12" font-weight="600" fill="#F5F5F6">Tier 1 Read-Only</text>
            <text x="338" y="114" font-family="monospace" font-size="10" fill="#22C55E">Auto-runs status queries</text>
            <rect x="325" y="148" width="200" height="62" rx="6" fill="#111213" stroke="#EAB308" stroke-opacity="0.45"/>
            <text x="338" y="170" font-family="sans-serif" font-size="12" font-weight="600" fill="#F5F5F6">Tier 2 &amp; 3 Mutations</text>
            <text x="338" y="190" font-family="monospace" font-size="10" fill="#EAB308">Halts for human click</text>
            <rect x="325" y="224" width="200" height="46" rx="6" fill="#111213" stroke="#2C2E33"/>
            <text x="425" y="252" font-family="monospace" font-size="10" fill="#38B6F0" text-anchor="middle">Kernel SO_PEERCRED Check</text>

            <path d="M 540,155 L 595,155" stroke="#38B6F0" stroke-width="2"/>
            <polygon points="600,155 590,150 590,160" fill="#38B6F0"/>
            <text x="568" y="142" font-family="monospace" font-size="9" fill="#A1A3AB" text-anchor="middle">JSON-RPC</text>

            <rect x="600" y="20" width="220" height="270" rx="8" fill="#0B0C0E" stroke="#2C2E33" stroke-width="1.5"/>
            <rect x="600" y="20" width="220" height="34" rx="8" fill="#14161D"/>
            <text x="710" y="42" font-family="monospace" font-size="11" font-weight="600" fill="#F5F5F6" text-anchor="middle">3. COMPANION BRIDGES</text>
            <rect x="615" y="70" width="190" height="36" rx="5" fill="#111213" stroke="#2C2E33"/>
            <text x="628" y="92" font-family="monospace" font-size="10" fill="#F5F5F6">ssp.sock · Screen Studio</text>
            <rect x="615" y="114" width="190" height="36" rx="5" fill="#111213" stroke="#2C2E33"/>
            <text x="628" y="136" font-family="monospace" font-size="10" fill="#F5F5F6">eep.sock · Easy Edits</text>
            <rect x="615" y="158" width="190" height="36" rx="5" fill="#111213" stroke="#2C2E33"/>
            <text x="628" y="180" font-family="monospace" font-size="10" fill="#F5F5F6">alp.sock · Audio Labs</text>
            <rect x="615" y="202" width="190" height="36" rx="5" fill="#111213" stroke="#2C2E33"/>
            <text x="628" y="224" font-family="monospace" font-size="10" fill="#F5F5F6">atp.sock · Agentic Tuneup</text>
            <rect x="615" y="246" width="190" height="36" rx="5" fill="#111213" stroke="#2C2E33"/>
            <text x="628" y="268" font-family="monospace" font-size="10" fill="#F5F5F6">nwp.sock · Net Watch</text>
          </svg>
        </div>
      </div>

      <h2>License &amp; Downloads</h2>
      <p>
        Starship Control is licensed under <a href="https://www.apache.org/licenses/LICENSE-2.0" target="_blank" rel="noopener noreferrer">Apache-2.0</a>. Grab <code>.deb</code>, <code>.rpm</code>, or Arch Linux packages directly from the <a href="{{ '/downloads/sc/' | relative_url }}">Starship Control Downloads page</a>.
      </p>
    </div>

    <div class="zv-project-navigation">
      <a href="{{ '/projects/' | relative_url }}" class="zv-project-back" style="margin-bottom:0;">&larr; All projects</a>
      <a href="{{ '/projects/ssp/' | relative_url }}" class="zv-project-text-link">Next: Screen Studio Pro &rarr;</a>
    </div>
  </article>
</div>
