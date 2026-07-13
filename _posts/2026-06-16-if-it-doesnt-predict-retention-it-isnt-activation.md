---
title: "If it doesn’t predict retention, it isn’t activation"
subtitle: "A practical way to separate setup milestones from the moment a product starts to matter."
description: "A growth PM field note on choosing activation metrics that predict retained behavior instead of rewarding busywork."
date: 2026-06-16
image: /assets/images/notebook.jpg
layout: post
---

I have a mild allergy to activation metrics that look tidy in a dashboard but tell you almost nothing about whether a user is actually going to stick around.

You’ve probably seen the pattern.

A team picks a milestone that is easy to count:

- completed onboarding
- invited one teammate
- connected an integration
- uploaded a file
- clicked through every checklist item

The number goes up, everyone feels briefly better, and a month later retention is unchanged.

That usually means the team did not find activation. It found a convenient milestone.

Those are not the same thing.

The definition I keep coming back to is simple: activation should point to the moment a user starts getting real value from the product in a way that predicts they are more likely to come back.

That last part matters most.

If the behavior does not meaningfully predict retained usage, I do not think it deserves the label.

## Activation is a product judgment, not a funnel checkbox

This is where growth work gets interesting.

Activation is not just a reporting exercise. It is a judgment call about what “value realized” looks like in your product.

Sometimes that value shows up in a single action. More often it shows up in a pattern:

- a message sent and replied to
- a project created and revisited
- a teammate invited after an initial task is completed
- a piece of content saved, shared, or returned to
- a workflow repeated enough times that it stops being novelty and starts being habit

That is why I get nervous when activation gets defined too early by whatever lives nearest to signup.

New users do many things because the product asked them to, not because they understood why the product was worth keeping.

There is a difference between:

- “the user completed setup”
- “the user crossed into value”

The first can happen through compliance. The second usually shows up in behavior.

## A useful test: would you bet retention on it?

One practical filter I like is this:

If I had to bet next month’s retention on one early behavior, what would I choose?

That question forces a different standard.

A lot of onboarding tasks are still important. They may reduce friction. They may improve data quality. They may help sales. They may unlock downstream functionality.

But importance is not enough.

Activation should earn its status by correlating with the thing you actually care about later.

[Andrew Chen’s old retention essay](https://andrewchen.com/retention-is-king/) still holds up here. His core point was that growth gets fragile very quickly when retention is weak. I think the same logic applies one layer earlier: if your activation metric is not tied to retained behavior, you can end up optimizing the wrong part of the story with a lot of confidence.

## The trap: rewarding busywork

A lot of “activation” metrics are really proxies for effort.

The user did a bunch of stuff. Great.

But effort is not value.

I’ve seen teams celebrate checklist completion when the checklist itself was bloated. I’ve seen “invite a teammate” treated as sacred even when invites had almost no relationship to whether an account ever became healthy. I’ve seen setup steps bundled into activation because they were easy to instrument, not because they were the best predictors.

That’s the trap.

Measurement convenience quietly becomes product truth.

[PostHog’s write-up on finding activation metrics](https://posthog.com/product-engineers/activation-metrics) makes this point more concretely than most articles do. The part I appreciate is their insistence on comparing candidate early behaviors against later retention, instead of assuming onboarding completion or collaboration steps automatically count. That is a much better discipline than picking the neatest event name and moving on.

## What I look for instead

When I’m trying to choose or pressure-test an activation metric, I usually want four things.

### 1. It reflects experienced value, not administrative progress

If the event mostly proves the user finished your setup flow, I’m skeptical.

I want evidence they actually used the product in a way that exposed the core benefit.

For a collaboration tool, that may be a shared workflow completed. For a marketplace, it may be a successful first transaction. For a study product, it may be a practice loop repeated enough times to show the learner got something from it.

### 2. It is early enough to influence

An activation metric should happen soon enough that the team can design toward it.

If the “true” signal only appears 45 days later, it may be valuable analytically, but it is less useful operationally. Usually you need an earlier behavior that is directionally predictive.

This is where activation becomes a bridge between onboarding and retention, not a replacement for either.

### 3. It can survive segmentation

One of the easiest ways to fool yourself is by averaging across users with very different jobs, intent, or product entry points.

An activation event that works for power users may be nonsense for casual users. A B2B team metric may not translate to a single-player workflow. A signal that predicts retention in one acquisition channel may fall apart in another.

That does not mean you need twenty activation definitions. But it does mean you should check whether your “one metric” is hiding important differences.

[Rahul Vohra’s First Round piece on Superhuman and product-market fit](https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/) is useful here for the segmentation mindset alone. Different groups reach value differently. Your activation work gets better the moment you stop pretending every new user is on the same journey.

### 4. It is crisp enough to guide product decisions

“User understood the value” is not a usable metric.

“User created three dashboards” might be usable, but only if those dashboards actually map to later success.

The metric needs enough specificity that a team can ask good questions:

- what helps more users get there?
- what friction blocks that behavior?
- what channels send users who are more likely to reach it?
- what changes move the metric but hurt downstream quality?

If the metric cannot shape decisions, it is probably too vague or too ceremonial.

## A better working model

The model I like is:

1. Define the retained behavior that signals an account is genuinely healthy.
2. Look backward for early actions or action bundles that correlate with that outcome.
3. Filter out milestones that are necessary but not predictive.
4. Choose the metric that is both meaningful and operable.

That sounds obvious, but a surprising amount of activation work starts at step four.

Teams begin with the dashboard they want, not the user behavior they need to explain.

## What this changes in practice

When you treat activation as a retention-predictive judgment, a few things get clearer.

First, onboarding gets less performative.

Instead of stuffing every “helpful” task into the first-run experience, the team starts asking which moments are actually worth protecting and sequencing carefully.

Second, experiment ideas improve.

You stop shipping changes just because they increase surface-level completion rates. You start asking whether the experiment helps users reach a meaningful value threshold faster or more reliably.

Third, cross-functional conversations get better.

Design, product, engineering, lifecycle, and analytics can disagree usefully about what value realization really is. That is a much healthier debate than blindly inheriting whatever metric happened to exist last quarter.

## A simple gut check for teams

If your activation metric moved up 20% next month, what would you expect to happen after that?

If the honest answer is “I’m not sure retention would change,” then I would not trust the metric yet.

That does not mean it is useless. It may still be a useful setup KPI, a quality-of-onboarding metric, or an operational milestone.

Just call it what it is.

Not every early funnel event deserves the prestige of activation.

## The point

Activation is one of those growth concepts that gets flattened when it turns into dashboard furniture.

At its best, it is a disciplined attempt to answer a harder question:

What is the earliest believable sign that this product has started to matter?

That answer will rarely come from the cleanest checklist item.

Usually it comes from a more honest read of user behavior, value realization, and what retention is quietly trying to tell you.
