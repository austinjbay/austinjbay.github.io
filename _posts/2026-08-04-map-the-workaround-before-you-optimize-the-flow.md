---
title: "Map the workaround before you optimize the flow"
subtitle: "Why growth teams should study the unofficial ritual that already helps the user get the job done."
description: "A growth PM field note on using a workaround map to spot the spreadsheets, side notes, handoffs, and safety checks users rely on before a polished funnel quietly breaks them."
date: 2026-08-04
image: /assets/images/notebook.jpg
layout: post
---

I think a lot of growth teams are too eager to replace a workflow they have not actually understood.

We see a spreadsheet and call it messy.

We see a Slack ritual and call it manual.

We see a copy paste loop and call it inefficient.

We see a sticky note on a monitor and call it a patch.

Sometimes those labels are true.

Sometimes they are lazy.

A lot of unofficial workflow is not random clutter.

It is a survival strategy.

The user found a way to keep the job moving inside a system that does not fully cooperate yet.

That matters because growth product work often shows up right at the moment a team tries to formalize or accelerate that job.

Launch the self serve flow.

Add the onboarding checklist.

Automate the follow up.

Ship the import wizard.

Prompt the team invite.

Send the reactivation campaign.

The product team is proud because the journey now looks cleaner on the whiteboard.

Then adoption gets weird.

Users start the flow but do not finish it.

Invites go out but team usage stays shallow.

Imports happen but the new workspace still feels fragile.

Lifecycle clicks appear while real habit does not.

The team calls it friction.

Sometimes it is something more specific.

The polished flow accidentally removed a workaround that had been doing real product work.

## Workarounds are often where the product’s missing safety lives

I think this is one of the easiest growth mistakes to make when you are staring at a funnel all day.

Funnels flatten intent.

They flatten hesitation.

They flatten the side conversations and confidence checks that happen before a user takes the next step.

The user does not experience the journey that way.

They experience a whole problem.

