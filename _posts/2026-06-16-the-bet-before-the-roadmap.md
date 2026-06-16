---
title: "The Bet Before the Roadmap"
subtitle: "How growth PMs turn fuzzy conviction into experiments worth running."
description: "A lightweight bet memo template for turning early product conviction into practical experiments before the roadmap hardens around a solution."
date: 2026-06-16
layout: post
tags: [Product Discovery]
---

There is a funny little moment that happens before a roadmap becomes a roadmap.

Someone notices a pattern. A customer keeps saying the same thing in calls. A metric refuses to move. A competitor ships something annoying enough that everyone has an opinion. A support thread feels less like a one-off and more like smoke from a larger fire.

The team starts to develop conviction before it has a plan.

That stage is easy to skip because it does not look very official. It usually lives in Slack threads, notebook margins, hallway conversations, messy docs, and the five minutes after a meeting when someone says, “Wait, I think there might be something here.”

But for growth PMs, that fuzzy stage matters a lot.

It is where the bet starts.

Not the feature. Not the quarter-long initiative. Not the beautifully formatted roadmap item. The bet.

The thing we believe might be true enough to spend real time learning about.

## Roadmaps are bad at holding early conviction

Roadmaps are useful. I have written many of them. I will write many more.

But roadmaps have a way of making ideas look more certain than they are. Once something becomes a line item, it inherits a little costume of inevitability. It gets a name, a rough delivery window, maybe a sizing estimate. People start asking when it will ship instead of whether it is the right thing to learn next.

That shift can happen before the team has done the more important work of naming the belief underneath the idea.

For example:

- “Improve onboarding” might really mean “we believe new users do not reach value quickly enough.”
- “Launch a referral program” might really mean “we believe happy users have unused social motivation we are not giving them a way to act on.”
- “Build an AI assistant” might really mean “we believe users are getting stuck because they do not know what to do next, not because the underlying workflow is too hard.”

Those are different bets. They might lead to different experiments, different designs, and different ways of judging success.

If we rush straight to the roadmap item, we lose the nuance.

## The job is to make the bet visible

A lot of growth work starts as a hunch with receipts.

Not a random hunch. Not a vibe wearing a blazer. A hunch built from usage data, user conversations, competitive context, search behavior, lifecycle performance, sales objections, or the weird little patterns you only notice after staring at a funnel for too long.

The PM job is not to pretend that hunch is certainty.

The job is to make it visible enough that the team can inspect it together.

What do we believe? Why do we believe it? What is the smallest responsible way to learn? What would change our mind? Why now instead of later?

That is the bet before the roadmap.

I have found that when teams write this down early, the conversation gets better almost immediately. Designers can challenge the assumed user need. Engineers can suggest cheaper ways to learn. Data partners can pressure test the signal. Marketing can name channel realities. Leadership can see the shape of the risk without needing the team to over-package the solution.

The artifact does not need to be long. In fact, it is usually better when it is short.

## A lightweight bet memo

Here is the version I keep coming back to:

> **We believe...**
>
> **Because we observed...**
>
> **The smallest way to learn is...**
>
> **We'll know we're wrong if...**
>
> **This is worth doing now because...**

That is it.

It is not a PRD. It is not an experiment readout. It is not a strategy doc trying to win a Pulitzer in the appendix.

It is a container for conviction before the team turns conviction into commitments.

### We believe...

This is the actual bet.

Try to write it in plain language. If it takes three paragraphs to explain, it may not be clear enough yet. If it sounds like a feature request, push one layer deeper.

A feature-shaped version might be:

> We believe we should add more reminders during setup.

A bet-shaped version is closer to:

> We believe new users who complete one meaningful action in their first session are more likely to return, but too many users leave before finding that action.

Now there is something to work with.

### Because we observed...

This is where the receipts go.

The evidence can be quantitative or qualitative. Ideally it is some mix of both, but early bets rarely arrive with perfect instrumentation and a statistically satisfying bow on top.

That is fine. Just be honest about what you have.

- Trial users with no completed workflow churn at a much higher rate.
- Sales calls keep surfacing the same setup anxiety.
- Search demand is growing around a use case we barely address.
- Users who touch a certain template retain better, but most new users never see it.
- A side quest prototype got more organic usage than expected.

The point is not to make the evidence sound stronger than it is. The point is to show what created the conviction.

### The smallest way to learn is...

This is the part that keeps a bet from becoming a bloated roadmap item too early.

Small does not always mean easy. It means sized to the uncertainty.

