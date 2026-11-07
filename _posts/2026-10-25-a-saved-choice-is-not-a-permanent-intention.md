---
title: "A saved choice is not a permanent intention"
subtitle: "Products remember settings perfectly and can still forget what the user meant."
description: "A growth Product field note on intent freshness, revalidation, and knowing when a past choice is safe to reuse."
date: 2026-10-25
image: /assets/images/notebook.jpg
layout: post
---

I once worked on a product that got very good at remembering what people wanted.

During setup, a customer chose a weekly report, picked the recipients, and selected the projects to include. The product saved those choices and did the considerate thing. It stopped asking. Every Friday, it produced exactly what had been requested.

Months later, the open rate had fallen and several reports were being forwarded to different people. We initially treated this as a delivery problem. We tried better subject lines and a different send time.

The simpler explanation was that the product was faithfully repeating an old instruction. Teams had changed. Projects had ended. The report still worked, but the intention behind it had gone stale.

Growth teams usually celebrate remembered choices. Defaults reduce effort. Saved filters make a return visit faster. Automations turn one decision into repeated value. All of that is real.

The mistake is treating memory as evidence that the choice is still current.

A product can remember the user's words and lose the user's meaning.

## Convenience can outlive intent

Some choices age slowly. A preferred language may remain useful for years. Other choices can become wrong before the next session. The teammate who should approve an invoice, the audience for a campaign, and the project that belongs in a weekly digest all depend on circumstances outside the interface.

The product rarely sees the moment those circumstances change.

That creates an attractive measurement error. The automation keeps running, so recurring usage looks healthy. Messages are sent. Reports are generated. Rules fire. A dashboard can count all of it as retained behavior even when people have begun routing around the result.

I have learned to be suspicious when a product can manufacture activity from a decision the user made once. The activity may be valuable. It may also be the mechanical echo of a choice nobody would make today.

This is different from asking whether an automation produces an output. It is a question about whether the product still has a valid instruction to produce that particular output for this particular situation.

It is also different from revisiting a growth lesson after the market changes. That work asks whether the team should still believe an old result. This work asks whether the product should still act on one person's old instruction. The owner, evidence, and consequence are different.

