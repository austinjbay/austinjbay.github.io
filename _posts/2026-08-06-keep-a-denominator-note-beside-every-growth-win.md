---
title: "Keep a denominator note beside every growth win"
subtitle: "Why a lift means less when you cannot explain who was eligible, who disappeared, and who never had a fair shot to count."
description: "A growth PM field note on denominator discipline, survivorship bias, and the small artifact that keeps experiment readouts more honest."
date: 2026-08-06
image: /assets/images/notebook.jpg
layout: post
---

I think a lot of growth teams are better at reporting movement than describing the population that moved.

The signup rate improved.

The onboarding completion rate ticked upward.

The win back sequence drove more returns.

The SEO landing page converted better.

Sometimes those statements are true and still incomplete in the most dangerous way.

They tell you the numerator got better.

They do not tell you whether the denominator stayed honest.

Who was actually eligible to count.

Who saw the experience.

Who hit an instrumentation hole.

Who quietly dropped out before they could ever become part of the success story.

I think this matters more than many teams admit because growth work lives in shifting populations.

Traffic quality changes.

Acquisition mix changes.

Returning users and first time users blur together.

Logged in users get a smoother path than anonymous ones.

One browser gets the polished flow while another hits a bug you do not notice until later.

All of that can make a healthy looking lift sound more trustworthy than it is.

## Public health is stricter about denominators than most product dashboards

One reason I keep borrowing from epidemiology is that it is ruthless about defining who is actually at risk.

The CDC lesson on [measures of risk](https://archive.cdc.gov/www_cdc_gov/csels/dsepd/ss1978/lesson3/section2.html) makes a simple point that travels well into product work. The denominator should be limited to the population at risk.

That sounds obvious when you are studying disease.

It should sound just as obvious when you are studying product behavior.

If you are measuring onboarding completion, the denominator is not everyone who touched the homepage.

If you are measuring an upgrade prompt, the denominator is not every account in the database.

If you are measuring activation, the denominator is not every person who technically created a login but never reached the conditions where activation was even available.

A lot of growth confusion starts when teams use a denominator that is convenient instead of one that is defensible.

The number still looks crisp.

The conclusion gets weaker.

## The missing users often carry the real lesson

I think about Abraham Wald a lot in growth work.

Microsoft Research has a good writeup on [sample ratio mismatch in A/B testing](https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/) that retells the old aircraft story. The military first looked at planes that returned from combat and wanted to reinforce the spots with the most bullet holes. Wald realized the opposite. The missing planes were the real clue.

Growth teams make a gentler version of that mistake all the time.

We analyze the users who completed setup.

We interview the people who replied.

We optimize the surfaces that loaded correctly.

We celebrate the accounts that made it into the analysis table.

Meanwhile the users who bounced during a blank state, got filtered out by a join, never received the email, or hit the wrong eligibility logic quietly vanish from the story.

That is why I get nervous when a readout moves too quickly from lift to lesson.

A lot of apparent learning is really selective visibility.

## The denominator drifts faster than the chart implies

This shows up in ordinary product work more often than people think.

An onboarding completion rate improves because SSO users are now a bigger share of the cohort and they were always more likely to finish.

A trial conversion metric looks better because low intent search traffic fell off for unrelated reasons.

A reactivation campaign appears stronger because the send logic quietly excluded a set of dormant accounts with old deliverability problems.

A prompt looks more effective on mobile because one broken rendering path on desktop stopped the least patient users from ever seeing it long enough to count.

An experiment wins because only the users with the highest intent ever reached the treatment.

Each of those examples can produce a chart that looks clean.

Each can also produce the wrong product decision.

That is why I think denominator drift is one of the most underloved sources of bad growth judgment.

It rarely arrives as a dramatic outage.

It arrives as a plausible story with just enough truth to ship.

## This is not only an analytics problem

It is tempting to hand this entirely to data science or analytics.

I do not think that is enough.

The craft question is broader.

What journey are we actually claiming to understand.

What conditions make a user countable.

What system behavior can exclude someone before the metric ever starts.

What mix shifts would make the result less portable than the slide suggests.

The [Experiment Guide](https://experimentguide.com/) material on trustworthy online controlled experiments is useful here because it keeps returning to the same discipline. A result is only as good as the trustworthiness of the experiment and the decision rule around it.

That trustworthiness is not abstract.

It lives in boring but expensive details.

Eligibility.

Assignment.

Logging.

Segmentation.

Guardrails.

The people who never made it into the room.

## The artifact I like is a denominator note

This is the small document I want beside almost every growth readout, especially for onboarding, lifecycle, SEO landing pages, and early retention work.

It is not a giant spec.

It is one page if the team is disciplined.

Usually less.

## Denominator note

- What exact user population was eligible to count
- What event or state made someone enter that population
- What common paths, bugs, or delays could keep a user out
- What changed in channel mix, device mix, geography, or account type during the period
- What users were intentionally excluded and why
- What users may have been unintentionally excluded by logging, joins, or delivery failures
- What segment looked strongest and what segment looked weakest
- What downstream quality metric would make the apparent win feel less trustworthy
- What assumption about the denominator feels shakiest

I like this artifact because it slows down a very specific kind of overconfidence.

It forces the team to say whether the win came from helping more of the right users succeed or from observing a cleaner subset of users than before.

Those are not the same thing.

## Good growth teams learn to ask who became uncountable

That question has changed the tone of a lot of reviews for me.

Not only who converted.

Who stopped qualifying.

Who never saw the treatment.

Who hit the branch of the product we are pretending was marginal.

Who fell out of the CRM sync.

Who got the old template.

Who self selected into the path that now looks healthier.

Microsoft is blunt about this in its work on [data quality for trustworthy A B testing analysis](https://www.microsoft.com/en-us/research/articles/data-quality-fundamental-building-blocks-for-trustworthy-a-b-testing-analysis/). If the data are incomplete or biased, the decision gets shaky fast.

I think product teams should be just as blunt in ordinary growth reviews.

Not because every dashboard is lying.

Because every dashboard is selective.

The job is to understand how selective.

## This makes wins more portable

A denominator note is not only defensive.

It also helps you find the wins that are actually worth scaling.

If a lifecycle prompt improved conversion across high and low intent segments, across devices, and without obvious eligibility distortion, I trust it more.

If an onboarding change helped the messy middle of the cohort instead of only the already motivated slice, I trust it more.

If an SEO landing page improved conversion even after accounting for branded traffic mix, I trust it more.

In other words, denominator discipline does not make product teams more timid.

It makes them more precise about what kind of win they actually earned.

That precision matters when you are deciding whether to scale the change, repeat the pattern elsewhere, or let it influence strategy.

## I think this is part of product character

There is a version of growth work that treats every upward line as a permission slip.

I understand the temptation.

The quarter is moving fast.

The experiment was expensive.

The slide needs a point of view.

The team wants momentum.

But I think mature growth judgment looks a little different.

It is willing to ask whether the result got better because the product improved or because the population became easier to please, easier to observe, or easier to count.

That is a less glamorous question.

It is also the one that protects you from compounding the wrong lesson.

When I look back at the growth work I trust most, it usually has that quality.

The team did not just find a lift.

They understood who the lift belonged to.

They knew who was missing.

They could explain why the denominator deserved belief.

That is usually when I stop seeing a metric and start seeing judgment.
