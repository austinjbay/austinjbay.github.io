---
title: "A retention predictor is not automatically a growth lever"
subtitle: "The behavior that identifies your healthiest users may not be the behavior that made them healthy."
description: "A practical causal claim card for deciding when an activation signal is ready to become a product intervention."
date: 2026-11-22
image: /assets/images/notebook.jpg
layout: post
---

I have helped put an early user behavior on an activation dashboard and then watched it become a product requirement almost overnight.

The analysis looked convincing. People who completed the behavior retained at twice the rate of people who did not. The team added prompts, a checklist item, and a lifecycle message. We made the behavior easier to reach and felt surprised when retention barely moved.

The chart had answered one question. We quietly acted as if it had answered another.

It told us who was likely to stay. It did not tell us what would make someone stay.

That distinction is easy to nod at and surprisingly hard to keep alive in growth work. Predictive signals are useful because they arrive early. Product teams are useful because they can change what happens next. The trouble begins when we promote a good signal into a lever without testing whether moving the signal moves the outcome.

## The thermometer is not the furnace

A warm house and a high thermometer reading travel together. Turning the thermometer dial does not warm the room unless the dial controls a thermostat.

Activation behaviors can work the same way.

Imagine a planning product where customers who connect a calendar during their first week retain much better. The connection may create the value. It could bring real work into the product, lower the cost of returning, and make the planner part of a daily routine.

It could also identify people who already have a complicated schedule, arrived with a clear job, and were willing to invest in setup. Those customers might have retained anyway. Pushing a lightly interested user through calendar connection can raise the activation metric without producing any of the intent the event used to reveal.

