---
title: "Ati Motors — autonomous mobile robot"
slug: "ati-motors-amr"
org: "Ati Motors Pvt Ltd"
role: "New product initiatives intern"
status: "in-service"
place: "Bengaluru"
coords: [12.97, 77.59]
dates: "Sep 2024 – Apr 2025"
scale: "3 units"
users: "Robotics programmes at Christ College Bengaluru and VIT Coimbatore"
constraint: null
depth: "medium"
hero: "/assets/img/ati-motors-amr/hero.jpg"
hero_alt: "The light-duty AMR on a bench: a faceted chassis in cream and black with sensor cutouts on the top deck."
hero_caption: "The chassis. Faceted rather than curved, which is what makes it manufacturable in small numbers."
tags: ["ROS 2", "autonomous mobile robots", "deployment", "field support"]
order: 5
---

## What it is

A light-duty autonomous mobile robot for education and warehousing, developed at Ati Motors in Bengaluru. I led its development as a new product initiatives intern, between September 2024 and April 2025. Three units were built: one kept internally, one delivered to Christ College Bengaluru and one to VIT Coimbatore, both to serve as ROS 2 mules for their robotics programmes.

## The problem and the constraint

Ati's other robots are built to move payloads on a factory floor. This one had a different job. A university robotics programme needs a platform that students can put their own code on and drive around a corridor — which means the autonomy has to be complete enough to work out of the box and open enough that somebody can replace a piece of it without the robot becoming inert.

The other constraint was that I was an intern with an end date. Anything I built that only I understood would stop working the moment I left.

## What I did

I wrote the autonomy codebase in ROS 2 and brought it up across all three units. Then I deployed and maintained two of them in the field, which meant the whole lifecycle rather than the interesting part of it — commissioning on a site I did not design, mapping a building somebody else uses, and after-sales support when something stopped working on a Tuesday.

Field support is where the actual learning is. A robot that navigates a corridor reliably in the lab will find a way to fail in a building with glass doors, a floor that reflects, and people who move furniture. Every one of those is a bug you cannot reproduce at your desk.

Before I finished, I trained my successor and wrote up the technical workflows — the bring-up sequence, the deployment steps, the things that are not obvious from the code. Handing a project over properly is the part of an internship that is easiest to skip and hardest to justify skipping.

## Gallery

<figure>
  <img src="{{ site.baseurl }}/assets/img/ati-motors-amr/amr-chassis-top.jpg" alt="The AMR photographed from above on a workshop floor, showing the top deck, sensor mount and hazard markings.">
  <figcaption>Top deck, with the sensor mount fitted.</figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/assets/img/ati-motors-amr/amr-plant-run-poster.jpg" alt="An Ati autonomous mobile robot driving along a marked lane on a factory floor, past pallet trucks and shelving.">
  <figcaption>An Ati AMR running a lane on a plant floor.</figcaption>
</figure>
