---
title: "Run the premortem before you ship the test"
subtitle: "A small ritual that catches weak instrumentation, bad incentives, and shaky growth logic before they reach production."
description: "A growth PM field note on using experiment premortems to improve test quality before launch."
date: 2026-06-18
image: /assets/images/desk.jpg
layout: post
---

One of my favorite growth rituals happens before anything ships.

Not the launch review.

Not the QA pass.

Not the excited Slack message about how this test is going to unlock activation.

I mean the quieter moment where someone has to answer a less flattering question:

If this experiment goes badly, how will it go badly?

I like asking that before launch because growth work has a way of making optimistic stories sound more complete than they really are.

The team has a hypothesis.

The design looks cleaner.

The copy feels sharper.

The dashboard is ready.

The implementation is nearly done.

And now everyone is a little too ready to believe the test itself is the disciplined part.

Sometimes it is.

Sometimes the test is just a polished way to learn the wrong lesson.

## A test can be well-intentioned and still be fragile

This is the part I think growth teams under-discuss.

We treat experimentation like a safety blanket. If it is an A/B test, it must be rigorous. If there is a metric, it must be meaningful. If there is significance, it must be telling the truth.

That is a comforting story. It is not always a true one.

The [review of online controlled experiment challenges by Larsen, Deng, Kohavi, Stevens, and others](https://arxiv.org/abs/2212.11366) is useful partly because it reminds you how many ways experimentation can get messy in practice. Instrumentation issues, sample problems, metric selection problems, data quality problems, interference, novelty effects, and misread results all show up faster than most launch plans admit.

That does not mean you should stop testing.

It means the experiment deserves product judgment too.

## The premortem is a good forcing function

I still like Gary Klein’s old [Harvard Business Review piece on project premortems](https://hbr.org/2007/09/performing-a-project-premortem) because the mechanism is so simple.

Assume the project failed.

Now ask why.

That framing matters because it makes skepticism socially easier. People do not have to be the person derailing momentum. They just have to explain the plausible failure story.

For growth experiments, that is incredibly useful.

Before a test launches, teams are usually biased toward motion:

- we already wrote the copy
- engineering already scoped it
- design already polished it
- the quarter already needs a win

That is exactly when I want a small pause.

Not a giant process ceremony. Just enough structure to catch the obvious ways we might fool ourselves.

## Most experiment failures are not dramatic

When a growth test fails, it is often not because the product broke in half.

Usually it is something less cinematic:

- the primary metric moved, but only because users were pushed into a low-quality action
- the treatment hurt a segment the team forgot to isolate
- the instrumentation could not reliably attribute the behavior
- the test window was too short to observe downstream effects
- the metric improved while a more important guardrail quietly got worse
- the variant changed multiple things at once, so nobody knows what worked
- the idea addressed a symptom, not the actual bottleneck

Those are not rare edge cases.

That is normal growth work.

Which is why I do not think the real question is, “Should we experiment?”

The real question is, “How do we keep ourselves from learning the wrong thing with a straight face?”

## A simple artifact: the experiment premortem

The version I like is intentionally lightweight.

Before a test goes live, write down:

### 1. How this experiment could appear to win for the wrong reason

This is the first question for a reason.

If the variant increases a surface-level metric, what are the cheap ways that number could go up?

Examples:

- more clicks because the CTA got more aggressive, not more relevant
- more onboarding completions because steps were skipped, not understood
- more invites because the prompt became harder to dismiss, not more timely
- more usage because the treatment created noise, not value

This question usually exposes whether the team is measuring behavior quality or just behavior volume.

### 2. Which metric is the headline, and which metrics get veto power

This is where I borrow a lot from serious experimentation practice.

The [Experiment Guide site for *Trustworthy Online Controlled Experiments*](https://experimentguide.com/) repeatedly emphasizes choosing metrics carefully, including the overall evaluation criterion and the pitfalls of misleading wins. I think growth teams need a simplified version of that discipline even when the test is small.

You need to know:

- what metric is the main decision driver
- what supporting metrics add interpretation
- what guardrails would make you reject an apparent win

If you cannot name the veto metrics before launch, you will be tempted to negotiate with them afterward.

That is how bad wins become roadmap fuel.

### 3. What user segment is most likely to react differently

A lot of experiments average away the most important story.

New users may respond differently than returning users. Power users may tolerate friction that casual users will not. Team buyers may interpret the same prompt differently than solo users.

If the test only “works” because one segment loved it while another was quietly damaged, that is not a detail. That is the result.

I would rather name the likely fault line before launch than discover it later in a defensive readout.

### 4. What must be true in the data for us to trust the result

This is the boring part, which is usually why it matters.

Ask:

- are the critical events firing correctly
- is assignment stable
- do we understand who is entering the test
- are there dependencies on email delivery, CRM sync, or third-party logging
- could bots, internal traffic, or timing artifacts distort the outcome

None of this is glamorous. All of it is expensive to learn after the fact.

### 5. What downstream behavior would make a local lift feel suspicious

This is the retention brain speaking.

Sometimes the test metric improves and that should make you more cautious, not less.

If a nudge increases a conversion step but reduces downstream completion, trust, content quality, or retained usage, the “win” may just be a faster path into disappointment.

This is one reason I have become more cautious about celebrating early funnel lifts in isolation. They can be real and still be strategically wrong.

### 6. What would we do if the result is flat

I like including this because it keeps the team from smuggling hope into the analysis later.

If the result is neutral, what are the most likely interpretations?

- bad idea
- right idea, wrong timing
- right timing, weak execution
- underpowered test
- metric mismatch
- segment dilution

You do not need a perfect answer up front. But writing down the likely explanations makes the post-launch conversation much more honest.

## Why this helps

A premortem does not make the experiment better by magic.

It helps because it forces the team to separate four things that often get blurred together:

- the idea
- the implementation
- the measurement
- the decision rule

Those are different layers.

And when a growth team moves too fast, those layers get bundled into one vague belief that says, “we tested it.”

That sentence hides a lot.

You can test the wrong thing.

You can test the right thing with the wrong metric.

You can test the right thing with the right metric and still draw the wrong conclusion.

That is why I think experiment quality is not only a stats problem. It is a product judgment problem.

## This is especially useful when the org wants wins

The premortem becomes more valuable when the environment gets more politically charged.

Quarter-end pressure.

A new leader watching the dashboard.

A team that needs proof the new onboarding direction is working.

A lifecycle channel that has underperformed for months and finally shows a pulse.

That is when people become most vulnerable to a flattering read of weak evidence.

A small pre-launch document will not eliminate that bias. But it does create a record of what the team said would count before anyone saw the chart.

That is powerful.

It gives the future readout a spine.

## The artifact I’d actually use

If I were running this with a team, I would keep it to one short block:

## Experiment premortem

- Hypothesis:
- Primary metric:
- Guardrails / veto metrics:
- Most likely false-positive story:
- Most likely harmed segment:
- Instrumentation risks:
- Downstream behavior that would invalidate a “win”:
- If flat, first interpretation to check:

That is it.

No big workshop.

No mural board full of sticky notes unless your team really loves that sort of thing.

Just enough structure to catch bad logic while it is still cheap.

## A good sign the premortem is working

The best premortems usually produce one of three outcomes:

- the team sharpens the metric
- the team narrows the target segment
- the team realizes the experiment is combining too many changes at once

None of those outcomes are glamorous.

All of them are useful.

Sometimes the biggest value is discovering that the test should not launch yet.

That can feel slow in the moment.

Usually it is faster than spending two weeks running a test that teaches you almost nothing.

## The point

Growth teams talk a lot about learning velocity.

Fair enough.

But learning velocity is not just about how quickly you can launch tests.

It is also about how often your tests produce conclusions you can trust.

That is why I like the premortem.

It is a small habit that respects a bigger truth:

the cost of a bad experiment is not only that it loses.

It is that it can convince smart people to keep going in the wrong direction with unusually high confidence.
