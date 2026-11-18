---
title: "Do not mistake a backlog for a habit"
subtitle: "A strong first month can come from old work being cleared rather than new demand being created."
description: "A growth PM field note on separating accumulated work from recurring demand before an activation spike becomes a retention plan."
date: 2026-11-18
image: /assets/images/notebook.jpg
layout: post
---

I once watched a new workflow have an excellent first month.

People connected their accounts, imported years of material, and moved through it quickly. The usage chart had the shape every growth team wants. A steep start, several meaningful actions, and enough early return visits to make the product feel as if it had found a place in the week.

Then the work ran out.

Nothing had broken. People were not confused. The product had done the job unusually well.

The problem was our story about the job. We treated a pile of old work as evidence of a stream of new work.

That distinction now feels important to me whenever a product launches around cleanup, migration, review, organization, planning, or analysis. The first cohort may arrive carrying months of receipts, photos, leads, documents, applications, alerts, or unfinished tasks. Helping them clear that backlog can produce a beautiful activation curve.

It does not, by itself, tell us what will bring them back when the backlog is gone.

## A pile and a stream can look the same at first

Imagine a product that helps independent consultants review old client notes and turn them into follow-up tasks.

At signup, a consultant imports two years of notes. In the first week they review eighty records, create twelve tasks, and complete four follow-ups. They return on six different days. By the ordinary measures, this person looks deeply activated.

The next month, only three new client notes arrive. The consultant reviews all three in one sitting and does not return for another few weeks.

It would be easy to call this a retention failure. It might be one. The product may have failed to make new work easy to capture, or the follow-up tasks may not have been useful.

But there is another possibility. We used behavior from the initial reservoir to forecast behavior after the reservoir had been drained.

The difference is not semantic. It changes the product we should build.

If recurring demand is healthy and the product loses it, we should improve the return path. If new demand is naturally sparse, more reminders will mostly ask people to inspect an empty room. If the product is mainly valuable as an occasional cleanout, forcing it into a weekly habit may make the experience worse rather than better.

## Other fields separate what exists from what arrives

Epidemiology is careful about a related distinction.

Prevalence counts existing cases in a population, while incidence counts new cases arising during a period. The CDC's [field epidemiology guidance](https://www.cdc.gov/field-epi-manual/php/chapters/describing-epi-data.html) warns against mixing incident and prevalent cases in an analysis. A large pool today does not tell you how quickly new cases will appear tomorrow.

The analogy is imperfect, as analogies should be. A task is not an illness. The counting discipline still travels well.

An import can reveal the work already present when the product arrives. Ongoing capture reveals the work entering the system after that point. Both matter, but they answer different growth questions.

