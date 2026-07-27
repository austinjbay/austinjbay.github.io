---
title: "Map the exception path before you optimize the happy path"
subtitle: "Why growth teams should design recovery, retries, and awkward edge conditions with the same care they give the clean demo flow."
description: "A growth PM field note on exception handling, recovery design, and a simple exception map that helps teams protect momentum when real users arrive with imperfect conditions."
date: 2026-07-27
image: /assets/images/desk.jpg
layout: post
---

I think one of the easiest ways for a growth team to fool itself is to confuse a smooth demo path with a resilient product path.

The ad makes sense.

The homepage is clear.

The signup looks light.

The checklist moves.

The key action fires.

The dashboard records a win.

Then a real user shows up with the wrong file, the wrong expectation, the wrong permissions, a teammate who never accepted the invite, a calendar that syncs halfway, or a setup step they cannot finish until tomorrow.

That is where a lot of apparent momentum disappears.

Not because the product lacked a value proposition.

Because the product only really knew how to behave on a good day.

## The happy path gets too much of the team's moral attention

I understand why this happens.

The happy path is legible.

It is easy to storyboard.

It is easy to prototype.

It is easy to describe in a planning doc.

It is usually the path leadership sees in the demo and the one the experiment dashboard is built around.

But growth product is not only about making the ideal journey shorter.

A lot of the craft is about protecting motion when reality gets untidy.

The CSV has duplicate rows.

The domain cannot be verified yet.

The teammate who needed admin access is on vacation.

The prospect clicked from search with the wrong mental model.

The AI draft is close but too risky to send unchanged.

The user can see the next step but not complete it right now.

Those are not side quests.

Those are the product.

I think this is one reason teams can improve conversion on the clean path and still feel disappointed by the lived quality of activation or retention. The system gets better at starting momentum than at preserving it.

## Real growth work starts where the script breaks

One of the best product lessons hiding in plain sight comes from service design.

The [GOV.UK guidance on recovering from validation errors](https://design-system.service.gov.uk/patterns/validation/) is very plain about what good recovery looks like. Keep the user's information when you can. Explain what went wrong. Help them fix it. Do not make them re-enter work that is still usable.

That is not only form design advice.

I think it is a growth principle.

When a user hits a snag, the product should preserve as much progress, context, and dignity as possible.

That matters in onboarding.

It matters in upgrade flows.

It matters in AI assisted work.

It matters in referral loops and imports and invite flows and lifecycle returns.

A lot of churn is not dramatic rejection.

It is the accumulation of small recoveries the product handled badly.

The user has to guess what failed.

They have to repeat steps the system could have remembered.

They have to hunt for the one condition that is blocking progress.

They have to decide whether the problem is temporary, permanent, or their own fault.

Each moment is recoverable.

Together they make the product feel like an unreliable coworker.

## Distributed systems are stricter about retries than many products are

This is where I think software infrastructure is often more honest than product growth work.

The Amazon Builders' Library article on [making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) is about backend systems, but I think the underlying idea travels well. If a request has to be retried, the user should not pay twice for the same intent.

That is a technical principle.

It is also a product principle.

If a user retries an import, resends an invite, reconnects a calendar, regenerates a draft, or returns to finish setup after a timeout, the product should treat that as the same underlying job unless something meaningfully changed.

Yet a lot of growth surfaces behave as if every retry is a fresh burden.

The user has to restate the context.

The previous effort disappears.

The system creates duplicates.

The state becomes harder to interpret.

The user stops trusting that another click is safe.

That is not just a reliability problem.

It is a momentum problem.

I think growth teams should care more about retry safety because retry safety shapes whether an interrupted user comes back with confidence or reluctance.

## The best edge case work often begins with one excluded user

I also keep coming back to Microsoft's inclusive design principle to [solve for one and extend to many](https://inclusive.microsoft.design/articles/inclusive-101-guidebook).

I like it because it pushes against a lazy product habit.

We often call something an edge case when what we really mean is we do not feel like designing for that condition yet.

The tired parent using the product one-handed.

The new admin inheriting a messy workspace.

The user working through a flaky hotel connection.

The analyst who does not know the team's internal vocabulary yet.

The manager who can approve a tool but cannot complete the technical setup alone.

If you design recovery and wayfinding for that sharper condition, a lot of ordinary users get a better product too.

The interface becomes calmer.

The instructions get plainer.

The state gets more legible.

The next move becomes safer.

That is not edge-case work in the pejorative sense.

That is often the shortest route to a product that handles normal life.

## Products lose trust when they treat every problem like user error

This is another pattern I think is worth naming.

Some products respond to every break in the flow as if the user simply did the wrong thing.

Red text appears.

The button disables.

The system says there was a problem.

Nothing useful gets preserved.

Nothing specific gets explained.

The next move stays vague.

The [Nielsen Norman Group article on error-message guidelines](https://www.nngroup.com/articles/error-message-guidelines/) is still durable because it keeps returning to the same obligation. Tell users what went wrong in language they can understand and offer a constructive path forward.

That sounds obvious.

It is still surprisingly rare in growth surfaces.

Especially in flows where the system itself is carrying hidden complexity.

An import depends on formatting rules the user has never seen.

A setup step depends on a role they do not have.

A model output is blocked because the source quality was thin.

A shared workflow paused because another person has to act next.

The product knows a lot about the exception.

The user gets a shrug.

That is a bad bargain.

## The artifact I like is an exception map

When a growth team has a funnel that looks healthy in the mock and strangely brittle in the wild, I would write an exception map.

Not a giant service blueprint.

Not a taxonomy so comprehensive that nobody updates it.

Just a small working artifact for one important journey.

Usually a path with high intent and real interruption risk.

An onboarding flow.

An import flow.

An invite and collaborate flow.

An AI assisted draft flow.

A checkout with delayed verification.

Something where the user can make progress, hit a non-ideal condition, and still deserve a graceful route forward.

## Exception map

- The job the user thinks they are trying to complete
- The clean path the team usually demos
- The most common non-ideal conditions that interrupt that path
- Which of those conditions are user-fixable, system-fixable, or time-dependent
- What progress can be safely preserved when the interruption happens
- What retry should mean in each case
- What message would make the problem legible without sounding accusatory
- What next step should be available immediately
- What alternate path should exist if the clean path is blocked for a while
- What evidence would tell you the recovery path is working
- Owner

That is enough.

The goal is not to eliminate every messy condition.

The goal is to stop treating messy conditions as unowned.

## What usually changes once the map exists

A few useful things happen.

The team notices how many failure states are really silence states.

You find places where the product can preserve more state than it currently reveals.

You separate user mistakes from system constraints, which makes the copy less blameful and the flow easier to recover.

You see where an alternate path should exist instead of a dead end.

You start measuring recovery quality, not only first-pass completion.

That last point matters a lot to me.

A lot of growth dashboards quietly teach the team to admire first-pass success and ignore second-pass resilience.

But real users are busy, distracted, under-permissioned, on deadline, and occasionally confused for perfectly rational reasons.

A product that only works beautifully when conditions are pristine is not actually reducing friction very much.

It is just selecting for users who can supply their own resilience.

## The craft is not only in simplification

I still believe in removing steps.

I still believe in cleaner onboarding.

I still believe in sharper positioning and faster first value.

But I think there is another kind of craft that matters just as much in growth product.

It is the craft of making forward motion survive imperfection.

The user should be able to hit a wrong turn, a delay, a missing dependency, or a temporary failure without feeling like the whole story reset.

That is when the product starts feeling mature.

Not when the happy path gets one step shorter.

When the non-happy path still respects the user's intent.
