---
title: "Do not mistake a stack of tests for a portfolio"
subtitle: "Why a busy growth roadmap can still be one concentrated bet."
description: "A growth PM field note on finding shared assumptions across experiments and building a portfolio that can teach you more than one lesson."
date: 2026-09-27
image: /assets/images/notebook.jpg
layout: post
---

I think growth teams are unusually good at making one bet look like ten.

We test a shorter signup form.

We test a new landing page.

We test a lifecycle sequence.

We test a pricing message.

We test a different activation checklist.

The roadmap looks varied because the surfaces are different. There are different mocks, owners, metrics, and launch dates.

But all five tests might depend on the same belief.

The right users already understand the category and only need a little less friction before they act.

If that belief is wrong, the team does not have five independent ways to learn. It has five versions of the same disappointment.

A full experiment calendar is not necessarily an experiment portfolio.

## Variety on the surface can hide concentration underneath

Product teams usually group experiments by where they appear.

Acquisition owns the landing page. Onboarding owns setup. Lifecycle owns email. Monetization owns the paywall.

That division is useful for getting work done. It is less useful for understanding what the work assumes.

A landing-page rewrite and a welcome email can share a belief about urgency.

A template picker and an onboarding checklist can share a belief that users know which outcome they want.

A referral prompt and a team trial can share a belief that the first user has social permission to bring someone else in.

A paywall test and an annual-plan email can share a belief that the value is already legible enough for price to be the remaining objection.

When we review those tests by surface, they look unrelated. When we review them by premise, they start to bunch together.

That bunching matters because experiment count can create false comfort. Ten launches suggest ten chances to be right. Ten launches built on one uncertain premise are closer to one chance repeated ten times.

## Finance has a better definition of variety

Portfolio thinking offers a useful correction.