Hydrology offers another useful picture. The US Geological Survey describes the water cycle through [pools that store water and fluxes that move it](https://www.usgs.gov/water-science-school/science/water-pools-and-fluxes-data-tables). A reservoir can be large while the stream feeding it is small. Watching water leave the reservoir tells you something about the outlet. It does not tell you whether the reservoir will refill.

Growth dashboards often collapse all three quantities into activity.

We count items processed without separating old items from new ones. We count return sessions without asking whether a person returned to the original pile or to work that arrived later. We celebrate depth of use while missing that the product is consuming the very material that made depth possible.

The product can be working and the growth model can still be wrong.

## The first win can spend down future activity

There is a mild paradox here.

A faster product can make its own retention chart look worse.

Suppose one version of the consultant tool helps people review imported notes twice as quickly. Those users finish the initial backlog in a week. People on the older version take three weeks. A weekly active-user chart may favor the slower experience because unfinished old work keeps pulling people back.

That is not durable value. It is work in progress lingering in the system.

The same pattern appears in consumer products.

A photo organizer may help someone clear ten years of duplicates, then have very little to do each month. A financial tool may find all the subscriptions already on a statement, while only a few new charges need review later. A job-search product may help someone process a burst of openings during an active search, then go quiet after they accept a role.

In each case, lower frequency can be an honest consequence of completing the job. The question is whether enough new need arrives, at a useful cadence, to support the business and product experience we are planning.

That is a demand question before it is a lifecycle question.

## Keep a demand stock and flow note

Before turning early activity into a habit roadmap, I would write a short demand stock and flow note.

It should fit beside the activation brief and answer a few concrete questions.

### The starting stock

- What unfinished work can a new user bring on day one
- How far back that work can reach
- Whether the product imports it automatically or the user selects it
- How much of first-week activity can come from that starting material
- What completion looks like for the initial pile

### The incoming flow

- What creates genuinely new work after signup
- How often that work arrives without a product prompt
- Whether arrival is steady, seasonal, episodic, or tied to an outside event
- Who controls the arrival of new work
- What observable event distinguishes new work from imported work

### The drain

- How quickly the product helps a person finish each item
- Whether faster completion reduces sessions while improving the outcome
- What remains useful after an item is complete
- Whether unfinished work is being mistaken for a reason to return

### The growth decision

- The amount of incoming work needed to support the expected cadence
- The business model that fits if use is naturally occasional
- The product investment that would improve capture of legitimate new work
- The retention claim we will not make from the initial backlog

This note does not need precise forecasts on every line. It needs enough separation to stop one large number from doing several jobs.

For the consultant product, I would tag every reviewed note as imported before signup or created after signup. I would also record when the underlying client interaction occurred. A note synchronized today about a meeting from last year belongs to the starting stock, not the incoming flow.

That simple distinction makes the retention conversation much harder to bluff.

## Write the replenishment hypothesis

The hypothesis should make a claim about new demand, not merely continued use.

For the consultant example, I would write it this way.

> Among consultants who finish at least three quarters of their imported notes, at least half will receive four or more new client notes during the following four weeks, and at least two fifths of those consultants will turn one of those new notes into a completed follow-up within seven days of its arrival.

This can be wrong in useful ways.

New notes may arrive but fail to enter the product. That points toward capture and integration work. New notes may enter but produce no follow-up, which weakens the idea that note arrival creates the recurring job we imagined. The flow may exist only for consultants with a certain client volume, which may narrow the viable audience. Or new notes may be rare while the initial cleanup produces enough standalone value to support an occasional-use product.

None of those results can be repaired honestly by sending more reminders.

## Let the backlog finish before making the call

I would not begin with a large feature test.

Start by making the stock visible in the data. Mark items that existed before signup, items created after signup, and items completed by the product. Then recruit a few mature cohorts whose initial piles have had enough time to shrink.

For each cohort, plot the remaining starting stock and the arrival of new work by week. Put completed useful outcomes beside both. Do not use sessions as the main unit. A session can contain old work, new work, or no work at all.

Then compare three moments.

- While most of the starting stock remains
- Around the week the starting stock is mostly cleared
- During the following observation period when activity depends on new arrivals

The observation period should match the domain. Four weeks may be reasonable for client notes. A tax product may need a year. A hiring product may need to follow an entire search and accept that demand goes dormant afterward.

If new work arrives reliably but is not captured, run a proportionate test on capture. For example, randomly offer eligible users a simpler way to forward a newly created note into the product. The primary outcome should be new notes that lead to completed follow-ups, not use of the forwarding control.

If almost no new work arrives, stop treating the question as an onboarding experiment. Revisit the intended cadence, audience, and business model.

The decision method is deliberately asymmetric. A cheap instrumentation change can answer whether the flow exists. A costly retention program should wait until it does.

## Occasional value is still value

I do not want this argument to become another way to dismiss products that are useful infrequently.

Some of the best products should go quiet after they work. They help someone file a claim, complete a move, find a job, clean a library, or make a difficult decision. Their value is not diminished because it does not produce a daily streak.

The mistake is asking an episodic product to finance a recurring-use story it cannot support.

An occasional product can charge for the event, preserve state until the next episode, earn referrals, or serve a portfolio of infrequent needs. It can make the completed job memorable enough that people return when the need is real. Those are product and business choices, not apologies for a weak engagement chart.

The harder case is when the business truly requires regular use. Then the incoming flow has to be real. It might come from new transactions, new creative work, new team activity, or a changing external environment. The product can help capture and organize that flow. It should not invent busywork to simulate it.

## Growth needs an account of what refills

Early cohorts often arrive carrying history.

That history is useful. It gives the product material to work with and gives the team a faster chance to demonstrate value. It can also hide the absence of a recurring job.

I have learned to be careful when the strongest activation comes from clearing, importing, reviewing, or organizing what already exists. Those verbs describe valuable work. They also consume a stock.

Before I call the pattern a habit, I want to see what arrives after the old work is gone.

Not another prompt.

Not another session.

New demand that gives the product an honest reason to be useful again.
