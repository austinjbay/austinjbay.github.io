---
title: "Recalibrate activation before the signal drifts"
subtitle: "The early behavior that once predicted retention can quietly stop carrying the same meaning."
description: "A practical activation calibration card for checking whether an early growth signal still predicts the outcome the team thinks it does."
date: 2026-11-04
image: /assets/images/notebook.jpg
layout: post
---

I used to think the hard part of activation was finding the right signal.

Find the early behavior that best predicts retained use. Give it a clean event name. Put it on the dashboard. Help more new users reach it.

That is still hard. It is just not the whole job.

Products change after a team chooses an activation metric. The onboarding gets shorter. An import tool does more of the work. A free feature moves behind a paywall. A lifecycle campaign sends people straight to the action that used to require some discovery. Eventually the same event can be firing for a different reason.

The dashboard keeps its familiar shape while the meaning underneath it moves.

I think growth teams should treat activation more like a measuring instrument than a plaque on the wall. Finding the signal is the first calibration. Keeping it useful requires checking it against the outcome again.

## A stable event can hide a moving meaning

Imagine a team that defines activation as creating and sharing a first project within seven days. When the metric was chosen, people usually had to understand the workspace, add useful material, and decide that the project was worth putting in front of someone else. The event bundled several small acts of value and confidence.

Then the product adds an AI-generated starter project and puts the share button in the final step of onboarding. More people create and share. Activation rises.

That may be a real improvement. It may also mean the event is easier to produce without the understanding and intent it used to represent. The action stayed the same. Its information value changed.

