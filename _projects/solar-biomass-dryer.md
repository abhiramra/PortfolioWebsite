---
title: "Solar–biomass vegetable dryer"
slug: "solar-biomass-dryer"
org: "VeraTatva Engineering Consultants LLP"
role: "Research associate"
status: "in-service"
place: "Kadapa district, Andhra Pradesh"
coords: [14.47, 78.82]
dates: "Aug 2021 – Mar 2023"
scale: "30+ units"
users: "Marginal farmers"
constraint: "Unit cost and no grid power"
depth: "deep"
hero: "/assets/img/solar-biomass-dryer/hero.jpg"
hero_alt: "Two dryers on a rural plot, each a tall brick drying chamber with an inclined glazed solar collector running down to ground level. A mason stands on top of the nearer chamber; a stack of firewood sits alongside and turkeys forage in the yard."
hero_caption: "Two units in a yard in Kadapa district. The woodpile is the other half of the design — that is the biomass side of the fuel — and the mason on top is the reason the thing is buildable at all."
tags: ["thermal", "simulation", "deployed"]
card_line: "A sub-$200 solar and biomass crop dryer, 30+ built with farmers in Kadapa."
card_image: /assets/img/solar-biomass-dryer/card.jpg
---

## What it is

A vegetable dryer for small and marginal farmers in Kadapa district, built out of brick, mortar and local black limestone, that runs on sunlight with a biomass furnace underneath for the days sunlight is not enough. It is an indirect dryer: air is heated in a glazed collector and then passed over the produce, so the food never sits in direct sun. More than thirty units have been built for farmers across villages in the district with the NGO Aarti for Girls.

## The problem and the constraint

Drive through Kadapa in October and you will see tomatoes rotting at the roadside. When the wholesale price collapses it is not worth a farmer's time to hire labour to pick them, so the crop stays in the field. The farmers I surveyed in Nanapalli village had no cold storage near them and no preservation method they could afford at that volume. Drying is the obvious answer — it has been done in Rayalaseema for centuries — but the traditional method, produce on the ground in the open, does not give you something you can sell.

So the constraint was price, and it was severe. In a survey of twenty-two dryers on the Indian industrial market, exactly one came in under ₹30,000; the greenhouse designs start around ₹100,000. Farms here also have no reliable grid supply, so anything with a fan or an element was out. I set a target of about $200 a unit, which meant building out of what a mason in Kadapa already has on the shelf. That turned out to be an advantage: Kadapa stone — a local black limestone, dark from its organic content, about 30 cents a square foot — has high thermal mass and is used in every house in the district. The material with the right physics was also the cheapest one, and the one local masons already knew how to lay.

## What I did

I built the first prototype in September 2021 on hand calculations, then spent the next year finding out how wrong it was. I instrumented it — temperature and humidity loggers at the collector entrance and exit, at the tray and in the chimney — and put a weather station on a nearby roof to give the simulation real boundary conditions, then built a digital twin in DesignBuilder and calibrated it against the measurements.

Once the model matched, I ran the design one variable at a time. Widening the collector to 1.4 m raised the peak temperature rise across it to about 12.5 °C. Sizing every opening to 0.06 m² — the largest the chamber will take — roughly doubled peak airflow. Four-inch walls with plaster on both sides sat in the right place between retention and cost; nine-inch walls held heat better but flattened the peak too much. A 50 mm collector slab with 50 mm of thermocol behind it took collector exit temperature from about 45 °C to 50.5 °C, and thermocol costs nothing. Orientation came out of a separate study in Grasshopper: south-east at 15–20° for Kadapa, about 1,940 kWh/m² a year.

Those changes went into the Mark II. The other thing I did was find the produce somewhere to go. A partnership with Amano Foods India, a sauce and soup manufacturer, opened an offtake channel, so a farmer with a dryer has a buyer rather than a shed full of dried tomatoes. For a student engineering project that step is unusual, and it is the one that decides whether any of the rest matters.

## What went wrong

The sensors were in the wrong place for a month. Both collector sensors sat where direct sunlight fell on them, so they were reading their own heating rather than air temperature, and every number was inflated. I found it on 1 July 2022 and moved them, which left five usable days out of thirty-seven.

Then the digital twin came out colder than the real dryer, which is backwards — a simulated model is usually too ideal and needs leakage added to it. I spent weeks adjusting wall thickness, material properties and thermal mass for nothing. The fault was not in the model. The weather station measures solar radiation with a light sensor reporting lumens, and lumens are visible light only; heat also arrives in the infrared. I corrected the lumen conversion, which was about 8% off on its own, then used the output of a solar array on the same site to work out day by day what fraction of incoming radiation the station was actually seeing. Even then the corrected weather file kept corrupting because so few days were valid, so the calibration rests on a single matched pair — 3 July measured against 12 July simulated. That is thin, and I would rather it were not.

The Mark II improved, but not by as much as I expected. Drying time for the same batch came down; it did not reach the target. The remaining problems are construction rather than physics — sealing the glass, where sealant in Kadapa is expensive, plastering, and a door that seals well enough to be hard to open. There is still a lot to fix.

## Written up

The project has been written up twice. The conference paper documents the instrumentation, the DesignBuilder calibration and the sensitivity studies that produced the Mark II design, and I presented it at World Sustainable Energy Days.

The second is a shorter piece — *An affordable self-build biomass-cum-solar dryer for small and marginal farmers to reduce agri-produce waste* — in <a href="https://www.grihaindia.org/publications" rel="noopener"><em>Shashwat</em></a>, GRIHA's magazine, 2022, issue 3, pages 38–41. It makes the case for the material: the stone with the thermal mass this design needs happens to be the cheapest thing in the district and the one every local mason already knows how to lay, and it sets out the intent to open-source the design once it has been prototyped enough to be worth copying.

## Gallery

<figure>
  <img src="{{ site.baseurl }}/assets/img/solar-biomass-dryer/dryer-build.jpg" alt="A dryer under construction: brick drying chamber part-built, the glazed collector with its dark zigzag slats already in place below, a mason standing on the chamber top, mesh air inlet at the base.">
  <figcaption>Under construction. The dark zigzag slats in the collector are what heat the air on its way to the chamber; the mesh at the bottom is the inlet. Every part of this was laid by a local mason out of local materials, which was the point.</figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/assets/img/solar-biomass-dryer/design-sketch.jpg" alt="Hand-drawn dimensioned sketch of the dryer: a long inclined solar collector with internal slats feeding a taller drying chamber with a chimney, marked 356 cm overall.">
  <figcaption>The dryer, sketched with dimensions before anything was simulated: inclined collector with slats, drying chamber, chimney.</figcaption>
</figure>

<figure>
  <a class="video-poster" href="https://youtu.be/7ELi5-HV6ls"><img src="{{ site.baseurl }}/assets/img/solar-biomass-dryer/wsed-talk-poster.jpg" alt="A conference stage lit green and blue with WSED lettering; a speaker at a lectern beside a screen showing a slide titled 'Why solar cum biomass drying'."></a>
  <figcaption>Presenting the dryer at World Sustainable Energy Days.</figcaption>
</figure>
