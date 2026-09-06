# Abhiram Rachamadugu — portfolio

A map-led portfolio that sits alongside the one-page résumé PDF. A recruiter
reads the PDF in twenty seconds; this is where they go if it made them curious.

The organising idea is **a map of where the work happened** — Bengaluru, rural
Kadapa, a plant at Nelamangala, campuses in India, and Urbana-Champaign,
Illinois. The map is an **index, not the product**: what sits behind the pins
matters more than the map itself.

This file is the handoff for whoever fills in the content. Read it first.

---

## Ground rules (do not break these)

- **No JavaScript.** No `<script>` tags, no libraries, no analytics, no cookie
  banner. There is nothing to consent to. `grep -rn "<script" .` must stay empty.
- **Jekyll, built natively by GitHub Pages.** No Actions, no Node, no
  `package.json`. Content is Markdown + YAML front matter.
- **Tone is civilian throughout.** No defence framing, no weapons language, no
  marketing register. Sentence case everywhere (proper nouns aside); all-caps
  only in the letterspaced mono metadata labels.
- **Colour discipline.** `--mark` (the one red) appears only on map pins and
  prose link underlines. A page with fifteen red things stops reading as a map.
- **No dark mode.** An old map is a light object.
- **All internal links use `{{ site.baseurl }}`.** Never hard-code the domain.

`assets/css/main.css` is finished — the design system lives there. You should
not need to redesign it; add content, don't restyle.

---

## Local preview (optional)

GitHub Pages builds this for you. To preview locally you need Ruby + Jekyll:

```bash
gem install jekyll bundler
jekyll serve
```

(There is deliberately no `Gemfile`; if you add one, use the `github-pages`
gem so local output matches production, and keep `Gemfile`/`Gemfile.lock`
excluded in `_config.yml`.)

---

## Repo layout

```
_config.yml            site config, collections, permalinks, contact placeholders
index.md               the home page: map + stat strip + statement + text index
resume.md              the /resume/ page content (entries)
_layouts/              default, project, place, resume
_includes/             head.html, footer.html, map.svg (the whole map, inline)
_projects/             9 project files  ->  /work/<slug>/
_places/               3 place files    ->  /place/<slug>/
assets/css/main.css    the design system
assets/img/<slug>/     one dir per project — drop images here (currently empty)
assets/Abhiram-Rachamadugu-Resume.pdf   PLACEHOLDER — replace with the real PDF
```

Collections and permalinks (already set in `_config.yml`):

```yaml
collections:
  projects: { output: true, permalink: /work/:name/ }
  places:   { output: true, permalink: /place/:name/ }
```

`:name` is the filename without extension, so `_projects/taiyo-aerospace.md`
publishes at `/work/taiyo-aerospace/`. Layouts are auto-assigned by `defaults`,
so collection files need no `layout:` field.

---

## How to add or edit a project

Create `_projects/<slug>.md`. **Every field is present on every file**; use
`null` rather than omitting one. Copy this block:

```yaml
---
title: "Sentence-case project name"
slug: my-project              # must equal the filename
org: "Organisation"
role: "Your role"             # null for personal work
status: in-service            # in-service | in-build | ongoing | archived | worked-on-site
place: "Town, region"
coords: [14.47, 78.82]        # [lat, lon]; lon negative for west
dates: "Aug 2021 – Mar 2023"
scale: "30+ units"            # honest counter, or null
users: "Who it serves"        # or null
constraint: "The binding constraint"   # or null
depth: deep                   # deep | medium | thin  (how long the page should be)
hero: /assets/img/my-project/hero.jpg
tags: [thermal, deployed]     # or null
order: 5                      # sort position in the home list
---
```

Two fields carry the most weight and the layout gives them prominence:

- **`role`** — a pin silently implies ownership. "Engineering intern, three
  months" reads very differently from a founder line. Be precise; one inflated
  entry makes a reader discount all of them.
