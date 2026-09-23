---
title: "Map who can affect whom before you randomize"
subtitle: "An experiment can assign users independently while the product lets their outcomes spill across households, teams, and networks."
description: "A growth PM field note on interference, contagion, and choosing an experiment unit that matches how users affect one another."
date: 2026-09-12
image: /assets/images/notebook.jpg
layout: post
---

I think a lot of clean experiment readouts sit on top of a messy social assumption.

We randomize one user into treatment and another into control. We compare their outcomes. We act as if each result belongs only to the person who received the variation.

Then the product lets them talk, share, invite, approve, pay, or live together.

The treatment leaks.

A new household budgeting prompt shown to one partner changes how both partners categorize spending. A collaboration feature shown to one teammate changes the project that control users open tomorrow. A referral incentive changes what recipients hear even though the recipients were never assigned to treatment.

The experiment was randomized at the user level. The experience was not contained there.

## Independence is a product assumption

Standard experiment analysis usually relies on one person's outcome not being changed by another person's assignment. Researchers often discuss violations under interference. The [classic paper by Hudgens and Halloran](https://www.treatment-effects.com/Hudgens-Halloran-2008.pdf) formalizes causal effects when one person's treatment can affect others in a group.

I do not think every PM needs to reproduce the notation. I do think every experiment owner should understand the operational question underneath it.

Who can change because this user saw the treatment.

Contagion makes the issue vivid. A vaccine, message, or behavior can affect people beyond the directly treated person. Product effects spread too, although the mechanism is usually communication or shared state rather than biology. That is an analogy, not a claim that feature adoption follows an epidemic model.

The useful connection is that exposure has paths. If we do not map those paths, the control group can become partially treated and the measured difference can shrink, reverse, or move somewhere unexpected.

## Shared objects create spillovers

Consider a hypothetical family finance app testing a new weekly spending forecast.

The team randomizes individual accounts. One partner sees a forecast that says dining spend is likely to exceed the household target. They mention it over dinner. The other partner, assigned to control, spends less the next day. Their outcome changed because of treatment even though their interface did not.

Now consider a shared workspace. Treatment users get a better project template. A treated manager creates the project and five control teammates work inside the improved structure. If we analyze individual activation, the control group receives part of the benefit. If we analyze only template creation, we miss the downstream value.

The particular methods depend on the product and network. For this workspace, the practical question is whether the variation belongs to the person who creates the template or to everyone who works inside it. Randomization and analysis have to respect the connections through which treatment travels.

## Choose the unit where the experience can differ

User randomization is attractive because it creates lots of units and often balances quickly. But shared experiences make a conventional user-level comparison harder to interpret. It may answer a different question from the effect of rolling the feature out to everyone.

Possible units include a household, workspace, school, neighborhood, seller market, or connected cluster. Each choice trades statistical power and implementation simplicity against contamination risk.

If a paywall belongs to an individual subscription, user assignment may be sensible. If permissions change a shared workspace, workspace assignment is usually more coherent. If drivers and riders interact within a local market, even workspace logic is too small. Geography and time can become part of the unit.

LinkedIn's engineering team has written about [cluster experimentation](https://www.linkedin.com/blog/engineering/ab-testing-experimentation/detecting-interference-an-a-b-test-of-a-b-tests) as a way to detect and handle network interference. Cluster assignment is not magic. Connections still cross cluster boundaries, and larger units reduce the number of independent observations. It is a design choice that makes an assumption visible rather than wishing spillovers away.

## The artifact I want is an interference map

Before launch, put the affected entities and paths on one page.

| Element | Working assumption |
| --- | --- |
| Directly treated entity | Household member who sees the weekly forecast |
| Shared object | Household budget and transaction categories |
| Other affected entities | Partner, joint-account members, financial coach |
| Spillover path | Conversation, shared category edits, changed joint spending |
| Likely range | Same household during the weekly budget cycle |
| Proposed randomization unit | Household |
| Proposed analysis unit | Household for spend, individual comprehension with household-clustered uncertainty |
| Cross-unit leak | Coach serving households in both variants |
| Detection signal | Control users opening or editing treatment-created forecast objects |

Then name the assumptions in sentences.

- A forecast can affect every member of the same household.
- Effects outside the household are expected to be small except through a shared coach.
- Household identifiers are stable enough for assignment before exposure.
- A coach who serves both groups may carry language or practice across the boundary.

My hypothesis might be the following.

> If forecasts improve planning, households assigned together will predict end-of-week spend more accurately and better forecast comprehension than control households, without a rise in category corrections.

The correction measure matters because a shared forecast might create activity by creating confusion. The household assignment matters because individual assignment would mix the experience inside the exact unit whose behavior we want to understand.

## Mapping interference changes the conversation

The map forces product, data, and engineering to discuss how the feature actually moves.

Can a treated artifact be forwarded.

Does one administrator configure the experience for everyone.

Will a seller respond to treatment demand in a way that changes control demand.

Can people hold multiple accounts across variants.

Does the effect spread for one session, one week, or indefinitely.

Those questions may lead to cluster randomization, a switchback design across time, or a decision not to run a conventional randomized test. Switchbacks need a plan for effects that persist across time windows. Exposure-based analysis needs additional assumptions because exposure itself may be changed by treatment. A data scientist should help define the effect being estimated and the uncertainty calculation before launch.

An experiment does not become rigorous because the assignment service produced equal buckets. It becomes more credible when the unit of assignment matches the unit through which the product changes behavior.

Before trusting a user-level result, I would draw who can affect whom. The lines between users are part of the treatment whether the experiment table includes them or not.
