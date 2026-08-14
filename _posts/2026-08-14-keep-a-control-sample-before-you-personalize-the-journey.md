---
title: "Keep a control sample before you personalize the journey"
subtitle: "Why growth teams should save a small set of canonical good outcomes before they ask AI, lifecycle logic, or onboarding automation to scale taste."
description: "A growth PM field note on using a control sample pack to keep personalization, AI assistance, and growth automation anchored to what good actually looks like."
date: 2026-08-14
image: /assets/images/notebook.jpg
layout: post
---

I think one of the easiest ways for a growth team to create sophisticated nonsense is to automate before it has preserved a clear example of good.

The product can draft the message.

The assistant can recommend the next step.

The onboarding can adapt to the account.

The lifecycle system can tailor the nudge.

The ranking model can choose what to show first.

All of that can look advanced.

Then you ask a very simple question.

Advanced toward what.

That is the part I think teams skip.

They want personalization.

They want dynamic onboarding.

They want AI assistance.

They want a smarter growth loop.

They want the system to sound more human and more relevant and more helpful.

Good.

But if the team has not kept a small control sample of what a genuinely good outcome looks like, the product usually starts optimizing toward vibe instead of judgment.

The result sounds tailored.

It does not always sound right.

## A lot of personalization fails because the target stayed implicit

I do not mean the team lacks opinions.

Usually it has too many.

One marketer likes crisp copy.

One PM likes more explanation.

One sales lead wants urgency.

One designer wants fewer words.

One founder wants the product to sound ambitious.

One support teammate wants it to stop creating replies that need cleanup.

The system inherits all of that fog.

Then the team acts surprised when the output is inconsistent.

I keep seeing this in onboarding, lifecycle, search, AI drafting, templates, recommendations, and team products that are trying to adapt to different roles.

The product gets told to be helpful.

Helpful for whom.

In what moment.

By what standard.

Against which example.

