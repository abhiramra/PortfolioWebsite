---
title: "Forge, tooling, and blades"
slug: "bladesmithing"
org: "Personal project"
role: null
status: "ongoing"
place: "Kadapa, Andhra Pradesh"
coords: [14.47, 78.82]
dates: "2020 – Present"
scale: null
users: null
constraint: "No commercial anvil or stock supply — forge, tooling and steel sourced from scrapyards"
depth: "deep"
hero: "/assets/img/bladesmithing/hero.jpg"
hero_alt: "A blade at forging heat, glowing dull orange-red, lying on a stone slab with a sledgehammer resting beside it."
hero_caption: "A blade at heat on the stone slab that stands in for an anvil."
tags: ["metallurgy", "heat-treatment", "fabrication"]
order: 10
---

## What it is

A forge I built in the ground in Kadapa, and the knives that have come out of it. Charcoal, a length of pipe for a tuyere, blocks and rammed earth for the hearth, a stone slab where an anvil should be, and scrapyard steel.

This is the only hand-metalwork on the site. Everything else here is composites, polymers or CNC — a machine takes the material to a state you specified. Forge work is the opposite: you are running a heat treatment by eye, in a fire whose temperature you control with your breath and a pipe, on steel whose composition you do not know.

## The problem and the constraint

Start with the anvil, because it sets the tone. Buying an anvil in India is not a purchase, it is a project — they are not stocked, the ones that exist are old railway or industrial stock, and the shipping on 60 kg of steel to a district town is its own line item. The same is true of tongs, of a post vice, of a bick, and of any tool stock. So the forge was built rather than bought, the tooling was sourced from scrapyards, and the blades are drawn out on a stone slab.

Then the steel. Scrapyard stock has no certificate. The tanto in the video log is forged from an old leaf spring — 5160 spring steel, which is a known and forgiving alloy for a blade, and which is exactly why leaf springs are the stock everybody starts on. But that is knowledge about the *source*, not about the bar in your hand: leaf springs vary, and a piece of unidentified round bar from the same scrapyard tells you nothing at all. Every new piece is a characterisation problem before it is a forging problem, and getting that wrong shows up two operations later as a crack. The method is a spark test — hold the bar to a grinding wheel and read the spark stream, because carbon content changes how the sparks burst. It is crude, it will not give you a number, and it is enough to tell high-carbon from mild, which is the distinction that decides whether there is any point heat treating the piece at all.

This puts it in the same category as the other supply-constrained builds here — a bionic arm held under $200, a dryer that has to work without grid power. The constraint is not incidental to the project; it is what the project is about.

## What I did

**Built the forge.** Three of them, over about two years. The first, in December 2022, was a hearth set into the ground and walled with blocks — charcoal fuel, air delivered through a length of pipe. The second, in January 2024, moved up into a plastered trough at working height, which is easier on the back and holds a smaller, hotter fire in a smaller volume of fuel. The third, in August 2024, went back to a shallow pit dug straight into laterite soil, which is the cheapest and fastest thing to build and the one I would rebuild anywhere.

**Ran the heat treatment by eye.** This is the substance of the whole thing, and it is applied materials science done by hand. Forging heat is judged by colour. Austenitizing has to be hot enough to take the steel fully into austenite and no hotter, because holding it above that wastes carbon to decarburisation and coarsens the grain. Normalising cycles come next to relieve the stress the hammer put in and refine what the forging heat coarsened. Then the quench, which converts austenite to martensite — the hard, brittle phase — and which is where blades break. Then tempering, which trades some of that hardness back for a blade that will not shatter.

Every one of those steps has a temperature window, and the only instrument is an eye in the right light. Judging colour in bright sun is far harder than judging it at low light, which is why most of these photographs were taken at dusk.

**Made the knives.** Kitchen knives, a chef's knife, a tanto, blades still in the black. The knives are the output, not the subject.

**Went and trained in a working smithy.** In May 2024 I attended a blacksmithing workshop in Gifu, Japan, at the master blacksmith Asano Kajiya's workshop. It is the only time in any of this that I have worked at a proper hearth, on a real anvil, at a bench, with tooling that was made for the job — which is worth saying on a page whose entire argument is about not having those things. I went for the hammer technique and came back with that plus something I did not know I needed, which is in the next section. I also came back with friends I am still in touch with. The blade in the second photograph below is the piece I was drawing out there.

## The tanto, end to end

The one piece documented from stock to finished blade is a Japanese-style tanto forged from a leaf spring, in two parts. It is worth watching in order: the first video is the forging and the shaping, the second is grinding, the handle and the finish.

<!-- Poster images pending: assets/img/bladesmithing/tanto-part-1-poster.jpg and tanto-part-2-poster.jpg. Restore the .video-poster blocks (in git history) once they land. -->
<p>Watch the tanto build: <a href="https://youtu.be/ISwOCaOETow" rel="noopener">part 1 — forging the leaf spring (8:56)</a> · <a href="https://youtu.be/9Tbm--dfvNo" rel="noopener">part 2 — grinding, handle and finish (5:12)</a></p>

