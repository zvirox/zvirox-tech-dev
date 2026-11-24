---
layout: default
title: Open-Source Software Projects
description: Explore all 7 open-source Linux desktop and Android TV applications built under Zvirox with Rust, Tauri 2, React 19, Java, and ADB.
permalink: /projects/
image: "/assets/images/zvirox-logo.png"
---

{% assign linux_products = site.data.download_products | where: "category", "linux" %}
{% assign android_products = site.data.download_products | where: "category", "android" %}

<div class="zv-container">

  <!-- HERO SECTION -->
  <section class="zv-about-hero">
    <div class="zv-about-hero-content">
      <div class="zv-card-category">Open-source suite · Local-first tools</div>
      <h1 class="zv-about-hero-title">
        Software built to stay <span>on your hardware.</span>
      </h1>
      <p class="zv-about-hero-lead">
        Six native Linux desktop utilities wired into Starship Control over local Unix sockets, plus an Android TV launcher and rootless ADB cleanup toolkit. Zero cloud accounts, zero telemetry.
      </p>
      <div style="display:flex; gap:12px; flex-wrap:wrap; margin-top:24px;">
        <a href="{{ '/downloads/' | relative_url }}" class="zv-button zv-button-primary">Browse Downloads →</a>
        <a href="https://github.com/zvirox" target="_blank" rel="noopener noreferrer" class="zv-button zv-button-secondary">GitHub Organization ↗</a>
      </div>
    </div>
  </section>

  <!-- LINUX DESKTOP APPS (6 Apps with Logos) -->
  <section class="zv-section" aria-labelledby="proj-linux-heading">
    <div class="zv-section-header">
      <div>
        <div class="zv-card-category">Desktop suite · .deb / .rpm / .pkg.tar.zst</div>
        <h2 id="proj-linux-heading" class="zv-section-title">Linux Desktop Apps ({{ linux_products.size }})</h2>
      </div>
      <a href="{{ '/downloads/' | relative_url }}" class="zv-section-link">Download installers →</a>
    </div>

    <div class="zv-projects-grid">
      {% for product in linux_products %}
        {% assign rel = site.data.release_manifest.projects | where: "id", product.id | first %}
        <article class="zv-card zv-project-card">
          <div class="zv-card-body zv-project-card-body">
            <div style="display:flex; align-items:flex-start; justify-content:space-between; gap:12px; margin-bottom:14px;">
              <div class="zv-app-title-with-logo">
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
                  <div class="zv-card-category" style="margin-bottom:2px;">{{ product.license }}</div>
                  <h3 class="zv-card-title" style="margin:0;">
                    <a href="{{ product.project_url | relative_url }}">{{ product.name }}</a>
                  </h3>
                </div>
              </div>
              <div style="display:flex; gap:6px; align-items:center; flex-shrink:0;">
                {% if rel.status == 'available' and rel.latest %}
                  {% include downloads/release-badge.html channel=rel.latest.release_channel prerelease=rel.latest.prerelease tag_name=rel.latest.tag_name size="sm" %}
                  <span class="zv-badge-version" style="font-size:11px; padding:2px 7px;">{{ rel.latest.tag_name | escape }}</span>
                {% endif %}
              </div>
            </div>

            <p class="zv-card-excerpt">{{ product.tagline }}. {{ product.description }}</p>

            <div class="zv-project-card-footer">
              <div style="display:flex; gap:14px; align-items:center;">
                <a href="{{ product.project_url | relative_url }}" class="zv-section-link">Architecture →</a>
                <a href="{{ product.download_url | relative_url }}" class="zv-project-github-link" style="color:var(--zv-text-secondary);">Downloads</a>
              </div>
              <a href="https://github.com/{{ product.repo }}" target="_blank" rel="noopener noreferrer" class="zv-project-github-link">GitHub ↗</a>
            </div>
          </div>
        </article>
      {% endfor %}
    </div>
  </section>

  <!-- ANDROID TV APPS (1 App, left WITHOUT logo as requested) -->
  <section class="zv-section" aria-labelledby="proj-android-heading">
    <div class="zv-section-header">
      <div>
        <div class="zv-card-category">Television &amp; ADB tools · Android 8.0+</div>
        <h2 id="proj-android-heading" class="zv-section-title">Android TV ({{ android_products.size }})</h2>
      </div>
    </div>

    <div class="zv-projects-grid">
      {% for product in android_products %}
        {% assign rel = site.data.release_manifest.projects | where: "id", product.id | first %}
        <article class="zv-card zv-project-card">
          <div class="zv-card-body zv-project-card-body">
            <div style="display:flex; align-items:flex-start; justify-content:space-between; gap:12px; margin-bottom:14px;">
              <div>
                <div class="zv-card-category" style="margin-bottom:2px;">{{ product.license }} · Android TV</div>
                <h3 class="zv-card-title" style="margin:0;">
                  <a href="{{ product.project_url | relative_url }}">{{ product.name }}</a>
                </h3>
              </div>
              <div style="display:flex; gap:6px; align-items:center; flex-shrink:0;">
                {% if rel.status == 'available' and rel.latest %}
                  {% include downloads/release-badge.html channel=rel.latest.release_channel prerelease=rel.latest.prerelease tag_name=rel.latest.tag_name size="sm" %}
                  <span class="zv-badge-version" style="font-size:11px; padding:2px 7px;">{{ rel.latest.tag_name | escape }}</span>
                {% endif %}
              </div>
            </div>

            <p class="zv-card-excerpt">{{ product.tagline }}. {{ product.description }}</p>

            <div class="zv-project-card-footer">
              <div style="display:flex; gap:14px; align-items:center;">
                <a href="{{ product.project_url | relative_url }}" class="zv-section-link">Architecture →</a>
                <a href="{{ product.download_url | relative_url }}" class="zv-project-github-link" style="color:var(--zv-text-secondary);">Downloads</a>
              </div>
              <a href="https://github.com/{{ product.repo }}" target="_blank" rel="noopener noreferrer" class="zv-project-github-link">GitHub ↗</a>
            </div>
          </div>
        </article>
      {% endfor %}
    </div>
  </section>

</div>
