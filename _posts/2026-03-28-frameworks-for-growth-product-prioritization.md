---
title: "Frameworks for Growth Product Prioritization"
subtitle: "A few simple ways to decide what to ship when everything looks important"
description: "Notes on choosing the right prioritization framework for growth work, from experiments and onboarding fixes to platform investments."
date: 2026-03-28
image: /assets/images/ai-growth.png
layout: post
---

Growth work has a way of making everything feel urgent.

There’s always another onboarding step to improve, another activation drop-off to investigate, another lifecycle message to test, another pricing idea sitting in a doc somewhere. When a team starts taking growth seriously, the backlog expands fast. That’s usually a good sign. It means you’re seeing more opportunities.

The harder part is deciding what deserves attention now.

I’ve found that growth prioritization gets messy when teams use one framework for every kind of problem. Not all growth work is the same. A signup funnel fix is different from a referral loop. A quick experiment is different from rebuilding instrumentation. A pricing test is different from a months-long investment in team velocity.

So this post is less about *the* perfect framework and more about building a practical toolkit.

## Start with the kind of decision you’re making

Before scoring ideas, it helps to name the type of work in front of you.

A lot of prioritization pain comes from comparing unlike things:

- small experiments vs. foundational investments
- near-term conversion wins vs. long-term retention bets
- local optimizations vs. system improvements
- ideas with clear evidence vs. ideas based mostly on instinct

If all of these get put into one spreadsheet with one score, the output might look rigorous, but it often isn’t very useful.

A better starting point is to sort growth work into a few buckets:

- **Experiments:** fast tests with a clear hypothesis
- **Optimizations:** known friction points with fairly obvious upside
- **Infrastructure:** analytics, tooling, experimentation platform, data quality
- **Strategic bets:** pricing, packaging, acquisition loops, new channels, major onboarding redesigns

Once you know the category, the prioritization method usually gets simpler.

## Use RICE when the inputs are real enough

RICE is still useful. Reach, Impact, Confidence, Effort is a decent way to compare opportunities when you have at least some signal.

It works especially well for:

- onboarding improvements
- activation funnel ideas
- lifecycle interventions
- surfaces with meaningful traffic
- known problems with measurable conversion points

What I like about RICE is not the math. It’s the forcing function. It makes a team ask:

- How many people will this actually affect?
- If it works, how much does it matter?
- How confident are we that this is the real problem?
- What will it cost us to learn or ship?

That said, RICE breaks down when the numbers are fake-precise. If reach is a guess, impact is vibes, confidence is inflated, and effort ignores coordination cost, the score becomes theater.

For growth teams, I think RICE is best used as a structured conversation rather than a truth machine.

A simple version is usually enough:

- **Reach:** how much user volume is exposed
- **Impact:** how much movement you expect on the target behavior
- **Confidence:** how strong the evidence is
- **Effort:** design, engineering, analytics, review, and operational complexity

The important part is consistency. If the team scores one idea harshly and another generously, the framework won’t save you.

## Use ICE when speed matters more than precision

Sometimes you don’t need a robust model. You just need to decide what to test next.

That’s where ICE can be helpful: Impact, Confidence, Ease.

It’s lighter than RICE and better suited to a fast-moving experiment backlog. Especially in early-stage growth work, you often don’t know reach well enough for it to be worth debating.

ICE is useful when:

- you have many test ideas and limited time
- the cost of being directionally right is low
- you want to keep momentum without over-analyzing
- you’re working in a part of the product where measurement is still improving

The trap here is overvaluing ease. Teams naturally drift toward the easiest shippable things. That can create a long list of clean, tidy tests that never touch the main constraint.

So if you use ICE, it helps to pair it with one additional question:

**Is this aimed at the biggest current growth bottleneck?**

An easy test on the wrong part of the funnel is still the wrong test.

## Use constraint-based prioritization when the funnel is the story

A lot of growth prioritization gets easier when you stop treating the roadmap as a pile of ideas and start treating it as a system.

Every growth model has constraints. Maybe acquisition is healthy but activation is weak. Maybe activation is fine but retention drops before users experience value. Maybe retention is decent but expansion is underdeveloped. Maybe the issue isn’t product at all, but traffic quality.

When the team agrees on the current constraint, prioritization becomes much more grounded.

Instead of asking, “Which idea has the highest score?” you ask:

**What is most likely to relieve the limiting factor in the system?**

This approach is especially helpful because it reduces random acts of optimization. It keeps teams from polishing metrics that aren’t currently binding.

A simple way to work this way:

1. Map the user journey from acquisition to retained value.
2. Identify where the largest meaningful drop or friction exists.
3. Validate that it’s a real constraint, not just the most visible metric.
4. Prioritize work that directly addresses that point.
5. Re-evaluate once the system shifts.

