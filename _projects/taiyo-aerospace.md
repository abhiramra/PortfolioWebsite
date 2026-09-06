---
title: "Taiyo Aerospace"
slug: "taiyo-aerospace"
org: "Taiyo Aerospace Pvt Ltd"
role: "Founder"
status: "in-build"
place: "Bengaluru"
coords: [12.97, 77.59]
dates: "Jan 2025 – Present"
scale: "1 prototype airframe, 2 flying scale models"
users: null
constraint: "Self-funded, built in a home lab"
depth: "deep"
hero: "/assets/img/taiyo-aerospace/hero.jpg"
hero_alt: "Front view render of the Vritra airframe: a fixed-wing aircraft with a blended fuselage and a dorsal inlet, on a black background."
hero_caption: "Vritra, front view. The dorsal serpentine inlet feeds the turbine bay behind the payload volume."
tags: ["fixed-wing UAV", "carbon fibre", "autonomy", "propulsion"]
order: 1
---

## What it is

Taiyo Aerospace is a company I started in Bengaluru with one other engineer to build a jet-powered, autonomous fixed-wing aircraft for missions that are decided by how fast you can get there — blood and vaccines to a remote post, a wide-area search in the first hours after someone goes missing, damage assessment and resupply after a flood or an earthquake. The aircraft is called Vritra. It carries a 15 kg modular payload bay, packs into cases that fit in an SUV, and is meant to be assembled and launched by two people in under ten minutes from a short dirt strip.

The full-scale airframe is assembled and in ground testing. It has not flown yet.

## The problem and the constraint

Fast air platforms exist, and so do cheap ones. The gap is a platform that is fast *and* cheap enough that an organisation will actually risk flying it into a disaster zone, and that can be maintained on a domestic supply chain rather than an import licence. Everything about Vritra follows from trying to sit in that gap: a 2.4 m wingspan with detachable wings so it fits in cases, multi-fuel operation on Jet-A1 or commercial diesel so field logistics are ordinary diesel logistics, and a hot-pit turnaround under ten minutes so one airframe can fly repeat sorties.

The other constraint is that both of us are still undergraduates and the whole thing is self-funded. Design, fabrication and testing have all been paid for out of pocket, which sets the pace: we build what we can validate, in the order that lets the next step be cheap.

## What I did

I am responsible for the airframe — the structural design, the manufacturing, and getting the programme through its milestones. The airframe is a carbon-fibre monocoque unibody: one continuous shell rather than a frame with skins bolted to it, which gets the structural mass down and the stiffness up, but which means the tooling and the layup schedule *are* the design. There is no second chance to adjust a rib after the shell is cured. The inlet is a serpentine S-duct, which is a harder shape to lay up than a straight duct and was chosen anyway.

Propulsion is staged deliberately. Phase one flies the aircraft on an electric ducted fan at a reduced envelope, so that the structure, the control surfaces and the autonomy can be wrung out before turbine dynamics, hot section handling and fuel system behaviour are added to the list of things that can go wrong. Phase two integrates a JetCat P-250 micro-turbojet at roughly 25 kg of thrust, which is what opens the 450 km/h dash envelope.

Before the full-scale build, we flew a 70% scale aerodynamic prototype. That flight is what let us commit to the planform: it gave us yaw response, climb performance, pitch authority and surface drag under representative conditions, on an aircraft cheap enough to lose.

## What went wrong

We crashed several scale models before one flew. The causes were the two that account for most lost model aircraft and are no less embarrassing for it: centre-of-gravity mistakes, and control errors. Neither is exotic. Both are the kind of thing that a spreadsheet and a careful pre-flight are supposed to catch, and the reason they kept getting through is that we were iterating quickly on airframes we had built ourselves, where the mass of every part was an estimate until the thing was on the scales.

The flight that finally worked is what cemented the design. That is worth being precise about: the planform was not validated by analysis and then confirmed in the air, it was validated in the air after several attempts that were not. The 70% scale prototype that returned yaw response, climb performance, pitch authority and surface drag is the one that earned the full-scale build; the ones before it earned the changes.

Two things remain unproven rather than failed. The in-house flight controller is not ready, so a commercial Cube Orange+ is flying the aircraft while that board matures — an interim answer we chose over delaying ground testing. And the autonomy stack is still on a quadcopter testbed rather than on the aircraft, because putting unproven software on an unflown airframe means that when something goes wrong you cannot tell which half caused it.
