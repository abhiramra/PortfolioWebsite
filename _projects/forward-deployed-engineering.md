---
title: "Forward deployed engineering"
slug: "forward-deployed-engineering"
org: "Independent"
role: "Contract engineer"
status: "ongoing"
place: "Bengaluru"
dates: "May 2026 – present"
scale: "Three clients, four projects"
users: "Aarti for Girls; Terra Viridis' certification team"
constraint: "Everything had to keep running after I left"
depth: "deep"
hero: "/assets/img/forward-deployed-engineering/hero.jpg"
hero_alt: "A water-balance flow diagram in draw.io: rooftop catchment and municipal supply feeding a raw-water tank, domestic demand, an STP, and a treated-water tank splitting to reuse and sewer."
hero_caption: "The water-balance calculator's input: a draw.io network where the cells are named in plain language and the arrows are flows. The diagram is the model."
tags: ["Jekyll", "document pipelines", "LLM tooling", "systems solving"]
card_line: "Contract engineering — an NGO site, an AI document sorter, and a water-balance tool."
card_image: /assets/img/forward-deployed-engineering/card.jpg
card_alt: "A water-balance flow diagram: catchment and municipal supply feeding tanks, an STP, and treated-water reuse."
---

## What it is

A summer of contract work for three organisations. It sits on one page because it was one job: turn up at somebody else's problem, build the smallest thing that solves it, and leave it somewhere they can keep using it without me.

Aarti for Girls, the NGO in Kadapa — a full rebuild of [aartiforgirls.org](https://aartiforgirls.org). Terra Viridis Consultants, a sustainability consultancy — two internal tools, a document sorter and a water-balance calculator. And Varuna Law Associates, on secure custody of sensitive personal documents under the DPDP Act, which is at the planning stage and which I will write about when there is something built.

## The problem and the constraint

The constraint all three share is that I was going to leave, and none of these organisations has an engineer. Whatever I handed over had to be operable by the people already there, on the machines they already have, without a deployment story or a maintenance contract or a phone call to me in October.

That rules out most of what an engineer's instinct reaches for. It rules out a web app with a server somebody has to keep alive. It rules out a pipeline that only runs on the laptop it was written on. What it leaves, mostly, is this: find the tool the client is already living in, and make your thing come out the other end of it.

That is the through-line. The interesting decision in each of these was not the code. It was picking the interface.

## What I did

**Rebuilt the Aarti for Girls site.** It was a heavy, JavaScript-dependent site that was slow and broke in places. I rebuilt it in Jekyll as static HTML, and overhauled the content while I was in there, which turned out to be the larger half of the work. The architectural argument is about the audience: the traffic is almost entirely donors and CSR teams doing due diligence before they fund the NGO. To that reader, a slow or broken site signals an organisation that cannot get the basics right, at the exact moment they are deciding whether to trust it with money. Static HTML is fast and reliable, and it holds up to that scrutiny. The benefit of Jekyll on the other side is that a non-engineer can add a page by writing a markdown file.

**Built a semantic document sorter.** Builders send Terra Viridis document packets that run past ten thousand files, and every one of them has to be sorted against LEED and GRIHA certification criteria before anyone can assess anything. Doing that by hand is the job nobody wants and the reason certification takes as long as it does.

The tool extracts content locally with a Python script, classifies against the criteria through the Gemini API, and writes the result out as an Excel workbook where every row carries a filepath link straight to the source document. There is a frontend for running it. The decision I would defend is the output format: not a database, not a web viewer, a spreadsheet — because the certification team already works in spreadsheets, and a tool that makes them open something else is a tool they will stop using in a month. The next step is generating the certification deck itself from the same packet.

**Built a water-balance calculator.** Large projects have water networks with hundreds of inputs and outputs, and modelling them normally means either a spreadsheet nobody else can read or a specialist package nobody has.

The input is a draw.io flowchart. Cells are named in plain language, arrows are flows, and the engineer draws the network in the tool they would have used to explain it on a whiteboard anyway. Known quantities go in where they are known — design targets when the building does not exist yet, measured values when it does — and the calculator solves the rest of the system from what it has. The diagram is not documentation of the model. The diagram is the model, which means it cannot drift out of date, and the person maintaining it does not have to be able to code.
