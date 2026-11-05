---
title: "Measure whether demand had a chance to appear"
subtitle: "Why growth teams should separate a missing need from a need the product never made observable."
description: "A growth PM field note on imperfect detection, hidden product demand, and a practical demand visibility audit for making better roadmap and experiment decisions."
date: 2026-09-23
image: /assets/images/notebook.jpg
layout: post
---

I have heard some version of the same sentence in more roadmap conversations than I can count.

Nobody is using it.

Sometimes that is a clean signal. A feature is easy to find, relevant to the people we are studying, and still ignored after they understand what it does.

Sometimes the sentence is doing much more work than the evidence can carry.

Nobody searched with the word we expected.

Nobody opened the menu where we put the action.

Nobody requested a capability that they did not know software could provide.

Nobody clicked the lifecycle prompt that arrived after the job had already passed.

In those cases we have not measured demand. We have measured detected demand under one particular observation system.

That distinction sounds academic until a team removes a useful capability, declares a segment uninterested, or builds the wrong acquisition page because silence looked like a verdict.

## An empty count can hide two different realities

Ecologists deal with a version of this problem when they survey a site for a species.

An animal may be present and still go unseen. Weather, season, observer effort, habitat, and ordinary chance all affect whether presence becomes an observation. The US Geological Survey guide to [occupancy models for studying wildlife](https://pubs.usgs.gov/fs/2005/3096/fs20053096.pdf) explains how repeated surveys are used to estimate both occurrence and the probability of detection.

I like this idea for product work because it forces a distinction our dashboards usually flatten.

The user does not have the need.

The user has the need, but our product did not give it a fair chance to become visible.

Those conditions can produce the same zero in an event table. They should produce very different decisions.

Imagine a reporting product with a useful scheduled export buried under an overflow menu. Few people use it. The easy conclusion is that customers do not care about scheduled delivery.

But perhaps account owners keep downloading the same report on Friday and forwarding it by hand. Perhaps users search for email report while the interface calls the feature distribution. Perhaps the menu is only visible after a report is published even though people look for the action while drafting.

The product has built a weak detector and then blamed the market for a weak signal.

## Public health separates the system from the condition

Public health surveillance offers another useful comparison.

A surveillance system does not simply count cases. It has to consider whether the process finds the cases it is meant to find, whether the definition captures the right events, and whether reporting arrives in time to support action. The Centers for Disease Control and Prevention guidance on [evaluating public health surveillance systems](https://www.cdc.gov/mmwr/preview/mmwrhtml/rr5013a1.htm) treats sensitivity, data quality, representativeness, and timeliness as properties of the observation system.

Product analytics needs more of that humility.

An event count is partly a statement about behavior and partly a statement about instrumentation, language, placement, eligibility, timing, and awareness.

That does not make the count useless. It changes what the count is allowed to prove.

If a capability is visible to only workspace owners, low usage may tell us about owners rather than the account.

If search recognizes the product term but not the user's term, a low result count may tell us about vocabulary rather than intent.

If an onboarding choice appears before the user has encountered the problem it solves, a low selection rate may tell us about timing rather than preference.

If a prompt appears once and cannot be recovered, dismissal may tell us that Tuesday was busy.

Mid-career product judgment often means resisting the tidiest interpretation in the room. Silence is tidy. The system that produced it usually is not.

## Discoverability is part of the measurement instrument

Growth teams tend to discuss discoverability as a design concern after deciding a feature matters.

I think it also belongs upstream in research and measurement.

The Nielsen Norman Group description of [information scent](https://www.nngroup.com/articles/information-scent/) is useful here. People decide where to go based on cues that suggest a path will lead toward their goal. When our labels and placements offer weak cues, the resulting lack of interaction is not a neutral read on interest.

Search data has the same trap.

Google's explanation of the [Search Console performance report](https://support.google.com/webmasters/answer/7576553) distinguishes impressions, clicks, position, and the queries associated with visibility in search. A page cannot earn a click in a result the searcher never saw. Product surfaces deserve the same basic accounting.

Before treating nonuse as lack of demand, I want to know whether the relevant person had a credible opportunity to notice, understand, and try the capability while the need was alive.

Not theoretical access.

A credible opportunity.

## The artifact I use is a demand visibility audit

I would use this before removing a low-use feature, dismissing a repeated customer problem, or sizing a bet from search and event data alone.

Pick one user job and one candidate solution. Then write down the following.

- The job or tension we believe may exist
- The eligible people who could plausibly have it
- The moment when the need becomes active
- The observable behaviors that could reveal the need without our feature
- The words users employ when describing or searching for it
- The surfaces where the product currently offers a route
- The share of eligible users who actually encounter those surfaces
- The cue that explains what the route will do
- The effort and risk required to try it
- The event we currently treat as detected demand
- The reasons genuine demand could remain invisible
- The evidence that would convince us demand is truly weak
- The owner and review date

I also add a simple detection ladder.

- Exposed means the relevant surface was actually rendered
- Noticed means the user showed evidence of attending to the cue
- Understood means the user could reasonably predict the outcome
- Tried means the user began the action with the needed permissions and inputs
- Realized means the action produced the intended job outcome
- Repeated means the outcome was useful enough to seek again

The ladder keeps the team from treating one missing click as a complete demand study.

It also reveals where the product is losing the signal.

If exposure is rare, fix or test placement.

If people notice but do not understand, work on language and examples.

If they understand but do not try, inspect cost, trust, permissions, and timing.

If they try but do not realize the outcome, the problem is not hidden demand anymore. The product has failed the job.

That last distinction matters. A visibility audit should not become a clever defense for a feature people simply do not value.

## Write a hypothesis that can separate need from detection

Here is the kind of statement I would want before changing the reporting example.

> We believe workspace owners who manually download the same report in two consecutive weeks have latent demand for scheduled delivery. Showing those owners a plain language scheduled email option immediately after the second download will increase completed schedules within fourteen days without reducing successful report exports, because the capability will appear while the recurring job is visible.

This is more useful than saying better discoverability will increase usage.

It names the eligible population, the behavioral clue, the observation moment, the expected outcome, the time window, the guardrail, and the proposed reason.

It can also lose honestly.

If owners see the option, understand it, and keep doing the work manually, the demand case is weaker. If they start schedules but turn them off after one delivery, the initial click was curiosity rather than durable value. If exports fall because the prompt interrupts urgent work, the detector created harm in order to create a signal.

Those are decisions, not excuses.

## Run a detection test without manufacturing demand

There is an ethical and analytical line here.

Making a relevant capability legible is not the same as pressuring people into it. A prompt can increase usage by clarifying a route. It can also manufacture compliance through repetition, obstruction, or a default that is hard to reverse.

I would keep the test narrow.

Randomly assign only users who show the predeclared behavioral clue. Give the treatment group one contextual, dismissible route in the moment the job is active. Keep the underlying capability, pricing, and follow-up treatment the same. Do not auto-enroll anyone. Do not count the prompt click as success.

Measure exposure and eligibility first so the denominator is real. Then compare completed schedules, successful first deliveries, continued schedules after the normal repeat interval, manual exports, errors, and support contacts. Review a small sample of sessions or interviews to learn whether the cue revealed an existing job or introduced an idea with no durable use.

Predefine the decision.

Ship a clearer route when realized and repeated value rises without harming the core reporting job.

Keep learning when people engage but fail to realize the outcome.

Retire or deprioritize the idea when eligible users receive a fair, understandable opportunity and durable use remains weak.

That is a more responsible experiment than showing a louder banner to everyone and calling the resulting clicks proof of demand.

## Repeated observation beats one loud observation

The ecology analogy has another useful lesson.

One visit is fragile. Repeated observations under different conditions help separate absence from missed detection.

Product teams can do the same without pestering users.

Look across different traces of the same job.

Searches that use adjacent language.

Manual work that approximates the feature.

Support conversations that describe the outcome without naming the solution.

Repeated navigation to a nearby surface.

Files exported and then reimported somewhere else.

These signals should not be added into a fake precision score. They are evidence for deciding whether a cleaner detection test is worth running.

The pattern matters more than any single proxy.

I have become wary of both extremes in growth work. One team treats every stray request as a mandate. Another treats every missing event as disinterest. Both positions avoid the harder job of understanding how demand becomes observable.

## Sometimes zero really does mean no

The point is not to rescue every neglected feature.

Some capabilities are visible, clear, timely, safe to try, and still not useful enough. Mature product work needs to accept that result.

The visibility audit earns that confidence.

When the right people encounter a clear route at the relevant moment, understand the outcome, face a proportionate cost, and still do not proceed, the team can stop romanticizing latent demand.

Until then, be precise about what the dashboard says.

It may say nobody used the feature.

It may not yet say nobody needed it.
