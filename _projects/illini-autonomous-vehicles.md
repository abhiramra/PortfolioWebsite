---
title: "Illini Autonomous Vehicles"
slug: "illini-autonomous-vehicles"
org: "Illini Autonomous Vehicles"
role: "Vice president & fixed-wing lead"
status: "in-build"
place: "Urbana-Champaign, Illinois"
coords: [40.11, -88.24]
dates: "Jan 2024 – Present"
scale: "1 fixed-wing airframe"
users: null
constraint: "Five students, about fifteen hours of field time a season"
depth: "deep"
hero: "/assets/img/illini-autonomous-vehicles/hero.jpg"
hero_alt: "Skyfall v1, a carbon-fibre plate quadrotor with exposed wiring, sitting on a grass sports field beside a painted line."
hero_caption: "Skyfall v1, the carbon-fibre test mule. Every hour it flew produced training imagery for the detection model."
tags: ["fixed-wing", "multirotor", "carbon fibre", "autonomy"]
order: 2
---

## What it is

Illini Autonomous Vehicles is UIUC's autonomous drone team. Two friends and I started it in January 2024 and began on fixed wings, which is what all three of us wanted to build. It has since split into two subteams — one multirotor, one fixed-wing — and I lead the fixed-wing side and serve as vice president. The team designs, builds and flies its own airframes, writes its own autonomy stack, and enters the SUAS competition each year; for 2026, in Tulsa, Oklahoma, 14–17 September.

## The problem and the constraint

The binding constraint is not money or ideas. It is field time. Five students carrying full course loads get somewhere around fifteen usable hours on a flight line across a season, rationed by weather, daylight, airspace and exams. A sortie that ends in a bug we could have caught on a laptop is a sortie we do not get back, so field time is never spent on anything reproducible on the ground: about thirty hours went into Gazebo and PX4 software-in-the-loop specifically to protect the fifteen that could not be replaced.

The second constraint is self-imposed. Nothing enters a competition configuration unless it has completed three consecutive full-mission rehearsals without anyone touching the controls. That rule costs us capability on purpose.

## What I did

On the fixed-wing side I designed and built a carbon-fibre monocoque fuselage — a load-bearing shell rather than a frame with a fairing over it, which is what buys the payload-to-weight ratio on a large airframe, and which is unforgiving, because the mould and the cure schedule decide the part before you ever see it. I also developed a tailless flying-wing glider on self-stabilising airfoils, so pitch stability comes out of the section geometry instead of out of a tail the aircraft then has to carry.

The 2026 competition entry came from the multirotor side. I was first author on the team's technical design report, so what follows is the team's work rather than mine alone — but it is the clearest thing we have written about how we make decisions, and the failure in it is the most useful thing on this page. Three airframes flew that season under the Skyfall name. v1 was a two-plate carbon-fibre quadrotor: heavy, ugly, and kept deliberately as a test mule, because a small team badly needs one aircraft nobody is afraid to fly. It flew most of the season's hours and produced the entire imagery set the detection model was trained on. v2 was designed inward from the transport requirement — a single laser-sintered polyamide shell with bonded aluminium panels, arms retained in slots with thumbscrews, no exposed wiring, assembled without tools inside three minutes.

The decision I would defend hardest is one we declined. The competition awards 75 points for keeping every battery under 100 Wh. Matching our 444 Wh pack inside that limit meant five parallel packs, five balance harnesses and five new single-point failures, for about forty hours of redesign. We turned the points down and spent those hours on the autonomy chain instead, which is worth 200.

## What went wrong

During flight testing, v2 developed a progressive heading error and departed controlled flight, coming down from about six metres onto grass. Nobody was hurt and nothing was damaged except the airframe, which cracked badly enough to be unairworthy. No logs survived, so the diagnosis is reconstruction from inspection and bench reproduction, and we say so in the report.

Three causes, and the point is that they were not independent. The upper access panel was not preloaded properly by its fasteners, so the shell flexed and passed motor-order vibration into the GNSS mast instead of damping it. The mast itself was not stiff enough in bending, so the antenna and its magnetometer moved at rotor harmonics. And the camera cable ran close enough to the compass to inject interference into it. The flight controller blends the external compass into its heading solution, so a corrupted reading was averaged in rather than rejected, and the error never announced itself — it just drifted.

What makes this worth writing down is why nobody caught it. On an open frame the mast is a visible cantilever with an obvious load path and an obvious distance to the wiring. Sealed inside a shell, neither route was visible, and neither came up in review. The fixes are a rigid carbon mast, a 300 mm minimum separation between the GNSS module and the camera cable — established by a bench interference sweep rather than by eye — and the Jetson baseboard interposed as a ground plane. The process fix matters more: a modal survey and a magnetic interference sweep are now gate criteria before first flight rather than diagnostics after one.

Losing v2 cost us the best packaging configuration we had built. We chose to compete on a proven commercial platform carrying our own avionics and autonomy rather than rush a replacement structure through a shortened qualification.

## Gallery

<figure>
  <img src="{{ site.baseurl }}/assets/img/illini-autonomous-vehicles/skyfall-v3-integration.jpg" alt="A carbon-fibre quadrotor frame part-assembled on a kitchen counter, arms and motors fitted, wiring loom laid out around it.">
  <figcaption>Integration happens wherever there is a flat surface.</figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/assets/img/illini-autonomous-vehicles/skyfall-v2-sls.jpg" alt="Skyfall v2, a fully enclosed white laser-sintered polyamide quadrotor, standing on grass.">
  <figcaption>Skyfall v2, the enclosed SLS airframe. The only frame photograph that survives it.</figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/assets/img/illini-autonomous-vehicles/fixed-wing-takeoff-poster.jpg" alt="A twin-boom fixed-wing UAV accelerating down a paved runway, grass either side, clear sky.">
  <figcaption>Fixed-wing takeoff, April 2024. Still from flight-test footage.</figcaption>
</figure>
