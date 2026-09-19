---
layout: default
title: "Home"
permalink: /
no_masthead: true
---

<section class="hero" aria-label="Introduction">
  <picture class="hero-media">
    <source media="(max-width: 700px)" type="image/webp" srcset="{{ site.baseurl }}/assets/img/home/hero-mobile.webp">
    <source media="(max-width: 700px)" srcset="{{ site.baseurl }}/assets/img/home/hero-mobile.jpg">
    <source type="image/webp" srcset="{{ site.baseurl }}/assets/img/home/hero-desktop.webp">
    <img class="hero-img"
         src="{{ site.baseurl }}/assets/img/home/hero-desktop.jpg"
         alt="Abhiram at a forge in a master smith's workshop in Gifu, Japan, a fountain of orange sparks rising from the hearth beside him."
         width="1600" height="1000" fetchpriority="high" decoding="async">
  </picture>

  <a class="hero-resume mono" href="{{ site.baseurl }}/resume/">Résumé <span aria-hidden="true">→</span></a>

  <div class="hero-caption wrap">
    <h1 class="hero-name">{{ site.author }}</h1>
    <p class="hero-tagline">{{ site.tagline }}</p>
    <p class="hero-credit mono">Forge of Asano Kajiya · Gifu, Japan · 2024</p>
  </div>
</section>

<section class="highlights wrap" aria-label="Highlights">
  <p class="highlights-lead">Most of it designed, built by hand, and taken into the field — often where the budget is thin and the constraint is the point.</p>
  <ul class="highlights-list">
    {% for h in site.data.highlights %}
    <li class="highlight">
      <span class="highlight-label mono">{{ h.label }}</span>
      <p class="highlight-text">{{ h.text }}</p>
    </li>
    {% endfor %}
  </ul>
</section>

<section class="work wrap" aria-label="Selected work">
  {% for slug in site.data.order %}
    {% assign p = site.projects | where: "slug", slug | first %}
    {% if p %}{% include card.html p=p %}{% endif %}
  {% endfor %}
</section>
