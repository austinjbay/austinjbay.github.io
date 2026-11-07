---
title: "Estimate the rebound before you credit the rescue"
subtitle: "Why a better week after an intervention may be the recovery you were going to get anyway."
description: "A natural-recovery baseline for separating regression toward the mean from the incremental effect of a product rescue."
date: 2026-10-31
image: /assets/images/notebook.jpg
layout: post
---

The worst week has a way of making a growth team decisive.

A healthy account suddenly goes quiet. A subscriber who usually completes three workouts finishes none. A small-business customer misses the task that has predicted renewal for months. Someone opens a channel, names the risk, and starts a rescue.

The customer gets a carefully timed message. A success manager offers a call. The product makes the next action unusually easy. The following week is better.

Everyone exhales, and the rescue gets the credit.

It may deserve some. But an unusually bad week is not a neutral place to begin measuring improvement. It is an extreme observation. Some part of what made it extreme may be temporary noise, a vacation, an outage, a sick child, or ordinary variation in a behavior that was never perfectly steady. Even if the team does nothing, the next observation will often be closer to the customer's usual level.

That movement is regression toward the mean. In product work, it creates a particularly seductive attribution error. We intervene because the moment is unusually bad, then treat the fact that it became less unusual as evidence that our intervention worked.

The question is not whether the customer recovered.

The question is how much more they recovered than we should have expected without the rescue.

## Extreme weeks contain signal and weather

Suppose a planning product has a customer who completed four weekly plans in each of the prior six weeks. Then they complete none. A lifecycle message offers to rebuild the next plan from their last successful one. The customer completes three plans the following week.

It is tempting to call that a recovery of three and put the message in the playbook.

But the zero may contain two things at once.

- A real deterioration in the customer's relationship with the product
- A temporary deviation from their underlying pattern

The first creates room for a rescue to help. The second creates a rebound whether or not anyone helps.

This is not the same as saying every bad week is random. A lost job, a broken integration, or a change in team ownership can permanently change behavior. Regression toward the mean does not promise that every individual will bounce back. It says that when we select cases partly because their observed result is extreme, the group will tend to look less extreme on a later measurement when those measurements are imperfectly correlated.

