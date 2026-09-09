#!/usr/bin/env python3
"""
Image pipeline for the image-led editorial grid.  Run from anywhere:

    python tools/build_images.py

Requires Pillow (`pip install pillow`).  It is a build-time helper only — the
`tools/` directory is excluded from the Jekyll build.

From the reviewed, EXIF-stripped source images it produces:
  * 10 card images at a single 3:2 ratio (1200x800), lightly graded, WebP + JPEG
  * the full-bleed home hero (the Gifu, Japan forge photo), art-directed into a
    desktop 16:10 crop and a mobile 4:5 crop, WebP + JPEG
  * a WebP sibling for each existing project hero.jpg (the JPEG stays as fallback)

Design rules honoured (see the brief, §6):
  * one aspect ratio for every card image (3:2); crop-to-fill, never letterbox
  * consistent crop logic (subject-centred unless overridden)
  * a light unifying grade (subtle contrast + slight desaturation) so phone
    photos, CAD renders and video stills read as one set
  * EXIF is never written back out

Re-run it whenever a source image changes.  It only writes the derived files
(`card.*`, `hero.webp`, `home/hero-*`), never the reviewed sources.
"""

import os
from PIL import Image, ImageEnhance, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "img")

# ---- light unifying grade -------------------------------------------------
CONTRAST = 1.05   # a touch of punch
COLOR    = 0.92   # pull the loudest phone-photo saturation toward the set
def grade(im):
    im = ImageEnhance.Contrast(im).enhance(CONTRAST)
    im = ImageEnhance.Color(im).enhance(COLOR)
    return im

# ---- crop-to-fill ---------------------------------------------------------
def crop_fill(im, target_ratio, v_anchor=0.5, h_anchor=0.5):
    """Crop im to exactly target_ratio (w/h), keeping as much as possible."""
    w, h = im.size
    cur = w / h
    if cur > target_ratio:                 # too wide -> trim width
        new_w = round(h * target_ratio)
        x0 = round((w - new_w) * h_anchor)
        box = (x0, 0, x0 + new_w, h)
    else:                                  # too tall -> trim height
        new_h = round(w / target_ratio)
        y0 = round((h - new_h) * v_anchor)
        box = (0, y0, w, y0 + new_h)
    return im.crop(box)

def save_pair(im, out_base, jpg_q=86, webp_q=80):
    im = im.convert("RGB")
    jpg, webp = out_base + ".jpg", out_base + ".webp"
    im.save(jpg, "JPEG", quality=jpg_q, optimize=True, progressive=True)   # no exif
    im.save(webp, "WEBP", quality=webp_q, method=6)
    print(f"  {os.path.relpath(jpg, ROOT)}  {im.size[0]}x{im.size[1]}  "
          f"jpg={os.path.getsize(jpg)//1024}k webp={os.path.getsize(webp)//1024}k")

def load(path):
    im = Image.open(path)
    im = ImageOps.exif_transpose(im)       # honour orientation, then drop exif
    if im.mode in ("RGBA", "LA", "P"):     # flatten any transparency onto white
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        return bg
    return im.convert("RGB")

# 1. CARD IMAGES  (3:2, 1200x800, graded).
# (slug, source path relative to repo root, vertical anchor, horizontal anchor).
# Sources that are card-only (not shown on a page) live in tools/sources/ so
# they are not published; the rest reuse an in-repo hero/gallery image.
CARDS = [
    ("taiyo-aerospace",            "tools/sources/taiyo.jpg",                                            0.50, 0.50),
    ("illini-autonomous-vehicles", "assets/img/illini-autonomous-vehicles/fixed-wing-takeoff-poster.jpg", 0.50, 0.50),
    ("ati-motors-amr",             "assets/img/ati-motors-amr/amr-plant-run-poster.jpg",                 0.50, 0.50),
    ("solar-biomass-dryer",        "assets/img/solar-biomass-dryer/hero.jpg",                            0.50, 0.50),
    ("bionic-arm",                 "assets/img/bionic-arm/hero.jpg",                                     0.50, 0.50),
    ("children-for-children",      "assets/img/children-for-children/coaching-launch.jpg",               0.45, 0.50),
    ("abb-tata-motors",            "assets/img/abb-tata-motors/hero.jpg",                                0.48, 0.50),
    ("bladesmithing",              "assets/img/bladesmithing/finished-knives.jpg",                       0.40, 0.50),
    ("pneumatic-exoskeleton",      "tools/sources/exoskeleton.jpg",                                      0.50, 0.32),
    ("machani-robotics",           "tools/sources/machani.jpg",                                          0.30, 0.50),
]
# fraction to trim off the left before the 3:2 crop (to drop an edge bystander)
LCROP = {}
print("Cards (3:2, graded):")
for slug, src, va, ha in CARDS:
    im = load(os.path.join(ROOT, src))
    lc = LCROP.get(slug, 0)
    if lc:
        w, h = im.size
        im = im.crop((int(w * lc), 0, w, h))
    im = crop_fill(im, 3/2, v_anchor=va, h_anchor=ha)
    im = grade(im.resize((1200, 800), Image.LANCZOS))
    save_pair(im, os.path.join(IMG, slug, "card"), jpg_q=84, webp_q=76)

# 2. HOME HERO (Gifu, Japan forge; desktop 16:10 + mobile 4:5, graded)
print("\nHome hero (forge, Gifu Japan):")
home = os.path.join(IMG, "home"); os.makedirs(home, exist_ok=True)
src = load(os.path.join(IMG, "bladesmithing", "gifu-workshop.jpg"))     # 1100x1467
d = grade(crop_fill(src, 16/10, v_anchor=0.28).resize((1600, 1000), Image.LANCZOS))
save_pair(d, os.path.join(home, "hero-desktop"), jpg_q=88, webp_q=82)
m = grade(crop_fill(src, 4/5, v_anchor=0.06).resize((1080, 1350), Image.LANCZOS))
save_pair(m, os.path.join(home, "hero-mobile"), jpg_q=88, webp_q=82)

# 3. PROJECT HERO WebP siblings (JPEG stays as fallback; no grade, no resize)
print("\nProject hero WebP siblings:")
for slug in [s for s, *_ in CARDS]:
    src = os.path.join(IMG, slug, "hero.jpg")
    if not os.path.exists(src):
        continue
    out = os.path.join(IMG, slug, "hero.webp")
    load(src).save(out, "WEBP", quality=82, method=6)
    print(f"  {os.path.relpath(out, ROOT)}  webp={os.path.getsize(out)//1024}k")

print("\nDone.")
