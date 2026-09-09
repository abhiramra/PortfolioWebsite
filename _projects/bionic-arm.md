---
title: "Bionic arm"
slug: "bionic-arm"
org: "Personal project"
role: null
status: "archived"
place: "Bengaluru"
coords: [12.97, 77.59]
dates: "Apr 2021 – Jan 2022"
scale: null
users: null
constraint: "Under $200 a unit, printed and tested at home"
depth: "deep"
hero: "/assets/img/bionic-arm/hero.jpg"
hero_alt: "The bionic hand standing on a white cloth: orange printed fingers and tendon guides above a white forearm brace, with servos, wiring and a battery connector on the outside of the brace."
hero_caption: "The hand with the servo bank and wiring exposed on the brace."
tags: ["3D printing", "materials testing", "print-in-place", "embedded ML"]
card_line: "A 3D-printed bionic hand under $200, its materials chosen by breaking them."
card_image: /assets/img/bionic-arm/card.jpg
---

## What it is

A 3D printed bionic hand and forearm gauntlet, built through several iterations at home in Bengaluru while I was in school, at a unit cost under $200 — the last one came in around ₹9,000 in materials. Tendon-driven fingers, servos in the brace, a Raspberry Pi Zero W running the control code in Python, a LiPo pack through a converter, and a PCA9685 driving the servo bank. It takes voice commands.

## The problem and the constraint

Commercial myoelectric prostheses cost more than a car in India. The open-source printed-hand projects that exist are excellent, but most of them are designed around printers and filaments that are easy to get in the US or Europe, and around an assembly step that assumes a bench, a vice and patience.

I set two constraints. Under $200 a unit, because above that the thing is an interesting object rather than a usable one. And the gauntlet had to print in place — printed as a single assembly with the joints already articulated, coming off the bed ready to use, with no assembly at all. Print-in-place makes the geometry considerably harder to design and makes the print itself less forgiving, but it removes the step where a build goes wrong, and it cuts print time and material.

## What I did

The part of this project I would put first is not the hand. It is the material work.

I did not want to choose filaments off datasheets, because the datasheet number is measured on a moulded coupon and I was printing thin, small, articulated parts on a hobby machine — a different material in every way that mattered. So I bought filament and tested it myself — tensile and impact testing at home, across more than twenty types, from PLA through PETG to polycarbonate, nylon and TPU — and then assigned each part of the hand to a material on the basis of what I had measured rather than what was claimed.

What came out of it was specific and mostly unintuitive:

| Material | Where it went | What I found |
|---|---|---|
| PLA | Arm brace, electronics mounts, joint pins | Fine for big parts and for small accurate ones. Too weak for fingers — they broke from installation stress, not from use. Too rigid for the palm brace, which needs to move. |
| PETG | Finger rings, string guides | Good strength and good abrasion resistance where the tendons rub. Will not do joints: small cross sections come out weak, because the melt is more viscous and does not knit. |
| Polycarbonate | Joints, pulleys; a replacement for PETG | The toughest consumer filament there is. Prints so hot that overhangs collapse, so the geometry has to be designed around it. Ships from Europe, which in practice is the real constraint. |
| Nylon | Joints, palm brace | Strong and flexible, which is exactly what a joint wants. Hygroscopic enough that it has to be dried before printing and kept dry during it. |
| TPU | Joint connections | Extremely high tensile strength and rubber-like, which opens up joint designs nothing else allows. More hygroscopic than nylon, very slow, poor overhangs. |

The final hand is a mix of PLA, PETG and polycarbonate, and every one of those choices came out of a test rather than a spec sheet. The raw tensile and impact numbers are gone — I lost that data years ago, which is annoying and is the reason this is a table of findings rather than a table of figures. What survived is the conclusions, and they are the part I still use.

The hand went to the IRIS National Fair in 2021-22 as project ENMC01. I was a finalist and did not win.

Alongside that: the fingers are three-linked, which is the balance point between articulation and something that can actually be printed and strung; print settings settled at 0.15 mm layers and about 10 °C above the recommended nozzle temperature, which is what got layer adhesion where it needed to be on the thin sections; and the voice interface runs a compact model exposed through an API on the arm, so a spoken command becomes a grip.

The same instinct shows up again at a <a href="{{ site.baseurl }}/work/bladesmithing/">forge in Kadapa</a>, reading steel temperature by eye with no pyrometer and no idea what the stock is. Different century of technology, same approach: find out what a material does by making it do it.

## What went wrong

Most of the failures were print failures, and they are the reason the material table exists. The first set of fingers was PLA and they snapped during stringing — not in use, during assembly, which is worse, because it means the part cannot survive being built. Joints printed in PETG came out visibly weak at the small cross sections. Polycarbonate solved the strength problem and created a supply problem: it ships from Europe, so a failed print costs weeks rather than an evening.

Print-in-place has its own failure mode. When a print-in-place joint fuses, you do not get a part with a defect — you get a solid block, and there is nothing to salvage. That is the trade for having no assembly step.

## Gallery

<figure>
  <img src="{{ site.baseurl }}/assets/img/bionic-arm/gauntlet-cad-annotated.jpg" alt="Annotated CAD render of the gauntlet showing multi-linked fingers, string pathways, palm brace, hinged opening, arm brace and cutouts to mount servos.">
  <figcaption>The gauntlet in CAD. The string pathways are the part that decides whether the hand works: they keep the tendons from tangling and hold a straight pull to the servo.</figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/assets/img/bionic-arm/gauntlet-v2.jpg" alt="A blue printed forearm gauntlet on a small table in a garden, with servo mounts, a control board and a loom of orange and black wires.">
  <figcaption>An earlier gauntlet, printed in one piece with the hinge already articulated.</figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/assets/img/bionic-arm/printed-arm-bench.jpg" alt="The printed arm standing on a wooden ledge outdoors: white brace, orange finger assembly, servo bank and a LiPo battery beside it.">
  <figcaption>Bench setup on a balcony. This is the whole workshop.</figcaption>
</figure>
