---
title: "Decide when you will look before the result gets loud"
subtitle: "A fixed-horizon experiment changes when the team keeps checking and stops at the most exciting chart."
description: "A practical experiment decision cadence for planning reviews, stopping rules, harm overrides, and continuous monitoring before a growth test begins."
date: 2026-11-20
image: /assets/images/notebook.jpg
layout: post
---

There is a familiar moment in a growth experiment.

The test has been live for three days. Someone posts a screenshot showing the treatment ahead. The result looks convincing enough to feel like news. A leader asks whether we really need to wait another week.

Sometimes the chart falls back by the planned end date. Sometimes it crosses the line again. Sometimes the team ships while the result is flattering and never learns which ending it would have reached.

I understand the temptation. Waiting can feel bureaucratic when customers are arriving every minute and the dashboard already has an opinion.

But a fixed-horizon experiment makes a particular promise. We will collect the amount of information we planned, then use the result to decide. Checking repeatedly and stopping when the chart becomes exciting is a different decision rule. The dashboard still displays the familiar confidence interval or probability, so the change can be almost invisible.

We did not merely see the answer early. We gave noise more chances to audition as an answer.

The practical fix is not to hide the dashboard. It is to decide before launch when the team will look, what each look can change, and which problems are important enough to interrupt the plan.

## A calendar can be part of the method

Imagine a planning product testing a new invitation step after someone creates a first project. The primary outcome is whether an account completes meaningful collaborative work within fourteen days.

On the first morning, invitations rise sharply. On the third day, collaborative work looks positive. On the fifth day, the interval around the effect narrows just enough to exclude no change. The team stops the test and announces a winner.

There are at least two problems hiding in that tidy story.

The first is statistical. If the analysis was designed for one final look, every unplanned chance to stop on a favorable result makes the original threshold less meaningful. Microsoft’s experimentation team says that repeated measurement requires methods that account for early peeking and multiple testing. In the absence of highly certain movement, it recommends running to the predetermined duration. [Its during-experiment guidance separates early safety checks from an ordinary final decision](https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-during-experiment-stage/).

The second is a product problem. Fourteen-day collaboration has not matured for the later arrivals. An early read is disproportionately about people who moved quickly. Those may be exactly the accounts that would collaborate without the new step.

The chart is not dishonest. The team is asking it a question the experiment was not built to answer.

## Clinical trials make the interim look part of the plan

Clinical research has an obvious reason to look before the end. Waiting can expose people to a harmful treatment or withhold an unusually effective one. Yet that urgency does not turn every glance into a free decision.

FDA guidance describes adaptive designs as changes made from accumulating data according to a prespecified plan. It asks teams to plan the timing of interim analyses and the criteria for stopping, while protecting trial integrity. [The guidance treats an interim look as part of the design rather than a casual status check](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/adaptive-design-clinical-trials-drugs-and-biologics-guidance-industry).

That is the useful transfer for product teams.

We do not need to pretend an invitation experiment carries the stakes of a drug trial. We can still borrow the discipline of separating a planned efficacy decision from a safety override. A severe accessibility failure, a payment error, a privacy issue, or clear user harm should not wait for a conversion metric to mature. The override exists precisely because welfare outranks a neat readout.

What should not happen is quietly relabeling ordinary excitement as an emergency.

## Quality control watches continuously without improvising continuously

Industrial quality control offers a second connection.

A factory cannot inspect a process only once at the end of a quarter. It needs to notice dangerous or unusual movement while production continues. The answer is not to react emotionally to every wiggle. A control chart pairs ongoing observation with a center line and limits that define which patterns warrant investigation. [The NIST handbook explains that control limits are chosen around the behavior expected from an in-control process](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc31.htm).

The important idea is that looking and deciding are different actions.

A growth team can monitor assignment balance, crashes, complaints, latency, and other integrity or harm signals continuously. It can reserve the primary outcome for planned decision reviews. Or, if the business truly needs to make a benefit decision at any moment, it can use a method designed for that cadence.

