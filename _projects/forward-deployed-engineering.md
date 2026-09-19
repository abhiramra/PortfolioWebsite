---
title: "Mechanisms"
slug: "forward-deployed-engineering"
role: "Independent consultant"
status: "ongoing"
place: "Kadapa"
dates: "May 2026 – present"
scale: "Three clients — an NGO, a consultancy and a law firm"
users: "Aarti for Girls' leadership, managers and teachers; Terra Viridis' certification team"
constraint: "Everything had to keep running after I left"
depth: "deep"
hero: null
tags: ["organisation design", "information systems", "Jekyll", "document pipelines"]
card_line: "Contract work for an NGO, a consultancy and a law firm — systems built to outlast me."
card_image: /assets/img/forward-deployed-engineering/card.jpg
card_alt: "A water-balance flow diagram: catchment and municipal supply feeding tanks, an STP, and treated-water reuse."
---

## What it is

A summer of contract work for three organisations, on one page because it was one job. The largest piece of it was not software, which surprised me more than it should have.

Aarti for Girls, the NGO in Kadapa — a redesign of how the organisation moves information, and then a rebuild of [aartiforgirls.org](https://aartiforgirls.org). Terra Viridis Consultants, a sustainability consultancy and the sister company of the firm I built the [solar–biomass dryer]({{ site.baseurl }}/work/solar-biomass-dryer/) with — two internal tools. And Varuna Law Associates, on secure custody of sensitive personal documents under the DPDP Act, which is at the planning stage and which I will write about when there is something built.

## The problem and the constraint

Every one of these turned out to be the same problem wearing different clothes: information existed, and it had no reliable way to move.

At Aarti it moved by phone call, at the moment somebody noticed it was needed. At Terra Viridis it sat inside ten-thousand-file document packets nobody could sort, and inside water networks that lived in one engineer's spreadsheet. In each case the organisation was not short of information. It was short of a mechanism — a standing channel with a shape and a schedule, so that things arrive because it is Tuesday rather than because somebody is panicking.

The constraint on top of that: I was going to leave, and none of these organisations has an engineer. Whatever I handed over had to be run by the people already there, on the machines they already have, with no deployment story and no phone call to me in October. That rules out most of what an engineer's instinct reaches for, and it is why several of these answers are duller than they could have been. A mechanism somebody actually keeps using beats a better one they abandon.

## What I did

**Put Aarti on a schedule.** The reorganisation came first and everything else followed from it. I set up weekly management meetings for each of Aarti's ventures, attended by the whole leadership and the managers with something at stake. The theory is simple: unscheduled escalation is a symptom, not a personality trait. If there is no regular place for information to arrive, it arrives as an emergency, because an emergency is the only thing urgent enough to justify interrupting somebody. Give it a standing slot and most of it stops being urgent. Emergency calls — do this, do that, now — became much less frequent.

This was a reorganisation of mechanisms, not of people. Nobody's job moved and nobody was reorganised out. I did it with my mother's guidance, which is the only reason a twenty-year-old got to redesign how an organisation talks to itself.

**Standardised how the school tracks its students.** Aarti runs a school, and student progress was being held in individual teachers' heads and individual teachers' formats. I built a system to hold it instead — a frontend the teachers actually use, with the student data stored securely, because it is data about children and that is not a corner to cut.

On top of it sits a monthly tracking mechanism. Every teacher rates every student they teach on a qualitative scale, across three metrics kept deliberately independent: performance, responsiveness and enthusiasm. Collapsing those into one score is the obvious thing to do and it destroys the signal. A student who is behind academically but lights up in class is a completely different case from one coasting on ability and bored, and a single number makes them look identical. Kept apart, and tracked month over month, the shape of a child's year becomes visible while there is still time to do something about it.

**Then rebuilt the website.** Only then. The site was a heavy, JavaScript-dependent build that was slow and broke in places; I rebuilt it in Jekyll as static HTML and overhauled the content, which was the larger half of the work. The site's traffic is almost entirely donors and CSR teams doing due diligence before they fund the NGO, and to that reader a slow or broken site signals an organisation that cannot get the basics right, at the exact moment they are deciding whether to trust it with money. The order matters more than the rebuild: a website is a description of what an organisation does, and describing an organisation that has just stopped running on emergency phone calls is a different job from describing one that still is.

**Built a semantic document sorter.** Builders send Terra Viridis document packets that run past ten thousand files, and every one has to be sorted against LEED and GRIHA certification criteria before anyone can assess anything. The tool extracts content locally with a Python script, classifies it against the criteria through the Gemini API, and writes out an Excel workbook where every row links straight to its source document. The decision I would defend is the output: not a database, not a web viewer, a spreadsheet — because the certification team already works in spreadsheets, and a tool that makes them open something else is a tool they stop using in a month. Next is generating the certification deck from the same packet.

**Built a water-balance calculator.** Large projects have water networks with hundreds of inputs and outputs, normally modelled in a spreadsheet nobody else can read. The input here is a draw.io flowchart: cells named in plain language, arrows as flows, drawn in the tool an engineer would have used to explain it on a whiteboard anyway. Known quantities go in where they are known — design targets before the building exists, measured values after — and the calculator solves the rest of the system from what it has. The diagram is not documentation of the model. The diagram *is* the model, so it cannot drift out of date, and whoever maintains it does not have to be able to code.
