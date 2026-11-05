---
title: "Keep the assignment in the experiment"
subtitle: "The people who never received or used a treatment are often part of the product result, not noise to remove from it."
description: "A growth PM field note on preserving random assignment, diagnosing treatment reach, and separating the effect of a product policy from the effect among users who received it."
date: 2026-10-22
image: /assets/images/notebook.jpg
layout: post
---

A growth experiment can look much better after we remove the people it failed to reach.

That should make us nervous.

Imagine a team testing a new onboarding checklist. Half of eligible accounts are assigned to the new experience. Some never return after signup. Some arrive on a mobile screen where the checklist does not render. Some dismiss it before completing a task. Among the people who use the checklist, activation is excellent.

The tempting readout compares checklist users with everyone in control and calls the treatment a winner.

But the product was not a checklist floating outside the system. It was a policy for assigning a checklist, delivering it, and making it worth using. Failure at any of those steps belongs in the first answer.

## Usage is an outcome, not an admission ticket

People who take up a treatment are usually different from people who do not.

They may have more urgent jobs, newer browsers, more time, greater confidence, or simply another reason to return. Once we keep only the users who engaged with the new experience, randomization no longer protects the comparison in the same way. We are selecting people using behavior that happened after assignment and may have been changed by the treatment itself.

This is not an argument against studying engaged users. It is an argument for asking the policy question before the participation question.

The policy question asks what happened when we assigned the new experience to the eligible population. The participation question asks what happened for people who actually received or used it. Both can matter. They are not interchangeable.

