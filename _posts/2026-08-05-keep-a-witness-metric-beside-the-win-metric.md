---
title: "Keep a witness metric beside the win metric"
subtitle: "Why growth teams need one small measure that can testify whether a local lift still looks like real product progress."
description: "A growth PM field note on guardrails, proxy metrics, and the practical artifact that keeps an A B win from quietly teaching the wrong lesson."
date: 2026-08-05
image: /assets/images/notebook.jpg
layout: post
---

I think a lot of growth teams know how to pick a target and are less disciplined about picking a witness.

We want signup completion to go up.

We want invite acceptance to go up.

We want trial to paid conversion to go up.

We want dormant users to come back.

That part is easy to say.

The harder question is whether the movement still looks like product progress once the rest of the system gets a vote.

Sometimes the answer is yes.

Sometimes the lift arrives with a smell.

The onboarding step completes more often, but support tickets climb because the explanation got thinner.

The invite prompt gets more sends, but team retention gets worse because the invites are arriving before the workspace feels ready.

The win back campaign revives logins, but those users bounce again because the product never solved the reason they left.

The dashboard still gives the team a green shape.

The user experiences something messier.

That gap is where I like a witness metric.

Not a giant metric zoo.

Not twelve executive scorecards.

Just one small measure beside the main win that can tell you whether the thing you improved still resembles the value you meant to create.

## A win metric tells you where motion happened

A witness metric tells you what that motion cost

I think about this the same way I think about a movie trailer.

The trailer can do its job and still misrepresent the film.

You can leave with a full theater and a disappointed audience.

The marketing result was real.

The product result was not.

Growth metrics can behave the same way.

A local number moves because the team made the next action easier, louder, more urgent, or more visible.

That is not meaningless.

But it is incomplete.

Microsoft’s experimentation guidance makes this point more rigorously than most product teams do. In its piece on [patterns of trustworthy experimentation during the experiment stage](https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-during-experiment-stage/), Microsoft recommends a holistic metric set that includes guardrail metrics for the parts of the product you do not want to degrade, even when those parts are not the headline goal.

I like that framing because it pulls the conversation out of a fake binary.

Either the test won or it lost.

Real product judgment is usually more interesting than that.

The change increased account creation.

Good.

It also increased abandonment one step later.

Less good.

It improved clickthrough.

Good.

It also taught people to click into something that felt less trustworthy once they arrived.

Bad.

That does not mean every mixed result is a failure.

It means the team should understand the trade with open eyes before it calls the trade a strategy.

## A lot of bad growth decisions come from overloving the proxy

The thing that makes this tricky is that growth work often operates through proxies.

We rarely get to optimize the deepest objective directly.

We want durable value, but we measure activation events.

We want product trust, but we measure response rates.

We want confident team adoption, but we measure invites sent, seats filled, or workflows started.

That is normal.

It is also dangerous.

