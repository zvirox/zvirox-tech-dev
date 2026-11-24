---
layout: default
title: Screen Studio Pro
description: Clean, fast screen recording built natively for Wayland and X11 on Linux with PipeWire capture and hardware encoding.
permalink: /projects/ssp/
redirect_from:
  - /projects/screen-studio-pro/
image: "/assets/images/logos/screen-studio-pro.png"
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Screen Studio Pro",
  "operatingSystem": "Linux",
  "applicationCategory": "MultimediaApplication",
  "description": "Fast screen recording studio built natively for Linux Wayland and X11 desktops with PipeWire, webcam picture-in-picture, and hardware encoding.",
  "url": "https://zvirox.in/projects/ssp/",
  "downloadUrl": "https://zvirox.in/downloads/ssp/",
  "license": "https://opensource.org/licenses/MIT",
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

    {% assign ssp_tags = "Rust,Tauri 2,React 19,PipeWire,Wayland / X11,FFmpeg" | split: "," %}
    {% include projects/project-hero.html app_id="ssp" tags=ssp_tags %}

    <div class="zv-post-content zv-project-content">
      <h2>Overview</h2>
      <p>
        <strong>Screen Studio Pro</strong> gives Wayland and X11 Linux users a focused capture studio without bloated streaming scenes. Pick a full monitor, single window, or custom box through native desktop portals, balance microphone and desktop sound levels, float a webcam overlay, and save clean MP4 or MKV videos directly to disk.
      </p>

      <h2>Core Features</h2>
      <ul>
        <li><strong>Wayland &amp; X11 Portals:</strong> Works across Hyprland, niri, KDE Plasma, GNOME, MangoWC, and X11 via PipeWire and xdg-desktop-portal.</li>
        <li><strong>Dual Audio + Webcam PiP:</strong> Mix mic and desktop audio with live gain meters while floating a circular or rounded camera bubble.</li>
        <li><strong>Floating Recording HUD:</strong> Pause, insert chapter markers, or stop recordings from a compact desktop capsule.</li>
        <li><strong>Hardware-First Encoding:</strong> Supports VAAPI and NVENC GPU acceleration with x264 fallback.</li>
        <li><strong>Crash-Safe Recordings:</strong> Writes to Matroska (MKV) first and remuxes cleanly to MP4 on stop so interrupted captures keep their footage.</li>
        <li><strong>Built-In Recording Library:</strong> Browse takes with auto thumbnails and hand clips straight to Easy Edits Pro or Starship Control.</li>
      </ul>

      <h2>Technology Direction & Capture Architecture</h2>
      <p>
        Screen Studio Pro bypasses traditional capture bottlenecks by utilizing Wayland's zero-copy DMA-BUF memory sharing and PipeWire media routing:
      </p>

      <!-- Architecture Teardown Diagram -->
      <div class="zv-teardown-schematic" aria-label="Screen Studio Pro Architecture Teardown">
        <div class="zv-teardown-header">
          <div class="zv-teardown-title-wrap">
            <span class="zv-teardown-category">Wayland capture teardown</span>
            <span class="zv-teardown-subtitle">xdg-desktop-portal · PipeWire DMA-BUF · Rust Crash-Safe Remux</span>
          </div>
          <span class="zv-teardown-shield">🔒 ZERO CLOUD LEAK</span>
        </div>
        <div class="zv-teardown-body">
          <svg class="zv-teardown-svg" viewBox="0 0 840 380" fill="none" xmlns="http://www.w3.org/2000/svg">
            <!-- Column 1: Wayland Compositor & Audio Sources -->
            <rect x="20" y="20" width="220" height="290" rx="8" fill="#140f13" stroke="#ef4444" stroke-opacity="0.4" stroke-width="1.5"/>
            <rect x="20" y="20" width="220" height="34" rx="8" fill="#20141a"/>
            <text x="130" y="42" font-family="'Liberation Mono', monospace" font-size="11" font-weight="700" fill="#fca5a5" text-anchor="middle">1. WAYLAND DESKTOP</text>
            
            <rect x="35" y="70" width="190" height="52" rx="5" fill="#24141c" stroke="#334155" stroke-width="1"/>
            <text x="45" y="90" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Compositor Surfaces</text>
            <text x="45" y="106" font-family="'Liberation Mono', monospace" font-size="10" fill="#f87171">Hyprland · KDE · Mutter · niri</text>
            <text x="45" y="117" font-family="'Liberation Mono', monospace" font-size="9" fill="#94a3b8">Screen · Window · Region</text>

            <rect x="35" y="132" width="190" height="56" rx="5" fill="#24141c" stroke="#334155" stroke-width="1"/>
            <text x="45" y="152" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Audio Routing</text>
            <text x="45" y="168" font-family="'Liberation Mono', monospace" font-size="10" fill="#38bdf8">PipeWire Loopback Node</text>
            <text x="45" y="181" font-family="'Liberation Mono', monospace" font-size="9" fill="#94a3b8">System Audio + Microphone sync</text>

            <rect x="35" y="198" width="190" height="54" rx="5" fill="#24141c" stroke="#334155" stroke-width="1"/>
            <text x="45" y="218" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Webcam Stream</text>
            <text x="45" y="234" font-family="'Liberation Mono', monospace" font-size="10" fill="#34d399">V4L2 / PipeWire video feed</text>
            <text x="45" y="246" font-family="'Liberation Mono', monospace" font-size="9" fill="#94a3b8">Circular PiP overlay with blur</text>

            <rect x="35" y="262" width="190" height="34" rx="5" fill="#1a1117" stroke="rgba(239,68,68,0.3)" stroke-width="1"/>
            <text x="130" y="284" font-family="'Liberation Mono', monospace" font-size="10" fill="#fca5a5" text-anchor="middle">xdg-desktop-portal ScreenCast</text>

            <!-- Arrow 1 -> 2: DMA-BUF Memory Sharing -->
            <path d="M 240,150 L 290,150" stroke="#ef4444" stroke-width="2"/>
            <polygon points="295,150 285,145 285,155" fill="#ef4444"/>
            <text x="267" y="140" font-family="'Liberation Mono', monospace" font-size="9" fill="#ef4444" text-anchor="middle">DMA-BUF</text>
            <text x="267" y="170" font-family="'Liberation Mono', monospace" font-size="8.5" fill="#94a3b8" text-anchor="middle">Zero-Copy</text>

            <!-- Column 2: Rust Recording Core -->
            <rect x="295" y="20" width="250" height="290" rx="8" fill="#141118" stroke="#ef4444" stroke-opacity="0.6" stroke-width="1.8"/>
            <rect x="295" y="20" width="250" height="34" rx="8" fill="#221524"/>
            <text x="420" y="42" font-family="'Liberation Mono', monospace" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">2. RUST RECORDING CORE</text>

            <rect x="310" y="70" width="220" height="66" rx="5" fill="#1f182b" stroke="#a855f7" stroke-opacity="0.4" stroke-width="1"/>
            <text x="320" y="90" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Smooth Cursor &amp; Auto-Zoom</text>
            <text x="320" y="106" font-family="'Liberation Mono', monospace" font-size="10" fill="#c084fc">Mathematical Easing Curves</text>
            <text x="320" y="120" font-family="'Liberation Mono', monospace" font-size="9.5" fill="#94a3b8">Auto-pans to active window bounds</text>
            <text x="320" y="132" font-family="'Liberation Mono', monospace" font-size="9" fill="#38bdf8">Eliminates jerky mouse movements</text>

            <rect x="310" y="146" width="220" height="68" rx="5" fill="#1f182b" stroke="#a855f7" stroke-opacity="0.4" stroke-width="1"/>
            <text x="320" y="166" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Crash-Proof Stream Sink</text>
            <text x="320" y="182" font-family="'Liberation Mono', monospace" font-size="10" fill="#34d399">Continuous MKV Segmenter</text>
            <text x="320" y="196" font-family="'Liberation Mono', monospace" font-size="9.5" fill="#94a3b8">Guaranteed file recovery if crash</text>
            <text x="320" y="208" font-family="'Liberation Mono', monospace" font-size="9" fill="#e2e8f0">Lossless fast remux to MP4 on stop</text>

            <rect x="310" y="224" width="220" height="72" rx="5" fill="#1f182b" stroke="#a855f7" stroke-opacity="0.4" stroke-width="1"/>
            <text x="320" y="244" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Floating HUD &amp; Markers</text>
            <text x="320" y="260" font-family="'Liberation Mono', monospace" font-size="10" fill="#ffa5d0">Frosted-glass Wayland layer-shell</text>
            <text x="320" y="276" font-family="'Liberation Mono', monospace" font-size="9.5" fill="#94a3b8">Pause · Resume · Chapter markers</text>

            <!-- Arrow 2 -> 3: Direct Hardware Render -->
            <path d="M 545,150 L 595,150" stroke="#38bdf8" stroke-width="2"/>
            <polygon points="600,150 590,145 590,155" fill="#38bdf8"/>
            <text x="572" y="140" font-family="'Liberation Mono', monospace" font-size="9" fill="#38bdf8" text-anchor="middle">Hardware</text>
            <text x="572" y="170" font-family="'Liberation Mono', monospace" font-size="8.5" fill="#94a3b8" text-anchor="middle">NVENC/VAAPI</text>

            <!-- Column 3: Hardware Encoders & Local Catalog -->
            <rect x="600" y="20" width="220" height="290" rx="8" fill="#0d141e" stroke="#38bdf8" stroke-opacity="0.5" stroke-width="1.5"/>
            <rect x="600" y="20" width="220" height="34" rx="8" fill="#15202f"/>
            <text x="710" y="42" font-family="'Liberation Mono', monospace" font-size="11" font-weight="700" fill="#38bdf8" text-anchor="middle">3. HARDWARE &amp; VAULT</text>

            <rect x="615" y="70" width="190" height="66" rx="5" fill="#162335" stroke="#34d399" stroke-opacity="0.4" stroke-width="1"/>
            <text x="625" y="90" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">HW Codec Selection</text>
            <text x="625" y="106" font-family="'Liberation Mono', monospace" font-size="10" fill="#34d399">VAAPI / NVENC (Preferred)</text>
            <text x="625" y="122" font-family="'Liberation Mono', monospace" font-size="9.5" fill="#94a3b8">Low-power x264 CPU fallback</text>

            <rect x="615" y="148" width="190" height="66" rx="5" fill="#162335" stroke="#34d399" stroke-opacity="0.4" stroke-width="1"/>
            <text x="625" y="168" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Local SQLite Vault</text>
            <text x="625" y="184" font-family="'Liberation Mono', monospace" font-size="10" fill="#38bdf8">Encrypted local catalog</text>
            <text x="625" y="200" font-family="'Liberation Mono', monospace" font-size="9.5" fill="#94a3b8">Duration · Bitrate · Codec tags</text>

            <rect x="615" y="226" width="190" height="70" rx="5" fill="#162335" stroke="#34d399" stroke-opacity="0.4" stroke-width="1"/>
            <text x="625" y="246" font-family="'Liberation Sans', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Zero-Server Policy</text>
            <text x="625" y="264" font-family="'Liberation Mono', monospace" font-size="10" fill="#facc15">No HTTP daemons</text>
            <text x="625" y="282" font-family="'Liberation Mono', monospace" font-size="9" fill="#94a3b8">No cloud telemetry or tracking</text>

            <!-- Bottom Airgap Shield -->
            <rect x="20" y="325" width="800" height="38" rx="6" fill="#082015" stroke="#22c55e" stroke-opacity="0.6" stroke-width="1"/>
            <text x="420" y="348" font-family="'Liberation Mono', monospace" font-size="11" font-weight="700" fill="#4ade80" text-anchor="middle">✔ ZERO CLOUD LEAK: SCREEN CAPTURES AND AUDIO STREAMS ARE WRITTEN DIRECTLY TO LOCAL DISK VAULT</text>
          </svg>
        </div>
      </div>

      <p>
        Screen Studio Pro pairs a Rust capture and FFmpeg encoding core with Tauri 2 and a React 19 interface. PipeWire and native desktop portals stream screen frames locally with zero telemetry or network listeners.
      </p>

      <h2>Current Status</h2>
      <p>
        Screen Studio Pro is now in <strong>Public Beta</strong> ({% assign ssp_rel = site.data.release_manifest.projects | where: "id", "ssp" | first %}{{ ssp_rel.latest.tag_name | default: "v0.1.0-beta.1" }}), shipping `.deb`, `.rpm`, and Arch Linux packages built from tagged releases.
      </p>

      <h2>Resources &amp; Downloads</h2>
      <ul>
        <li><a href="{{ '/downloads/ssp/' | relative_url }}">Download Linux Packages (.deb, .rpm, Arch)</a></li>
        <li><a href="https://github.com/zvirox/screen-studio-pro" target="_blank" rel="noopener noreferrer">Source Code on GitHub ↗</a></li>
      </ul>
    </div>

    <nav class="zv-project-navigation" aria-label="Project navigation">
      <a href="{{ '/projects/sc/' | relative_url }}" class="zv-section-link">
        &larr; Previous: Starship Control
      </a>
      <a href="{{ '/projects/eep/' | relative_url }}" class="zv-section-link">
        Next: Easy Edits Pro &rarr;
      </a>
    </nav>

  </article>


</div>
