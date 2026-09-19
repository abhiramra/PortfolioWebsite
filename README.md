# Abhiram Rachamadugu — portfolio

An image-led editorial portfolio that sits alongside the one-page résumé PDF. A
recruiter reads the PDF in twenty seconds; this is where they go if it made them
curious.

The organising idea is **breadth of field and adaptability** — eleven projects
spanning aerospace, autonomy, thermal engineering, materials, manufacturing and
nonprofit operations. The case is made by **the grid itself**: eleven tiles,
obviously unlike each other, all substantial. No thesis statement required.

The home page is three parts: a full-bleed forge **hero**, a flat two-column
**grid** of the eleven projects, and a **footer** of contact details. Each tile
earns the click; the project pages carry the writing.

---

## Ground rules (do not break these)

- **No JavaScript.** No `<script>` tags, no libraries, no analytics, no cookie
  banner. `grep -rn "<script" .` over the built site must stay empty.
- **Jekyll, built natively by GitHub Pages.** No Actions, no Node, no
  `package.json`. Content is Markdown + YAML front matter.
- **Tone is civilian throughout.** No defence framing, no marketing register.
  **Sentence case everywhere** (proper nouns aside); no Title Case, no all-caps.
- **One accent.** `--accent` (the one red) appears only on link underlines and
  focus rings. Never decorative.
- **No dark mode.** A single warm-neutral light palette; the hero is the most
  saturated thing on the site by a wide margin, and nothing competes with it.
- **All internal links and `src`s use `{{ site.baseurl }}`.** The custom domain
  is not set yet, so never hard-code the host.

`assets/css/main.css` is the whole design system. Add content; don't restyle.

---

## Repo layout

```
_config.yml            site config, the projects collection, contact details
index.md               home page: hero + two-column grid + footer
resume.md              the /resume/ page content (entries)
_data/order.yml        the grid order — a plain list of project slugs
_layouts/              default, project, resume
_includes/             head.html, footer.html, card.html
_projects/             11 project files  ->  /work/<slug>/
assets/css/main.css    the design system
assets/img/<slug>/     per-project images (hero, card, gallery — see below)
assets/img/home/       the home hero renditions (generated)
tools/build_images.py  the image pipeline (build-time helper, excluded)
assets/Abhiram-Rachamadugu-Resume.pdf   the résumé PDF the header links to
```

Collection and permalink (in `_config.yml`): `projects` → `/work/:name/`, where
`:name` is the filename without extension, so `_projects/taiyo-aerospace.md`
publishes at `/work/taiyo-aerospace/`. The `project` layout is auto-assigned by
`defaults`, so project files need no `layout:` field.

There is **no places collection and no map** — that was the previous design.

---

## Local preview (optional)

GitHub Pages builds this for you. To preview locally you need Ruby + Jekyll:

```bash
gem install jekyll bundler
jekyll serve
```

(There is deliberately no `Gemfile`; if you add one, use the `github-pages`
gem so local output matches production, and keep it excluded in `_config.yml`.)

---

## How to add or edit a project

Create `_projects/<slug>.md`. Copy this front matter; use `null` rather than
omitting a field:

```yaml
---
title: "Sentence-case project name"
slug: my-project              # must equal the filename
org: "Organisation"
role: "Your role"             # null for personal work
status: in-service            # in-service | in-build | ongoing | archived | worked-on-site
place: "Town, region"
coords: [14.47, 78.82]        # legacy/unused (the map is gone); harmless to keep
dates: "Aug 2021 – Mar 2023"
scale: "30+ units"            # honest counter, or null
users: "Who it serves"        # or null
constraint: "The binding constraint"   # or null
depth: deep                   # deep | medium | thin
hero: /assets/img/my-project/hero.jpg
hero_alt: "Describe the hero image."
hero_caption: "Optional caption under the hero."
tags: [thermal, deployed]     # or null
card_line: "One sentence, <=90 chars, that earns the click."
card_image: /assets/img/my-project/card.jpg   # null -> a graceful placeholder tile
card_alt: "Alt for the card image, only if it differs from the hero crop."
---
```

Two fields carry the most weight and the layout gives them prominence:

- **`role`** — be precise; `in-build` is not `in-service`, intern is not
  founder. One inflated entry makes a reader discount all of them.
- **`status`** — label honestly so the deployed entries read as trustworthy:
  `in-service`, `in-build`, `ongoing`, `archived`, `worked-on-site`.

### The card (home grid)

Each tile shows **image · title · one mono metadata line (`status · dates`) ·
one sentence (`card_line`)** — no prose. The whole card is the link. Keep
`card_line` to one sentence, ≤ 90 chars, sentence case. If `card_image` is
`null` the tile renders a hairline placeholder that reads "image pending".

### The grid order

`_data/order.yml` is the single source of truth for the grid — a plain list of
the project slugs, read left-to-right then down so each pair sits as siblings. Reorder
there; the project files carry no `order` field.

### Project body structure

The Markdown body fills, in this order: **What it is · The problem and the
constraint · What I did · What went wrong · Gallery** (some pages omit a section
for honest reasons — see the bodies). Gallery images use plain figures; the
`project` layout lazy-loads every in-body image automatically, so the bodies
stay clean:

```html
<figure>
  <img src="{{ site.baseurl }}/assets/img/my-project/1.jpg" alt="…">
  <figcaption>Caption.</figcaption>
</figure>
```

**Video:** never self-host, never embed an iframe. Link out to YouTube with a
static poster image (`.video-poster` adds a play overlay), or a plain text link.

Optional end-of-page links: add a `links:` list to the front matter
(`- { label: "Repo", url: "https://…" }`).

---

## Images

The pipeline is `tools/build_images.py` (needs Pillow). It reads the reviewed,
EXIF-stripped sources in `assets/img/<slug>/` and writes the **derived** files
only — it never touches a source:

- **Cards** — one 3:2 ratio for every tile (1200×800), crop-to-fill, a light
  unifying grade (subtle contrast + slight desaturation) so wildly different
  sources read as one set. WebP + JPEG.
- **Home hero** — the Gifu, Japan forge photograph, art-directed into a desktop
  16:10 crop and a mobile 4:5 crop, graded, WebP + JPEG, in `assets/img/home/`.
- **Project heroes** — a WebP sibling next to each `hero.jpg`; the layout serves
  it through `<picture>` with the JPEG as fallback.

Rules that still apply, per the brief: no identifiable photographs of Children
for Children recipients or of the Kadapa farmers; strip EXIF from every image
(the pipeline never writes it back); Ati Motors product/AMR footage only; Taiyo
the supplied render only. Re-run the pipeline after changing any source:

```bash
python tools/build_images.py
```

---

## The résumé

`resume.md` uses the `resume` layout (ruled sections, mono dates). It is
transcribed faithfully from `assets/Abhiram-Rachamadugu-Resume.pdf`; the header's
download button links to that PDF.

---

## Contact

Footer only — no form (GitHub Pages has no backend). Values live in `_config.yml`
under `contact:` (`email`, `phone_in`, `phone_us`, `linkedin`, `github`,
`location`) and `resume_pdf`.

---

## Before you ship

- `grep -rn "<script" _site` returns nothing.
- No EXIF on any published image.
- Every card is a link across its full area, and keyboard-reachable.
- 390 px viewport is usable; the grid collapses to one column.
- Uniform card heights, even with a two-line title.
- Hero text stays legible against the dark photograph.
- No absolute URLs — `{{ site.baseurl }}` throughout.
- Pages builds green.
