---
title: "Make a segment earn the right to change the product"
subtitle: "A cohort difference becomes useful when it changes a decision, not merely when it makes a dashboard more interesting."
description: "A growth PM field note on separating meaningful user differences from noisy slices with a practical segment warrant and learning plan."
date: 2026-11-01
image: /assets/images/notebook.jpg
layout: post
---

I think growth teams are too quick to turn a difference in a chart into a new kind of user.

Mobile users activate less often. Small teams retain better. People who arrived from a template gallery invite more coworkers. Before long, the dashboard has filters, the roadmap has variants, and the lifecycle system has six branches.

The difference may be real. The segment may still be useless.

A useful segment has to do more than describe who behaved differently. It has to reveal a different need, constraint, or response that gives the product a better decision to make. Otherwise we have taken ordinary variation and converted it into permanent product surface area.

## A cut in the data is not yet a boundary in the product

Segmentation feels responsible because averages hide important stories. They absolutely can. A blended activation rate can conceal a broken experience for screen reader users, a pricing model that only works for large accounts, or a setup step that is impossible on a phone.

But every available property also offers a new way to slice the result. Device, country, acquisition source, company size, role, plan, and signup week can produce a lot of apparently interesting winners and losers.

Statistics has a plain warning for this. The more comparisons we make, the easier it becomes to find a difference by chance. The [NIST guidance on multiple comparisons](https://www.itl.nist.gov/div898/handbook/prc/section4/prc47.htm) recommends choosing important contrasts in advance or using methods that account for examining many of them together.

The product version of that warning is less mathematical but just as important. If we search enough cuts after a test, one of them will give us a story. A story found in the same data that inspired it is a lead, not yet a product strategy.

## Good segmentation is a form of mapmaking

This makes me think about maps.

A map is not improved by showing every feature the cartographer can find. It is improved by showing the detail that helps someone use the map at a particular scale. The [USGS calls this generalization](https://www.usgs.gov/centers/cegis/science/generalization). A useful map reduces detail while preserving the features that matter for its purpose.

Growth teams have the same job. The territory contains millions of individual circumstances. We need a representation simple enough to make decisions without erasing a difference that changes the journey.

That means a segment should be judged against its use.

Country may be a meaningful boundary when payment methods, regulation, or language change the product. It may be a weak boundary when it merely stands in for a need we have not understood. Company size may change procurement and collaboration. It may tell us very little about the first job a person wants to finish.

The [UK Government Service Manual](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs) makes a useful distinction here. It recommends understanding all kinds of users while grounding user needs in research and in what people are trying to accomplish. The label helps only when it carries evidence about the job or constraint underneath it.

## The artifact I want is a segment warrant

Before a cohort gets its own onboarding, message sequence, or roadmap lane, I want a short warrant for treating it differently.

**Observed difference**

Write the behavioral gap, the comparison, the observation window, and the uncertainty around it. Keep the raw attribute separate from the behavior. “Mobile” is an attribute. “Cannot complete document upload from a phone” is a constraint.

**Reason it may exist**

Name the mechanism we believe connects the attribute to the outcome. This is where interviews, session review, support contacts, and operational evidence should meet the chart. If the only explanation is that this group is different, we are not ready.

**Decision it could change**

Name the product choice that would be different if the mechanism is true. The answer might be a distinct path. It might also be fixing the shared path for everyone.

**Cost of the boundary**

List the new states, content, instrumentation, quality checks, and maintenance the segment creates. A branch is not free after the experiment ends.

**Evidence that would retire it**

Write down what would let us merge the paths again. Segments should be allowed to expire when a constraint disappears or when later evidence shows the response was not meaningfully different.

The crisp hypothesis could read this way.

> We believe new workspace administrators with an external approval requirement complete setup less often because they cannot confidently invite teammates before approval. If we let them prepare the workspace and hand off an approval packet without sending invitations, their setup completion will improve without increasing abandoned prepared work.

The warrant is not “enterprise users need a custom onboarding.” It identifies a constraint, a different product decision, and an outcome that can prove the distinction useful.

## Confirm the boundary before you pave it

I would run the learning plan in two passes.

First, investigate the mechanism. Recruit people on both sides of the proposed boundary. Watch the part of the journey where their behavior separates. Review support and sales evidence without treating either as a substitute for observation. Check whether the attribute predicts the constraint or merely happens to travel with it.

Then test the smallest decision the warrant suggests. Randomize the proposed experience within the candidate group when that is practical. Keep the existing experience as the comparison. Preselect the main outcome and the few subgroup contrasts that matter before reading the result. Measure the cost created by the branch as well as its local lift.

For the approval example, I would track completion of a prepared workspace, successful approval handoff, eventual teammate participation, and prepared work that never becomes active. I would also interview a small sample of people who ignore the new path. That combination tells us whether we removed the proposed constraint or simply moved the abandonment point.

If the experience helps both groups, we may have found a better default rather than a segment. If the candidate group does not recognize the constraint, the label was probably doing imaginary explanatory work. If the lift appears once and disappears in a fresh sample, we should resist building a permanent branch around it.

## Use this when the difference could change the work

A segment warrant is useful when a team is about to personalize a journey, interpret an experiment by cohort, create a specialized lifecycle path, or reserve roadmap capacity for a class of users. It is especially useful when a familiar business label is starting to sound like a user need.

It is not the right tool for obvious access requirements, legal obligations, safety protections, or basic compatibility. Those do not need to win an incremental lift before they deserve attention. It is also overkill for a temporary diagnostic filter that will not change the experience.

The judgment call is whether the boundary helps us serve a real difference or merely makes uncertainty look organized.

Good growth work notices variation. Mature growth work is slower to turn that variation into architecture.
