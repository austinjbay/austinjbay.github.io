---
title: "Hold the journey still long enough to learn"
subtitle: "A clean experiment can still teach the wrong lesson when the surrounding product keeps changing underneath it."
description: "A growth PM field note on creating a learning window around consequential experiments without turning a fast team into a frozen one."
date: 2026-10-23
image: /assets/images/notebook.jpg
layout: post
---

Growth teams like to say that they are learning quickly.

Sometimes what we mean is that we are changing many things quickly.

A new onboarding step starts its experiment on Monday. Lifecycle changes the welcome email on Tuesday. The pricing team moves a plan benefit on Wednesday. A reliability fix lands on Thursday and makes imports faster for everyone. On Friday the experiment reports a lift.

The randomization may be sound. The result may be statistically convincing. The lesson can still be muddy.

The treatment did not meet the product we thought it would meet. It met a journey that kept moving while we watched.

I do not think the answer is to make one team the traffic cop for every release. Products need fixes, launches, and ordinary maintenance. But when an experiment could change what we believe about the product, the surrounding journey needs a short period of deliberate stability.

Learning needs a window, not just a test.

## A valid comparison can answer an obsolete question

Imagine a hypothetical planning product testing a guided first project. The team believes that choosing a template and naming one next action will help new users finish a useful plan within a day.

Halfway through the test, another team ships a faster importer. Then lifecycle replaces a generic welcome message with one that links directly to the project screen. Both changes reach treatment and comparison groups.

Random assignment still protects the comparison between the two groups. That is valuable. Yet the product question has changed.

The guided project may work only when paired with the new import speed. The welcome message may make the guide redundant. An average lift can tell us what happened across the bundle of conditions that existed during the run. It cannot automatically tell us what the guide will do after the message changes again or when the importer is unavailable.

This is not an argument against simultaneous work. It is an argument for knowing which surrounding conditions are part of the claim.

## Manufacturing asks whether the process stayed stable

Manufacturing offers a useful mental model here.

The [NIST handbook on process stability](https://www.itl.nist.gov/div898/handbook/ppc/section4/ppc45.htm) explains that a process has to behave consistently over time before its capability can be judged. If the process itself is moving, a precise reading does not rescue the interpretation.

A growth journey is not a factory line. People arrive with intention and context that machined parts do not have. Still, the discipline travels well. Before attributing a result to one product change, ask whether the other parts of the experience stayed stable enough for that attribution to remain useful.

Software operations reaches the same idea from another direction. Google SRE recommends [canarying releases](https://sre.google/workbook/canarying-releases/) by exposing a limited share of real traffic and watching before expanding. Its guidance warns that overlapping canaries add mental effort and can contaminate the signal.

The connection I find useful is not that a growth experiment is a release canary. Their purposes differ. A canary asks whether a change is safe enough to expand. A product experiment asks whether a change produces an outcome worth pursuing. Both become harder to read when several nearby systems move at once.

Science gives this a plain name. We are trying to hold enough of the apparatus steady to understand the thing we deliberately changed.

## Use a learning window brief

For an experiment that could alter strategy, I would write a short learning window brief before assignment begins.

**The decision**

Write the choice the result will inform. Shipping a button treatment does not deserve the same coordination as deciding that guided creation should become the core onboarding model.

**The focal change**

Name the exact experience that differs between treatment and comparison. Include flags, eligibility rules, copy, and important service behavior.

**The surrounding surface**

List the nearby parts of the journey that could change the meaning or strength of the result. For the guided project, that might include the importer, the welcome message, template inventory, project load time, and the first upgrade prompt.

**The quiet window**

Set the dates when discretionary changes to that surrounding surface should wait. Tie the duration to the time needed for the main outcome to mature, not to a convenient sprint boundary.

**The allowed exceptions**

Security, accessibility, legal, reliability, and serious user harm do not wait for an experiment. Name who can approve an exception and how the change will be logged. A learning window is never permission to leave a broken journey in place.

**The release record**

Record everything that did change, including configuration, campaigns, model versions, operational rules, and vendor behavior. Code deploys are only part of the product.

**The exit**

State when normal shipping resumes and which delayed changes go first. If the team cannot name the end, it has written a freeze rather than a window.

The brief should be small enough to read during a launch review. Its purpose is not ceremony. It gives the team a shared answer when someone asks whether a nearby change can wait four days or whether the test should restart.

## Write the stability hypothesis too

Most experiment plans state what the treatment should do. Fewer state what must remain true around it.

For the planning product, I would write both.

> We believe asking new planners to choose a template and name one next action will increase the share who complete a useful plan within twenty-four hours, because it turns an empty workspace into a specific commitment.

Then I would add a falsifiable stability hypothesis.

> We believe the treatment effect will not differ materially between users who import existing work and users who start manually. If it does, import behavior is part of the mechanism and the guide should not be described as a general onboarding improvement.

That second statement makes the surrounding product testable. It also sharpens the decision. If the guide only works after a successful import, I may still ship it. I would place it after import and stop pretending it solves the empty start for everyone.

That is product judgment, not statistical housekeeping.

## Measure the window as part of the experiment

Start with concurrent treatment and comparison groups. A simple before-and-after view is especially vulnerable when the journey is changing over time.

Choose one main outcome that matches the decision and let it mature. For the example, useful-plan completion within twenty-four hours is better than a click on the template picker. Keep assignment logs and exposure logs separate so that a broken flag does not become a behavioral story.

Alongside the outcome, build a release timeline from the first assignment through the last outcome window. Mark changes to copy, routing, performance, notifications, pricing, data pipelines, and operations. The record should include incidents and emergency fixes, not only planned launches.

If an important surrounding change lands mid-run, do not quietly average across it. Add a pre-change and post-change interaction that was specified before reading those slices when possible. If the interaction is large, extend or rerun the test under the condition you expect to keep. If the sample is too small, say the result applies to the combined operating conditions you actually observed.

The summit report on [practical online controlled experiments](https://www.microsoft.com/en-us/research/uploads/prod/2020/07/2019-FirstPracticalOnlineControlledExperimentsSummit_SIGKDDExplorations.pdf) describes how interactions between concurrent experiments can change a measured treatment effect. Not every overlap matters. The point is to make consequential overlap visible enough to investigate rather than assuming randomization makes the whole environment irrelevant.

I would also repeat the important treatment after the window when the product has returned to its normal release rhythm. A smaller confirmation run can reveal whether the effect survived outside the carefully held period. Stability is a way to earn an interpretable first answer, not a permanent laboratory around the product.

## Do not confuse stillness with rigor

There are bad ways to use this idea.

A team can freeze too wide a surface because it did not do the work of identifying likely interactions. It can stop urgent fixes to protect a dashboard. It can reserve all traffic for one executive-backed bet. It can use a long test as an excuse to avoid making product decisions.

None of that is rigor.

The window should be narrow around the journey, proportional to the decision, and interruptible for user welfare. Most button, copy, and ranking experiments do not deserve a broad coordination exercise. Many can run together because they are distant in the experience or because the team only needs a local answer.

I would use the brief when the test could redefine onboarding, pricing, a core loop, or the product story itself. Those are the moments when a clean chart can create an expensive belief.

Fast shipping and clean learning are not enemies. They just operate on different clocks.

The craft is knowing when the next change is more valuable than an answer, and when holding the journey still for a few days will keep months of roadmap work from resting on a result nobody can explain.