That is why I still like the GOV.UK guidance on [mapping a user’s whole problem](https://www.gov.uk/service-manual/design/map-a-users-whole-problem). It is a useful reminder that the thing you are redesigning is usually only one slice of a broader task the user is trying to complete.

Inside that broader task, workarounds carry a lot of weight.

The spreadsheet might be the only place the team can see status clearly.

The Slack message might be the social cue that makes an invite feel safe to send.

The manual export might be the user’s proof that the new system will not trap their data.

The copied template might be the only version of the workflow that new teammates can actually understand.

From the outside, each of these can look like avoidable mess.

From the inside, they can be the user’s safety rail.

If you remove the rail before the product can carry the same load, the experience does not become cleaner.

It becomes riskier.

## Complex systems keep running because people keep patching the gaps

This is one reason I come back to Richard Cook’s short essay [How Complex Systems Fail](https://how.complexsystems.fail/). It is about high stakes systems, not SaaS onboarding, but the idea travels well. Complex systems keep working because people adapt around their flaws in real time.

That is not only a hospital or aviation story.

It is also a product story.

The operations lead keeps a side list because the CRM does not make handoff status legible enough.

The teacher exports a roster every Friday because the grade sync is technically live but not yet trusted.

The recruiter sends a calendar note after the automated email because candidates miss the real answer if it only lives in the tool.

The growth marketer tags accounts by hand because the lifecycle rules cannot yet distinguish curiosity from buying intent.

These are not elegant behaviors.

They are adaptive behaviors.

They are what people do when the official system does not fully protect the work.

I think teams get into trouble when they interpret every workaround as evidence that users are behind the times.

Sometimes the opposite is true.

The user may be more realistic about the job than the product is.

They know where the edge cases are.

They know which teammate still needs a nudge.

They know which record cannot be trusted yet.

They know where cleanup really starts.

If you only study the designed path, you miss the compensating behavior that makes the job viable at all.

## Automation can increase toil when it removes the wrong manual step

This is where a lot of growth work becomes quietly expensive.

The team automates a visible manual task and assumes the total effort went down.

Sometimes the effort just moved.

Google’s SRE book has a durable definition of [toil](https://sre.google/sre-book/eliminating-toil/) as work that is manual, repetitive, and without enduring value.

That framing is helpful here because not all manual work is equally dumb.

Some manual work is pure waste.

Some manual work is a temporary inspection layer that protects quality, trust, or recoverability while the system is still maturing.

If a product removes the visible task but leaves the underlying uncertainty intact, the user invents a new form of toil somewhere else.

Now the import is automatic, but the user keeps a shadow sheet to verify what landed.

Now the invite sequence is automated, but the manager still sends personal reassurance because the first time setup feels too abrupt.

Now the lifecycle campaign triggers perfectly, but support inherits the confused replies because the event model cannot tell blocked users from idle ones.

The product looks more automated.

The service got more exhausting.

That is a bad trade, even if the local conversion step improves for a week.

## A lot of workaround value is backstage

One reason this problem survives is that the useful part of a workaround is often invisible to the team redesigning the experience.

The visible part might be a spreadsheet.

The real value might be that the spreadsheet creates a shared review moment between two teammates.

The visible part might be an exported CSV.

The real value might be that the export gives the buyer a feeling of reversibility before they commit the team.

The visible part might be a follow up Slack message.

The real value might be that it lets the sender translate the generic product state into language the recipient actually understands.

That is why service blueprints are still useful beyond classic service design projects. NN group’s piece on [service blueprints](https://www.nngroup.com/articles/service-blueprints-definition/) is a good reminder that user journeys sit on top of frontstage and backstage work, dependencies, and evidence.

When growth teams skip that view, we treat the user facing touchpoint as the whole product.

It almost never is.

A self serve motion may still rely on an operator reviewing data quality.

A supposedly simple invite flow may still depend on a manager pre-selling the value in another channel.

A new activation step may still need an analyst to sanity check the output before anyone believes it.

That does not mean the product failed.

It does mean the product is not yet what the funnel claims.

## The artifact I like is a workaround map

When a team says users have an ugly manual process and we should automate it, I like slowing the room down with a workaround map.

Not a giant research deck.

Just a one pager that asks what the unofficial workflow is doing for the user right now.

## Workaround map

- Official flow we want the user to adopt
- Existing workaround the user relies on today
- What problem the workaround solves
- What uncertainty or risk it reduces
- What backstage dependency it compensates for
- What evidence it gives the user that the job is still safe
- What new failure we create if we remove it too early
- What product behavior would need to exist before the workaround can disappear
- What smaller migration step would let us earn that replacement gradually

I like this artifact because it changes the tone of the conversation.

The team stops mocking the current behavior and starts learning from it.

You begin to ask better questions.

Why does the customer success team export the account list before triggering the campaign.

Why does the user keep inviting one teammate manually before they trust the bulk invite.

Why does the analyst compare two dashboards before they believe the activation number.

Why does the buyer wait to import historical data until after one narrow use case works.

Those are not anti automation questions.

They are sequencing questions.

They help you tell the difference between waste and protection.

## Good growth work replaces the function of the workaround, not just the shape

This is the part I think matters most.

A product rarely wins by making the workaround impossible.

It wins by making the workaround unnecessary.

That is a higher bar.

If the workaround gave the user confidence, the product has to create confidence.

If the workaround created a shared review step, the product has to create a shared review step.

If the workaround preserved reversibility, the product has to preserve reversibility.

If the workaround translated product language into job language, the product has to do that translation itself.

Otherwise you have not truly replaced anything.

You have just confiscated a user owned defense.

I think this is why some polished launches underperform despite looking obviously better to the team that shipped them.

The interface improved.

The lived safety model regressed.

Users feel that faster than the dashboard does.

They hesitate a little longer.

They wait for a teammate.

They keep the old system alive in parallel.

They complete the flow but do not change their real habit.

That is one reason a rollout can look fine in starts and weak in retained usage.

The team measured adoption of the new surface.

The user was still testing whether the new surface deserved to become the real workflow.

## What I would do in practice

If I were working this with a team, I would pick one high intent journey where adoption feels softer than expected.

Maybe the first import.

Maybe the first invite.

Maybe the first campaign launch.

Maybe the first workflow handed from evaluator to everyday user.

Then I would talk to users and internal operators with one goal.

Find the unofficial moves that keep the journey safe today.

Not just the clicks inside the product.

The side note.

The exported file.

The calendar hold.

The preflight Slack message.

The manager review.

The screenshot saved for later.

The duplicate system they keep open during the transition.

Then I would map what each of those moves is really doing.

Usually the answer falls into a few categories.

- preserving confidence
- creating shared understanding
- reducing cleanup risk
- making status visible
- keeping a retreat path open
- translating the workflow into the user’s actual job

Only after that would I decide what to automate, what to stage, what to expose more clearly, and what to leave alone for now.

That order matters.

If you start with the designed flow, you optimize the diagram.

If you start with the workaround, you learn what the job has been demanding all along.

## A simple gut check

When you find a manual ritual around your product, ask a harder question than how do we remove this.

Ask what danger, ambiguity, or missing capability this ritual is absorbing for the user today.

If you do not have a good answer, the workaround is probably smarter than the flow you are trying to replace.