Sometimes the smallest way to learn is a fake door, a concierge test, a lifecycle email, a one-off landing page, a prototype in five user calls, a manual workflow behind the scenes, or a narrowly scoped experiment for one segment.

Sometimes it is a side quest.

I think this is one of the underrated values of side projects at work. They give teams a place to explore adjacent conviction without forcing every idea through the main-roadmap machinery too soon. A small tool, a scrappy internal prototype, or a low-risk surface area can teach you whether the opportunity has a pulse.

The trick is to be clear about what you are trying to learn. A side quest without a learning goal can become a distraction. A side quest with a crisp bet can become a very cheap compass.

### We'll know we're wrong if...

This field is uncomfortable in the best way.

It asks the team to name the evidence that would make them stop, shrink the idea, or change direction.

Not because we want the work to fail. Because we want to protect ourselves from falling in love with the shape of the solution.

Examples:

- Users see the prompt but do not take the action.
- The action increases, but downstream activation does not improve.
- The users who engage are not the segment we intended to serve.
- Qualitative feedback shows the problem is real, but our proposed timing feels intrusive.
- The manual version requires so much support that it breaks the economics of the idea.

This is also where teams can separate “the bet was wrong” from “the execution was wrong.” That distinction matters. Sometimes the underlying belief is still right, but the test was too buried, too slow, too confusing, or aimed at the wrong moment.

Writing the failure condition up front makes the later readout less political.

### This is worth doing now because...

Growth teams usually have more plausible ideas than capacity.

The now matters.

Why this bet, this month, with these people, instead of the other ten things we could do?

Good answers might include:

- The user pain is showing up across multiple channels.
- The experiment is cheap and could unlock a larger roadmap direction.
- A new technical capability makes the test possible now.
- Seasonality creates a narrow learning window.
- The team has adjacent work in flight, so the marginal cost is lower.
- The current roadmap has a dependency that this learning could de-risk.

Bad answers usually sound like “because a stakeholder asked for it loudly” or “because we already put it in the deck.”

Those may be real pressures. They are not the same thing as strategic timing.

## An example bet memo

Here is a deliberately simple version:

> **We believe...** new users are more likely to activate if they complete one useful workflow before we ask them to configure the rest of the product.
>
> **Because we observed...** users who complete that first workflow retain better, while session recordings and support tickets suggest setup asks are creating friction before users understand the payoff.
>
> **The smallest way to learn is...** to route a small segment of new users into a guided first workflow and delay two setup prompts until after completion.
>
> **We'll know we're wrong if...** completion of the first workflow does not increase, users still abandon at the same step, or delayed setup prompts reduce downstream team adoption without improving activation.
>
> **This is worth doing now because...** the onboarding team is already touching this surface area, and the result could clarify whether next quarter's roadmap should focus on faster value discovery or deeper setup education.

This is not fancy. That is why I like it.

You can imagine a designer sketching from it. You can imagine an engineer proposing a simpler routing approach. You can imagine a data partner turning it into an experiment plan. You can imagine a PM saying, “Actually, I think the risk is not setup friction. I think it is unclear motivation.”

Great. That is the point.

The memo gives the team something specific to disagree with.

## Bets make roadmap conversations more honest

A roadmap is often a bundle of bets pretending to be a schedule.

That is not a criticism. It is just the nature of product work. We are trying to allocate effort against an uncertain future with imperfect information and a lot of humans involved.

The healthiest teams I have worked with do not remove uncertainty. They get better at handling it.

They say things like:

- “This is a high-conviction, low-evidence bet.”
- “This is a low-cost learning bet before we decide whether to staff the bigger version.”
- “This is strategically important, but the riskiest assumption is user motivation.”
- “This is probably not roadmap-ready yet, but it is experiment-ready.”

That language is useful because it creates more options than yes or no.

Some bets deserve a roadmap slot. Some deserve a two-week experiment. Some deserve a prototype. Some deserve a side quest. Some deserve to be written down and left alone until the evidence gets louder.

## A small ritual

Before an idea graduates into planning, try asking for the bet memo.

Not as a bureaucratic gate. Not as homework for the PM. More like a small ritual of clarity.

If the memo is easy to write, the team probably understands the idea well enough to decide what to do next.

If the memo is hard to write, that is useful too. It means there is still fog around the user, the evidence, the learning path, or the timing.

Better to find that fog before the roadmap hardens.

The best product bets often start as fuzzy conviction. A good team does not shame that fuzziness out of the room. It gives it a shape, runs the smallest useful test, and stays honest about what it learns.

That is the work before the work.

And in growth, it is often where the real leverage begins.
