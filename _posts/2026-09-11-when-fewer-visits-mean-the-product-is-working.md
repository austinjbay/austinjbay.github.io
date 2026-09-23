---
title: "When fewer visits mean the product is working"
subtitle: "Some products earn trust by staying quiet after the job is done, which means absence needs better evidence than a retention chart can offer."
description: "A growth PM field note on calm technology, outcome-based observability, and telling successful absence from churn."
date: 2026-09-11
image: /assets/images/desk.jpg
layout: post
---

I think product teams sometimes confuse being visited with being valuable.

That confusion is understandable. Sessions are visible. Daily active users fit neatly on a dashboard. A person who does not return looks like a person we lost.

But some products are supposed to make themselves less necessary.

A backup product runs quietly. A bill-pay service handles the scheduled payment. A travel alert should remain silent when the train is on time. A security tool can protect an account without asking its owner to admire the dashboard every morning.

In those products, fewer visits may be the result we promised.

The hard part is telling successful absence from abandonment.

## Quiet can be a feature

Mark Weiser and John Seely Brown explored how technology can become an unremarkable part of everyday life in [The Coming Age of Calm Technology](https://calmtech.com/papers/coming-age-calm-technology). Their argument was not that interfaces should vanish regardless of consequence. It was that good technology can move between the center and periphery of attention.

That feels especially relevant to growth work. We often treat attention as the product's fuel when attention may be the cost the product was hired to remove.

Imagine a hypothetical subscription that checks household utility plans and alerts a customer only when switching would save enough to justify the hassle. A user visits in January, connects the account, and hears nothing for four months. That might mean the connection broke and the user forgot the service. It might also mean the product checked every week and correctly found no worthwhile action.

The session chart cannot distinguish those stories.

## Observe the outcome, not only the interface

Site reliability engineering offers a useful analogy. Google's chapter on [monitoring distributed systems](https://sre.google/sre-book/monitoring-distributed-systems/) separates symptoms that matter to users from internal causes and recommends monitoring signals such as latency, traffic, errors, and saturation. A healthy system is not defined by engineers opening the console frequently. It is defined by the service continuing to produce the intended result.

A growth team can adopt the same posture without pretending product engagement is a server.

For the utility example, I would want evidence that the account connection remains valid, checks still complete, the rules are still eligible to detect savings, and the customer receives a clear periodic receipt of that work. Those are closer to outcome observability than raw visits.

The analogy has limits. Human trust is not server uptime. A completed background job does not prove the user still values the service. It simply gives us a more honest starting point than assuming silence is failure.

This is also where notifications need restraint. I would reserve interruption for a change the user can understand and act on. If the system has no meaningful change to report, manufacturing a reason to return can turn calm value into upkeep.

## Healthy absence has positive evidence

I would not relabel every inactive user as quietly successful. That would be a convenient way to hide churn.

Healthy absence should leave evidence.

- The delegated job continues to run successfully.
- The underlying data or permission remains current.
- The promised outcome is delivered when its condition occurs.
- The user can inspect a legible record without doing maintenance.
- Periodic confirmation, when appropriate, is understood rather than ignored.
- Support contacts and cancellations do not reveal surprise about what the product was doing.

There should also be evidence that falsifies the story.

- A connection expires and is not repaired.
- Background checks stop or repeatedly fail.
- A qualifying event occurs and no action or alert follows.
- Users return mainly to verify whether the product is alive.
- Cancellation research says people forgot the service, distrusted it, or no longer needed the outcome.

The important move is specifying both lists before looking at the curve. Otherwise every quiet cohort can be explained after the fact.

## The artifact I want is a healthy-absence brief

Pick one job that should happen without frequent interface use.

**Promised outcome**

The service checks eligible utility plans weekly and alerts the household when estimated annual savings exceed its chosen threshold.

**Evidence the absence is healthy**

- Ninety-eight percent of scheduled checks complete in the hypothetical target period.
- Account permissions remain valid.
- Households with no qualifying change receive a quarterly work receipt.
- Households with a qualifying change receive the alert within the promised window.
- A small research sample can accurately explain what the service is doing for them.

**Evidence that would falsify it**

- Silent check failures rise.
- Users repeatedly open the app just to confirm it still works.
- Qualifying changes go unreported.
- Cancellation responses show forgotten value rather than completed value.
- The quarterly receipt creates confusion or reveals stale inputs.

**Decision**

Do not optimize return visits unless outcome evidence weakens. Repair observability, permissions, or communication first.

My hypothesis would be narrow.

> If we show a trustworthy quarterly record of completed checks without inventing a task, users will better understand the background value while median visits remain flat or fall.

That is not a hypothesis about sending more reminders. It is a test of whether evidence can carry trust without demanding attention.

## Absence needs a different dashboard

Engagement remains useful for products where value is created through active practice, creation, or conversation. I am not arguing that visits never matter.

I am arguing that the metric should match the job.

If a product promises to handle something, protect something, or watch something, the growth team should be able to observe whether that outcome continues while the user is away. It should also name the conditions that would prove the quiet is unhealthy.

That is a higher standard than calling inactivity success. It requires the product to produce evidence beyond its own screen.

Sometimes the most respectful retention experience is not a streak, a badge, or a reason to come back tomorrow.

It is a job done reliably enough that the user can go do something else.