OpenAI’s piece on [measuring Goodhart’s law](https://openai.com/index/measuring-goodharts-law/) puts the issue plainly. When you optimize a proxy objective, you have to keep checking whether the true objective is still improving too.

That is not just an AI alignment problem.

It is a growth product problem all day long.

A team targets document uploads because uploads predict activation.

Then they make the upload ask more aggressive.

Uploads rise.

The imported documents are junk.

The user does not come back.

The proxy kept moving after the value stopped.

Or a team targets invite sends because team formation matters.

They put the invite ask earlier.

Invites rise.

Acceptance quality falls because people are now inviting teammates before they understand what story to tell them.

The proxy kept moving after the product promise got thinner.

I think this is one reason experienced growth people start sounding a little suspicious even when the chart is up and to the right.

We have seen too many local wins that behaved like borrowed money.

## Good measurement sounds more like service design than scoreboard worship

One reason I like reading outside classic product growth writing is that other fields are often more honest about mixed evidence.

Public service teams are usually forced to be.

The GOV.UK service manual on [setting performance metrics for your service](https://www.gov.uk/service-manual/measuring-success/how-to-set-performance-metrics-for-your-service) pushes teams to define benefits, write hypotheses, choose a small set of meaningful metrics, and combine digital analytics with other data sources instead of treating one dashboard as the whole truth.

That last part matters.

Do not just use digital analytics.

That line should be hanging in more growth war rooms.

The clickstream tells you something.

Support transcripts tell you something else.

Cancellation reasons tell you something else.

Sales calls, user interviews, onboarding session notes, and screenshot recordings each hold a different part of the truth.

Even usability benchmarking guidance from GOV.UK is more grounded than a lot of startup experimentation culture. Their [usability benchmarking advice](https://www.gov.uk/service-manual/measuring-success/usability-benchmarking-a-website-or-whole-service) explicitly recommends measuring whether users completed the task, whether they abandoned it, and how confident they felt that they got the right answer.

I love the confidence part.

Confidence is often the missing witness metric in growth work.

Teams celebrate that the user clicked through.

The user is not actually sure they did the right thing.

That uncertainty shows up later as delay, workaround behavior, teammate hesitation, refund demand, or silent churn.

The metric moved.

The habit never formed.

## A witness metric should sit close to the product promise

This is the part that I think gets overcomplicated.

A witness metric is not every metric that exists.

It is the nearby measure that can testify whether your main win still resembles the progress you promised the user.

If your main metric is onboarding completion, the witness metric might be first week retention, setup error rate, or user confidence after setup.

If your main metric is invites sent, the witness metric might be invite acceptance rate, invited teammate activation, or median time to first shared outcome.

If your main metric is content published, the witness metric might be later edits, deletions, support contacts, or return usage.

If your main metric is reactivation opens, the witness metric might be meaningful session depth instead of raw return.

I infer from Microsoft’s metric taxonomy and Google’s HEART framing that the right witness metric is usually the one nearest to the user promise that could be quietly damaged while your main metric improves. Google Cloud’s writeup on [measuring developer experience with the HEART framework](https://cloud.google.com/blog/products/application-development/how-platform-engineers-can-improve-their-developers-experience) describes HEART as a way to choose the right metrics based on goals while balancing behavioral data with user sentiment. The article is about developer experience, but the principle travels well.

The witness metric should usually do one of three jobs.

It should tell you whether quality stayed intact.

It should tell you whether confidence stayed intact.

It should tell you whether the user got closer to an outcome that survives the moment of measurement.

If it does none of those, it may be interesting, but it is probably not a witness.

## The artifact I like is a witness metric brief

When a team is preparing a growth test that feels likely to create side effects, I like a one page witness metric brief.

Not because process is beautiful.

Because memory is weak when the graph turns green.

## Witness metric brief

- Main metric we hope to move
- User promise behind that metric
- Failure mode that could make this win misleading
- Witness metric that would reveal that failure mode
- Why this witness sits close to the promised value
- What movement would count as acceptable tension
- What movement would make us pause or shut the test down
- What non dashboard evidence we will review beside the numbers
- Owner

That is enough for most tests.

The point is not to predict every second order effect in advance.

The point is to make one adult promise before the experiment starts.

If this number rises while this other thing gets worse, we will not pretend we did not see it.

## The witness metric also protects the team from storytelling drift

I think this is one of the quieter benefits.

Without a witness metric, teams become very talented courtroom lawyers for their favorite chart.

They explain away the support spike.

They call the retention dip noisy.

They say the quality complaints are anecdotal.

They argue that the win is still worth it because the primary goal moved.

Sometimes they are right.

Sometimes they are defending a result that already told them the truth.

The witness metric makes the argument cleaner.

You decided in advance what kind of collateral damage mattered.

You named the nearby measure that would reveal it.

Now you have to face your own standards.

That is useful discipline for growth teams because our work sits close to temptation.

We are often changing defaults, prompts, sequences, copy, ranking, urgency, and timing.

Those levers can create real value.

They can also create pressure, noise, confusion, or low quality behavior that flatters the dashboard before it punishes the product.

I do not think the answer is to become anti measurement or anti experimentation.

I think the answer is to become slightly harder to impress.

Pick the win metric.

Then pick the witness who gets to testify beside it.

If the witness still believes the story, you may have found progress.

If not, you may have found a cheaper way to fool yourself.