A [BMJ review of regression toward the mean](https://pmc.ncbi.nlm.nih.gov/articles/PMC1125994/) describes the same trap in health care. People are often treated when a measurement or symptom is unusually severe. A later improvement can then make an ineffective treatment look useful. The more extreme the selected observation and the less stable the repeated measure, the larger the apparent recovery can be.

The connection to growth work is uncomfortable because rescue programs are often built to find exactly those extreme moments. That makes operational sense. It also makes before-and-after evidence unusually weak.

I think of the bad week as a mix of signal and weather. The signal is a durable change worth responding to. The weather is the part likely to pass. A team that credits the rescue with the whole rebound quietly claims it changed both.

## The next week is not the counterfactual

Teams often compare the trigger week with the week after the intervention. That answers a descriptive question about what happened next. It does not answer what would have happened next without the intervention.

The distinction matters because the trigger itself selected a low point.

Imagine a basketball coach who benches a reliable shooter after the worst game of the season. The replacement plays, and the shooter makes more shots in the following game. We cannot infer that the benching fixed the shot. The original game was chosen because it was exceptional. Ordinary performance would look like improvement.

The same pattern appears in industrial work. A team inspects a machine immediately after an unusually high defect count. The next batch has fewer defects. Maintenance may have helped, but random fluctuation around the process would also make another extreme batch less likely. This is why a process engineer wants a view of the system over time, not a victory story built from the noisiest point.

Product behavior adds another complication. The customer's usual level may itself be moving. Tenure, seasonality, billing cycles, weekdays, and changing team size can all affect the next week. The useful comparison is therefore not the global average and not a simple copy of the prior week. It is the expected next outcome for customers with a similar history and a similarly bad observation, before the rescue adds anything.

That expectation is a natural-recovery baseline.

## Build an expected rebound curve

Before scaling a rescue, I would build a small artifact called an expected rebound curve.

Start with past episodes where the same outcome fell sharply but no comparable rescue was delivered. For each episode, preserve enough history to describe the state before the fall and then record what happened over the next few relevant periods.

The working sheet can stay simple.

| Field | What to record |
| --- | --- |
| Normal level | Typical behavior before the bad period |
| Trigger observation | Behavior in the unusually bad period |
| Drop size | Distance from the prior normal level |
| Stability | How much the behavior usually varies |
| Context | Tenure, plan, season, and known disruptions |
| Next outcome | Behavior in the following period without a rescue |
| Later outcome | Behavior after enough time for a slower return |

For a given triggered customer, find historical episodes that looked similar before and during the drop. Their average path afterward is the expected rebound curve. It might show that customers who normally complete four plans, then fall to zero, naturally return to two the next week and two and a half the week after that.

Now the customer who returned to three after a rescue still improved by three from the low point. But only one of those completed plans sits above the natural-recovery baseline for the next week.

That one is not automatically the treatment effect. Historical comparisons can miss changes in customer mix, product quality, or calendar conditions. The curve is a prior expectation and a challenge to the team's story. It gives the experiment a sensible null, not a causal verdict.

The curve should become more specific only when the data earns it. I would begin with a few features that affect both the size of the drop and the likely return.

- The customer's typical level before the trigger
- The magnitude of the bad observation relative to that level
- The ordinary week-to-week volatility of the behavior
- Tenure and lifecycle stage
- Calendar conditions shared by many customers
- Known product incidents that affected the trigger period

Volatility is easy to overlook. A fall from four to zero means something different for a customer who has completed exactly four plans for months than for one whose record moves between zero and six. The second customer has more natural rebound built into the observation.

I would plot the baseline as a range rather than a single heroic decimal. Product data is rarely stable enough to justify false precision. Show the median path and a useful interval around it. Then put the observed path for rescued customers on the same chart.

The visual question becomes plain. Did rescued customers merely travel through the range where similar customers usually land, or did they recover farther and stay there longer?

## Do not train the baseline on the rescue

The cleanest historical episodes are ones from before the rescue existed or from places where it was genuinely unavailable for reasons unrelated to customer risk. If rescued episodes are included, their later outcomes will teach the baseline to expect part of the intervention's effect. The rescue then disappears into the recovery we call natural.

It is also worth separating a shared shock from an individual extreme. If a service outage caused nearly every customer to miss a task, the rebound after restoration is not mainly regression toward the mean. It is recovery from a known cause. Likewise, a holiday week may repeat on a calendar and should be represented as context rather than treated as private customer volatility.

Repeated measurements help us see the difference. The [Institute for Work and Health guidance](https://www.iwh.on.ca/what-researchers-mean-by/regression-to-mean) recommends using multiple baseline measurements rather than selecting on a single measurement when possible. In a product setting, the history is often already available. We should use it to estimate the customer's usual level and ordinary variation instead of letting one dramatic week define the whole story.

There is a judgment call here. Waiting for several bad weeks may be unacceptable when the downside is large. The answer is not to withhold help until the statistics feel tidy. Help the customer when helping is the right product decision. Just do not turn urgent service into causal evidence it cannot provide.

## Test the lift above recovery

Consider a subscription fitness product where established members usually complete at least two workouts each week. A member becomes eligible for a rescue after completing no workouts in a week despite having completed at least two in most of the prior six weeks.

The rescue is a single message that offers to place one previously completed workout onto the member's chosen day. It is plausible, relevant, and small enough to test without rebuilding the product.

I would state the hypothesis this way.

> Among established members after their first zero-workout week, offering one-tap scheduling of a familiar workout will increase the share who complete a workout within the next seven days by at least six percentage points above natural recovery, without increasing message opt-outs.

Randomly assign eligible members at the moment of the trigger. One group receives the scheduling rescue. The other receives no rescue during that seven-day measurement period. Both groups will contain members whose bad week mixed durable trouble with temporary variation, so both groups should rebound. The difference between them estimates the lift above that recovery.

Before reading the result, use earlier untreated episodes to draw the expected rebound curve. This is a useful operational check. If the randomized comparison group recovers far more or less than history predicted, investigate what changed before generalizing the result. The randomized comparison still carries the causal claim for this test. The historical curve helps the team understand the environment in which that claim was learned.

The primary outcome should be completion of at least one workout within seven days of assignment. Secondary outcomes can include completed workouts over the following three weeks and repeat zero-workout weeks. Message opt-outs and complaints are sensible guardrails.

The hypothesis fails if the lower bound of the planned uncertainty interval does not clear zero, or if the point estimate misses the six-point bar the team decided would justify the interruption and implementation cost. It also fails if opt-outs rise beyond the agreed tolerance. A large before-and-after rebound does not rescue a weak randomized difference.

That last sentence is the discipline. If both groups recover by twenty points and the intervention adds one uncertain point, the honest conclusion is that members often recover after a zero week and this rescue did little beyond that. The program may still have helped a few people. It did not earn a broad claim.

## Give natural recovery a seat in the review

Rescue work creates vivid anecdotes. A customer replies with gratitude. A success manager describes the account that came back. A chart rises sharply from its lowest point.

None of those observations is fake. They are simply incomplete accounts of causality.

In the review, I would show three quantities together.

- The observed drop before the trigger
- The rebound we expected without intervention
- The additional recovery attributable to the rescue

That decomposition changes the conversation. The team can still care about the whole customer recovery while being precise about the smaller part it caused. It can also discover when a rescue is aimed at weather rather than signal. Perhaps the right product move is not more outreach. It may be to wait, to make the next ordinary return easy, or to reserve human effort for cases whose behavior stays below the expected rebound curve.

This is not an argument for passivity after a bad week. It is an argument for humility after a better one.

Customers recover for reasons that belong to them. Their schedule clears. Their motivation returns. A temporary problem passes. The product should be glad when that happens.

It should not automatically take the credit.
