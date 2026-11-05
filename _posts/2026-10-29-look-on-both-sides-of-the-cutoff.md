---
title: "Look on both sides of the cutoff"
subtitle: "A continuous difference in customer behavior can become an abrupt difference in what the product allows."
description: "A growth Product field note on policy cliffs, near-cutoff comparisons, and deciding when a hard threshold is worth keeping."
date: 2026-10-29
image: /assets/images/notebook.jpg
layout: post
---

An operations product I worked on once had a sensible rule.

Small jobs could run immediately. Large jobs needed a manual review. The boundary was a round number that had been chosen years earlier, and it had survived because it was easy to explain and easy to implement.

Then we looked at the jobs just below and just above it.

They were not meaningfully different. The people running them had similar histories, similar error rates, and similar reasons for being there. Yet one group got an answer in minutes while the other sometimes waited until the next day. A continuous difference in size had become an abrupt difference in experience.

The dashboard made this hard to see. It reported completion for small jobs and large jobs as if those were natural kinds of work. They were categories created by our own policy.

Product teams make these boundaries all the time. A workspace gets one experience at nine seats and another at ten. A seller receives funds today or enters a review queue. A customer with twenty-nine days of activity is new while one with thirty is established. An account one unit below a usage limit keeps working while the next one stops.

Sometimes the line is necessary. A product cannot make every decision as a smooth curve. But the line should not inherit more meaning than the evidence gives it.

When the input changes a little and the experience changes a lot, I want to look closely at both sides of the cutoff.

## The cliff belongs to the policy

Thresholds are attractive because they turn judgment into a rule.

They make routing predictable. They let a team say which customers qualify, when a limit applies, and who needs another review. They are often easier to operate than a score nobody can explain.

The trouble begins when we forget that the product created the cliff.