This is familiar in other fields. [NIST describes measurement drift as a slow change in how a gauge responds and recommends using check standards to detect it](https://www.itl.nist.gov/div898/handbook/mpc/section4/mpc453.htm). NIST also notes that [recalibration intervals depend on the instrument, its environment, and the accuracy the work requires](https://www.nist.gov/calibrations/recommended-calibration-interval), rather than one universal schedule.

Public health has a related problem with definitions. The CDC warns that [changes in a surveillance case definition can affect reported trends](https://www.cdc.gov/hepatitis/php/surveillance-guidance/general-surveillance.html). A line can move because the underlying condition changed, because the way cases are found changed, or because the counting rule changed.

Activation deserves the same suspicion.

The product is both the thing being observed and part of the instrument doing the observing. When we redesign the path, we can change what the signal means.

## Prediction is a relationship, not a property

It is tempting to say that sharing a project is predictive of retention as if predictiveness lives permanently inside the event.

It does not.

The relationship belongs to a particular product, population, entry path, and period. Change enough of those conditions and an honest analysis from last year can become a weak assumption this year.

Machine learning teams deal with a version of this problem in production. Google recommends monitoring for [drift in inputs, predictions, and model quality](https://developers.google.com/machine-learning/managing-ml-projects/production), because a model that performed well when it launched can degrade as its operating conditions change. An activation definition is not a machine learning model, but it is still a compact prediction. It says that people who do this early thing are more likely to do the later thing we care about.

That claim should be allowed to expire.

Not every product change requires a metric funeral. The point is not to churn the definition until nobody can compare one quarter with the next. The point is to notice when the event has become easier to manufacture, detached from value, or less useful for making decisions.

## Keep an activation calibration card

I would keep the artifact to one page and attach it to the metric definition.

### The current signal

- The exact qualifying behavior and observation window
- The retained outcome it is meant to predict
- The eligible population and important exclusions
- The last period when the relationship was checked
- The strength of the relationship then

### The conditions around it

- The product steps a person had to complete when the signal was validated
- The main entry paths that produced the behavior
- The prompts, incentives, defaults, or automation that can now produce it
- Recent changes to pricing, instrumentation, acquisition mix, or the core workflow
- Reasons the same event might now carry less or different intent

### The next check

- The later outcome and maturity window needed for a fair comparison
- A stable historical cohort for reference
- The product change most likely to have altered the signal
- The owner and the event that triggers recalibration
- The decision if the signal has weakened

The most useful line is the trigger.

A calendar reminder can help, but product changes are usually a better prompt. Recheck after a major onboarding redesign, a new shortcut to the qualifying event, an instrumentation rewrite, a pricing change that alters who can perform the action, or a meaningful shift in where new users come from.

Do not wait for the retention chart to make the problem obvious. By then the team may have spent months optimizing a ceremonial action.

## Write the drift hypothesis before running the analysis

Here is one I would use for the project example.

> We believe the new starter-project flow increased first-week project sharing without increasing fourth-week collaborative use by the same proportion, because users can now reach the share event before adding enough of their own work to make the project worth revisiting.

This is more useful than asking whether activation is still good.

It names the product change, the early signal, the later check, and the mechanism that may have weakened their relationship. It also leaves room for a better result. The starter project may remove blank-page friction while preserving everything that made sharing meaningful.

The analysis should compare mature cohorts from before and after the change. Within each period, measure the later outcome for people who did and did not reach the activation event. Look at both the absolute retained rate among activated users and the lift relative to otherwise eligible users who did not activate.

That second view matters. If retention rises for everyone because the product got better, activated users may still look healthy even while the signal becomes less discriminating.

I would also compare how people reached the event. A manually built project, an imported project, and a generated starter may all end with the same share event while representing different amounts of commitment. This is an investigation of the definition, not an excuse to declare three permanent activation systems. The goal is to learn whether the current label still groups together behavior with a useful common meaning.

If possible, use a staged rollout or an experiment that changes the route to the event without changing the event itself. The cleanest question is whether making the milestone easier raises the downstream outcome, not only the milestone count. Keep the retention window fixed, let every cohort mature, and audit the event payload before interpreting the chart.

## Recalibration can fail in both directions

There are several ways to get this wrong.

A team can overreact to normal noise and redefine activation every time a weekly chart wiggles. That destroys continuity and makes the metric impossible to use. Recalibration needs a mature window, enough users, and a material product or population change worth investigating.

A team can also confuse weaker discrimination with a worse product. Suppose a redesign helps many more people retain, including those who never hit the old signal. The old event may become a worse predictor because value is now available through another legitimate path. That is good product news and metric news at the same time. Keep the improvement. Retire or widen the definition.

The opposite failure is more political. A team makes the activation event easier, celebrates the lift, and avoids looking downstream because the new number is useful in a roadmap review. Recalibration is uncomfortable when a metric has become part of the team's identity.

There is a technical failure too. An apparent change in meaning can come from a duplicated event, a changed identity join, missing mobile traffic, or a retention query that uses a different eligibility rule. Google’s production guidance asks whether [the system computing an input ever changes and how the team will know](https://developers.google.com/machine-learning/crash-course/production-ml-systems/questions). Growth analytics deserves that same basic discipline. Check the measuring system before inventing a behavioral story.

Finally, correlation was never proof that forcing the early action would cause retention. Highly motivated users may simply do both. Recalibration can tell us whether the signal still sorts future outcomes. A randomized change to the path is stronger evidence about whether helping someone reach it creates value.

## The judgment call is whether to repair, replace, or demote

When the signal weakens, the PM has a real choice.

Sometimes the metric is sound and the path needs repair. If generated starter projects retain well only after users add one piece of their own work, the product can help people reach that meaningful state before prompting a share.

Sometimes the definition needs replacing. A completed collaboration may now be more informative than a sent invitation because the product made invitations nearly automatic.

Sometimes the honest move is demotion. The event can remain a useful onboarding completion measure without carrying the larger claim of activation.

And sometimes nothing should change. A modest decline in predictive strength may be acceptable if the metric is still early, understandable, responsive to product work, and directionally tied to retained value. The statistically strongest signal is not automatically the best operating metric if it arrives too late or cannot guide a team.

That is the judgment growth PMs have to make. Preserve enough continuity to learn over time, but not so much that an old definition becomes immune to the product it is supposed to describe.

I still believe activation should predict retention.

I just no longer think proving that once is enough.
