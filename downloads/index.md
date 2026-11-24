---
layout: default
title: Downloads
description: Download Linux packages (.deb, .rpm, .pkg.tar.zst) and Android TV releases for all Zvirox open-source apps with SHA-256 verification.
permalink: /downloads/
---

{% assign linux_products = site.data.download_products | where: "category", "linux" %}
{% assign android_products = site.data.download_products | where: "category", "android" %}

<div class="zv-container zv-page-container">

  <!-- Hub Header -->
  <header class="zv-downloads-hero" style="text-align:left; margin:0 0 36px; max-width:none;">
    <div class="zv-card-category">Official packages · Verified on GitHub Releases</div>
    <h1 class="zv-downloads-title">Software Downloads</h1>
    <p class="zv-downloads-subtitle" style="margin:0; max-width:680px;">
      Pick an app below to open its installers, distro commands, release notes, and SHA-256 checksums. Every package runs locally without telemetry.
    </p>
  </header>

  <!-- Category 1: Linux Desktop Suite (6 Apps, with Logos) -->
  <section class="zv-dl-category-block" aria-labelledby="dl-linux-heading">
    <div class="zv-dl-category-header">
      <h2 id="dl-linux-heading" class="zv-dl-category-title">Linux Desktop Apps</h2>
      <span class="zv-dl-category-count">{{ linux_products.size }} apps · .deb / .rpm / .pkg.tar.zst</span>
    </div>

    <div class="zv-dl-hub-grid">
      {% for product in linux_products %}
        {% assign manifest_proj = site.data.release_manifest.projects | where: "id", product.id | first %}
        <article class="zv-dl-app-card">
          <div class="zv-dl-app-card-top">
            <div class="zv-dl-app-id-wrap">
              {% if product.logo %}
                <img
                  src="{{ product.logo | relative_url }}"
                  alt="{{ product.name }} logo"
                  class="zv-app-logo-chip"
                  width="40"
                  height="40"
                  loading="lazy"
                >
              {% endif %}
              <div>
                <h3 class="zv-dl-app-name">
                  <a href="{{ product.download_url | relative_url }}">{{ product.name }}</a>
                </h3>
                <span class="zv-dl-app-license">{{ product.license }}</span>
              </div>
            </div>

            <div class="zv-download-status-pills">
              {% if manifest_proj.status == 'available' and manifest_proj.latest %}
                {% include downloads/release-badge.html channel=manifest_proj.latest.release_channel prerelease=manifest_proj.latest.prerelease tag_name=manifest_proj.latest.tag_name %}
                <span class="zv-badge zv-badge-version">{{ manifest_proj.latest.tag_name | escape }}</span>
              {% else %}
                <span class="zv-badge zv-badge-planning">Planned</span>
              {% endif %}
            </div>
          </div>

          <p class="zv-dl-app-desc">{{ product.tagline }}. {{ product.description }}</p>

          <div class="zv-dl-app-formats">
            <span class="zv-tag">.deb</span>
            <span class="zv-tag">.rpm</span>
            <span class="zv-tag">.pkg.tar.zst</span>
            <span class="zv-tag">SHA256</span>
          </div>

          <div class="zv-dl-app-actions">
            <a href="{{ product.download_url | relative_url }}" class="zv-button zv-button-primary" style="min-height:38px; padding:0 14px; font-size:13px;">
              Open Downloads →
            </a>
            <div style="display:flex; gap:14px; align-items:center;">
              <a href="{{ product.project_url | relative_url }}" class="zv-link-subtle">Project</a>
              <a href="https://github.com/{{ product.repo }}" target="_blank" rel="noopener noreferrer" class="zv-link-subtle">GitHub ↗</a>
            </div>
          </div>
        </article>
      {% endfor %}
    </div>
  </section>

  <!-- Category 2: Android Apps (1 App, left WITHOUT logo as requested) -->
  <section class="zv-dl-category-block" aria-labelledby="dl-android-heading">
    <div class="zv-dl-category-header">
      <h2 id="dl-android-heading" class="zv-dl-category-title">Android Apps</h2>
      <span class="zv-dl-category-count">{{ android_products.size }} app · .apk + ADB toolkit</span>
    </div>

    <div class="zv-dl-hub-grid">
      {% for product in android_products %}
        {% assign manifest_proj = site.data.release_manifest.projects | where: "id", product.id | first %}
        <article class="zv-dl-app-card">
          <div class="zv-dl-app-card-top">
            <div class="zv-dl-app-id-wrap">
              <div>
                <h3 class="zv-dl-app-name">
                  <a href="{{ product.download_url | relative_url }}">{{ product.name }}</a>
                </h3>
                <span class="zv-dl-app-license">{{ product.license }} · Android TV 8.0+</span>
              </div>
            </div>

            <div class="zv-download-status-pills">
              {% if manifest_proj.status == 'available' and manifest_proj.latest %}
                {% include downloads/release-badge.html channel=manifest_proj.latest.release_channel prerelease=manifest_proj.latest.prerelease tag_name=manifest_proj.latest.tag_name %}
                <span class="zv-badge zv-badge-version">{{ manifest_proj.latest.tag_name | escape }}</span>
              {% endif %}
            </div>
          </div>

          <p class="zv-dl-app-desc">{{ product.tagline }}. {{ product.description }}</p>

          <div class="zv-dl-app-formats">
            <span class="zv-tag">.apk</span>
            <span class="zv-tag">ADB CLI</span>
            <span class="zv-tag">SHA256</span>
          </div>

          <div class="zv-dl-app-actions">
            <a href="{{ product.download_url | relative_url }}" class="zv-button zv-button-primary" style="min-height:38px; padding:0 14px; font-size:13px;">
              Open Downloads →
            </a>
            <div style="display:flex; gap:14px; align-items:center;">
              <a href="{{ product.project_url | relative_url }}" class="zv-link-subtle">Project</a>
              <a href="https://github.com/{{ product.repo }}" target="_blank" rel="noopener noreferrer" class="zv-link-subtle">GitHub ↗</a>
            </div>
          </div>
        </article>
      {% endfor %}
    </div>
  </section>

  <!-- Integrity Verification Note -->
  <aside class="zv-integrity-card" style="margin-top:44px;">
    <div class="zv-integrity-header">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" class="zv-integrity-icon"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
      <div>
        <h2 class="zv-integrity-title">Daily Sync &amp; SHA-256 Verification</h2>
        <p class="zv-integrity-sub">Release manifest refreshes daily at 06:00 AM IST directly from GitHub Releases.</p>
      </div>
    </div>
    <div class="zv-integrity-body">
      <div class="zv-integrity-step">
        <span class="zv-step-number">1</span>
        <div>
          <strong>Verify Package Digest</strong>
          <p>Run <code>sha256sum &lt;package-file&gt;</code> locally and match it with the SHA-256 digest shown on each app download page.</p>
        </div>
      </div>
      <div class="zv-integrity-step">
        <span class="zv-step-number">2</span>
        <div>
          <strong>Open Build Pipeline</strong>
          <p>All binaries compile from public tags inside GitHub Actions using <code>zvirox/release-workflows</code>.</p>
        </div>
      </div>
    </div>
  </aside>

</div>
