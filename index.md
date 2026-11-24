---
layout: default
title: Open-Source Software for Linux & Android TV
description: Local-first Linux desktop suite and Android TV tools built by Zvirox. Starship Control, Screen Studio Pro, Easy Edits Pro, Audio Labs Pro, Agentic Tuneup Pro, Net Watch Pro, and Your TV Friend.
permalink: /
---

{% assign linux_products = site.data.download_products | where: "category", "linux" %}
{% assign android_products = site.data.download_products | where: "category", "android" %}

<div class="zv-container">

  <!-- =====================================================
       1. LINEAR HERO SECTION + INTERACTIVE ECOSYSTEM MOTION STAGE
       ===================================================== -->

  <section class="zv-hero">
    <div class="zv-hero-split">
      <div class="zv-hero-content">
        <div class="zv-card-category">Local-first open source · Linux &amp; Android TV</div>

        <h1>
          Desktop and TV tools that run <span>on your own machine.</span>
        </h1>

        <p>
          Six Rust, Tauri 2, and React 19 apps for Linux alongside a rootless Android TV launcher. They connect locally over Unix sockets with zero accounts and zero telemetry.
        </p>

        <div style="display:flex; gap:12px; flex-wrap:wrap; align-items:center;">
          <a href="{{ '/downloads/' | relative_url }}" class="zv-button zv-button-primary">
            Download Apps →
          </a>
          <a href="#projects" class="zv-button zv-button-secondary">
            Explore Suite
          </a>
          <a href="https://github.com/zvirox" target="_blank" rel="noopener noreferrer" class="zv-project-github-link" style="padding:0 6px;">
            GitHub ↗
          </a>
        </div>

        <div class="zv-hero-stack">
          <span class="zv-hero-stack-label">Built with</span>
          <span class="zv-hero-stack-item">Rust</span>
          <span class="zv-hero-stack-item">Tauri 2</span>
          <span class="zv-hero-stack-item">React 19</span>
          <span class="zv-hero-stack-item">Aya eBPF</span>
          <span class="zv-hero-stack-item">GStreamer</span>
          <span class="zv-hero-stack-item">Java / ADB</span>
        </div>
      </div>

      <!-- Motion Stage: Starship Control Local Ecosystem -->
      <div class="zv-hero-stage" aria-hidden="true">
        <div class="zv-hero-stage-bar">
          <div class="zv-hero-stage-dots"><i></i><i></i><i></i><span style="margin-left:6px;">starship-control</span></div>
          <span style="color:#22C55E;">● SO_PEERCRED OK</span>
        </div>
        <div class="zv-hero-stage-hud">
          <div class="zv-hud-prompt-row">
            <span>"Record screen, strip noise, check bandwidth spike"</span>
            <span class="zv-hud-kbd">Super+Shift+Space</span>
          </div>
          <div class="zv-hud-nodes-grid">
            <div class="zv-hud-node">
              <img src="{{ '/assets/images/logos/screen-studio-pro.png' | relative_url }}" alt="" width="20" height="20">
              <div class="zv-hud-node-meta">
                <span class="zv-hud-node-name">Screen Studio Pro</span>
                <span class="zv-hud-node-sock">ssp.sock · PipeWire</span>
              </div>
            </div>
            <div class="zv-hud-node">
              <img src="{{ '/assets/images/logos/easy-edits-pro.png' | relative_url }}" alt="" width="20" height="20">
              <div class="zv-hud-node-meta">
                <span class="zv-hud-node-name">Easy Edits Pro</span>
                <span class="zv-hud-node-sock">eep.sock · Timeline</span>
              </div>
            </div>
            <div class="zv-hud-node">
              <img src="{{ '/assets/images/logos/audio-labs-pro.png' | relative_url }}" alt="" width="20" height="20">
              <div class="zv-hud-node-meta">
                <span class="zv-hud-node-name">Audio Labs Pro</span>
                <span class="zv-hud-node-sock">alp.sock · 14 MCP</span>
              </div>
            </div>
            <div class="zv-hud-node">
              <img src="{{ '/assets/images/logos/agentic-tuneup-pro.png' | relative_url }}" alt="" width="20" height="20">
              <div class="zv-hud-node-meta">
                <span class="zv-hud-node-name">Agentic Tuneup Pro</span>
                <span class="zv-hud-node-sock">atp.sock · Quarantine</span>
              </div>
            </div>
            <div class="zv-hud-node">
              <img src="{{ '/assets/images/logos/net-watch-pro.png' | relative_url }}" alt="" width="20" height="20">
              <div class="zv-hud-node-meta">
                <span class="zv-hud-node-name">Net Watch Pro</span>
                <span class="zv-hud-node-sock">nwp.sock · Aya eBPF</span>
              </div>
            </div>
            <div class="zv-hud-node">
              <img src="{{ '/assets/images/logos/starship-control.png' | relative_url }}" alt="" width="20" height="20">
              <div class="zv-hud-node-meta">
                <span class="zv-hud-node-name">Starship Cockpit</span>
                <span class="zv-hud-node-sock">Tier 2 Gate Armed</span>
              </div>
            </div>
          </div>
          <div class="zv-atp-scan-track"><div class="zv-atp-scan-fill" style="width:100%; background:#3355FF;"></div></div>
        </div>
        <div class="zv-hero-stage-footer">
          <span>6 Linux binaries (.deb / .rpm / Arch)</span>
          <span>100% local · 0 network listeners</span>
        </div>
      </div>
    </div>
  </section>


  <!-- =====================================================
       2. OPEN-SOURCE SOFTWARE SUITE (ALL 7 APPS)
       ===================================================== -->

  <section id="projects" class="zv-section">
    <div class="zv-section-header">
      <div>
        <div class="zv-card-category">Software suite · 6 Linux + 1 Android TV</div>
        <h2 class="zv-section-title">Open-Source Projects</h2>
      </div>
      <div style="display:flex; gap:16px; align-items:center;">
        <a href="{{ '/downloads/' | relative_url }}" class="zv-section-link">Downloads Hub →</a>
        <a href="{{ '/projects/' | relative_url }}" class="zv-project-github-link">All Projects →</a>
      </div>
    </div>

    <div class="zv-projects-grid">
      {% for product in linux_products %}
        {% assign rel = site.data.release_manifest.projects | where: "id", product.id | first %}
        <article class="zv-card zv-project-card">

          <!-- Animated Mini Motion Thumbnail per App -->
          {% if product.id == 'sc' %}
            <div class="zv-project-visual zv-visual-sc" aria-hidden="true">
              <div class="zv-visual-toolbar">
                <span class="zv-visual-badge"><span class="zv-dot zv-dot-cobalt"></span> COCKPIT + HUD</span>
                <span class="zv-visual-code">SO_PEERCRED</span>
              </div>
              <div class="zv-visual-sc-body">
                <div class="zv-sc-hud-bar"><span>"Check net traffic &amp; clean old builds"</span><span style="color:#38B6F0;">⌘⇧␣</span></div>
                <div class="zv-sc-bridges-row">
                  <span class="zv-sc-pill">ssp.sock</span><span class="zv-sc-pill">eep.sock</span><span class="zv-sc-pill">alp.sock</span><span class="zv-sc-pill">atp.sock</span><span class="zv-sc-pill">nwp.sock</span>
                </div>
              </div>
            </div>
          {% elsif product.id == 'ssp' %}
            <div class="zv-project-visual zv-visual-ssp" aria-hidden="true">
              <div class="zv-visual-toolbar">
                <span class="zv-visual-badge"><span class="zv-dot zv-dot-red"></span> PIPEWIRE PORTAL</span>
                <span class="zv-visual-code">MKV → MP4</span>
              </div>
              <div class="zv-viewfinder-viewport">
                <div class="zv-reticle zv-reticle-tl"></div><div class="zv-reticle zv-reticle-tr"></div>
                <div class="zv-reticle zv-reticle-bl"></div><div class="zv-reticle zv-reticle-br"></div>
                <div class="zv-viewfinder-window">
                  <div class="zv-sim-cursor"></div>
                  <div class="zv-sim-pip"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 7l-7 5 7 5V7z"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg></div>
                </div>
              </div>
            </div>
          {% elsif product.id == 'eep' %}
            <div class="zv-project-visual zv-visual-eep" aria-hidden="true">
              <div class="zv-visual-toolbar">
                <span class="zv-visual-badge"><span class="zv-dot zv-dot-cobalt"></span> GSTREAMER 60FPS</span>
                <span class="zv-visual-code">00:01:24:18</span>
              </div>
              <div class="zv-timeline-viewport">
                <div class="zv-timeline-track zv-track-video">
                  <div class="zv-track-clip zv-clip-vid1"><span>CLIP_A01.mkv</span></div>
                  <div class="zv-track-clip zv-clip-vid2"><span>GRADE.vaapi</span></div>
                </div>
                <div class="zv-timeline-track zv-track-audio">
                  <div class="zv-track-clip zv-clip-aud1"><svg class="zv-wave-svg" viewBox="0 0 120 12" preserveAspectRatio="none"><path d="M0,6 Q10,0 20,6 T40,6 T60,6 T80,6 T100,6 T120,6" fill="none" stroke="currentColor" stroke-width="1.5"/></svg><span>VOICE.wav</span></div>
                  <div class="zv-track-clip zv-clip-aud2"><span>CAPTIONS</span></div>
                </div>
                <div class="zv-timeline-playhead"></div>
              </div>
            </div>
          {% elsif product.id == 'alp' %}
            <div class="zv-project-visual zv-visual-alp" aria-hidden="true">
              <div class="zv-visual-toolbar">
                <span class="zv-visual-badge"><span class="zv-dot zv-dot-cyan"></span> DSP · 48 KHZ</span>
                <span class="zv-visual-code">14 MCP TOOLS</span>
              </div>
              <div class="zv-spectrum-viewport">
                <div class="zv-spectrum-bars">
                  <span style="--i:1; --h:65%;"></span><span style="--i:2; --h:85%;"></span><span style="--i:3; --h:45%;"></span><span style="--i:4; --h:95%;"></span>
                  <span style="--i:5; --h:75%;"></span><span style="--i:6; --h:60%;"></span><span style="--i:7; --h:88%;"></span><span style="--i:8; --h:70%;"></span>
                  <span style="--i:9; --h:92%;"></span><span style="--i:10; --h:55%;"></span><span style="--i:11; --h:80%;"></span><span style="--i:12; --h:62%;"></span>
                </div>
                <div class="zv-spectrum-grid"></div>
              </div>
            </div>
          {% elsif product.id == 'atp' %}
            <div class="zv-project-visual zv-visual-atp" aria-hidden="true">
              <div class="zv-visual-toolbar">
                <span class="zv-visual-badge"><span class="zv-dot zv-dot-emerald"></span> QUARANTINE VAULT</span>
                <span class="zv-visual-code">SHA-256 LOCK</span>
              </div>
              <div class="zv-visual-atp-body">
                <div class="zv-atp-gauge-row">
                  <div class="zv-atp-stat"><span class="zv-atp-stat-label">Vault</span><span class="zv-atp-stat-val">Reversible</span></div>
                  <div class="zv-atp-stat"><span class="zv-atp-stat-label">Shell</span><span class="zv-atp-stat-val">Zero sh</span></div>
                  <div class="zv-atp-stat"><span class="zv-atp-stat-label">Distros</span><span class="zv-atp-stat-val">apt/dnf/arc</span></div>
                </div>
                <div class="zv-atp-scan-track"><div class="zv-atp-scan-fill"></div></div>
              </div>
            </div>
          {% elsif product.id == 'nwp' %}
            <div class="zv-project-visual zv-visual-nwp" aria-hidden="true">
              <div class="zv-visual-toolbar">
                <span class="zv-visual-badge"><span class="zv-dot zv-dot-cyan"></span> AYA EBPF PROBES</span>
                <span class="zv-visual-code">1 HZ SQLITE</span>
              </div>
              <div class="zv-visual-nwp-body" style="padding:8px 14px;">
                <svg class="zv-nwp-spark" viewBox="0 0 320 56" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M 0,44 L 30,36 L 60,40 L 90,22 L 120,28 L 150,12 L 180,20 L 210,10 L 240,24 L 270,15 L 300,19 L 320,14" stroke="#3355FF" stroke-width="2" class="zv-nwp-flow-line"/>
                  <path d="M 0,50 L 40,46 L 80,48 L 120,40 L 160,44 L 200,34 L 240,39 L 280,32 L 320,36" stroke="#38B6F0" stroke-width="1.5" opacity="0.8"/>
                </svg>
              </div>
            </div>
          {% endif %}

          <div class="zv-card-body zv-project-card-body">
            <div style="display:flex; align-items:flex-start; justify-content:space-between; gap:10px; margin-bottom:10px;">
              <div class="zv-app-title-with-logo">
                {% if product.logo %}
                  <img src="{{ product.logo | relative_url }}" alt="{{ product.name }} logo" class="zv-app-logo-sm" width="28" height="28" loading="lazy">
                {% endif %}
                <div>
                  <div class="zv-card-category" style="margin-bottom:2px;">{{ product.license }} · Linux</div>
                  <h3 class="zv-card-title" style="margin:0;">
                    <a href="{{ product.project_url | relative_url }}">{{ product.name }}</a>
                  </h3>
                </div>
              </div>
              {% if rel.status == 'available' and rel.latest %}
                {% include downloads/release-badge.html channel=rel.latest.release_channel prerelease=rel.latest.prerelease tag_name=rel.latest.tag_name size="sm" %}
              {% endif %}
            </div>

            <p class="zv-card-excerpt">{{ product.description }}</p>

            <div class="zv-project-card-footer">
              <div style="display:flex; gap:12px; align-items:center;">
                <a href="{{ product.project_url | relative_url }}" class="zv-section-link">Explore →</a>
                <a href="{{ product.download_url | relative_url }}" class="zv-project-github-link" style="color:var(--zv-text-secondary);">{{ rel.latest.tag_name | default: "Downloads" }}</a>
              </div>
              <a href="https://github.com/{{ product.repo }}" target="_blank" rel="noopener noreferrer" class="zv-project-github-link">GitHub ↗</a>
            </div>
          </div>
        </article>
      {% endfor %}

      <!-- 7th Project: Your TV Friend (Android TV, left WITHOUT logo as requested) -->
      {% for product in android_products %}
        {% assign rel = site.data.release_manifest.projects | where: "id", product.id | first %}
        <article class="zv-card zv-project-card">
          <div class="zv-project-visual zv-visual-ytf" aria-hidden="true">
            <div class="zv-visual-toolbar">
              <span class="zv-visual-badge"><span class="zv-dot zv-dot-emerald"></span> ADB TV LAUNCHER</span>
              <span class="zv-visual-code">297 PROFILES</span>
            </div>
            <div class="zv-tv-viewport">
              <div class="zv-tv-screen">
                <div class="zv-tv-tile"></div>
                <div class="zv-tv-tile zv-tile-active"></div>
                <div class="zv-tv-tile"></div>
              </div>
              <div class="zv-adb-status">
                <span class="zv-adb-tag">ROOTLESS SAFE</span>
              </div>
            </div>
          </div>
          <div class="zv-card-body zv-project-card-body">
            <div style="display:flex; align-items:flex-start; justify-content:space-between; gap:10px; margin-bottom:10px;">
              <div>
                <div class="zv-card-category" style="margin-bottom:2px;">{{ product.license }} · Android TV</div>
                <h3 class="zv-card-title" style="margin:0;">
                  <a href="{{ product.project_url | relative_url }}">{{ product.name }}</a>
                </h3>
              </div>
              {% if rel.status == 'available' and rel.latest %}
                {% include downloads/release-badge.html channel=rel.latest.release_channel prerelease=rel.latest.prerelease tag_name=rel.latest.tag_name size="sm" %}
              {% endif %}
            </div>

            <p class="zv-card-excerpt">{{ product.description }}</p>

            <div class="zv-project-card-footer">
              <div style="display:flex; gap:12px; align-items:center;">
                <a href="{{ product.project_url | relative_url }}" class="zv-section-link">Explore →</a>
                <a href="{{ product.download_url | relative_url }}" class="zv-project-github-link" style="color:var(--zv-text-secondary);">{{ rel.latest.tag_name | default: "Downloads" }}</a>
              </div>
              <a href="https://github.com/{{ product.repo }}" target="_blank" rel="noopener noreferrer" class="zv-project-github-link">GitHub ↗</a>
            </div>
          </div>
        </article>
      {% endfor %}
    </div>
  </section>


  <!-- =====================================================
       3. WHY ZVIROX (HUMANIZED ENGINEERING PRINCIPLES)
       ===================================================== -->

  <section class="zv-section">
    <div class="zv-section-header">
      <div>
        <div class="zv-card-category">How every app is built</div>
        <h2 class="zv-section-title">Built for Local Ownership</h2>
      </div>
    </div>

    <div class="zv-features-grid">
      <div class="zv-feature-card">
        <div class="zv-feature-icon" aria-hidden="true">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="8" rx="2" ry="2"/><rect x="2" y="14" width="20" height="8" rx="2" ry="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/></svg>
        </div>
        <h3 class="zv-feature-title">Runs Offline by Default</h3>
        <p class="zv-feature-desc">
          Videos, voice profiles, network traffic logs, and disk scans stay on your drive. Nothing sends background pings or requires an account to start working.
        </p>
      </div>

      <div class="zv-feature-card">
        <div class="zv-feature-icon" aria-hidden="true">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/></svg>
        </div>
        <h3 class="zv-feature-title">Verified Local Automation</h3>
        <p class="zv-feature-desc">
          Starship Control talks to companion apps over kernel-checked Linux Unix sockets instead of open localhost ports. Read checks run directly; file edits stop for your click.
        </p>
      </div>

      <div class="zv-feature-card">
        <div class="zv-feature-icon" aria-hidden="true">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        </div>
        <h3 class="zv-feature-title">Inspectable Open Code</h3>
        <p class="zv-feature-desc">
          Every app publishes public source trees under AGPL-3.0, Apache-2.0, or MIT alongside automated SHA-256 package digests generated directly on GitHub Actions.
        </p>
      </div>
    </div>
  </section>


  <!-- =====================================================
       4. MEASURED METRICS
       ===================================================== -->

  <section class="zv-section">
    <div class="zv-section-header">
      <div>
        <div class="zv-card-category">Codebase numbers</div>
        <h2 class="zv-section-title">Across the Suite</h2>
      </div>
    </div>

    <div class="zv-numbers-grid">
      <div class="zv-number-card">
        <span class="zv-number-val">7</span>
        <span class="zv-number-label">Open Apps</span>
        <span class="zv-number-sub">6 Linux desktop + 1 Android TV</span>
      </div>
      <div class="zv-number-card">
        <span class="zv-number-val">3</span>
        <span class="zv-number-label">Linux Formats</span>
        <span class="zv-number-sub">.deb, .rpm, and Arch .pkg.tar.zst</span>
      </div>
      <div class="zv-number-card">
        <span class="zv-number-val">489</span>
        <span class="zv-number-label">Editor Commands</span>
        <span class="zv-number-sub">Easy Edits Pro command catalog</span>
      </div>
      <div class="zv-number-card">
        <span class="zv-number-val">14</span>
        <span class="zv-number-label">Audio MCP Tools</span>
        <span class="zv-number-sub">Audio Labs Pro local automation</span>
      </div>
      <div class="zv-number-card">
        <span class="zv-number-val">297</span>
        <span class="zv-number-label">TV Profiles</span>
        <span class="zv-number-sub">Catalogued in Your TV Friend</span>
      </div>
    </div>
  </section>


  <!-- =====================================================
       5. LICENSING PANEL
       ===================================================== -->

  <section class="zv-section">
    <div class="zv-teaser-panel">
      <div class="zv-teaser-content">
        <div class="zv-card-category">Per-project licensing</div>
        <h2 class="zv-teaser-title">Clear licenses with zero guesswork</h2>
        <p class="zv-teaser-text">
          Screen Studio Pro and Your TV Friend use MIT. Starship Control and Audio Labs Pro use Apache-2.0. Agentic Tuneup Pro, Net Watch Pro, and Easy Edits Pro use AGPL-3.0, with commercial terms available on request for Easy Edits Pro.
        </p>
      </div>
      <a href="{{ '/licensing/' | relative_url }}" class="zv-button zv-button-primary" style="white-space:nowrap;">
        Licensing Overview →
      </a>
    </div>
  </section>


  <!-- =====================================================
       6. LATEST GUIDES (4 MOST RECENT POSTS)
       ===================================================== -->

  <section class="zv-section">
    <div class="zv-section-header">
      <div>
        <div class="zv-card-category">Technical writing</div>
        <h2 class="zv-section-title">Latest Guides</h2>
      </div>
      <a href="{{ '/guides/' | relative_url }}" class="zv-section-link">All guides →</a>
    </div>

    <div class="zv-article-grid">
      {% if site.posts.size > 0 %}
        {% for post in site.posts limit: 4 %}
          <article class="zv-card">
            <div class="zv-card-body">
              {% if post.categories and post.categories.size > 0 %}
                <div class="zv-card-category">{{ post.categories | first }}</div>
              {% else %}
                <div class="zv-card-category">Guide</div>
              {% endif %}
              <h3 class="zv-card-title">
                <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
              </h3>
              {% if post.excerpt %}
                <p class="zv-card-excerpt">{{ post.excerpt | strip_html | truncate: 140 }}</p>
              {% endif %}
              <div class="zv-card-meta">
                <span>{{ post.date | date: "%b %d, %Y" }}</span>
                <span>•</span>
                <span>Read →</span>
              </div>
            </div>
          </article>
        {% endfor %}
      {% endif %}
    </div>
  </section>


  <!-- =====================================================
       7. CLOSING CALL TO ACTION
       ===================================================== -->

  <section class="zv-section">
    <div class="zv-hero" style="margin-bottom:0; padding:44px 36px;">
      <div class="zv-hero-content" style="max-width:740px;">
        <div class="zv-card-category">Built in public</div>
        <h2>Inspect the source. Run the binaries.</h2>
        <p style="margin-bottom:24px;">
          Maintained solo by Prakashpuri Gauswami (@zvirox) in Patan, Gujarat, India. Bug reports, pull requests, and security audits are always welcome on GitHub.
        </p>
        <div style="display:flex; gap:12px; flex-wrap:wrap;">
          <a href="https://github.com/zvirox" target="_blank" rel="noopener noreferrer" class="zv-button zv-button-primary">GitHub Profile ↗</a>
          <a href="https://github.com/sponsors/zvirox" target="_blank" rel="noopener noreferrer" class="zv-button zv-button-secondary">Sponsor on GitHub ↗</a>
          <a href="mailto:info@zvirox.in" class="zv-button zv-button-secondary">info@zvirox.in</a>
        </div>
      </div>
    </div>
  </section>

</div>