This isn’t as neat as a spreadsheet score, but it’s often closer to reality.

## Separate learning bets from delivery bets

One of the most useful distinctions in growth prioritization is this:

Some work is meant to **learn**.  
Some work is meant to **deliver**.

Learning bets answer questions:

- Do users understand this value prop?
- Does social proof change conversion here?
- Are users dropping because of confusion or motivation?
- Will a tighter paywall increase starts but hurt downstream quality?

Delivery bets are different. They’re based on stronger evidence and are expected to produce meaningful business impact.

The mistake is treating both kinds of work the same way.

A learning bet may be worth doing even if the direct upside is modest, because it reduces uncertainty around a much bigger opportunity. A delivery bet should usually clear a higher bar on confidence, coordination, and expected outcome.

I like seeing these separated in the backlog. It creates healthier conversations.

Otherwise teams end up arguing past each other. One person is optimizing for insight. Another is optimizing for shipped impact. Both are reasonable. They’re just using different standards.

## For strategic growth bets, use narrative over scoring

Big growth opportunities often don’t fit tidy prioritization models.

Think:

- changing pricing and packaging
- introducing a referral mechanism
- shifting self-serve onboarding
- investing in enterprise-ready expansion paths
- entering a new acquisition channel that changes the top of funnel

These are not just backlog items. They’re strategic choices with dependencies, second-order effects, and real downside risk.

For these, I’ve found that a written narrative is usually better than a score.

A good strategic prioritization memo might cover:

- the problem or opportunity
- why it matters now
- what evidence supports it
- what assumptions are unresolved
- expected upside if it works
- likely costs and tradeoffs
- how long it will take to know if it’s working
- what we won’t do if we pursue it

This forces clearer thinking than assigning a 7 for impact and a 3 for effort.

Growth leaders sometimes reach for scoring frameworks because they feel objective. But on larger bets, false objectivity can hide weak reasoning. A short, honest narrative tends to expose it faster.

## Add a “cost of delay” lens

Some growth work is valuable not because it has the highest upside, but because waiting makes it more expensive.

Examples:

- missing instrumentation that blocks learning
- compliance or deliverability issues affecting lifecycle channels
- technical debt in experimentation infrastructure
- onboarding friction compounding user confusion every day
- seasonal opportunities with a short window

This is where cost of delay is useful.

If two ideas look similar in expected impact, but one gets worse every month you postpone it, that should matter. Prioritization frameworks often underweight time.

You don’t need a complicated model here. Just ask:

- What happens if we do this next quarter instead?
- Does delay reduce the upside?
- Does delay increase the cost?
- Does delay block other work?

Growth teams are often under pressure to show quick wins. That can make it easy to defer invisible but important work. Cost of delay helps balance that instinct.

## Don’t let scoring replace judgment

This is probably the main thing.

Frameworks are there to improve judgment, not replace it.

A healthy prioritization process usually combines a few inputs:

- quantitative evidence
- qualitative insight
- strategic context
- team capacity
- sequencing constraints
- intuition from people close to the user and the system

If a framework says an idea should rank first, but everyone with context knows it’s not the right next move, that tension is worth unpacking. Sometimes the framework reveals bias. Sometimes the framework is just flattening reality.

Either way, the conversation is the point.

## A practical stack that works well enough

If I were setting up a simple growth prioritization system for a team, I’d probably use something like this:

**1. Start with the current growth constraint.**  
Align on where the biggest bottleneck is right now.

**2. Split work into categories.**  
Experiments, optimizations, infrastructure, strategic bets.

**3. Use lightweight scoring within each category.**  
ICE or RICE for comparable items, not for everything.

**4. Separate learning bets from delivery bets.**  
Different goals, different bars.

**5. Use narrative memos for bigger decisions.**  
Especially when the work changes systems, not just screens.

**6. Review often.**  
Growth systems move. The thing worth prioritizing this month may not be the thing worth prioritizing next month.

That may sound less elegant than having one master framework, but I think it maps better to the actual work.

## What good prioritization feels like

Good growth prioritization doesn’t mean everyone agrees all the time.

It usually feels more like this:

- the team knows what problem it is trying to solve
- the reasons behind priorities are visible
- quick tests don’t crowd out important investments
- important investments don’t smother momentum
- strategy and execution are connected
- people can disagree without the whole process breaking down

That’s a better bar than perfect scoring.

In practice, prioritization is mostly about shared clarity. Frameworks help, but only if they help the team see the work more honestly.

And in growth, honesty matters. There are too many tempting ideas, too many local wins, and too many ways to confuse motion with progress.

So I’d keep the frameworks. Just hold them lightly.