Wind speed is continuous even though hurricane categories are not. The National Hurricane Center is explicit that the [Saffir-Simpson scale](https://www.nhc.noaa.gov/pdf/sshws.pdf) classifies hurricanes by sustained wind speed and does not account for storm surge, rainfall, or tornadoes. Moving from the top of one category to the bottom of the next changes the label. It does not suddenly create an entirely different storm.

A product threshold has the same compression problem. The rule may use one observable value because the system needs an answer. The customer outcome can still depend on many things the value does not contain.

Suppose a bookkeeping product requires a guided setup for businesses importing more than 1,000 transactions. The policy may be directionally wise. Larger imports can take longer and expose more mapping problems.

But 999 and 1,001 transactions do not describe two different customers. File quality, account complexity, prior bookkeeping experience, and the age of the records may matter more. If the guided path adds three days, the product has manufactured a sharp delay from a tiny difference in one input.

That does not prove the threshold is wrong. It tells us where its cost is easiest to inspect.

## Keep a policy cliff brief

Before changing a hard boundary, I write a one-page policy cliff brief.

| Field | What to write |
| --- | --- |
| Running value | The continuous measure used by the rule |
| Current cutoff | The exact point where treatment changes |
| Experience below | What a customer receives just under the line |
| Experience above | What a customer receives just over the line |
| Claimed risk or benefit | Why an abrupt change is supposed to help |
| Near-cutoff evidence | Outcomes in narrow bands on both sides |
| Manipulation check | Whether people or operators can move the recorded value |
| Smoother alternative | A warning, ramp, review sample, or wider evidence rule |
| Keep condition | The result that would justify the cliff |
| Remove condition | The result that would make us soften or retire it |

The brief starts with the running value because vague language hides a surprising amount of policy. “High volume” is not a rule. Transactions in the uploaded file is. So is expected processing time, prior failure rate, or total value at risk.

Then write the two experiences in customer language. Do not write “standard” and “enhanced.” Write “the import begins immediately” and “the import waits for an appointment.” The consequence of the line should be visible before the team debates its rationale.

The near-cutoff band should be chosen before looking for a flattering result. For the import example, I might begin with the two hundred eligible attempts on either side, then check whether a narrower band tells the same story. If the conclusion exists only when the band is unusually wide, customers far from the line may be doing the explanatory work.

This artifact is not a case for abolishing rules. It is a way to stop a convenient number from becoming a theory of the customer.

## The neighborhood around the line can teach you something

Economists use regression discontinuity designs when access to a treatment changes at a known threshold. The intuition is unusually useful for product work. People just below and just above a line can be more comparable than broad groups with different labels.

The method has serious conditions. The [practical guidance from David Lee and Thomas Lemieux](https://www.nber.org/system/files/working_papers/w14723/w14723.pdf) explains why researchers inspect the shape around the threshold, test alternative bandwidths, and ask whether the running value can be precisely manipulated. A chart with a vertical line is not enough.

One striking application examined very low birth weight. The conventional 1,500 gram threshold can lead to more intensive treatment for infants just below it. Douglas Almond and his coauthors used that boundary to study treatment and mortality among infants close to the line. Their [research on newborn care](https://www.nber.org/system/files/working_papers/w14522/w14522.pdf) found both higher treatment intensity and lower mortality just below the threshold.

The product lesson is not that every operational rule deserves a clever causal paper. It is that a boundary can create a useful local comparison. If adjacent cases receive meaningfully different treatment, outcomes near the line can help us judge whether the difference earns its cost.

For the bookkeeping flow, I would plot the running value rather than begin with two bars. On the horizontal axis goes transaction count. On the vertical axis goes a customer outcome such as a correctly completed import within seven days. I would also plot time to completion, requests for help, mapping corrections, and abandonment.

I would look for three things.

- Whether the customer outcome jumps at the same point as the experience
- Whether the supposed risk rises smoothly or actually changes near the line
- Whether the count bunches suspiciously just below the cutoff

The last check matters. An operator may split a file to avoid the guided path. A customer success manager may edit a value to get an important account through. If people can sort cases around the boundary, the neighboring groups are no longer naturally comparable. The bunching is also product evidence. It says the policy is teaching people to work around the product.

## Sometimes the honest test is to move the line

Historical analysis can reveal a cliff, but it may not settle the decision. The teams on each side may differ in an unrecorded way. The threshold may have changed who attempted the journey at all. Operators may quietly compensate for the slower path.

When the downside is reversible, I prefer a narrow randomized band around the cutoff.

For imports between 900 and 1,100 transactions, randomly assign eligible customers to immediate processing or guided setup. Keep customers with known high-risk file conditions out of the test and route them according to those conditions directly. Compare correct completion within seven days as the primary outcome. Read waiting time, abandonment, correction work, and support effort alongside it.

The hypothesis should be able to lose.

> We believe guided setup for imports near 1,000 transactions will increase correctly completed imports within seven days by at least five percentage points, because transaction count near the cutoff identifies complexity that customers cannot resolve in the immediate path.

If guided setup reduces errors but the added wait causes an equal amount of abandonment, the threshold has not produced the claimed customer benefit. If the benefit appears only for old files or mixed currencies, those conditions may deserve the rule instead of raw transaction count. If no credible improvement appears, I would remove the hard cutoff and offer immediate processing with help available.

There are cases where I would not randomize. I would not relax a statutory requirement, expose customers to a severe irreversible loss, or test a boundary whose primary purpose is containing harm merely to get a cleaner readout. The method has to fit the consequence.

In those cases, use past threshold changes, staged operational rollouts, or careful review of near-cutoff cases. A decision can remain conservative while its rationale is examined.

## A smooth rule can be worse

Hard cutoffs have real advantages.

A bright line can be understandable. It can constrain arbitrary treatment by individual operators. It can make an entitlement dependable rather than negotiable. A gradual score can look more sophisticated while hiding unstable inputs and making the result impossible for a customer to anticipate.

Smoothing also creates failure modes of its own. A usage warning at every step can become a month of low-grade anxiety. A model that gradually increases review may reproduce the same cliff in less visible form. A discretionary exception process can favor customers who know whom to ask.

There are also natural discontinuities in the world. One remaining seat cannot hold two people. A payment either clears the available balance or it does not. A legal filing is on time or late. Product design cannot wish those constraints into curves.

The question is not whether every threshold should disappear. It is whether the abrupt product consequence follows a real constraint, a demonstrated benefit, or merely a round number that was easy to ship.

## The judgment call lives near the edge

For the bookkeeping product, I would not replace the 1,000 transaction cutoff with a more mysterious complexity score on the first pass.

I would make a narrower call.

Let imports proceed immediately unless the product can name a condition that has predicted an unsuccessful import, such as unsupported file structure, mixed accounting periods, or a prior mapping failure. Offer guided setup before the run, but do not require it on transaction count alone. Preserve a hard stop only for conditions where proceeding would corrupt records or create work that cannot be recovered cleanly.

That call gives up some operational neatness. More customers may ask for help after starting. The team will need to learn which conditions actually make an import difficult.

It also stops making two nearly identical customers live through different products because one file contains two extra rows.

Thresholds are useful servants. They are poor explanations.

Whenever a team points to a line and says the customers above it are different, I want to move closer. Not to deny that differences exist, but to see whether the difference belongs to the customer or to the rule we drew.

The edge is where that distinction becomes visible.