The same habit is behind the <a href="{{ site.baseurl }}/work/bionic-arm/">bionic arm</a>: buy twenty filaments and break them all rather than read the datasheet. Here there is no datasheet to read in the first place — which turned out to cut both ways, as the next section explains.

## What went wrong

For about four years I did not harden a single blade.

I did not know that at the time, which is the whole problem. I was quenching far too cold — taking the steel out of the fire below its critical temperature, dropping it in water, and getting back something that looked exactly like a hardened blade. It was the right shape. It was the right colour. It took an edge. It just was not hard, because the steel had never gone into austenite, so there was nothing there to transform into martensite. Every one of those blades was a normalised bar of steel with a bevel ground on it.

A quench crack is unambiguous — the blade is in two pieces in the bucket and you know immediately. A quench that simply did nothing is the opposite: it is silent. Nothing looks wrong. And if your only instrument is your own eye, and your eye is calibrated wrong, you will repeat the same error indefinitely and produce a stack of evidence that you are doing it right.

What fixed it was watching somebody who knew. In Gifu I saw Asano Kajiya bring a piece up and quench it properly, and the colour he was working at was visibly hotter than anything I had been calling ready. That is the entire correction: not a technique, not a tool, just seeing the target once so I knew what I was aiming at. I had been reading temperature by eye for years without ever having seen the answer key.

There is a lesson in it that cuts against how I usually work. On the <a href="{{ site.baseurl }}/work/bionic-arm/">bionic arm</a> the empirical approach worked, because a filament that is too weak snaps in your hands and tells you so. Here the same instinct failed for four years, because the failure was invisible and self-consistent. Testing your own materials only teaches you something if the test can actually come back negative.

The visible failures are the cheap ones by comparison. The dark pitting across the blanks in the gallery is forge scale — the bill for every extra minute the steel spends at heat in an open charcoal fire, and every bit of it has to come off on the grinder, taking blade thickness with it. Working without an anvil costs accuracy too: a stone slab does not return energy to the hammer the way a hardened face does, so the same shape takes more heats to reach, and more heats means more scale.

## Gallery

<figure>
  <img src="{{ site.baseurl }}/assets/img/bladesmithing/forging-on-stone.jpg" alt="Working at a ground forge: a person lifting a stone slab beside a small block-walled hearth burning charcoal in a dug pit.">
  <figcaption>The first forge, December 2022: blocks set into a pit, charcoal, and a slab to work on.</figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/assets/img/bladesmithing/forge-pit-aug2024.jpg" alt="A shallow forge dug into red laterite soil, charcoal burning in the centre, a length of pipe entering from one side as a tuyere.">
  <figcaption>The third forge, August 2024. The pipe is the air supply; everything else is earth and charcoal.</figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/assets/img/bladesmithing/forge-fire-aug2024.jpg" alt="A charcoal forge at dusk throwing a tall fountain of orange sparks well above the fire.">
  <figcaption>The third forge at full draught, August 2024. Those are charcoal sparks, not steel burning.</figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/assets/img/bladesmithing/forge-hearth-jan2024.jpg" alt="A raised forge hearth built into a plastered trough, lined with earth and stone, with charcoal glowing red in the middle.">
  <figcaption>The second forge, January 2024: raised to working height, lined, holding a smaller and hotter fire.</figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/assets/img/bladesmithing/quench.jpg" alt="Tongs holding a blade above a white bucket of water, the surface still rippling from the quench.">
  <figcaption>The quench. This is the operation that decides whether the last three hours were worth anything.</figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/assets/img/bladesmithing/gifu-workshop.jpg" alt="Abhiram at a forge in a timber-framed workshop, a dense column of orange sparks rising from the hearth beside him.">
  <figcaption>At Asano Kajiya's workshop in Gifu, May 2024.</figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/assets/img/bladesmithing/gifu-blade.jpg" alt="A rough-forged blade blank held in one hand over a worn timber bench, a wooden-handled file and a small stake tool lying behind it.">
  <figcaption>The blank I was drawing out in Gifu, on somebody else's very good bench.</figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/assets/img/bladesmithing/forged-blanks.jpg" alt="Three forged blade blanks laid on a white sheet, edges partly ground bright, the rest still dark with forge scale.">
  <figcaption>Three blanks part-way through grinding. The dark patches are forge scale.</figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/assets/img/bladesmithing/rough-ground-blades.jpg" alt="Two rough-ground blades held in one hand outdoors against red earth, still unhandled, drilled for pins.">
  <figcaption>Two blades drilled for pins, before handles.</figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/assets/img/bladesmithing/finished-knives.jpg" alt="Three finished kitchen knives with red wooden handles laid side by side, blades polished, on a dark seat.">
  <figcaption>Three finished kitchen knives.</figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/assets/img/bladesmithing/chefs-knife.jpg" alt="A finished chef's knife with a pale burl wood handle, blade left dark with forge finish, photographed on white paper.">
  <figcaption>A chef's knife with the forge finish left on the blade.</figcaption>
</figure>
