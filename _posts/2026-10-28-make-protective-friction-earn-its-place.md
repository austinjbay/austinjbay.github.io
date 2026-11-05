---
title: "Make protective friction earn its place"
subtitle: "Some steps slow a journey because the product is clumsy. Others give a person one last good chance to avoid an expensive mistake."
description: "A growth Product field note on protective friction, harm budgets, and testing when a slower path produces a healthier outcome."
date: 2026-10-28
image: /assets/images/notebook.jpg
layout: post
---

I once helped review a flow that made it impressively easy to invite an entire company into a new workspace.

The old version asked the administrator to choose groups, preview the recipient count, and confirm the invitation. The new version inferred the groups and put one bright button at the end. Completion went up. Time to invite fell. On the usual growth dashboard, the work was an uncomplicated win.

Then the support notes arrived.

One administrator had invited contractors who should not have seen the workspace. Another had sent a half-finished welcome to several hundred people. A third could not tell whether the button would notify everyone immediately. These were not frequent outcomes, but each one was expensive enough to change how the customer felt about the product.

We had treated every pause as waste. A few of those pauses had been doing a job.

Growth Product work rightly looks for friction. Extra fields, repeated decisions, and mysterious confirmations can drain intent from a journey. But friction is a description of effort, not a verdict on its value. A speed bump and a pothole both slow a car. Only one was put there on purpose.

The useful question is not whether a step adds effort. It is whether the effort is proportional to a mistake the step can actually prevent.

## A fast path can move risk onto the user

Consider a payroll product that lets an operator approve a payment file.

A second confirmation will lower the clean completion rate a little. It may also catch the wrong pay period, a surprising total, or an account that was included by mistake. Removing it makes the product faster when everything is right and much more consequential when something is wrong.

The same pattern appears in less dramatic places. Publishing a campaign can notify a large audience. Changing a workspace default can alter another person's routine. Deleting an integration can stop a downstream report. An AI action can rewrite a large set of records before anybody sees the first bad one.

In each case, the product team can book the immediate benefit of speed while the customer absorbs the tail risk.

