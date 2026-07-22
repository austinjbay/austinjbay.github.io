---
title: "Check the denominator before you call it progress"
subtitle: "Why growth product judgment gets better when teams study who was actually eligible for the win, who was counted out, and what the average is hiding."
description: "A growth PM field note on using a denominator note to keep lifts honest when segment mix, eligibility rules, and blended reporting distort the story."
date: 2026-07-22
image: /assets/images/notebook.jpg
layout: post
---

I think a lot of growth teams learn the right lesson one layer too shallow.

The experiment lifted conversion.

The new onboarding path improved activation.

The lifecycle send increased return rate.

The new prompt improved completion.

All of that may be true.

It still may not mean what the room thinks it means.

Because one of the easiest ways to misread progress is to skip the denominator.

Who was actually eligible for the outcome.

Who was quietly excluded.

Which segment got bigger during the test window.

Which segment got smaller.

Whether the average improved because the experience got better, or because the mix changed.

I do not think this is only a stats problem.

I think it is a product judgment problem.

Growth teams make real decisions off blended rates all the time.

We ship the flow.

We expand the audience.

We change the lifecycle cadence.

We rewrite the page.

We call something a best practice.

If the denominator story is fuzzy, those downstream decisions get shakier than they look.

## A lot of healthy looking lifts are really mix stories

This shows up in more places than experiment readouts.

An onboarding metric improves because more high-intent users arrived that week.

A signup completion rate rises because users on the hard path were screened out earlier.

An activation number looks stronger because invited teammates were excluded from the cut.

A reactivation campaign appears more effective because the dormant users most likely to ignore it were never actually eligible for the send.

A support burden looks stable because the denominator changed from all new accounts to only the ones that made it far enough to create a ticket.

None of those are fake outcomes.

They are incomplete outcomes.

That distinction matters.

The [CDC guidance on frequency measures](https://archive.cdc.gov/www_cdc_gov/csels/dsepd/ss1978/lesson3/section1.html) is useful here because public health has always had to be strict about who belongs in the denominator. The numerator only means something when it is tied to the population actually at risk.

That sounds obvious in epidemiology.

It should sound just as obvious in product work.

Yet growth reporting often smuggles multiple populations into one tidy rate and then acts surprised when the story gets slippery.

## The average is often carrying more argument than it deserves

I like averages.

I use them constantly.

I just do not trust them alone when the decision is expensive.

A blended number can tell you whether something noteworthy happened.

It cannot always tell you why.

That is one reason I keep returning to the experimentation literature from Ron Kohavi and colleagues at [ExP Platform](https://exp-platform.com/). Trustworthy experimentation is not only about randomization and p values. It is also about learning the right thing from the result you observed.

In growth work, the dangerous mistake is not always celebrating noise.

Sometimes it is celebrating a real effect without understanding its shape.

The overall metric improved.

Great.

Did it improve because the product genuinely got easier for the intended user.

Did it improve because the easy segment got more weight.

Did it improve because the hard segment got filtered away.

Did it improve because only some surfaces adopted the change.

Did it improve because the denominator quietly narrowed to people already halfway through the job.

Those are different stories.

They deserve different follow-up actions.

## Other fields are less casual about the denominator than product teams are

Hospitals do not talk about infection rates without arguing over exposure windows and who counts in the population.

Baseball people do not confuse a hot streak against weak pitching with a stable view of talent.

Warehouse operators do not judge picking speed without separating easy orders from ugly ones.

Teachers do not read class performance the same way if the assignment was optional and only the confident students turned it in.

Each field has learned some version of the same lesson.

The rate is inseparable from the population that produced it.

That is why I also like the broader research argument from Christopher Bryan, Elizabeth Tipton, and David Yeager in [Behavioural science is unlikely to change the world without a heterogeneity revolution](https://www.nature.com/articles/s41562-021-01143-3). Their point is bigger than product analytics, but it travels well. Effects vary across contexts and groups more than tidy summaries admit.

I think growth PMs run into that constantly.

The team wants one answer.

The product is giving you several at once.

## Eligibility rules are part of the product story

One reason this gets missed is that denominator decisions often hide in instrumentation, audience definitions, and operational shortcuts.

The campaign only targeted users with synced data.

The experiment only included web traffic.

The new onboarding report only counted users who reached a certain page depth.

The activation view excludes invited users because identity stitching is messy.

The comparison report groups self-serve trials and sales assisted starts because nobody wanted to maintain two dashboards.

Again, some of those choices are reasonable.

But they are not neutral.

They shape what kind of progress you are allowed to see.

That is why I think eligibility logic deserves more daylight in growth teams.

Not as analytics bureaucracy.

As product context.

If the metric ignores the users you most need to learn from, the dashboard can become a very polished avoidance mechanism.

## The artifact I like is a denominator note

When a team is about to socialize a win, expand a rollout, or use a metric as a decision trigger, I like writing a denominator note.

Not a giant appendix.

Not a performative stats lecture.

Just a small artifact that forces the population story into the room before the conclusion hardens.

## Denominator note

- Outcome being reported
- Numerator in plain English
- Denominator in plain English
- Who was eligible to be counted
- Who was excluded and why
- Which segments made up a larger share of the denominator during the readout window
- Which segments were underrepresented relative to the intended product audience
- Whether the denominator changed from the prior baseline, experiment arm, or reporting cut
- What hidden operational work, targeting rule, or instrumentation constraint shaped eligibility
- What decision would be dangerous if this blended rate were misread
- What segmented view or follow-up cut should be reviewed before rollout
- Owner

That is usually enough.

The point is not to make every weekly metric review feel like graduate school.

The point is to stop treating blended outcomes like self-explanatory truth.

## This changes the decisions you make after the readout

Once the denominator note exists, several good things happen.

You get more honest about whether a win generalizes.

You catch when the product improved mostly for the users who already had momentum.

You notice when a lifecycle result depends on an audience definition that will not survive scale.

You stop over-learning from a path that excluded the messy but commercially important segment.

You give engineering and analytics a clearer brief about what needs to be instrumented next.

You also get a better conversation with leadership.

Not, did the rate move.

But, for whom did it move, under what counting rules, and does that match the decision we are about to make.

That is a much better growth question.

## The product audience is wider than the dashboard’s first draft

That may be the main thing I want to preserve here.

A metric is always a summary of a population story.

If the population story is blurry, the summary can still look beautifully precise.

That precision is not the same thing as understanding.

I do not think growth PMs need to become statisticians before lunch.

But I do think we should become harder to impress with a rate that arrives without its denominator logic attached.

Before you celebrate the lift, expand the treatment, or turn the result into doctrine, ask one more question.

Who exactly was this progress made of.
