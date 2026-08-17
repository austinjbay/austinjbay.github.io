---
title: "Write the provenance note before you ship the advice"
subtitle: "Why growth teams should record where a recommendation, prompt, score, or default came from before asking users to trust it."
description: "A growth PM field note on provenance, trust, and a simple working note that helps teams explain why the product is making a suggestion in the first place."
date: 2026-08-17
image: /assets/images/notebook.jpg
layout: post
---

I think a lot of growth products now have an advice layer whether they mean to or not.

The product recommends the next step.

The onboarding picks the setup path.

The lifecycle system chooses the nudge.

The AI assistant drafts the reply.

The dashboard highlights the account that needs attention.

The template gallery sorts a few starting points to the top.

Sometimes none of that is presented as a dramatic prediction system.

It just shows up as a suggestion, a default, a rank, a prefilled sentence, or a quiet little label that says recommended.

That can feel lightweight from the team side.

It does not feel lightweight from the user side.

Advice changes behavior.

Advice changes what gets ignored.

Advice changes what people think the product knows.

Once a product starts steering, I think it owes the user and the team a better answer to one basic question.

Where did this advice come from.

## Good advice needs a visible backstory

I do not mean every product needs a long explanation panel.

I mean the team should be able to point to the source of the suggestion with some precision.

Was this next step based on behavior from similar accounts.

Was it based on firm setup rules from operations.

Was it based on an experiment that only held for new teams under a certain size.

Was it generated from the user’s own prior actions.

Was it written by AI with a prompt assembled from account metadata and help center text.

Was it inherited from a sales playbook that nobody has revisited in a year.

That trail matters more than a lot of teams admit.