Software infrastructure already makes this distinction. The HTTP caching standard describes a stored response as fresh only while it can be reused without checking the origin. Once it is not fresh, the cache may need validation before reuse. The standard is about network responses, not people, but the discipline travels well. Reuse needs a condition, not just a memory. The [IETF specification for HTTP caching](https://www.rfc-editor.org/rfc/rfc9111.html) makes freshness, validation, and invalidation separate parts of the system.

Products are usually less careful with intent. We save the selection but not the conditions that made the selection sensible.

## A choice has a situation attached

Consider a hiring product that asks a manager to save an interview scorecard for future roles.

Reusing it next week for another opening on the same team may remove busywork. Reusing it eighteen months later for a different level can quietly turn convenience into policy. The manager sees a familiar template and assumes someone has kept it current. The product sees a saved object and assumes the manager still endorses it.

Neither assumption has been tested.

Medicine offers a much higher-stakes version of the same distinction. An advance decision can record a person's wishes for circumstances in which they cannot communicate them. NHS guidance explains that such a decision must still be valid and applicable to the situation, and that later words or actions can contradict it. The point is not that product settings resemble medical decisions in consequence. They plainly do not. The useful connection is that a recorded preference and a present preference are not automatically the same thing. Context determines whether the old instruction applies. The [NHS guidance on advance decisions](https://www.nhs.uk/tests-and-treatments/end-of-life-care/planning-ahead/advance-decision-to-refuse-treatment/) is explicit about that boundary.

We encounter a gentler version in a home kitchen. A label saying bake for thirty minutes preserves an instruction. It does not preserve the oven, the pan, the altitude, or the size of the dish. An experienced cook treats the time as a prior decision to inspect, not a command that overrides present evidence.

Good products should be able to do the same.

## Keep an intent freshness register

The artifact I use is an intent freshness register. It is a small table for choices the product plans to reuse without asking again.

| Saved choice | Situation at capture | What could make it stale | Evidence still available | Revalidation rule | Safe fallback |
| --- | --- | --- | --- | --- | --- |
| Weekly project report | Active launch with six named owners | Project closes or ownership changes | Recipient opens, forwards, and project activity | Ask after two low-use sends or an owner change | Pause and keep a draft |
| Interview scorecard | Same team and role level | Level, manager, or hiring plan changes | Recent edits and use on comparable roles | Confirm when role level or manager differs | Start from a copy marked for review |
| Campaign audience | Consent and segment rules at launch | Eligibility or communication purpose changes | Current eligibility check | Recompute before every send | Exclude uncertain records |
| Approval route | Finance lead owns this cost center | Reorganization or leave changes authority | Directory and recent approval behavior | Confirm after an owner change or repeated reassignment | Route to manual review |

The register forces five useful decisions.

- Record why the choice was reasonable when it was made
- Name the external change that could invalidate it
- Decide which behavior is evidence of continued fit
- Set a condition for checking again
- Choose what the product does when confidence is low

The last column matters. Revalidation should not become a modal that blocks every return visit. A safe fallback might pause a send, create a reviewable draft, or make a copy instead of overwriting the old object.

I do not give every setting an arbitrary expiration date. That only replaces one careless default with another. The rule should follow the volatility and consequence of the choice.

A theme preference has low consequence and obvious correction. Keep using it. An approval route can move money or delay work for several people. Check it when the organization changes. A campaign audience can create legal and reputational harm. Recompute eligibility at the moment of use rather than trusting a saved list.

Freshness is not just elapsed time. It is the relationship between the old situation and the current one.

## Look for stale intent before adding prompts

Start with evidence already produced by the workflow.

For a scheduled report, inspect forwarding, recipient removal, immediate deletion, manual reruns with different filters, and edits made after generation. For an approval rule, inspect reassignment, escalation, and time spent waiting on people who no longer own the decision. For a saved audience, compare the saved membership with current eligibility at send time.

None of these behaviors proves that intent is stale. A forwarded report may be useful. A reassigned approval may cover a holiday. Treat them as candidates for review, not verdicts.

Then talk to people near the mismatch. Ask what they believed the product would remember, what changed outside it, and how they currently repair the result. I would rather hear about five real repairs than invent twenty clever freshness scores from event data.

The most important measurement choice is the unit of reuse. Counting generated reports will flatter the automation. Count reports that reach a currently relevant audience and prompt useful follow-up. Counting rules fired will do the same. Count decisions completed without reassignment or correction.

This changes the growth question from whether the product repeated the behavior to whether the repeated behavior still served the job.

## Test revalidation at the point of doubt

Do not ask everyone to reconfirm everything on a calendar. That creates ceremonial clicking and teaches people to dismiss the question.

Use the register to identify a meaningful change signal. For the weekly report, that might be two consecutive sends with no recipient engagement plus a material change in project membership. Randomly assign eligible reports to the existing behavior or a lightweight review.

The review should show the stored choice and the reason it was flagged. Let the owner keep it, change it, or pause it from the same surface. Keep the report content and delivery schedule otherwise unchanged.

Here is the hypothesis I would use.

> We believe asking report owners to review recipients after two low-use sends and a material membership change will increase the share of scheduled reports that are opened by a current project member and lead to a project action within four weeks, because owners can repair stale delivery intent, while the share of active reports that are paused and restarted within seven days will not rise by more than five percentage points.

The primary outcome is useful delivery to a current member followed by a relevant action. The restart measure protects against prompts that create mistaken pauses. I would also measure recipient edits, forwards, owner dismissals, and reports deleted shortly after review.

Analyze the reports that qualified for review, including owners who ignored the prompt. Otherwise the team will measure only the people willing to tidy their settings.

Run the test long enough to observe several scheduled uses. A same-session confirmation rate tells you that people can click a button. It does not tell you that the repaired choice survived another real week of work.

The experiment can falsify the idea cleanly. If flagged reports are already reaching the right people, or if review produces no durable changes, the trigger is weak and should be removed. If owners change recipients but the report still produces no useful action, freshness was not the main problem. The report itself may not deserve to exist.

## Apply this where change is hidden and consequential

Intent freshness work is useful when the product acts later, acts repeatedly, or acts on behalf of someone who may not be present. Scheduled communication, permissions, approvals, saved audiences, recommendations, and reusable templates are good candidates.

It is less useful for low-consequence preferences that are easy to notice and reverse. Do not interrupt someone every month to ask whether they still prefer dark mode. Do not add review machinery when the current situation is already checked at the moment of action. Do not use freshness language to turn a clear consent requirement into a product judgment.

It also does not excuse bad defaults. If most people correct a saved choice immediately, the capture experience may be wrong. If nobody can explain why a rule exists, revalidation will not give it meaning.

The judgment is whether silent reuse creates more value than silent drift creates harm.

## Remember the reason, not only the answer

Saving a choice is one of the quiet ways a product becomes easier to live with. People should not have to reconstruct every preference on every visit.

But durable convenience requires a little humility. Teams change. Projects end. Responsibilities move. A person can make a sound choice in April that becomes a poor instruction in October without anyone having made a mistake.

Mid-career Product work has made me less interested in whether a product can remember and more interested in whether it knows when memory is no longer enough.

Keep the setting. Keep the situation that justified it. Watch for evidence that the two have separated. Then revalidate at the point where doubt becomes meaningful.

A saved choice is useful memory.

It is not permanent permission to stop paying attention.
