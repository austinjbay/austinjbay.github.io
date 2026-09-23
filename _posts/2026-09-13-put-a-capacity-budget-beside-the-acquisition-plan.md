---
title: "Put a capacity budget beside the acquisition plan"
subtitle: "Demand can grow faster than the product's ability to seat, match, verify, or activate the people who arrive."
description: "A growth PM field note on finite capacity, admission control, and knowing when acquisition is sending more work than the product can serve."
date: 2026-09-13
image: /assets/images/desk.jpg
layout: post
---

I think growth teams are taught to see demand as an uncomplicated good.

More qualified traffic.

More reservations.

More sellers applying.

More accounts ready to onboard.

Then the product reaches a point where each new arrival makes the next arrival's experience worse.

The restaurant has eighty seats, a kitchen that can plate forty covers an hour, and a host stand promising tables as if only the dining room matters. The marketplace has plenty of buyer interest but not enough verified providers to serve it this afternoon. The SaaS funnel can close ten teams a week while implementation can activate six.

At that point acquisition is not only filling a funnel. It is feeding a finite system.

## A reservation is a capacity promise

Restaurants make the idea concrete. A table at seven is not simply a lead. It is a claim on a table, kitchen, server, and slice of time.

Accept too few reservations and the room sits empty. Accept too many and every promise degrades together. Parties wait. Courses bunch up. Staff improvise. A full reservation book can coexist with a bad service.

Digital products hide this constraint better. The signup page can accept another account almost without limit. The scarce resource appears later as human review, inventory, implementation support, compute, or the attention of existing participants.

Queueing theory gives the shape of the problem. Little's Law relates the average number of items in a stable system to arrival rate and time in the system. John Little revisits the result and its conditions in [Little's Law as Viewed on Its 50th Anniversary](https://pubsonline.informs.org/doi/10.1287/opre.1110.0940). The formula does not tell a growth team which experience to build. In a stable system, it helps relate throughput, time in the system, and work in progress. If arrivals persistently exceed completions, the backlog grows and the stable-system assumption no longer describes that growing queue.

## Reliability teams already control admission

Site reliability engineering treats unlimited incoming work as a reliability risk. Google's guidance on [handling overload](https://sre.google/sre-book/handling-overload/) discusses protecting a service when demand exceeds the resources available to answer it. Admission control can reject or defer work so the system does not collapse for everyone.

A marketplace or assisted onboarding motion is not a server. People interpret delay, fairness, and rejection in ways machines do not. Still, the analogy is useful. Accepting every arrival is not generous when the product cannot provide the promised service.

Imagine a hypothetical expert marketplace with 120 qualified consultation slots next week. Marketing expects to acquire 180 buyers, historical booking intent is 50 percent, and existing repeat customers are likely to request 55 slots.

Expected new demand is 90 slots. Total expected demand is 145. The product is already 25 slots over capacity before accounting for time-zone fit, specialty, cancellations, or uneven days.

A blended weekly total can make the gap look manageable. Tuesday evening may be overwhelmed while Friday morning remains empty. Capacity needs the same segmentation as the promise.

## Changing demand is not adding supply

This distinction matters because the remedies look superficially similar in a dashboard.

Changing demand means narrowing targeting, pacing campaigns, moving appointments to quieter windows, pricing peak times differently, or placing arrivals into an honest queue. It changes who arrives or when.

Adding supply means recruiting providers, improving provider utilization, reducing service time, automating a review, or increasing infrastructure. It changes what the system can fulfill.

A discount for Friday morning shifts demand. It does not create another expert. A faster verification flow may add usable provider capacity. It does not necessarily reduce buyer demand. A waitlist protects the experience. It does not solve the underlying shortage.

A restaurant can choose to release fewer tables online because its kitchen is short-staffed. That ordinary operating decision is worth carrying into growth planning. Demand shown on a screen is not equivalent to serviceable capacity behind it.

## The artifact I want is a capacity budget

Build it for the same segment and time window users encounter.

| Capacity line | Hypothetical weekly amount |
| --- | --- |
| Qualified provider slots | 120 |
| Reserve for existing customers | 55 |
| Cancellation recovery buffer | 10 |
| Safely available to new demand | 55 |
| Expected new booking demand | 90 |
| Budget gap | 35 |

Then break the budget down by specialty, geography, and time window. Add the service-level promise, the leading saturation signal, and the owner who can change demand or supply.

My hypothesis could read this way.

> If we pace acquisition by specialty and appointment window when forecast demand exceeds safe capacity, a greater share of new buyers will see at least three viable slots and complete a consultation, even if total signups fall.

I would watch completed consultations per eligible arrival, total consultations, viable choices shown, time to service, provider utilization, and the share of visitors deferred. Deferred people must stay visible in the accounting. Otherwise we can manufacture a better completion rate by admitting fewer people and ignoring everyone turned away. Since buyers compete for shared slots, the experiment also needs an assignment plan that accounts for effects across buyers. A signup decline would not automatically invalidate the test. The goal is served demand, not an arrival record.

## Growth has to account for the room

Capacity is not an excuse to stop growing. It is a reason to define growth as fulfilled value rather than accumulated demand.

Sometimes the right move is more supply. Sometimes it is a narrower campaign. Sometimes it is a clear reservation window rather than a vague promise. Often it is a paired plan that creates supply before releasing the next wave of demand.

What I would not do is celebrate acquisition while the queue quietly buys the metric with longer waits and worse matches.

The funnel does not end when someone asks to be served. A capacity budget makes the rest of the promise visible.
