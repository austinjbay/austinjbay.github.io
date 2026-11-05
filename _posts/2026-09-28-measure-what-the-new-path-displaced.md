---
title: "Measure what the new path displaced"
subtitle: "A new growth surface can look productive while mostly moving behavior that would have happened somewhere else."
description: "A growth PM field note on substitution, incrementality, and tracing where a new path gets its apparent wins."
date: 2026-09-28
image: /assets/images/notebook.jpg
layout: post
---

I think growth teams are naturally drawn to the new path.

We add a home-screen shortcut, an onboarding checklist, a lifecycle email, or a landing page for a promising search term. People use it. The path reports conversions. The launch deck gets a satisfying upward line.

Then an older path gets quieter.

That detail often lands as cleanup. Maybe the navigation needs work. Maybe the email stole attention from an in-product prompt. Maybe the new SEO page receives visits that used to arrive through another page.

Sometimes nothing is wrong. A clearer path can replace a worse one and leave users better off.

But replacement is not the same as growth.

Before I call a new surface successful, I want to know what it displaced.

## Every path gets its users from somewhere

Imagine a product that helps small teams schedule field work.

The team adds a prominent button that creates tomorrow's schedule from the dashboard. Usage is immediate. Schedule creation through the button rises from zero to 800 actions a week. The button looks like an activation win.

At the same time, creation from the calendar falls by 500 actions. Another 150 users stop duplicating last week's schedule. Total completed schedules rise by 60, while abandoned drafts and support questions rise too.

The feature did not create 800 new acts of useful work. It rerouted a large amount of existing intent, retired one workaround, created some extra attempts, and perhaps produced 60 additional outcomes.

That is still potentially worthwhile. The new route may be faster, easier to find, or more legible to a first-time user. The mistake is using traffic through the new door as evidence that the building became busier.

This is the difference between attribution and incrementality.

Attribution tells us which surface touched an outcome. Incrementality asks whether the outcome happened because that surface existed. The UK government's [Green Book](https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2026) asks appraisers to distinguish additional outcomes from what would have happened anyway and to account for displacement and substitution. Product features are not regional economic programs, but the accounting lesson travels well. A visible beneficiary does not prove a net new benefit.

## A supermarket and a search engine know this problem

Retailers have long had to ask whether a new product grew the category or merely took sales from an item already on the shelf.

The distinction matters because the local chart can be completely honest while the portfolio conclusion is wrong. A new sparkling-water flavor can hit its sales target and still leave total sparkling-water sales flat. The launch created choice, and possibly a better choice, without creating demand.

Product navigation works the same way. A new shortcut competes with menus, search, bookmarks, habits, and memory. A lifecycle message competes with the user's intention to return on their own. A template competes with a blank canvas and with templates that already exist.

SEO has an especially clean version of the problem. Two pages can compete to represent the same intent. Google's documentation on [canonical URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) explains that duplicate or very similar pages can be consolidated around a representative URL. Publishing another page may move impressions and links between our own pages rather than expand the set of useful queries we serve.

The lesson is not to avoid new paths. It is to give them a source account.

## Build a displacement map

The artifact I want is small enough to fit beside an experiment brief.

| New path | Likely source | Behavior that may move | User benefit if it moves | Net outcome to watch |
| --- | --- | --- | --- | --- |
| Dashboard schedule button | Calendar creation | Existing schedules | Less navigation | Completed schedules per eligible team |
| Setup reminder email | Organic return | Return sessions | Better timing | First useful schedule per signup |
| New SEO guide | Existing comparison page | Search impressions and visits | Better intent match | Qualified new visitors across both pages |
| Starter template | Blank project | Project starts | Less assembly work | Projects that reach a real handoff |

These are prompts, not claims about a particular product.

For the proposed path, I would write down five things.

- The existing routes that serve the same intent
- The behavior each route is likely to surrender
- The outcome that should grow if the change is truly additive
- The user cost that might shrink even when the outcome stays flat
- The old surface we would retire if substitution is the actual goal

The fourth line matters. Incrementality is not the only legitimate reason to ship.

If the dashboard button saves time, reduces errors, or makes scheduling available to people who could not find the calendar flow, a flat schedule count may hide a real product improvement. That benefit needs its own evidence. Measure time to a valid schedule, correction rate, confidence, or successful use among previously stuck teams.

Do not force every replacement into a growth story. A better route can simply be a better route.

## Write a hypothesis about the total

Here is the falsifiable statement I would use for the scheduling example.

> We believe showing the dashboard shortcut to eligible teams will increase the share that publishes a valid schedule within seven days, not merely move schedule creation away from the calendar, while leaving correction requests no higher.

The statement refuses to count button clicks as the win. It names the population, the useful outcome, the observation window, the likely source of substitution, and a quality boundary.

It can be wrong in several informative ways.

The shortcut may only reroute experienced schedulers. It may produce more schedules but also more corrections because the compact flow hides important context. It may help new teams while slowing established ones. It may save enough time to justify itself without changing publication at all.

Each result leads to a different product decision.

## Test the system, not the surface

Randomize eligible users or teams into the old experience and the experience with the new path. Keep both groups observable across every route that can complete the job.

The primary measure should sit downstream of the route. For scheduling, that might be teams with a published and subsequently used schedule per eligible team. For lifecycle, it might be a completed job rather than an email click. For SEO, it might be qualified organic entrances across the relevant page cluster rather than visits to the new URL.

Then inspect the route mix.

If use of the new path rises by 800 and use of old paths falls by roughly the same amount while the downstream outcome stays flat, the test found substitution. If the outcome rises and the old paths stay stable, it found a more additive effect. Most results will sit between those poles.

I would also separate people who had used an old route before from those who had not. A shortcut that mainly attracts experienced users is doing different work from one that lets previously inactive users complete the job. That split should be chosen before the results arrive, not discovered after the overall metric disappoints.

For a lifecycle test, holdout is especially important. Click attribution will give the message credit for people who would have returned anyway. A control group gives their ordinary behavior somewhere to remain visible.

For an SEO change, I would watch query-level impressions, clicks, and useful downstream actions across the whole intent cluster. I would also inspect whether the new page answers a distinct question. If it does not, improving or consolidating the existing page may be better than making the site compete with itself.

Run the test long enough for the displaced behavior to appear. People do not always abandon an old habit on first exposure. Early novelty can make the new route look additive before routines settle.

## Replacement needs an honest decision

Suppose the new route mostly substitutes for the old one and is clearly better.

Keep it, then finish the job.

Retire the redundant prompt. Simplify the calendar entry point. Consolidate the overlapping article. Move the maintenance and measurement burden toward the path users now prefer.

Running both forever is not neutral. Parallel routes create more copy to reconcile, more analytics definitions to maintain, more edge cases to test, and more choices for a person who only wanted to finish the work.

Suppose the new route substitutes and is not meaningfully better.

That is a reason to remove it, even if its own dashboard looks healthy.

And suppose it reaches people the old route never served.

That is the strongest growth case. The team has not merely reassigned credit. It has expanded who can get to value or increased the amount of useful value produced.

Good growth judgment can hold all three possibilities without embarrassment.

A feature may create net new behavior. It may replace an old behavior with a better one. Or it may move activity around while adding little besides another surface to own.

The new-path chart cannot tell those stories apart.

Measure the total. Trace the source. Then decide whether you created growth, improved the route, or simply changed where the same work gets counted.