This is one reason accessibility guidance treats error prevention as more than a nice confirmation pattern. The W3C guidance for [legal, financial, and data submissions](https://www.w3.org/WAI/WCAG22/Understanding/error-prevention-legal-financial-data.html) says that at least one safeguard should be available, such as reversibility, an error check, or a review and confirmation step. The important idea is not that every action deserves a modal. It is that consequential actions deserve a credible route for detecting or correcting mistakes.

Security teams make a related distinction. The current NIST guidance on [authentication assurance](https://pages.nist.gov/800-63-4/sp800-63b.html) sets different requirements for different assurance levels rather than treating every sign-in as equally risky. Product journeys can use the same judgment. The amount of interruption should follow the consequence and likelihood of error, not the team's preference for either safety or speed in the abstract.

Protective friction moves risk back into view before the commitment is made.

## Keep a friction warrant

I use a small artifact called a friction warrant. It forces a team to explain why a pause deserves to exist.

| Decision | User effort | Specific harm it can prevent | Evidence the check can detect it | Recovery if missed | Smallest adequate safeguard |
| --- | --- | --- | --- | --- | --- |
| Invite 640 people | Review audience and confirm | Unintended access and a premature announcement | Audience count and group names are visible before send | Revoke access and send a correction | Show recipient count, unusual groups, and send timing |
| Approve payroll | Recheck period, total, and funding account | Incorrect or duplicate payment | The product can compare the file with the prior run | Bank recall may be slow or impossible | Interrupt only on material changes or anomalies |
| Delete an integration | Read impact and type its name | Broken reports and silent data loss | The product knows active dependencies | Reconnection may not restore missing history | Show affected jobs and delay final deletion |

The warrant has to name a harm. “This feels safer” is not enough. Nor is “users might make a mistake.” What mistake, how often, how costly, and what could this particular step reveal before it happens?

It also has to explain the mechanism. A generic confirmation that repeats the button label rarely protects much. People learn to clear it. A useful safeguard presents information that can change the decision, such as the audience, total, scope, timing, or downstream effect.

Medical-device teams have learned this lesson under higher stakes. The FDA guidance on [human factors and usability engineering](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/applying-human-factors-and-usability-engineering-medical-devices) asks manufacturers to identify critical tasks where a use error could cause serious harm and to evaluate the interface around those tasks. A growth flow is not a medical device. The transferable habit is to start with the hazardous outcome, then work backward to the point where design can still change it.

Finally, the warrant asks for the smallest adequate safeguard. Sometimes that is a preview. Sometimes it is an anomaly warning, a short delay with undo, a permission check, or a second person for a truly consequential action. The answer should rarely be another paragraph of legal copy.

## Test protection without manufacturing harm

The naive experiment removes the safeguard for half of eligible users and compares completion. I would not do that when the suspected harm is severe or hard to reverse. An experiment does not become ethical merely because the sample is random.

Start with the decisions the existing step actually changes. Instrument the confirmation without changing it. Record whether people go back, alter the audience, fix an input, abandon the action, or ask someone else to review it. Sample those sessions and support cases. A step that nobody uses to inspect or correct anything may be ceremony. A step that catches a small number of expensive errors may be earning its place.

Then reduce the burden while preserving the protective mechanism. Replace a generic confirmation with a review that highlights unusual scope. Suppress the interruption for low-risk, familiar actions. Escalate it when the amount, audience, permissions, or departure from prior behavior crosses a sensible threshold.

Here is the hypothesis I would write for the invitation flow.

> We believe replacing the generic confirmation with a risk-triggered audience preview will reduce median time to invite while keeping unintended invitations per thousand sends no worse, because routine invitations will proceed directly and unusually broad invitations will expose the information needed to catch a mistake.

I would compare the current confirmation with the risk-triggered version among actions that are reversible and below a pre-agreed harm ceiling. The primary product outcome is a successful invitation that remains in place after seven days. The protection measure is unintended invitations, using rapid revocation, recipient removal, and tagged support contacts as imperfect but inspectable evidence. Time and abandonment tell us what burden we removed.

Before launch, set a harm budget. Decide how much deterioration in the protection measure would stop the test even if completion improves. For rare, serious outcomes, historical simulations and staged exposure may be more honest than waiting for a conventional significance threshold. Run old events through the proposed trigger. Ask which known mistakes it would have caught and which normal actions it would have interrupted.

This is closer to testing a smoke alarm than a headline. You care about detection, false alarms, and the cost of a miss. Click-through alone cannot settle the decision.

## Protection can become theater

Not every slow step is secretly wise.

Teams sometimes give inherited friction a noble story after the fact. A required phone call is called fraud prevention even though nobody can name the fraud signal it reveals. A destructive-action modal says “Are you sure?” without showing what will be destroyed. An approval queue protects an internal hierarchy rather than the customer. A warning appears so often that it becomes a reflex test.

Those steps do not deserve preservation. They need evidence or removal.

Protective friction can also be distributed unfairly. A risk system may challenge people using new devices, assistive technology, shared networks, or unfamiliar names more often than everyone else. Aggregate conversion can look acceptable while one group repeatedly pays the safety tax. Review trigger rates, completion, and false alarms across relevant access patterns before calling a risk-based path smarter.

There is a failure mode in the other direction too. A team can make the warning beautifully specific while leaving recovery terrible. If an accidental send can be recalled for thirty seconds, the undo may protect better than a long preview. If a payment cannot be reversed, prevention deserves more weight. The shape of recovery changes how much friction is justified before the action.

## The judgment is about who carries the downside

The hard call for a growth PM is not whether to favor conversion or safety. It is where the product should interrupt, for whom, and with what evidence.

I would keep friction when the harm is meaningful, the step can reveal information that changes the decision, and recovery is weak. I would narrow it when risk is concentrated in recognizable conditions. I would remove it when the team cannot show a mechanism, a changed decision, or a prevented outcome.

That judgment will sometimes cost a small amount of immediate completion. It can also make a product easier to trust with larger audiences, higher-value actions, and more autonomy. The person who knows the product will catch an unusual scope can move faster the rest of the time.

Growth teams are often the people with the energy and instrumentation to remove a step. That gives us a responsibility to understand what the step was carrying first.

A pothole should be fixed.

A speed bump should still have to prove that this is the right road, the right height, and the right place.
