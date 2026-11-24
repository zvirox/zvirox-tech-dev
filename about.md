---
layout: default
title: About Zvirox & Maintainer
description: Prakashpuri Gauswami (@zvirox) — Cybersecurity Analyst, SOC Practitioner, and open-source Linux & Android TV software builder in Gujarat, India.
permalink: /about/
---

{% assign linux_products = site.data.download_products | where: "category", "linux" %}
{% assign android_products = site.data.download_products | where: "category", "android" %}

<div class="zv-container">

  <!-- HERO SECTION -->
  <section class="zv-about-hero">
    <div class="zv-about-hero-content">
      <div class="zv-card-category">Maintainer · Cyber Defender · Gujarat, India</div>
      <h1 class="zv-about-hero-title">
        Hi, I'm Prakashpuri Gauswami <span>(@zvirox)</span>
      </h1>
      <p class="zv-about-hero-lead">
        Cybersecurity Analyst, SOC Practitioner, and Agentic AI Builder in Patan, Gujarat, India. I orchestrate AI coding agents to build open-source Linux desktop and Android TV tools that keep user data strictly offline.
      </p>
    </div>
  </section>

  <!-- MAINTAINER & MISSION -->
  <section class="zv-about-intro">
    <div class="zv-content">
      <p>
        I hold a Bachelor of Computer Applications (BCA) degree and spend my time focused on <strong>Blue Team operations, SOC analysis, SIEM monitoring, and threat detection</strong>.
      </p>

      <p>
        Before focusing full-time on defensive security and local Linux software, I worked for <strong>7+ years in banking and compliance operations</strong> across Axis Bank, Kotak Mahindra Bank, and ICICI Bank, holding a <strong>99% compliance audit score</strong> and working under strict operational controls. That background shaped how I build tools today: every destructive action needs a confirmation gate, clear audit logs, and zero silent side effects.
      </p>

      <p>
        As an <strong>agentic AI builder and vibe coder</strong>, I direct AI coding agents to architect and ship real working applications under <a href="https://zvirox.in">zvirox.in</a> for three reasons:
      </p>

      <ul>
        <li>
          <strong>Hands-On System Security:</strong> Building real desktop apps forces me to inspect IPC channels, kernel Unix socket peer credentials, privilege boundaries, and package integrity pipelines first-hand.
        </li>
        <li>
          <strong>Tools I Actually Use:</strong> I love creating audio and video on Linux without paying cloud subscriptions or shipping raw footage to third-party servers.
        </li>
        <li>
          <strong>Local-First Open Source:</strong> Giving fellow Linux and Android TV users fast utilities that run privately on their own drives.
        </li>
      </ul>

      <p class="zv-about-philosophy">
        <strong>Independent &amp; Non-Commercial:</strong> Zvirox has zero investors, zero ads, and zero telemetry. Work is backed by community feedback, <a href="https://github.com/sponsors/zvirox" target="_blank" rel="noopener noreferrer">GitHub Sponsors</a>, and <a href="https://ko-fi.com/zvirox" target="_blank" rel="noopener noreferrer">Ko-fi</a>.
      </p>
    </div>
  </section>

  <!-- CYBERSECURITY & DEFENSIVE HOMELAB -->
  <section class="zv-section">
    <div class="zv-section-header">
      <div>
        <div class="zv-card-category">Security operations</div>
        <h2 class="zv-section-title">Defensive Homelab &amp; Toolkit</h2>
      </div>
    </div>

    <div class="zv-features-grid">
      <div class="zv-feature-card">
        <h3 class="zv-feature-title">SIEM &amp; Endpoint Telemetry</h3>
        <p class="zv-feature-desc">
          Virtualized multi-node KVM/QEMU security lab running <strong>Wazuh SIEM</strong> to collect centralized logs, investigate <strong>Windows Sysmon</strong> telemetry, and audit Linux system events.
        </p>
      </div>
      <div class="zv-feature-card">
        <h3 class="zv-feature-title">Network &amp; Protocol Analysis</h3>
        <p class="zv-feature-desc">
          Packet inspection in <strong>Wireshark</strong>, host discovery and port enumeration with <strong>Nmap</strong>, and practical TCP/IP, DNS, DHCP, and SSH hardening diagnostics.
        </p>
      </div>
      <div class="zv-feature-card">
        <h3 class="zv-feature-title">OS Hardening &amp; Stack</h3>
        <p class="zv-feature-desc">
          Daily driver administration across Arch Linux, Fedora, Ubuntu, and Kali Linux alongside Rust, Java, Python, TypeScript, Tauri 2, React 19, Aya eBPF, and GStreamer.
        </p>
      </div>
    </div>
  </section>

  <!-- ALL 7 OPEN-SOURCE PROJECTS -->
  <section class="zv-section">
    <div class="zv-section-header">
      <div>
        <div class="zv-card-category">Open-source suite</div>
        <h2 class="zv-section-title">What I Build ({{ site.data.download_products.size }} Apps)</h2>
      </div>
      <a href="{{ '/downloads/' | relative_url }}" class="zv-section-link">Downloads Hub →</a>
    </div>

    <div class="zv-projects-grid">
      {% for product in linux_products %}
        {% assign rel = site.data.release_manifest.projects | where: "id", product.id | first %}
        <article class="zv-card zv-project-card">
          <div class="zv-card-body zv-project-card-body">
            <div style="display:flex; align-items:flex-start; justify-content:space-between; gap:10px; margin-bottom:12px;">
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
                <a href="{{ product.project_url | relative_url }}" class="zv-section-link">Overview →</a>
                <a href="{{ product.download_url | relative_url }}" class="zv-project-github-link">{{ rel.latest.tag_name | default: "Downloads" }}</a>
              </div>
              <a href="https://github.com/{{ product.repo }}" target="_blank" rel="noopener noreferrer" class="zv-project-github-link">GitHub ↗</a>
            </div>
          </div>
        </article>
      {% endfor %}

      {% for product in android_products %}
        {% assign rel = site.data.release_manifest.projects | where: "id", product.id | first %}
        <article class="zv-card zv-project-card">
          <div class="zv-card-body zv-project-card-body">
            <div style="display:flex; align-items:flex-start; justify-content:space-between; gap:10px; margin-bottom:12px;">
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
                <a href="{{ product.project_url | relative_url }}" class="zv-section-link">Overview →</a>
                <a href="{{ product.download_url | relative_url }}" class="zv-project-github-link">{{ rel.latest.tag_name | default: "Downloads" }}</a>
              </div>
              <a href="https://github.com/{{ product.repo }}" target="_blank" rel="noopener noreferrer" class="zv-project-github-link">GitHub ↗</a>
            </div>
          </div>
        </article>
      {% endfor %}
    </div>
  </section>

  <!-- VERIFICATION BLOCK -->
  <section class="zv-section">
    <div class="zv-section-header">
      <div>
        <div class="zv-card-category">Public records</div>
        <h2 class="zv-section-title">Career Focus &amp; Identity</h2>
      </div>
    </div>

    <div class="zv-verification-box">
      <div class="zv-verification-row">
        <span class="zv-verification-label">Maintainer</span>
        <span class="zv-verification-value">Prakashpuri Gauswami (@zvirox)</span>
      </div>
      <div class="zv-verification-row">
        <span class="zv-verification-label">Location</span>
        <span class="zv-verification-value">Patan, Gujarat, India</span>
      </div>
      <div class="zv-verification-row">
        <span class="zv-verification-label">Role Focus</span>
        <span class="zv-verification-value">SOC Analyst L1 / Blue Team Security Operations</span>
      </div>
      <div class="zv-verification-row">
        <span class="zv-verification-label">General Email</span>
        <span class="zv-verification-value"><a href="mailto:info@zvirox.in">info@zvirox.in</a></span>
      </div>
      <div class="zv-verification-row">
        <span class="zv-verification-label">Direct &amp; Security</span>
        <span class="zv-verification-value"><a href="mailto:zvirox@proton.me">zvirox@proton.me</a></span>
      </div>
      <div class="zv-verification-row">
        <span class="zv-verification-label">Sponsor</span>
        <span class="zv-verification-value">
          <a href="https://github.com/sponsors/zvirox" target="_blank" rel="noopener noreferrer">GitHub Sponsors ↗</a> ·
          <a href="https://ko-fi.com/zvirox" target="_blank" rel="noopener noreferrer">Ko-fi ↗</a>
        </span>
      </div>
      <div class="zv-verification-row">
        <span class="zv-verification-label">Social Profiles</span>
        <span class="zv-verification-value">
          <a href="https://github.com/zvirox" target="_blank" rel="noopener noreferrer">GitHub</a> ·
          <a href="https://www.linkedin.com/in/plgsevala" target="_blank" rel="noopener noreferrer">LinkedIn</a> ·
          <a href="https://www.youtube.com/@zvirox_in" target="_blank" rel="noopener noreferrer">YouTube</a> ·
          <a href="https://www.instagram.com/plg.sevala" target="_blank" rel="noopener noreferrer">Instagram</a> ·
          <a href="https://www.facebook.com/plg.sevala" target="_blank" rel="noopener noreferrer">Facebook</a>
        </span>
      </div>
    </div>
  </section>

</div>