Medicine has to separate similar stories all the time. A symptom can help predict an outcome without being a useful treatment target. Epidemiology calls the mixing of a treatment effect with other causes confounding. Miguel Hernán and James Robins make the practical point that causal questions need well-defined interventions and assumptions, not only associations in observed data. [Hernán’s description of this work is candid about both the value and the risk of causal inference from observational evidence](https://hsph.harvard.edu/profile/miguel-hernan/).

Growth teams do not need to turn every funnel review into a graduate seminar. We do need to state which kind of claim we are making.

## Prediction, mechanism, and intervention are different claims

I find it useful to separate three levels.

**A predictive claim** says people who do the early behavior are more likely to reach the later outcome.

**A mechanism claim** says the early behavior plausibly changes something that matters, such as available content, social commitment, accumulated work, or the cost of returning.

**An intervention claim** says helping more eligible people complete the behavior will improve the later outcome.

Each claim asks for different evidence.

Historical cohorts can support prediction. Interviews, session review, and product traces can make a mechanism more believable. A randomized intervention is usually the cleanest way to learn whether the team can turn the behavior into a lever. Microsoft’s account of online controlled experiments describes randomization as the reason experiments can establish causality and assess how product changes affect customer behavior. [That is the standard the intervention claim has to approach](https://www.microsoft.com/en-us/research/publication/online-experimentation-at-microsoft/).

The levels can disagree without anyone making a bad analysis. A connected calendar may remain an excellent retention predictor and a poor lever for users who did not choose it on their own. That still makes it useful for forecasting, diagnosis, or finding customers who need less help. It just should not carry a causal promise it has not earned.

## Keep a causal claim card

Before turning an activation signal into onboarding work, I would put one page beside the metric.

### The observed relationship

- The exact early behavior, eligibility rule, and time window
- The later outcome and the size of the observed difference
- The cohorts where the relationship has held
- The plausible factors that could cause both behaviors

### The proposed mechanism

- What changes for the user immediately after the behavior
- Why that change should affect the later outcome
- Who can complete the event without receiving that value
- Who can receive the value through another path

### The intervention

- What the product will change to help the behavior happen
- Whether the change alters capability, understanding, motivation, or only event completion
- What the intervention might do directly to retention beyond the target behavior
- What result would make the team stop treating the behavior as a lever

### The decision

- **Predictor only** when the relationship is useful but the mechanism is weak
- **Candidate lever** when the mechanism is credible but untested
- **Demonstrated lever** when an intervention changes both the behavior and the later outcome
- **Diagnostic signal** when the event helps explain healthy usage but should not be maximized

The language matters. Candidate lever creates a useful pause between seeing a chart and redesigning onboarding around it.

## Write the causal hypothesis in two steps

A normal growth hypothesis can hide the gap by jumping straight from a prompt to retention.

I would make both links falsifiable.

> We believe offering an in-context calendar connection after a new user creates a second dated task will increase first-week calendar connections among eligible accounts by at least 15 percent because the benefit is visible at the moment scheduling work becomes repetitive. We further believe the induced connections will increase fourth-week planning activity by at least 5 percent because imported commitments give users a current reason to return.

The first sentence tests whether the product can move the candidate behavior. The second tests whether the users moved by the intervention also receive the downstream value.

That word induced is doing important work. If connection rises only among people who were already going to connect later that afternoon, the team mostly changed timing. If connection rises and retained planning does not, the behavior may be a marker, the intervention may be weak, or the mechanism may need a condition the product did not provide.

## Use an encouragement when you should not force the behavior

Some candidate levers can be assigned directly. A team can randomly give eligible users a faster import flow and compare downstream outcomes with the current flow.

Others should remain voluntary. Connecting a calendar, inviting a colleague, publishing work, or linking a bank account involves context and consent that a product should not manufacture for the sake of a clean test.

In those cases, randomize an encouragement rather than the behavior itself. Show a well-timed explanation, a useful preview, or a lower-effort entry point to one randomly selected group. Leave the choice with the user.

Then read the experiment in layers.

- Did assignment to the encouragement increase the target behavior
- Did assignment improve the retained outcome across everyone eligible
- Did it change guardrails such as disconnects, undo actions, support contacts, or trust-related exits
- Was the encouragement itself useful in a way that could affect retention without the target behavior

The first result checks whether the encouragement was strong enough to teach us anything. The second is the primary product result. The third catches a metric win bought with a worse experience. The fourth protects the causal story.

There is a formal statistical tradition behind this design. Angrist, Imbens, and Rubin showed how randomized assignment with imperfect compliance can identify an average causal effect for the people whose behavior was changed by the assignment. [Their original instrumental-variables paper is careful about the assumptions and the subgroup the estimate describes](https://doi.org/10.1080/01621459.1996.10476902).

That last limitation matters for product judgment. The experiment does not necessarily reveal what calendar connection would do for every customer. It can reveal what it did for the people persuaded by this particular intervention. A subtle explanation may move cautious users. A setup concierge may move complex accounts. Those are different product policies even if the event at the end is identical.

I would not reach for an instrumental-variables estimate by default. Start with the effect of assignment on the downstream outcome. It answers the decision the team actually owns, which is whether to ship the encouragement. Bring in specialist help if estimating the effect among persuaded users would materially change the decision.

## A null result still needs product judgment

Suppose calendar connections rise by 18 percent and fourth-week planning does not move.

The shallow conclusion is that calendar connection does not matter. The opposite shallow conclusion is that the experiment failed and the original correlation still proves it matters.

Neither is good enough.

Look at what the intervention actually created. Did newly connected users import calendars with no relevant events? Did the product bury imported commitments on a screen they rarely revisited? Did the prompt cause people to connect a secondary calendar while healthy existing users had connected their primary one? The event can be technically identical while the useful dose of the mechanism is absent.

This is not permission to rescue every favorite idea with a new explanation. The claim card should have named the mechanism and its observable traces before the result arrived. If the expected intermediate change happened and retention did not, demote the lever. If the intermediate change never happened, the test challenged the intervention more than the underlying mechanism. Decide whether that mechanism is important enough to earn one meaningfully different attempt.

A positive result needs judgment too. If the encouragement improves retention while barely changing connections, the message may have helped users clarify their planning job through another route. Ship the experience if the total result and guardrails are healthy, but do not credit calendar connection for work it did not do.

## Let a signal keep the job it earned

I still want activation metrics that predict retention. Prediction gives a growth team an earlier view of whether new users are finding their way toward value.

I just do not want the dashboard to smuggle in a product prescription.

Some signals are signposts. Some are switches. The most interesting ones may be both, but they have to earn those jobs separately.

When a retained cohort tells you that an early behavior matters, keep the insight. Write down the mechanism. Build an intervention that can move the behavior without faking it. Then judge the intervention on the later outcome, including the people who were offered help and chose not to take it.

The craft is not finding more behaviors that healthy users share.

It is learning which of those behaviors the product can responsibly help cause, and whether causing them actually makes the user healthier.
