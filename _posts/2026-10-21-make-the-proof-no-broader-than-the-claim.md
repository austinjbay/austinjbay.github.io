---
title: "Make the proof no broader than the claim"
subtitle: "Why growth teams should show the conditions around a customer outcome instead of asking one success story to stand in for everyone."
description: "A practical field note on reference classes, proof distance, and making customer evidence useful without sanding away the conditions that produced it."
date: 2026-10-21
image: /assets/images/notebook.jpg
layout: post
---

I once helped put an impressive customer result on a product page.

The customer had saved a great deal of time. The quote was real, the customer was happy, and the page performed better after we added it. We congratulated ourselves for finally giving a confident product claim some proof.

Only later did we notice how much machinery sat behind the result.

That customer had clean source data, an experienced operator, a narrow workflow, and an implementation partner. Many of the people arriving on the page had none of those things. They were not being deceived by the story, exactly. They were being invited to carry it much farther than the evidence could travel.

This is an ordinary growth Product mistake. We find our strongest outcome and remove the details that seem to weaken it. The company size disappears. The starting condition becomes vague. The work required to reach the result gets compressed into a logo and one polished sentence.

The proof becomes easier to scan and harder to use.

I have come to think of this as proof distance. It is the gap between the circumstances that produced an outcome and the circumstances in which we imply another user should expect it.

Strong proof does not eliminate that distance. It makes the distance visible.

## A result is also a description of its conditions

