---
layout: default
title: "Home"
permalink: /
---

<section class="home-head wrap-wide">
  <h1>{{ site.author }}</h1>
  <p class="tagline">{{ site.tagline }}</p>
</section>

<div class="map-wrap">
  <figure class="map-figure">
    {% include map.svg %}
    <figcaption class="map-caption caption">
      A map of where the work happened. Large pins mark where the work was done;
      small open circles and the dotted area mark where it was deployed. Select a
      pin, or use the list below — the site is fully navigable without the map.
    </figcaption>
  </figure>
</div>

<section class="stats" aria-label="By the numbers">
  <div class="stat"><span class="num">30+</span><span class="lab">dryers in service</span></div>
  <div class="stat"><span class="num">3</span><span class="lab">robots deployed</span></div>
  <div class="stat"><span class="num">1,090</span><span class="lab">scholarships</span></div>
  <div class="stat"><span class="num">2</span><span class="lab">aircraft in build</span></div>
</section>

<div class="statement">
  <p>I build hardware in places that make it hard — a forge dug into the ground in Kadapa, a bionic hand held under $200, a jet airframe laid up in a home lab. The constraint is usually the interesting part, because it decides the architecture long before any preference does. What is here is ten of those projects, including the parts that did not work.</p>
</div>

<section class="index-block">
  <h2>The work</h2>
  <p class="index-note">Every project, in one plain list — the accessible path and the mobile fallback.</p>
  <ul class="linklist">
    {% assign items = site.projects | sort: "order" %}
    {% for p in items %}
    <li>
      <a href="{{ p.url | prepend: site.baseurl }}">
        <span class="li-title">{{ p.title }}</span>
        <span class="li-org">{{ p.org }}</span>
        <span class="li-meta">{{ p.status | replace: '-', ' ' }} · {{ p.dates }}</span>
      </a>
    </li>
    {% endfor %}
  </ul>
</section>

<section class="index-block">
  <h2>Places</h2>
  <p class="index-note">The clusters the map is built around.</p>
  <ul class="linklist">
    {% assign pls = site.places | sort: "title" %}
    {% for pl in pls %}
    <li>
      <a href="{{ pl.url | prepend: site.baseurl }}">
        <span class="li-title">{{ pl.title }}</span>
        <span class="li-meta">{{ pl.projects | size }} entr{% if pl.projects.size == 1 %}y{% else %}ies{% endif %}</span>
      </a>
    </li>
    {% endfor %}
  </ul>
</section>
