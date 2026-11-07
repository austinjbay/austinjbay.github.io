---
title: "Design the reconciliation before the records disagree"
subtitle: "Shared products grow into systems of record, and systems of record eventually tell different stories."
description: "A growth Product field note on reconciliation briefs, shared truth, and testing how teams recover when records diverge."
date: 2026-10-26
image: /assets/images/notebook.jpg
layout: post
---

The first version of collaboration usually feels wonderfully simple.

One person imports a customer list. Another connects the billing system. A third edits an account owner in the product. The team invites more people because the workspace is finally useful enough to share.

Then Monday morning arrives with three answers to an ordinary question.

The CRM says Priya owns the account. The billing export says Marco. The workspace says nobody does. Each answer made sense when it was written. None is obviously the one the team should keep.

This is where a growth story can quietly become an operations story. More integrations, contributors, and recurring workflows create more ways for reasonable records to disagree. The product may detect the mismatch, but detection is not reconciliation. Someone still needs to understand what changed, decide what should survive, and leave the shared state coherent.

I have seen teams treat that moment as an edge case to hide behind an error banner. I think it belongs much closer to the center of collaborative product design.

If a product asks a team to build shared truth inside it, the product should also help that team repair shared truth when it splits.

## Agreement is a product capability

Many products look like a single surface while sitting between several legitimate sources.

A commerce platform has an order, a payment provider has a charge, and a warehouse has a shipment. A planning tool has a due date while the calendar has another. An AI workspace has the uploaded source, a generated answer, and a later correction from a teammate.

The naive design question is which system wins. The more useful question is what evidence a person needs to resolve this particular disagreement.

That distinction matters because recency is not authority. The latest edit may be an intentional correction, an old system finishing a delayed sync, or a bulk import overwriting careful work. Silently choosing the newest value can make the interface look calm while making the underlying work less trustworthy.

Database systems are explicit about this problem. PostgreSQL uses [multiversion concurrency control](https://www.postgresql.org/docs/current/mvcc-intro.html) so each statement works from a consistent snapshot while concurrent changes occur. That machinery does not tell a product team which account owner is correct. It does make an important principle visible. Multiple versions are a normal condition to manage, not evidence that somebody behaved badly.

Git is similarly candid. When two branches change the same area, [Git preserves both sides and asks for a resolution](https://git-scm.com/docs/git-merge#_how_conflicts_are_presented) rather than randomly selecting one. Most customers should never see conflict markers, but the underlying posture is worth borrowing. Preserve the competing claims long enough for the right person to make an informed choice.

## Reconciliation is different from correction

A correction assumes we know the current value is wrong.

Reconciliation begins before that confidence exists. It asks how the records differ, where each came from, whether they describe the same thing, and who can settle the difference.

Medicine treats this as real work at a transition. The Centers for Medicare and Medicaid Services defines [medication reconciliation](https://www.cms.gov/Regulations-and-Guidance/Legislation/EHRIncentivePrograms/downloads/Stage2_HospitalCore_11_MedicationReconciliation.pdf) as identifying the most accurate medication list by comparing the medical record with a list obtained from a patient, hospital, or other provider. The point is not to assume the hospital list or the external list is automatically right. The comparison is the work.

Product teams often compress that work into a modal with two unlabeled values and a button that says resolve. That is technically a choice and practically a scavenger hunt.

A good reconciliation experience should answer a few plain questions.

- What is different
- Where did each version come from
- When and how was each version changed
- What else will change after this choice
- Who can make the call when the evidence is not enough

This is not only a reliability concern. It affects whether a growing team is willing to connect another source, invite another operator, or move another recurring process into the product.

## Keep a reconciliation brief

The artifact I would use is a reconciliation brief. It is a small design document for one shared object that can receive competing updates.

| Decision | What to write down |
| --- | --- |
| Shared object | The customer, order, schedule, document, or other thing people believe they share |
| Competing claims | The values that can disagree without either source being obviously broken |
| Evidence shown | Source, author, timestamp, change method, and relevant surrounding state |
| Safe automatic cases | The differences the product can combine or discard without interpretation |
| Human decision | The differences that require context, authority, or a conversation |
| Consequence preview | The records, automations, and teammates affected by the choice |
| Resolution owner | The person or role who can settle an ambiguous case |
| Durable trace | What the next person can inspect to understand the decision |

For the account owner example, an exact duplicate can be combined automatically. An empty local value can accept a named CRM owner when the workspace has explicitly designated the CRM for that field. Two different named owners should probably remain visible until someone with account context decides.

The brief should also name what happens after resolution. Does the chosen owner write back to the CRM. Will the next scheduled import reverse the decision. Does reassignment trigger a territory workflow. A choice that immediately gets undone is not a resolution. It is a loop with nicer copy.

I would make one brief for a high-consequence object, not a universal policy for every field. Product catalogs, team calendars, and customer records fail differently. The useful level is close enough to the work that the evidence and consequence are concrete.

## Test a disagreement rather than a happy sync

Integration tests often prove that matching records travel successfully. That is necessary and oddly comforting. It is not the hard product claim.

The hard claim is that a team can recover when two reasonable sources diverge.

I would run a task-based experiment with teams that already manage account assignments across a CRM and the product. Seed a realistic disagreement in a sandbox. One source shows the original owner. The other shows a reassignment made later through a bulk operation. Give both groups the same underlying history.

The current experience shows the two values and a generic resolution control. The proposed experience shows the source, actor, time, change method, consequence preview, and a path to send the case to the designated owner.

Here is the falsifiable hypothesis.

> We believe teams using the evidence-rich reconciliation flow will choose the intended owner in at least eighty percent of seeded cases, compared with no more than sixty percent in the current flow, and will leave fewer than ten percent of cases unresolved after one business day.

The intended answer should be established in the scenario before the test, not inferred from whatever participants click. I would also ask each participant to explain the choice in one sentence. That helps distinguish a reasoned resolution from a lucky selection.

If accuracy improves but nearly every case gets escalated, the evidence may still be inadequate. If people resolve quickly and the next import reverses their work, the write-back policy is broken. If both groups struggle, the team may not share a real rule for ownership yet. The product has surfaced an operating ambiguity rather than an interface problem.

That is still useful learning.

## Shared truth needs a repair path

Growth teams naturally celebrate the moment another source is connected or another teammate joins. Those are visible expansions of the product's reach.

The less glamorous work begins when those additions bring their own histories, update rhythms, and legitimate claims. A mature shared product cannot promise that records will never diverge. It can promise not to erase the disagreement before people understand it.

This changes how I think about collaboration. The job is not only to help several people act on the same object. It is to help them restore a common object after their actions no longer line up.

The reconciliation brief makes that repair work designable. It names the evidence, the automatic cases, the human judgment, the downstream consequence, and the person who can close the question.

That may feel operational for a growth team. In practice, it is often what lets the next integration, teammate, and workflow arrive without making the product more fragile.

Shared truth is not a state a product reaches once.

It is a state the product must know how to rebuild.
