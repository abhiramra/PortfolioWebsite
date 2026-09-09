---
title: "Pneumatic exoskeleton"
slug: "pneumatic-exoskeleton"
org: "Personal project"
role: null
status: "archived"
place: "Kadapa"
coords: [14.47, 78.82]
dates: "Jul 2020"
scale: null
users: null
constraint: "Metal tubing, off-the-shelf pneumatic cylinders, built in a month"
depth: "deep"
hero: null
tags: ["pneumatics", "mechanism design", "Arduino", "fabrication"]
card_line: "A pneumatic exoskeleton of tubing and cylinders, built to lift 80 kg."
card_image: /assets/img/pneumatic-exoskeleton/card.jpg
card_alt: "Abhiram wearing the pneumatic exoskeleton on a terrace, lifting a weighted bar."
---

## What it is

An upper-body exoskeleton built from metal tubing and pneumatic cylinders in July 2020, designed to lift 80 kg (180 lb). An Arduino drives solenoid valves that admit air to the cylinders; there is no software worth the name and no feedback loop. It is a mechanism, and everything interesting about it is mechanical.

I filmed the whole build as a three-part series, and the videos are a better record of it than anything I could write here. What follows is the context they do not have.

## The problem and the constraint

This was built in Kadapa in July 2020, during the lockdown, out of metal tubing and commodity pneumatic parts. Pneumatics for two reasons. The first is availability: it was what could be had in Kadapa in the middle of a lockdown, and a part you cannot buy is not a design option. The second is that I wanted the actuation to be *fast*. Air is compressible, which makes it hard to hold a position accurately, but it moves quickly and it takes shock well — and for an arm that is supposed to help you lift something, speed matters more than precision. The whole architecture follows from that actuator choice rather than the other way round.

Which makes the geometry the hard part. A pneumatic cylinder gives you a straight push over a fixed stroke; an elbow needs a rotation through a large angle. Getting one from the other means placing the cylinder's anchor points so the moment arm stays adequate across the whole range of motion, while the stroke is long enough to cover that range, while the cylinder does not foul the arm at either end. Those three requirements fight each other and the window where all three hold is narrow. On a build with no analysis behind it, finding that window is the entire job.

## What I did

Part 1 — **The arms.** The linkage: mounting points, moment arms and stroke, worked out on the frame rather than on paper. This is where the design either works or does not.

Part 2 — **The body.** A backplate to react the load, and the cylinders fitted to the arms. In the video I say it took considerably more work than expected, which was true, and the reason is that a backplate is not a bracket — it has to take the reaction of everything the arms do and put it into the wearer's torso without concentrating it anywhere.

Part 3 — **The test.** Finishing, paint, and the demonstration: a 60 kg curl with the exoskeleton on.

The design figure and the demonstrated figure are different, and I would rather show both than pick the flattering one. The mechanism was designed around 80 kg; what is on film is 60 kg.

## What went wrong

The honest answer is that this is the most junior thing on the site and it shows. There is no force feedback, no proportional control and no compliance — the valves are open or shut, so the arms move at whatever rate the air can fill the cylinder, which is not how you want to move a load near a person. The build is bolted tube, so the tolerances are whatever the drill press gave. And it was never taken past the demonstration.

It also never got where it was going. The arms were meant to be the first stage of a full-body exoskeleton, legs included, and I never built the rest. Some of that is that the leg problem is genuinely much harder — an arm reacts its load into your torso, legs react theirs into the ground, and that means load paths, balance and a failure mode where the thing falls over with you inside it. Most of it is that the lockdown ended and I moved on to other projects.

What it did teach me is the thing I have used ever since: on a build like this the actuator is not chosen after the design, it *is* the design, and picking it by what you can actually get hold of in the place you are standing is a legitimate engineering decision rather than a compromise.

## Gallery

<!-- Poster images pending: assets/img/pneumatic-exoskeleton/ep1-poster.jpg, ep2-poster.jpg, ep3-poster.jpg. Restore the .video-poster blocks (in git history) once they land. -->
<p>Watch the three-part build: <a href="https://youtu.be/z_kfKeZA6iI" rel="noopener">ep. 1 — the arms (4:20)</a> · <a href="https://youtu.be/afo4sa5EW2Y" rel="noopener">ep. 2 — the body (4:44)</a> · <a href="https://youtu.be/2LlFXm5InOk" rel="noopener">ep. 3 — final test (2:26)</a></p>