Clinical researchers have to ask whether a result produced in one study population and setting applies to another. A [consensus study indexed by the National Library of Medicine](https://pubmed.ncbi.nlm.nih.gov/38146072/) defines external validity through the ability to generalize across populations, settings, interventions, outcomes, and other relevant context.

That is a useful discipline for product evidence.

A team says that customers close their books three days faster. I want to know what close process they started with, who configured the product, what integrations were available, and whether the result appeared in the first month or the sixth.

A case study says a marketplace seller doubled revenue. I want to know whether the seller brought an existing audience, entered an empty category, or received hands-on help that ordinary sellers do not receive.

An onboarding page says teams get value in ten minutes. I want to know whether value means creating a project, inviting a colleague, or completing the job that justified buying the product.

These questions do not make the outcome less impressive. They tell a prospective user whether the outcome belongs in the comparison set for the decision in front of them.

That is the part we often lose when a customer story travels from research to sales enablement to a landing page. Each handoff rewards brevity. The conditions look like caveats, so they fall away. What remains is a vivid result with an invisible denominator.

The UK government's [Magenta Book guidance on evaluation](https://www.gov.uk/government/publications/the-magenta-book/magenta-book-annex-a-analytical-methods-for-use-within-an-evaluation-html) makes a related point. Understanding context and the mechanism behind an outcome helps people judge whether findings can generalize. A result without its mechanism is not useless, but it is less portable than it appears.

## Exceptional stories quietly become forecasts

Customer proof sits in an awkward place between testimony and prediction.

The words may describe what happened to one customer. The placement often tells the reader what could happen to them. Put a dramatic outcome beside a signup button and it begins to behave like a forecast, even if nobody wrote the words you should expect this too.

The [Federal Trade Commission guidance on endorsements](https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking) is unusually concrete about this problem. A specific result in an endorsement can be understood as what others will generally achieve. A vague disclaimer does not repair that impression. The guidance calls for evidence that the result is typical or a clear disclosure of generally expected performance.

That is a legal and advertising standard, not a complete product framework. Still, it exposes a product question worth asking.

What forecast will a reasonable user build from this proof?

Growth teams spend a lot of time tuning whether a story is credible. Is the logo recognizable. Does the quote sound human. Is the metric concrete. Those are good questions, but credibility is only one dimension.

A perfectly credible story can still be a poor reference case.

The regional bank running a six-month implementation may be credible and irrelevant to the founder trying the self-serve plan tonight. The creator with a million subscribers may be credible and irrelevant to someone building an audience from zero. The power user with a dedicated analyst may be credible and irrelevant to the operations manager who will own the workflow between other responsibilities.

The user does not merely need to believe the story. They need to place themselves in relation to it.

## Specificity can increase trust without shrinking ambition

Teams sometimes resist context because they fear it will make the proof feel smaller.

It will.

It will also make the proof more useful.

Saying that a customer cut weekly reconciliation from four hours to one hour after connecting two supported systems is narrower than saying teams save hours every week. The narrower statement gives the reader something to inspect. They can compare systems, frequency, starting effort, and required setup to their own situation.

Specificity also gives Product a better conversation with Marketing. Instead of arguing about whether a claim feels too bold, the team can ask which parts of the outcome are observed, which conditions appear necessary, and where the product has evidence beyond the featured customer.

This matters inside the product too.

An upgrade prompt that says people like you use automation is weak proof if like you only means the same plan. A setup checklist that promises a faster first result may borrow its benchmark from accounts with preloaded data. A lifecycle message may celebrate what successful teams do while omitting that those teams have an administrator maintaining the workflow.

The interface is full of tiny forecasts. Product managers should know which evidence those forecasts are borrowing.

## Write a proof distance card

Before a customer outcome appears on a page, in a prompt, or in a sales-assisted trial, I now want a short proof distance card.

It is not a compliance document. It is a product artifact that fits beside the mockup and keeps the evidence attached to the conditions that made it true.

Write down six things.

- **The observed result** states exactly what changed and how it was measured.
- **The starting state** records what was true before the product entered the workflow.
- **The reference user** describes the customer role, scale, and relevant experience without inventing a marketing persona.
- **The enabling conditions** name the data, integrations, assistance, permissions, and repeated work required.
- **The time horizon** says how long it took for the result to appear and over what period it was measured.
- **The proposed inference** writes the conclusion we expect a reasonable reader to draw from where the proof appears.

Then mark each element as observed, inferred, or unknown.

That last move is important. Teams often know the result and barely know the starting state. The card should show that weakness rather than filling the space with confident copy.

Here is a compact example.

The observed result is that one finance team reduced weekly reconciliation from four hours to one. The team began with a stable spreadsheet process. An operations lead connected two supported systems with help from an implementation specialist. The saving appeared after five weeks. We propose using the story to show that recurring reconciliation work can become materially faster when the source systems are supported and someone owns setup.

That inference can travel. A promise that every finance team will save three hours cannot.

## Test applicability rather than applause

The easiest experiment is a copy test that celebrates the variant with more clicks. That can reward the broadest interpretation, which is the thing we are trying to avoid.

Use a proportionate judgment method first.

Put the proof in front of five to eight people who are plausibly considering the product. Ask each person what they believe happened, what they expect would happen for them, and what conditions they think are required. Do not ask whether the story is convincing. Ask them to make the forecast in their own words.

Compare those forecasts with the proof distance card. If people assume a shorter timeline, less setup, a different starting state, or a broader result, the proof is creating distance the page does not acknowledge.

Then test a contextual version against the existing version where traffic and stakes justify it. Keep the underlying outcome the same. Add the two or three conditions most necessary for judging applicability. Measure movement into a qualified next step and successful early use, not only clicks on the nearby button. Watch cancellation reasons and sales conversations for evidence that expectations changed.

A precise hypothesis might read this way.

> For first-time visitors evaluating the self-serve reconciliation plan, adding the supported source systems, setup owner, and five-week time horizon to the customer outcome will reduce low-intent trial starts while increasing the share of new trials that connect a supported source and complete a second reconciliation within fourteen days, because visitors can judge whether the result is applicable to their own workflow before they sign up.

The experiment does not need to prove that contextual proof always wins. It needs to tell us whether better-calibrated expectations improve the part of the journey we actually care about.

If traffic is low, do not manufacture certainty from a small conversion test. Use the forecast interviews, review a month of sales calls and cancellation notes, and make a product judgment. The size of the method should match the cost of being wrong.

## Honest boundaries are a growth capability

There is a version of growth that treats every condition as friction in the story.

I understand the temptation. A broad claim gives more people room to imagine themselves inside it. A famous logo makes uncertainty feel settled. The best customer outcome is more exciting than the distribution of ordinary ones.

But acquisition is not improved when the page wins an interpretation the product cannot keep.

The more durable craft is to help the right user make a better forecast. Sometimes that means a smaller number. Sometimes it means admitting that the outcome required expertise, clean inputs, or patience. Sometimes it means finding a less dramatic story that sits much closer to the person making the decision.

Mid-career Product work has made me less impressed by proof that sounds universal and more interested in proof that knows its boundaries.

A customer story should not have to carry every prospect, every workflow, and every future outcome. Give it the conditions that made it true. Let the reader see the distance. Then ask the product to earn the rest.
