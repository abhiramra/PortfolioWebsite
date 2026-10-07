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

  <div class="hero-caption wrap">
    <h1 class="hero-name">{{ site.author }}</h1>
    <p class="hero-tagline">{{ site.tagline }}</p>
    <p class="hero-credit mono">Forge of Asano Kajiya · Gifu, Japan · 2024</p>
  </div>
</section>

<section class="highlights wrap" aria-label="Highlights">
  <p class="highlights-intro">I'm a mechanical engineer and a repeat founder, with work across an exceptionally wide range of fields. I'm as comfortable with the project management as with the engineering — which is usually what decides if the engineering is used. A few of the results:</p>
  <div class="highlights-row">
    <ul class="highlights-list">
      {% for h in site.data.highlights %}
      <li>{{ h }}</li>
      {% endfor %}
    </ul>
    <a class="highlights-resume mono" href="{{ site.baseurl }}/resume/">Résumé <span aria-hidden="true">→</span></a>
  </div>
</section>

<section class="work wrap" aria-label="Selected work">
  {% for slug in site.data.order %}
    {% assign p = site.projects | where: "slug", slug | first %}
    {% if p %}{% include card.html p=p %}{% endif %}
  {% endfor %}
</section>