Netflix describes this trade directly. Its fixed-horizon analysis is not valid for unlimited peeking, while anytime-valid sequential tests can preserve false-positive guarantees as the data stream is watched. [Its account of sequential testing explains why continuous monitoring needs a different method](https://netflixtechblog.com/sequential-a-b-testing-keeps-the-world-streaming-netflix-part-1-continuous-data-cba6c7ed49df).

The lesson is not that every PM should implement a sequential test. It is that the way we intend to watch belongs in the experiment design.

## Keep an experiment decision cadence

I would put one page beside the experiment brief and review it at launch. The page should be understandable to the person who will be asked for a decision when the result gets loud.

**The decision**

- The product choice this experiment can change
- The eligible population and unit of assignment
- The practical effect large enough to change that choice

**The outcome and maturity window**

- One primary outcome and why it matches the decision
- The time each assigned unit needs for that outcome to mature
- The latest assignment date included in the final read

**The planned looks**

- Launch checks that can diagnose setup but cannot declare a winner
- Exact review times or information milestones
- The purpose and permitted decision at each review

**The minimum information**

- Minimum sample or event count before a benefit decision
- Required weekday, billing, or usage-cycle coverage
- Data quality checks that must pass

**The decision rules**

- Evidence required to ship, continue, stop for futility, or rerun
- What happens when the estimate is promising but still uncertain
- Whether interim looks have been accounted for in the analysis

**The overrides**

- Harm signals that can stop or reduce exposure at any time
- Integrity failures that pause interpretation, such as broken assignment or missing outcomes
- The named person with authority to invoke each override

**The monitoring method**

- Fixed horizon with planned looks, group sequential analysis, or another valid sequential approach
- The analyst who confirms that the method matches the cadence
- The maximum duration or information boundary even when monitoring is continuous

**The record**

- Product owner, analysis owner, and final decision owner
- At every review, the data available, checks performed, decision made, rationale, and next permitted look
- Any deviation from the page and why it was necessary

This is not a form for proving that statistics happened. It is a compact agreement between product urgency and evidentiary patience.

The most useful row may be the one that says what a review is allowed to do. A day-one check can catch a broken treatment. It cannot promote a treatment because the click rate looks wonderful. A midpoint review can continue or stop under its planned rule. It cannot invent a new success threshold because the original one is inconvenient.

## Test whether the cadence changes team behavior

I would not assume this page helps merely because it sounds responsible. I would test the operating habit.

Here is the falsifiable hypothesis.

> We believe precommitting the observation and decision cadence will reduce premature benefit decisions and later winner reversals by at least one quarter across eligible growth experiments, without increasing median time to detect a severe harm signal by more than one hour.

Winner reversal needs a concrete definition before the review. I would count an experiment whose early ship or stop direction disagrees with the estimate after the originally intended outcome window has matured. A premature decision is a benefit decision made before the recorded minimum information or outside a planned rule. Harm detection begins when the harm first appears in telemetry and ends when the owner acknowledges or acts on it.

For one quarter, introduce the cadence page to a randomly selected half of comparable experiment teams if the organization has enough volume. Stratify assignment by team or experiment risk so one group does not receive all the consequential tests. The comparison group uses the current review practice. Both groups keep the same automated harm alerts and escalation policy.

Record every dashboard review if the platform supports it, but do not confuse viewing with deciding. The primary operating outcomes are the share of tests with a premature decision and the share with a winner reversal. Secondary outcomes include time to a valid decision, time to harm acknowledgment, experiment duration, and the number of deviations from the original plan.

After each test, let the full intended window mature even if the product decision happened earlier, unless doing so would expose users to harm. That shadow read provides the comparison needed to identify reversals without pretending the team could have known the later result at the time.

If random rollout is too disruptive, phase the page across teams in a staggered order and compare each team with its own prior practice. That evidence will be weaker because seasonality, staffing, and platform changes can move at the same time. It is still more informative than collecting opinions about whether the template felt rigorous.

## The limits belong on the page too

A lower reversal rate does not prove every decision became better. Teams may delay borderline calls, choose safer experiments, or write rules loose enough that no decision technically violates them. A later result is not automatically the truth when treatment effects change over time. Logged dashboard views can miss screenshots, exports, and conversations. Severe harms may be too rare during one quarter to estimate detection delay with much confidence.

There is also a governance effect. Teams that know they are being observed may follow the cadence more carefully than they will six months later. I would repeat the audit after the novelty has worn off and read a sample of review notes for substance rather than mere completion.

The artifact cannot rescue a weak outcome, a broken randomization, or an experiment whose users never had time to reach value. It only makes the observation rule visible.

## Rigor should buy a decision worth waiting for

Not every product change deserves this ceremony.

I would use the full page when a test could change a core journey, pricing, a costly roadmap commitment, or a claim the company expects to repeat. I would also use it when the primary outcome matures slowly, the expected effect is small, or leaders are likely to watch the result closely.

For a low-risk copy change with a reversible decision, the cadence can be a few lines in the experiment brief. For a severe regression, fraud vector, privacy problem, or accessibility failure, move first and preserve the evidence you can. No confidence threshold is worth knowingly extending harm.

When continuous benefit decisions are genuinely valuable, invest in a sequential method with someone qualified to own it. Do not use sophisticated language as permission to stop whenever the room gets impatient. The method, thresholds, and decision rules still need to be chosen before the interesting result arrives.

The product judgment is not rigor or speed.

It is where waiting protects the company from an expensive false belief, where monitoring protects users from avoidable harm, and where a reversible choice is small enough to make without turning the experiment into a courtroom.

I still want teams to look early.

I want them to know what they are looking for.