- **`status`** — `in-build` is not `in-service`. Label honestly so the deployed
  entries read as trustworthy. The values: `in-service` (deployed and running),
  `in-build` (being built, not yet deployed), `ongoing` (a continuing practice
  that is neither deployed nor archived), `archived` (finished, not maintained),
  `worked-on-site` (a role at someone else's site). Each has a status-tag style
  in `main.css`.

### Project body structure

The Markdown body fills, in this order (headings already stubbed in each file):

1. What it is
2. The problem and the constraint
3. What I did
4. What went wrong
5. Gallery

Images go in `assets/img/<slug>/`. Lay a gallery out with the `.gallery` grid:

```html
<div class="gallery">
  <figure><img src="{{ site.baseurl }}/assets/img/my-project/1.jpg" alt="…">
    <figcaption class="caption">Caption.</figcaption></figure>
</div>
```

**Video:** never self-host, never embed an iframe. Use a static poster image
inside a link to YouTube (the `.video-poster` class adds the “watch” overlay):

```html
<a class="video-poster" href="https://youtu.be/ID" rel="noopener">
  <img src="{{ site.baseurl }}/assets/img/my-project/poster.jpg" alt="…">
</a>
```

Optional end-of-page links: add a `links:` list to the front matter
(`- { label: "Repo", url: "https://…" }`) and the layout renders a Links block.

---

## How to add or edit a place

`_places/<slug>.md` needs a title, coords, and the list of project slugs it
contains. The “Work here” list is generated from that list:

```yaml
---
title: "Bengaluru"
slug: bengaluru
coords: [12.97, 77.59]
projects: [taiyo-aerospace, ati-motors-amr, abb-tata-motors]
---
```

There are three places: `bengaluru`, `kadapa`, `urbana-champaign`.

---

## The résumé

`resume.md` uses the `resume` layout and is styled as a printed record (ruled
sections, mono dates in a right-hand column). The experience/project entries are
pre-filled **only** with the role/org/dates/place already fixed by the brief;
every bullet, the summary, education and skills are marked `_placeholder_` and
must be **transcribed faithfully from the PDF** — do not rewrite or reorder.

Then **replace `assets/Abhiram-Rachamadugu-Resume.pdf`** (currently a marked
placeholder) with the real one-page PDF so the download button resolves.

---

## Contact

Footer only — no form (there is no backend). The values are placeholders in
`_config.yml` under `contact:` (`email`, `phone`, `linkedin`). Nothing is
published until you fill them in.

---

## The map — how it maps to the collections

`_includes/map.svg` is the whole map: **hand-authored inline SVG, committed, no
runtime library, no JavaScript.** It is included into `index.md`. Interaction is
CSS-only (hover, focus) and the styling lives in `main.css` (search `--- Map SVG`).

Every pin is a link and every destination is **also** in the plain text list
below the map, so the site is fully navigable — and keyboard-accessible —
without touching the map. Keep that invariant.

### Pin inventory

| Pin | Tier | Panel | Links to |
|---|---|---|---|
| Bengaluru | primary (worked) | South India + inset | `/place/bengaluru/` |
| Kadapa | primary (worked) | South India | `/place/kadapa/` |
| Nelamangala | primary (worked) | inset | `/work/abb-tata-motors/` |
| Urbana-Champaign | primary (worked) | Illinois | `/place/urbana-champaign/` |
| Christ College | deployment | inset | `/work/ati-motors-amr/` |
| VIT Coimbatore | deployment | South India | `/work/ati-motors-amr/` |
| Kadapa dryer area | deployment area (30 km circle) | South India | `/work/solar-biomass-dryer/` |

Tulsa, Oklahoma (SUAS competition) is deliberately a **text mention on the
Illini project page only** — no pin.

Primary pins are 7px filled `--mark`; deployment pins are 4px open `--mark-soft`;
the deployment *area* is a dashed 30 km-radius circle (a distribution, not a
point). To retarget a pin, edit its `<a href="{{ site.baseurl }}/…">` in
`map.svg`. To restyle any tier, edit `main.css` — do not add inline styles.

### How the geometry was made (so you can reproduce it)

The map was generated **once** by a throwaway script, then the output was
committed and the script deleted (per the brief — the repo never needs Node).
If you ever need to regenerate or add a pin at a precise coordinate, reproduce
the same setup:

- **Data:** Natural Earth `ne_50m_admin_1_states_provinces` (Indian states +
  Illinois, filtered by bounding-box overlap with each panel window) and the
  Plotly `geojson-counties-fips` file (Champaign County = FIPS `17019`).
- **Projection:** `d3-geo` `geoMercator`, fit **per panel** to a lon/lat window
  (fit the window rectangle, not the geometry bounds, then clip geography to the
  neat line). Project each pin's `[lon,lat]` with that **same** panel projection
  so pins land correctly. Round all coordinates to 1 decimal place.
- **Panel windows** (`[[W,S],[E,N]]`, degrees):
  - South India — `[[76.0, 10.5], [79.5, 15.0]]`
  - Greater Bengaluru inset — `[[77.28, 12.82], [77.78, 13.22]]`
  - Illinois — `[[-91.6, 36.8], [-87.0, 42.7]]`
- **Master frame:** `viewBox="0 0 1000 700"`. South India is translated to
  `(75, 60)`, Illinois to `(≈590, 60)`; the inset is nested inside the South
  India group in its bottom-right corner. The inset's location on the main panel
  is shown by the dashed **locator rectangle** and two leader lines — standard
  survey-sheet practice, and it keeps the Nelamangala/Bengaluru labels from
  colliding at the main panel's scale.

Moving an existing label is just editing its `x`/`y` numbers. Adding a pin at a
new coordinate means projecting that coordinate the same way — quickest via a
scratch d3-geo script using the window and translate above.

### Cartographic conventions used (keep them)

- Serif **italic** for regions/districts (Karnataka, Andhra Pradesh, …),
  serif **roman** for settlements (Bengaluru, Kadapa, …), **mono** for metadata
  (coordinates, degree ticks, scale bars, deployment labels).
- A 1px graticule behind each panel, degree ticks at the frame edges, an honest
  per-panel scale bar (the panels are at different scales — saying so is the
  point), and a double-rule neat line around each panel.
- `role="img"` on the root `<svg>` with `<title>`/`<desc>`; the text index is
  the accessible path.

---

## Responsive

Below 700px the interactive map is hidden and the text index carries navigation
(three survey panels are unusable on a phone). Everything is usable at 390px.

## Before you ship

- `grep -rn "<script" .` returns nothing.
- Every pin is reachable and activatable by keyboard alone.
- Every page is reachable without touching the map.
- 390px viewport is usable.
- No hard-coded absolute URLs — `{{ site.baseurl }}` throughout.
- Pages builds green.
