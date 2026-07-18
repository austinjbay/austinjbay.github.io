---
title: "Write the detour map before the user needs it"
subtitle: "Why retained usage depends on how your product handles the first broken expectation, not only the first successful flow."
description: "A detour map helps teams design for the first broken expectation so users can recover momentum instead of quietly drifting."
date: 2026-07-13
image: /assets/images/notebook.jpg
layout: post
---

I think a lot of growth teams overdesign the straight line.

The landing page is tuned.

The setup flow gets cleaner.

The checklist gets shorter.

The first value moment gets measured to death.

Then the real world arrives and bends the route.

The CSV has duplicate columns.

The teammate invite sits unanswered.

The AI draft is close but not safe to send.

The integration connects but syncs only part of the account.

The reminder email brings someone back into a state that now behaves differently than it did yesterday.

That bend is where a lot of product judgment becomes visible.

Not because the product failed in some dramatic way.

Because the user has to answer a quieter question.

When the obvious next move stops working, does this product still help me continue.

## The happy path gets too much credit

I do not think teams do this on purpose.

The straight line is easier to storyboard.

It is easier to instrument.

It is easier to test in a clean experiment.

It is easier to present in a review.

The detour is messier.

It often sits between functions.

Part of it feels like UX.

Part of it feels like lifecycle.

Part of it feels like support.

Part of it feels like backend reliability.

So it becomes everybody's concern in theory and nobody's artifact in practice.

That is expensive.

A lot of users do not leave because the product lacked a happy path.

They leave because the first detour made the product feel brittle, blameful, or forgetful.

I keep coming back to [NN Group's guidance on error messages](https://www.nngroup.com/articles/error-message-guidelines/) for this reason. The useful point is not only that error copy should be clear. It is that products should help people recognize what happened, recover efficiently, and preserve their effort.

That is not a narrow UI writing lesson.

I think it is a growth lesson.

If the product breaks the user's momentum at the first non-ideal moment, the team may still log a completed signup while quietly losing the chance at repeated use.

## Detours are where trust becomes operational

Trust sounds abstract until the product needs to recover.

Then it gets concrete fast.

Did my work survive.

Do I know what happened.

Is there a safe next step.

Can I still get to the outcome I came for.

Do I need to wait, fix something, or ask someone else.

Products that answer those questions well feel calm, even when something goes wrong.

Products that do not answer them push interpretation work back onto the user.

The user has to diagnose the situation, guess at severity, and invent a fallback plan.

That is effort most dashboards do not count.

I think of this the same way I think about city transit during a service interruption.

People can tolerate a reroute surprisingly well when the system makes the reroute legible.

Which line is affected.

What still runs.

What alternate path will get me close.

How long the delay will likely be.

When the signs are good, the system still feels competent.

When the signs are bad, even a minor interruption feels chaotic.

Products work the same way.

The product does not need to pretend the route is still perfect.

It needs to help the user keep moving with confidence.

## Good detours preserve progress, not only politeness

This is the part I think teams underrate.

Many products have learned how to apologize.

Fewer have learned how to preserve motion.

The best recovery moments do more than say something went wrong.

They make a few practical things obvious.

- What still succeeded
- What failed or is incomplete
- What work was preserved
- What the safest next move is
- What backup path still leads toward value
- When the user should come back if time is part of the answer

That standard shows up in service design more than product teams usually admit. The [GOV.UK error message guidance](https://design-system.service.gov.uk/components/error-message/) is blunt in a useful way. Explain what went wrong and how to fix it.

Again, that sounds basic.

It is.

But a lot of growth surfaces still stop one step early.

They acknowledge the issue without helping the user continue.

A trial user imports contacts and gets a vague warning.

A returning user clicks a lifecycle nudge and lands in a generic account home.

A teammate accepts an invite and sees an empty workspace without the setup context that would make the invitation make sense.

An AI flow says something could not be generated right now but does not preserve the prompt, the partial work, or the clearer fallback.

In each case the product may be technically honest while still being operationally unhelpful.

That gap matters because detours often happen at the exact moment the user is deciding whether your product is sturdy enough for regular life.

## Cloud systems and good kitchens both publish the backup plan

One reason I like borrowing ideas from infrastructure is that infrastructure teams are less embarrassed about contingency planning.

Google Cloud's guidance on [graceful degradation](https://cloud.google.com/architecture/framework/reliability/graceful-degradation) is useful because it treats partial service as a design choice, not only a failure state.

Keep core functions available.

Reduce scope intelligently.

Help the system stay useful under strain.

I think product teams should steal that instinct.

Not every growth flow can stay fully intact under every condition.

That is fine.

The question is whether the product degrades in a way that preserves the user's sense of progress.

A good kitchen does this all the time.

If a dish is eighty-sixed, the staff does not merely announce disappointment.

They reroute the table.

They name the constraint.

They suggest the closest good alternative.

They keep the meal moving.

That is what a product should do when the obvious route is unavailable.

Not hide the detour.

Design it.

## The artifact I like is a detour map

When a team has decent first session movement but weak repeat confidence, I would write a detour map.

Not a giant service blueprint.

Not a full edge case taxonomy.

Just a small working artifact for one meaningful journey.

Usually an onboarding path, a collaborator path, an import flow, a lifecycle return path, or an AI assisted workflow where partial failure is common enough to matter.

## Detour map

- Primary user job
- Normal path to first meaningful value
- First likely detour or broken expectation
- What the user will most likely fear in that moment
- What progress must be preserved
- What explanation should appear in plain language
- What safest next move should be obvious
- What fallback path still keeps the user near the original job
- What lifecycle, support, or in product follow up should close the loop if recovery is delayed
- Evidence
- Owner

That is enough to expose a lot.

You start noticing when the system knows more than the interface reveals.

You see where support articles are carrying clarity that the product should carry itself.

You find lifecycle messages that reopen a journey without respecting the detour already in progress.

You notice places where teams measured start rate carefully and left recovery quality to chance.

## What changes once the detour is visible

A few useful things usually happen.

Onboarding gets more honest because the team stops acting like setup will proceed cleanly for everyone.

Activation gets stricter because progress is no longer counted as healthy if one weird moment can erase user confidence.

Lifecycle gets sharper because reminders can acknowledge the state the user is actually in instead of sending everyone back to the same generic surface.

Product judgment improves because people stop debating only the ideal route and start asking whether the product remains competent under ordinary mess.

That last part matters to me.

I think a lot of retained usage is shaped by whether the product feels graceful on a Tuesday afternoon when the user's data is odd, their teammate is late, and their attention is already split.

Not when the demo script is clean.

## Where I would start

I would not begin with every exception your system has ever produced.

I would pick one path with real business weight and real user intent.

Maybe the first import.

Maybe the first invite.

Maybe the first AI generated artifact someone might actually reuse.

Maybe the lifecycle return path for users who already started something important.

Then I would ask a plain question.

If the obvious route bends here, does the product still leave the user with a believable way forward.

If the answer is no, I do not think that is a support cleanup task.

I think it is growth work.

Because repeated use depends on more than initial success.

It depends on whether the product can carry momentum through ordinary interruption.

## The point

The best products do not only make progress feel possible when everything behaves.

They make progress feel recoverable when something does not.

That is what a good detour map protects.

Not perfection.

Continuity.
