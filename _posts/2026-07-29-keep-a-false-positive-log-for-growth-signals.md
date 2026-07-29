---
title: "Keep a false-positive log for growth signals"
subtitle: "Why growth teams should study the moments a product says success before the user would agree."
description: "A growth PM field note on false positives, proxy metrics, and a simple artifact for finding places where the product celebrates too early."
date: 2026-07-29
image: /assets/images/desk.jpg
layout: post
---

I think one of the most expensive mistakes in growth product work is celebrating too early.

The account was created.

The onboarding checklist was completed.

The invite was sent.

The integration connected.

The first project was generated.

The activation event fired.

All of those can be real events.

None of them automatically mean the user got what they came for.

That gap matters.

I keep thinking about it as a false positive.

The system says success.

The dashboard says success.

The team meeting says success.

The user might still say not really.

When that happens a growth team does not only misread performance.

It also starts designing from the wrong story.

## A growth false positive is a product judgment problem

I do not mean false positive in the strict statistical sense.

I mean the broader operating problem where the product, the metric, or the team records a win before the user would recognize one.

That happens all the time.

A user signs up because the landing page was persuasive, but they have not actually found a credible path to value.

A team counts an import as complete because the file uploaded, but the user still cannot use the output.

A collaboration product celebrates an invite sent even though no teammate accepted, replied, or changed the account from solo to shared.

An AI tool logs a draft generated even though the draft is weak enough that the user quietly starts over somewhere else.

I like the Google HEART framework for this reason. In the original [Google research on user-centered metrics](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/), task success sits alongside adoption and retention because product health is not only about motion. It is also about whether the user actually completed the thing that mattered.

That sounds obvious.

Teams still miss it constantly.

We count the visible event because it is easy to instrument.

We skip the harder question of whether the event deserves to stand in for success.

That is not a data problem first.

It is a product judgment problem.

## Other fields are more careful with presumptive wins

Medicine is often more honest about uncertainty than growth dashboards are.

The CDC guidance on [prostate cancer screening](https://www.cdc.gov/prostate-cancer/screening/get-screened.html) explains false positives plainly. A test can point toward a condition that is not really there, and the result can still produce stress, extra work, and bad downstream decisions.

I think product teams should steal that humility.

A positive signal is not always a confirmed outcome.

Sometimes it is only an indication that more verification is needed.

That is how a lot of growth events should be treated.

Did the user create the workspace.

Good.

Did they populate it with meaningful data, understand what to do next, and experience a reason to come back.

Different question.

Did a trial user click the paywall upgrade button.

Interesting.

Did they complete payment, understand what changed, and succeed at the job that drove the upgrade intent.

Different question again.

I think many growth teams compress those states into one.

Started becomes succeeded.

Intent becomes outcome.

Movement becomes value.

That is how false positives get normalized.

## False positives distort strategy before they distort metrics

The obvious cost is reporting.

The less obvious cost is product direction.

Once a team has chosen the wrong proxy, it starts feeding the organization the wrong lesson.

You hear things like this.

Users love the new onboarding because completion is up.

The invite prompt works because more people send invites.

The content loop is healthy because SEO signups increased.

The AI assist is sticky because generation volume is climbing.

Maybe.

Maybe not.

The GOV.UK guidance on [measuring the success of your service](https://www.gov.uk/service-manual/measuring-success/measuring-the-success-of-your-service) says not to rely only on digital analytics and to combine performance data with research and other evidence sources. I think that is exactly right for growth product work too.

If the chosen signal gets detached from the lived outcome, the team starts optimizing for ceremony.

Users perform the gesture.

The business records the move.

The real job remains unfinished.

That is not harmless.

It can make a roadmap look cleaner than the product feels.

## The user often knows the truth before the team does

One reason I like pairing behavioral data with user confidence is that it exposes a more interesting failure mode.

The user can appear to finish while actually leaving unconvinced.

Or worse, the user can think they succeeded when they did not.

Jeff Sauro wrote about this well in MeasuringU on [user interface disasters](https://measuringu.com/ui-disasters/). The truly dangerous cases are not only failed tasks. They are failed tasks that users believe were completed successfully.

That idea travels well into growth product.

A user thinks the data sync is done, but key records never mapped.

A team admin thinks teammates were fully provisioned, but permissions quietly failed.

A new subscriber thinks their account is live, but the core workflow is still blocked behind setup work nobody explained.

Those are not only UX bugs.

They are growth distortions.

The team may record those sessions as healthy progress.

The user records them as confusion, mistrust, or later churn.

This is why some products have decent activation charts and shaky word of mouth.

They are producing administrative success more reliably than felt success.

## The artifact I like is a false-positive log

When a team has a suspiciously cheerful funnel and a murkier user reality, I like making a false-positive log.

It is not complicated.

It is a forcing function for asking which wins are confirmed and which are merely suggestive.

## False-positive log

- The signal or event the team currently counts as success
- The user outcome that would deserve to be called success
- Why the current signal might overstate reality
- What evidence would confirm the user outcome more credibly
- Which segments are most vulnerable to this mismatch
- What support tickets, replay sessions, interviews, or churn notes suggest the current metric is lying
- What product change could narrow the gap between recorded success and real success
- What metric change could distinguish started, provisional, and confirmed outcomes
- Owner

This artifact gets useful fast.

You start seeing how many growth events are really hand raises rather than finished outcomes.

You notice where a celebratory screen appears before the workflow can stand on its own.

You find places where the funnel is measuring submission while the user is judging usefulness.

You also get a more disciplined conversation about activation.

Not what can be counted earliest.

What can be trusted earliest.

## A lot of growth systems need a provisional state

I think product teams are sometimes too binary in how they report progress.

Success or failure.

Activated or not.

Converted or not.

Completed or abandoned.

Real user journeys are often messier than that.

Some states deserve an honest middle category.

Submitted.

Processing.

Partially configured.

Needs collaborator action.

Ready for review.

Useful once one more dependency clears.

Those are not evasive labels.

They are often the most truthful ones.

A provisional state can protect the user from misplaced confidence and protect the team from bad inference.

It also helps with design.

If you admit a moment is provisional, the interface has to explain what still needs to happen.

That usually leads to better guidance, better messaging, and fewer hollow congratulations.

## This changes how I look at activation work

I still care about early momentum.

I still want fast paths to value.

I still like simple proxy metrics when they are directionally sound.

But I trust an activation definition more when the user would defend it, not only when the instrumentation can detect it.

That usually means asking a stricter set of questions.

Did the user finish the administrative step or the meaningful step.

Did the event capture effort or payoff.

Did the product make the outcome legible enough that the user would say yes, that worked.

Did we confirm the behavior with more than one kind of evidence.

Could support, research, or retention data embarrass this metric if we looked closely.

Those questions slow a team down in a healthy way.

They make it harder to confuse an internal milestone with a user win.

## What I would do this week

Pick one growth journey that matters.

Usually signup to first value, invite to collaboration, or trial to paid.

Then list every event in that path where the team currently says success.

For each one, ask whether the user would agree without being coached.

If the answer is no, mark it as provisional.

If the answer is maybe, find the confirming evidence you wish you had.

If the answer is yes, write down why you believe it.

That is a small exercise.

It can clean up a surprising amount of product thinking.

Because a lot of what looks like a growth problem is really a naming problem.

We called something success before it had earned the word.