Clinical research has wrestled with the same boundary for a long time. The [CONSORT guidance asks trial reports to show how many participants were assigned, received the intended treatment, and entered the primary analysis](https://www.consort-spirit.org/item-22a-randomized). That flow matters because excluding people who did not follow treatment can create a cleaner story and a less trustworthy comparison.

Software makes nonreceipt easy to overlook. There is no pill bottle to count. There is a flag, a render, an event, and a query. A user can be assigned without becoming eligible at runtime, become eligible without receiving the component, receive it without noticing it, or notice it without acting.

Every transition can change the group we are looking at.

## Delivery is part of the product claim

This makes me think about public programs as much as clinical trials.

A benefit can be effective for the people who complete an application and still have little effect on the population it was meant to help. Awareness, eligibility rules, paperwork, timing, and trust all sit between the policy and its use. Take-up is not clerical detail. It is part of whether the program works in practice.

Growth products have their own version of that chain.

A lifecycle message has to be sent, delivered, understood, and acted on. An onboarding module has to load in the right session, fit the viewport, feel relevant, and survive dismissal. A recommendation has to be available when the underlying job is present. The intervention in the roadmap may be one box. The intervention in the world is a sequence of gates.

The [ICH guidance on trial estimands](https://database.ich.org/sites/default/files/E9-R1_Step4_Guideline_2019_1203.pdf) is useful here because it insists on defining the treatment effect we want before choosing the analysis. One approach treats events such as discontinuing treatment as part of the treatment policy being compared. Another can ask a more hypothetical question about what might happen without that event.

A growth team does not need clinical vocabulary to borrow the discipline.

Before filtering a readout, say whether the decision is about shipping the whole product policy as it currently works or about the potential of the experience when it is successfully received. If it is the first, nonreceipt belongs in the result. If it is the second, we need a credible design for that narrower claim rather than an after-the-fact filter that rewards enthusiasm.

## Keep an assignment-to-outcome map

The practical artifact I want is a one-page map that follows the population from randomization to the outcome.

**Decision population**

Name the people or accounts the ship decision is meant to cover. Record the eligibility rule before assignment and the randomization unit.

**Assignment**

Record the expected allocation and the actual counts in each variant. Keep the assignment event independent of treatment behavior.

**Opportunity**

Define the condition under which someone could encounter the treatment in either variant. This might be returning to the setup page or reaching an unfinished project. The condition cannot depend on clicking the treatment-only component.

**Receipt**

Record whether the experience was actually delivered. Include render failures, unsupported clients, message bounces, latency, and flag errors rather than quietly dropping them.

**Use**

Record the intended interaction and the plausible reasons someone might decline it. Use is a diagnostic outcome, not the gate into the primary comparison.

**Product outcome**

Measure the result for everyone assigned, then show the same sequence of opportunity, receipt, use, and outcome by variant. Keep guardrails on the assigned population too.

**Decision rule**

Write what the team will do if assignment helps, if receipt is weak, or if use looks promising while the assigned result is flat.

The map turns a vague complaint about dilution into a product diagnosis. A small assigned effect can mean the experience is weak. It can also mean the experience is strong but the delivery system rarely gives it a fair chance. Those lead to different next moves.

## Counterfactual logging keeps the middle honest

The hardest line on the map is opportunity.

Suppose the new checklist appears only when an account has an unfinished setup task. Treatment logs a checklist impression. Control has no checklist and therefore no impression. Filtering both groups to people with an impression would leave no control group at all. Filtering control with a rough proxy can be nearly as dangerous if the treatment changes that proxy.

The cleaner move is counterfactual logging. Instrument the shared condition that would make a user eligible to see the treatment, whether the user is in treatment or control. Microsoft’s guidance on [post-experiment analysis](https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-post-experiment-stage/) recommends checking that this triggered population has the expected variant balance and that the people outside it look like an unaffected comparison.

That advice connects product implementation to causal interpretation. The control experience sometimes needs extra instrumentation before launch so the team can later identify comparable opportunities. Analytics is not only a scoreboard attached after the build. It is part of the experimental treatment design.

The assigned population should also pass a sample ratio check before anyone reads the win metric. Microsoft’s field guide to [sample ratio mismatch](https://www.microsoft.com/en-us/research/publication/diagnosing-sample-ratio-mismatch-in-online-controlled-experiments-a-taxonomy-and-rules-of-thumb-for-practitioners/) describes how missing or unevenly logged users can make a harmful change look useful or the reverse. If the planned split and observed split do not agree beyond plausible chance, stop and diagnose the pipeline.

## Write the hypothesis at the level of the decision

For the checklist example, I would write this.

> We believe assigning the contextual checklist to new workspace owners with an unfinished first project will increase the share that publishes a usable project within fourteen days, because the checklist will make the remaining work visible at the next relevant visit. We will measure all assigned owners and expect the gain to occur through more eligible visits receiving the checklist and more received checklists leading to resumed work, without increasing dismissals or support contacts.

This claim can fail in useful ways.

If checklist users publish more but the assigned population does not, the team has evidence about potential and a reach problem, not a shipping win. If treatment creates more eligible visits, that effect belongs in the result rather than being filtered away. If receipt differs by device, the product has found an implementation boundary. If assignment improves publishing while measured use stays low, the logging may be incomplete or another part of the variant may be doing the work.

A falsifiable hypothesis should leave room for each of those answers.

## Run the experiment with two readouts

I would make the assigned-population readout primary.

Randomize eligible workspace owners before the next visit. Check allocation counts and identity joins. Measure usable projects, retained collaborative work, dismissals, and support contacts for every assigned owner through the full outcome window. Do not require a checklist impression or click to enter this comparison.

Then use the assignment-to-outcome map as a diagnostic readout.

Compare shared opportunity by variant. Compare receipt among users with an opportunity. Compare use among users who received the experience. Inspect browser, device, latency, and acquisition path for broken gates. These cuts explain the primary result. They do not replace it.

If the assigned result is flat and receipt is low because the component fails on mobile, fix delivery and rerun the experiment. If receipt is healthy and use is low, revisit relevance or interaction cost. If use is healthy and the assigned result still does not move, the checklist action may be busywork rather than a bridge to value.

There is one important restraint. Do not claim that the difference among users who chose to use the checklist is the causal effect of checklist use. Random assignment identifies the effect of assignment. Estimating the effect among people whose behavior complied with assignment requires stronger methods and assumptions. Most growth decisions do not need that estimate before the team can repair obvious failures in reach.

## A diluted result can be the most practical result

Teams sometimes dislike the assigned estimate because it makes a promising experience look small.

But a ship decision inherits the delivery system we actually have. If only a fraction of eligible users receive the feature, the business will only receive a fraction of its value. That is not statistical pessimism. It is product reality.

The diagnostic layers still protect ambition. They can show that the idea deserves a better surface, a more reliable trigger, or a narrower eligible population. They can tell us where to spend the next week.

What they should not do is turn the people our product failed to reach into missing paperwork.

Growth experiments are tests of systems, not screenshots. Keep the assignment in the experiment long enough to learn whether the whole system works.