Owning many assets is not the same as being diversified when those assets tend to move together. The US Securities and Exchange Commission’s investor education site makes the same practical distinction in its guidance on [asset allocation and diversification](https://www.investor.gov/introduction-investing/getting-started/asset-allocation). Spreading money across investments can reduce risk, but concentration can remain when the holdings share the same exposure.

Growth roadmaps have exposures too.

They are assumptions about motivation, comprehension, trust, timing, intent, and the job a user is trying to do.

Imagine a team running eight onboarding tests. Four remove steps. Two make the call to action louder. Two add reminders after abandonment.

That looks like a healthy amount of experimentation.

It may still be heavily exposed to the belief that willing users are being blocked by effort.

None of the tests seriously examine whether people are unsure what the product is for, whether the promised outcome matters yet, or whether the initial use case attracts people who were never likely to retain.

If effort is not the real constraint, the portfolio can lose across every row while teaching the same lesson slowly.

The lesson from finance is not that PMs should calculate a clever frontier for the roadmap. It is simpler.

Count shared exposure, not only individual items.

## Reliability engineering asks how separate things fail together

There is a second useful connection in reliability engineering.

Redundancy sounds reassuring until supposedly independent components depend on the same thing. Two services can run on separate machines and still fail together because they rely on the same upstream system, configuration, or overloaded resource.

The Google SRE book’s chapter on [addressing cascading failures](https://sre.google/sre-book/addressing-cascading-failures/) describes how local overload can spread through retries and shared dependencies. Adding more moving pieces does not automatically create resilience. Sometimes it creates more paths for one failure to travel.

The same is true of a growth program.

Different experiments can share an audience source that is becoming less qualified.

They can share an event whose meaning is weaker than the team thinks.

They can share copy based on the same untested customer story.

They can share a model of activation that rewards quick setup even when durable value takes a different shape.

They can share a seasonal moment that makes every result look healthier.

This is not an argument against coordinated strategy. A portfolio should have a point of view.

It is an argument against confusing coordination with independent evidence.

If every test fails when one premise fails, the team should know that before it reads five results as five separate votes.

## The artifact I like is a shared-assumption map

I would make this beside the experiment roadmap, not inside each individual test brief.

Put upcoming experiments down the left side. Put the important assumptions across the top. Mark every assumption that has to be true for each test to work.

Useful columns often include these.

- The user has the problem we think they have
- The arriving audience is sufficiently qualified
- The user understands the promise
- The user can act without help from someone else
- The proposed moment is when the need is live
- The behavior we measure represents meaningful progress
- The value is strong enough for the user to return
- The commercial trade feels reasonable after value is understood

The exact labels should come from the product, not this list.

Then add four fields for each assumption.

- Evidence we have already seen
- Experiments exposed to it
- A test that could distinguish it from a competing explanation
- What we would change if it were false

I call the finished artifact a shared-assumption map.

The useful part is not the grid itself. It is the conversation created by a crowded column.

If seven tests all require users to understand the category before signup, that belief deserves more attention than its one-line appearance in seven briefs suggests.

If every activation idea assumes the acquisition mix stays constant, the team should stop calling channel quality a background condition.

If no test could succeed when users arrive with a different job than expected, the roadmap is not exploring the problem. It is defending one account of it.

## Add one test that can disagree with the rest

The fix is not to force artificial variety into every quarter.

Some premises really are well supported. Some strategic periods should be concentrated.

The fix is to make concentration explicit and buy at least one credible way for reality to disagree.

Suppose a team believes incomplete onboarding is mainly an effort problem.

The concentrated portfolio might include fewer fields, clearer progress, saved state, and a follow-up reminder. Each could improve the experience. Each still leans toward the same explanation.

A useful counter-test would examine comprehension rather than effort.

Before changing the flow, randomly show eligible new users one of two opening experiences. The control starts setup as usual. The variant asks the user to choose the outcome they expect, then reflects that outcome back in concrete product language before setup begins.

The falsifiable hypothesis is straightforward.

If comprehension is a meaningful hidden constraint, the variant should increase completion of a downstream value event among eligible new users even if median setup time does not fall.

The primary measure should be the downstream value event, not clicks on the new choice.

The guardrails should include signup completion, setup abandonment, support contacts, and a short measure of whether users chose an outcome they could actually pursue. Results should also be read by acquisition source so a change in traffic mix does not masquerade as stronger understanding.

If the variant changes stated intent but not downstream value, the comprehension account weakens.

If it improves value completion while the friction tests do not, the roadmap has learned something more important than which screen won.

It has learned that the portfolio was concentrated around the wrong constraint.

That is what a disagreeing test is for.

## Independence should be part of experiment quality

Growth teams already spend time on whether an individual test is trustworthy.

Was assignment random.

Was exposure logged correctly.

Did the sample reach the planned size.

Did a guardrail move.

Did someone peek and stop early.

Microsoft’s guidance on [trustworthy experimentation during the experiment stage](https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-during-experiment-stage/) is a good reminder that execution details can quietly invalidate a result.

I think portfolio quality deserves the same care.

A set of well-run tests can still produce narrow learning if they all ask reality the same question.

Before committing a growth cycle, I would ask a few uncomfortable questions.

Which assumption appears in the most experiment briefs.

Which two tests look different but would fail for the same reason.

Which result would cause us to update the strategy rather than only the interface.

What competing explanation has no fair test on the roadmap.

Where are we treating repeated evidence from one premise as independent confirmation.

Those questions do not make the roadmap less coherent.

They make the learning more honest.

## A portfolio should earn more than activity

There are good reasons to place several bets on one belief.

The evidence may already be strong. The opportunity may be urgent. Several surfaces may genuinely need to change together.

Concentration is not automatically a mistake.

Unseen concentration is.

It lets a team ship all quarter, collect a stack of clean readouts, and still finish with surprisingly little new knowledge about why users join, reach value, or stay.

I would rather see four tests that expose different parts of the growth model than twelve tests that polish one assumption from twelve angles.

The first portfolio may look smaller in a planning meeting.

It is doing more work.

That is the standard I want from a growth roadmap.

Not how many tests it contains.

How many important ways it allows us to be wrong.
