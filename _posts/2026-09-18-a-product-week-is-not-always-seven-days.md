---
title: "A product week is not always seven days"
subtitle: "Repeat value is easier to see when cohorts begin with the recurring job instead of an arbitrary signup date."
description: "A growth PM field note on seasonality, event time, and building observation windows around the cadence of the job."
date: 2026-09-18
image: /assets/images/notebook.jpg
layout: post
---

I think the calendar sneaks more product judgment into our dashboards than we admit.

We group activity into days, weeks, and months because the database makes those windows easy. Then we start treating them as if users experience the product in the same units.

They often do not.

Rent comes due around a monthly boundary. Travel planning swells before departure and goes quiet after the return. Garden planning follows weather and season more than a clean set of thirty-day intervals. A parent may use a school coordination product heavily at the start and end of a term.

A product week is not always seven days. Sometimes it is the interval between naturally recurring jobs.

## Calendar time can scramble the story

Imagine a hypothetical rent-splitting product.

Jordan signs up on August 30, adds roommates, and settles September rent on September 1. Casey signs up on September 2 after already paying rent elsewhere. In a seven-day activation report, Jordan looks active and Casey looks weak. In a thirty-day retention report, Jordan may appear to churn because the next rent cycle falls just outside the window while Casey returns near the end.

Their product fit may be identical. Their signup dates placed them at different distances from the job.

This is calendar bias. The reporting boundary determines which naturally timed opportunity each user gets to demonstrate value.

Seasonal adjustment exists in economic statistics because recurring calendar and seasonal patterns can obscure underlying movement. The [US Census Bureau overview of seasonal adjustment](https://www.census.gov/data/software/x13as/seasonal-adjustment-questions-answers.html) is about time series, not product retention. The analogy still helps. Before interpreting a change, separate the rhythm created by the calendar from the change you actually care about.

## Measure in event time

Event time aligns observation around a meaningful occurrence rather than a shared wall-clock date.

For rent splitting, day zero might be the first rent due date after the household is ready, not the signup date. For travel, it might be departure. For tax software, it might be the filing deadline or the arrival of required documents. For seasonal planning, it might be the first freeze, enrollment window, or annual renewal.

Google Analytics documents [cohort exploration](https://support.google.com/analytics/answer/9670133) around groups that share a common attribute. Signup week is one possible common attribute. It is not automatically the useful one. For our own analysis, we can align cohorts by the first eligible job or distance to a known event. That may require custom event modeling or warehouse analysis rather than a built-in report.

That shift changes both denominator and window.

Casey should not be considered to have missed a repeat-rent opportunity before another rent cycle occurred. Jordan should not be called retained merely for opening a reminder three days after signup. Both need a chance to perform the recurring job.

## The observation window should include opportunity

I would ask three questions before choosing a repeat-value window.

- When does the user become eligible to do the job again.
- How much variation exists around that event.
- How long after the event can successful completion reasonably occur.

For a monthly bill, the window might run from five days before the due date to three days after. For travel planning, a research phase might start eight weeks before departure while the execution phase begins two days before. Those are different product moments even when the same person uses both.

The [National Institute of Standards and Technology handbook on seasonality](https://itl.nist.gov/div898/handbook/pmc/section4/pmc443.htm) describes seasonality as a pattern repeated at fixed periods. Product teams should borrow the diagnostic habit without pretending every behavior is regular. First look for recurring opportunity. Then test whether the cadence is stable enough to anchor measurement.

## The artifact I want is a cadence calendar

Map the job before writing the query.

| Job moment | User becomes eligible | Observation window | Success evidence | Calendar risk |
| --- | --- | --- | --- | --- |
| Set up household | Once roommates agree | Before next rent window | All shares confirmed | Signup may follow payment |
| Prepare rent | Five days before due date | Five days before through due date | Amounts reviewed | Weekends and holidays shift timing |
| Settle rent | Due date | Due date through three days after | Transfers resolved | Different lease dates |
| Repeat value | Next due date | Same relative window next cycle | Second settlement with less correction | Thirty-day window may end early |

Add segments for monthly and fortnightly schedules rather than forcing them together. Mark holidays, partial months, trips, and other events that remove or shift the opportunity.

My hypothesis might read this way.

> If the product shows each roommate a confirmed share during the five days before their actual rent date, more eligible households will complete a second settlement with fewer corrections than households receiving a generic seven-day reminder.

The unit of analysis is the eligible household-cycle. The comparison should not label households whose next rent job has not arrived as failures. Report them as not yet observable, and show their count. Define eligibility from information available before treatment. If the feature changes who becomes ready, excluding those households after assignment would bias the comparison. Keep the full assigned-household outcome beside the cycle-aligned diagnostic, and account for repeated cycles from the same household.

## Alignment changes product decisions

Once cohorts are aligned to the job, weak spots become more legible.

Perhaps first-cycle setup is strong but holiday-shifted payments fail. Perhaps travelers plan well before departure but cannot retrieve documents during the trip. Perhaps seasonal sellers return reliably each spring even though a monthly retention chart labels them dormant for most of the year.

This is different from arguing that absence is healthy. The central question here is whether every cohort received a comparable chance to repeat the job. A user may be entirely active in intent and still have no relevant event inside our reporting week.

I still use seven-day and thirty-day views. They are convenient operational lenses. I just do not want convenience to harden into a theory of user behavior.

Before calling a cohort retained or lost, put its members on the calendar of the job they hired the product to do. Repeat value should be measured when repetition becomes possible.