OpenAI’s guidance on [prompt engineering best practices](https://help.openai.com/en/articles/6654000-comprehensive-step-by-step-guide-to-prompt-engineering-with-chatgpt) makes a point I think travels well beyond prompt writing. Models respond better when you show the desired format through examples, not only when you describe it abstractly. That is a useful product lesson too.

A growth team can talk all day about relevance, clarity, motivation, or brand voice.

One concrete example of a strong output usually teaches more than a meeting full of adjectives.

## Other fields keep a known good reference on purpose

Labs keep controls because without a reference condition it gets much harder to tell whether a result is real.

Editors keep exemplars because style guides alone do not fully capture taste.

Kitchen teams taste the sauce because the recipe is not the same thing as the current batch.

Machine learning teams keep labeled examples because the system needs grounded signals, not only aspirations.

Google’s introduction to [supervised learning](https://developers.google.com/machine-learning/intro-to-ml/supervised) is basic in a good way here. The model learns from labeled examples and gets evaluated against known answers, not against a cloud of well-meant interpretation.

That sounds obvious in ML.

I think growth teams abandon that discipline the minute the conversation moves into lifecycle, onboarding, or product messaging.

We ask a system to personalize the welcome note without preserving a few examples of welcome notes that actually earned a reply.

We ask AI to draft follow-up copy without saving examples that match the product’s real level of confidence.

We ask onboarding logic to adapt to segment differences without keeping reference journeys for what good setup looks like for each segment.

We ask a recommendation system to choose the next best action without a small benchmark set of actions a thoughtful operator would have chosen.

Then the product drifts.

Not because the system is mysterious.

Because the team never pinned down the standard tightly enough for drift to be visible.

## Growth teams need something closer to a benchmark set for judgment

One reason I like borrowing from AI evaluation work is that it forces a more honest question.

How will you know the system is getting better.

Google Cloud’s documentation on [golden datasets and context evaluation](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-mysql/build-context-gemini-cli) is aimed at data agents, not product onboarding or lifecycle design. The transferable idea is still strong. You keep a stable set of known questions and expected answers so you can tell whether context changes actually improved the system.

That is the posture I want more growth teams to adopt.

Not because every growth problem is an ML problem.

Because every automation problem eventually becomes a judgment problem.

If you change the onboarding brief, the CRM prompt, the recommendation logic, the plan selection rules, or the lifecycle copy, what stable sample are you checking against.

What set of examples lets you say this got sharper rather than merely different.

A lot of teams answer that question with aggregate metrics only.

Open rate.

Activation rate.

Clickthrough.

Assisted adoption.

Those matter.

They are not enough.

Metrics can tell you that something moved.

They are slower at telling you that the system learned the wrong lesson.

## Examples do more than constrain the model

The obvious use of a control sample is to steer the system.

I think the better use is to align the humans.

Google PAIR’s guide on [explainability and trust](https://pair.withgoogle.com/guidebook-v2/chapter/explainability-trust/) notes that examples can help people understand surprising results and decide how much to trust the system. That matters inside the team too.

A good control sample pack makes taste discussable.

Now product can point to the onboarding state that feels appropriately light.

Lifecycle can point to the reminder that sounds confident without sounding needy.

Support can point to the AI draft that still preserves the important caveat.

Design can point to the recommendation block that is legible without pretending certainty.

Data can point to the ranking output that reflects real user intent rather than reporting convenience.

Without that pack, teams use proxy arguments.

Too wordy.

Too robotic.

Too generic.

Too salesy.

Too complex.

Those critiques are not wrong.

They are just weakly portable.

A shared set of examples turns aesthetic disagreement into product judgment.

It gets much easier to say this draft over-explains compared with our strong examples for a returning evaluator, or this recommendation is underspecified compared with the operator quality bar we already agreed on.

That is a healthier conversation than debating vibes from scratch every week.

## The control sample should represent the hard edges, not only the shiny cases

This is where teams often make the artifact too flattering.

They save the elegant examples.

They save the clean segment.

They save the easy persona.

They save the success case that everyone already knows how to serve.

Then they wonder why the automation looks smart in demos and brittle in the field.

If the sample is supposed to defend judgment, it needs to include awkward reality.

The hesitant team admin.

The confused evaluator with partial setup.

The user who needs a reminder without wanting a lecture.

The account with messy data.

The prospect that is real but still not a fit.

The user asking the product to do something it can partly do and partly cannot.

This is another reason the article on [using examples in prompt engineering](https://help.openai.com/en/articles/6654000-comprehensive-step-by-step-guide-to-prompt-engineering-with-chatgpt) matters beyond prompting. A few strong examples can define the format. The wrong few examples can quietly define the wrong product posture.

A control sample pack is not a trophy shelf.

It is a working representation of the judgment your product needs to preserve under pressure.

## The artifact I like is a control sample pack

When a team is trying to scale personalization, AI help, or adaptive onboarding and the quality conversation keeps collapsing into taste debates, I would make a control sample pack.

Not a giant taxonomy.

Not a full prompt library.

Not a monster content repository nobody maintains.

Just a compact set of canonical examples for the moments where product judgment matters most.

## Control sample pack

- The user moment or job to be done
- The segment or context that makes the example relevant
- The output the product currently produces
- The version a strong human operator would consider good
- What makes the good version good
- What tradeoff it is making on purpose
- What failure mode the example is protecting against
- Whether the sample is for onboarding, lifecycle, AI drafting, ranking, or recommendations
- Which examples are edge cases the system must still handle well
- Review owner

The point is not to freeze the product.

The point is to give the product a known reference while it evolves.

That reference helps in at least three ways.

It gives automation a clearer target.

It gives review a faster rubric.

It gives experimentation a way to detect when the system is winning the metric while losing the craft.

## This changes the way growth teams talk about quality

Once the pack exists, better questions show up.

Which examples are now outdated because the product matured.

Which segments are missing from the pack even though the automation touches them every day.

Which output got the metric lift by sounding more persuasive when it should have sounded more honest.

Which recommendation became more efficient by hiding uncertainty the user still needed to see.

Which onboarding variation looks personalized but actually strips away the context that helped serious users decide well.

I like those questions because they are about judgment in motion.

Not frozen taste.

Not static documentation.

Not a ritual for its own sake.

Just a way to keep the team honest about what good is while the machine gets more freedom to improvise.

That feels increasingly important to me.

A lot of growth work now involves teaching systems how to act on our behalf.

Before you ask the system to get more adaptive, more automated, or more persuasive, save a few examples of the behavior you would still be proud to defend by hand.