NIST’s glossary definition of [provenance](https://csrc.nist.gov/glossary/term/provenance) is broad on purpose. It is about the chronology of origin, development, ownership, location, and changes. That is not only a security or data lineage idea. I think it is a very useful product idea.

If a product is going to make a recommendation, the team should know the origin and changes behind that recommendation well enough to explain it, challenge it, and retire it when the context shifts.

Without that, recommendation surfaces start behaving like folklore.

Everyone uses them.

Nobody can quite explain why they deserve to exist.

## Other fields already know that trust improves when history stays attached

This is one reason I have been paying attention to provenance work in media.

The C2PA overview of [Content Credentials and provenance](https://c2pa.org/specifications/specifications/2.2/explainer/Explainer.html) is about digital media authenticity, not onboarding or lifecycle design. The transferable lesson is still strong. When people are asked to trust what they are seeing, origin and modification history matter.

I think products need a humbler version of that idea.

Not cryptographic proof for every tooltip.

Just enough history attached to important guidance that the system does not pretend its recommendations emerged from pure wisdom.

The same pattern shows up in software architecture.

Martin Fowler’s note on [Architecture Decision Records](https://martinfowler.com/bliki/ArchitectureDecisionRecord.html) is useful because it treats decisions as things that deserve a short durable backstory. What was decided. Why. What tradeoffs mattered. What would cause a revisit.

That is close to what many growth systems lack.

A recommendation rule gets added.

A setup default gets introduced.

A lifecycle branch gets copied from an older campaign.

A score threshold gets tuned during a launch week.

Months later the product is still steering users with logic that nobody has re-examined.

The recommendation may still work.

It may also be surviving on status, not merit.

## Growth products accumulate invisible advice debt

I think of this as advice debt.

Not bad advice exactly.

Unexplained advice that keeps operating after its evidence, audience, or owner has become fuzzy.

That debt shows up in a few familiar ways.

The product recommends a checklist step because it once correlated with activation, but nobody remembers that the result came from a narrow self-serve segment.

The sales assist panel pushes a playbook because one strong operator used it well, but the team never separated expert behavior from general behavior.

The AI draft sounds oddly confident because the prompt was built around support articles that assume ideal inputs.

The onboarding path keeps steering admins toward a teammate invite too early because the experiment win came from a period when traffic quality looked different.

The user sees a simple recommendation.

The team is actually looking at layers of sediment.

This is where NIST’s [Four Principles of Explainable Artificial Intelligence](https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence) feels relevant even outside explicit AI products. Trust goes up when people can understand the basis of a system’s output well enough to use appropriate judgment.

I do not think every product surface needs full explainability.

I do think more growth surfaces need enough explainability to prevent blind obedience.

## Provenance is useful even when the recommendation is simple

Sometimes teams hear provenance and think the system must be fancy.

I think the opposite is often true.

The simpler the recommendation looks, the easier it is for weak logic to hide inside it.

Recommended template.

Best next action.

Suggested teammate.

Top workflow.

Priority account.

Start here.

Those labels are powerful because they compress uncertainty into a clean instruction.

That is often good design.

It is also why the team should keep a record of what the instruction is resting on.

GOV.UK’s guidance on [how service assessments work](https://www.gov.uk/service-manual/service-assessments/how-service-assessments-work) makes a point I like very much. Do not only show the happy path. Show what happens when the journey gets messy, when evidence is missing, or when the ideal case breaks.

That is a strong standard for recommendation systems too.

When you review a product’s advice layer, do not only inspect the persuasive case where the suggestion looks smart.

Inspect the source material.

Inspect the assumptions.

Inspect the segment boundaries.

Inspect the stale cases.

Inspect the moments where the system is guessing from thin evidence.

A provenance note is one way to make that review possible.

## The artifact I like is a provenance note

This is not a giant governance framework.

It is a small working note attached to any product advice that meaningfully steers user behavior.

One recommendation surface can have one note.

One important default can have one note.

One ranking model, AI draft pattern, or lifecycle rule can have one note.

The note is not there to satisfy compliance theater.

It is there so the team can answer a practical question before shipping or scaling the advice.

Do we understand where this came from well enough to trust how it is being used.

## Provenance note

- Recommendation or advice surface
- User decision or behavior it is trying to influence
- Origin of the logic or content
- Inputs it relies on
- Segment or context where it is expected to hold
- Evidence that originally justified it
- Known weak spots or cases where confidence drops
- What changed most recently and why
- Review date
- Owner

This gets useful fast.

You find recommendation rules with no living owner.

You find AI prompts that quietly rely on stale docs.

You find onboarding defaults that only make sense for a traffic mix you no longer have.

You find rankings that were tuned around reporting convenience instead of user comprehension.

Most importantly, you find advice that sounds more certain than its lineage deserves.

## The note helps the team before it helps the interface

The obvious use is internal.

It makes reviews sharper.

It makes experimentation cleaner.

It makes it easier to retire old logic without turning every debate into archaeology.

I also think it changes how teams write the interface itself.

Once you have a provenance note, you start noticing when the UI is overstating certainty.

Maybe the product should say based on your recent setup instead of best next step.

Maybe the lifecycle system should ask a question before it gives a command.

Maybe the AI draft should signal the sources it used.

Maybe the dashboard should show why an account was flagged instead of only that it was flagged.

Maybe the recommendation should disappear entirely in the cases where the note says confidence is weak.

That is not only a copy improvement.

It is better product judgment.

The interface becomes more proportionate to the strength of the underlying evidence.

## This matters even more in mid-journey growth work

I think early funnel work gets most of the scrutiny because the surfaces are public.

Landing pages get reviewed.

Signup flows get replayed.

Onboarding gets measured.

Advice debt often builds later in the journey.

Inside the account.

Inside the sales handoff.

Inside the customer success prompt.

Inside the admin dashboard.

Inside the assistant panel where the product is quietly shaping what a human operator does next.

Those systems are powerful because they feel operational rather than promotional.

They still deserve the same discipline.

If a growth PM is using product guidance to steer setup, retention, resurrection, monetization, or expansion, that guidance should have a visible lineage.

Otherwise the product starts compounding decisions that no one would defend fresh today.

## A provenance note protects against two opposite failures

The first failure is blind trust.

The team assumes the recommendation is smart because it looks polished and keeps shipping around it.

The second failure is blanket skepticism.

Nobody trusts the recommendation layer, so every operator learns to ignore it.

Both outcomes are expensive.

One creates silent product drift.

The other creates feature theater.

A provenance note gives the team a middle ground.

This advice exists for a reason.

Here is the reason.

Here is the evidence.

Here is where it stops being reliable.

Here is who has to revisit it.

That is a much healthier operating posture than treating product advice as either magic or nonsense.

## The point is not to make the product sound cautious

I am not arguing that every recommendation should arrive wrapped in disclaimers.

Sometimes the right interface is still simple and direct.

Invite your teammate.

Connect your calendar.

Review this draft.

Start with this template.

The point is that the team should earn that simplicity.

Clear advice is good.

Unaccountable advice is not.

That distinction matters more as products absorb AI, automation, lifecycle orchestration, and more embedded recommendations across the journey.

The richer the advice layer gets, the more important it becomes to keep a note beside it that says where this came from and why we still believe it.

That is what keeps a useful recommendation from hardening into inherited product superstition.
