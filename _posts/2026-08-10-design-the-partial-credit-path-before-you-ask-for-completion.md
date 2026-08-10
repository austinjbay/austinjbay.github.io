---
title: "Design the partial credit path before you ask for completion"
subtitle: "Why growth teams should preserve unfinished work, honor smaller wins, and give users a believable way to keep going before they finish the whole journey."
description: "A growth PM field note on partial progress, incomplete setup, and a simple partial credit path that helps users keep momentum when full completion is too much to ask."
date: 2026-08-10
image: /assets/images/notebook.jpg
layout: post
---

I think a lot of growth teams quietly assume that incomplete work has no value.

The user finished setup.

The user invited the team.

The user published the page.

The user completed the profile.

The user connected the integration.

That framing sounds tidy.

It is also one of the easiest ways to lose people who were actually trying.

In many products, the user does not abandon because they rejected the value.

They abandon because the product only knows how to recognize the fully completed version of the job.

Half the import is done.

Three of six fields are filled.

One teammate accepted the invite and two did not.

The first workflow draft exists, but it is not polished.

The account is configured enough to be useful, but not configured enough to satisfy the system.

If the product treats that state as basically zero, the user starts to feel like their effort disappeared.

That is a dangerous moment.

Not because the user is lazy.

Because the product failed to preserve momentum.

## Many growth systems are harsher than good teachers

School is full of arguments about grading, but one thing good teachers understand is that partial credit is often a measurement choice, not charity.

It distinguishes between no understanding and some understanding.

It gives the learner evidence that part of the work is already real.

It makes the next step feel closer.

Products need the same judgment.

A lot of onboarding and activation flows behave like an exam graded only on perfect completion.

Either you finished the whole checklist or you did not.

Either the workspace is fully configured or it is not.

Either the first project shipped or it did not.

Either the listing is live or it is not.

That is convenient for dashboards.

It is not always honest about user effort.

I think this is one reason some growth funnels look more fragile than the product experience actually is.

The system throws away signal that the person was partway in.

Then the team treats incomplete work as lack of intent, when a lot of the time it was just an overloaded afternoon.

## Government service design is often more respectful of unfinished work than SaaS

This is one of those slightly embarrassing comparisons for software teams.

When people fill out a serious government service, the system often assumes interruption will happen.

Life happens.

People get pulled into school pickup.

They need to find a document.

They get tired.

They want to check something with a partner before continuing.

The [GOV.UK guidance on saving progress](https://www.sign-in.service.gov.uk/documentation/design-recommendations/save-progress) treats that as normal. The point is not merely storing state in a database. The point is giving users a sanctioned way to stop without losing the work that already counts.

The [ONS save and sign out pattern](https://service-manual.ons.gov.uk/design-system/patterns/save-and-sign-out) makes the same idea operational. Save what the user has already submitted, clear the session safely, and make the return path explicit.

I think a lot of growth products could learn from that posture.

Not every product needs a formal save and return flow.

But many products do need the underlying respect.

If a user gets eighty percent through setup, the product should know how to hold that value, explain what is preserved, and make resumption lighter than the original attempt.

That is not bureaucracy.

That is product empathy.

## E commerce learned this lesson the hard way

Checkout is one of the clearest examples of what happens when systems demand too much continuity.

Baymard’s research on [reducing cart abandonment](https://baymard.com/learn/reduce-cart-abandonment) keeps pointing back to the same problem. Long, complicated flows create drop off even when the user already wants the thing.

I think product teams sometimes misread that kind of abandonment.

They assume the desire went away.

Often the desire stayed and the friction won.

That matters outside commerce too.

A user can want the dashboard.

Want the AI workspace.

Want the team account.

Want the automation.

Want the habit.

And still not have enough uninterrupted attention to complete the whole ceremony in one sitting.

If the system only values the completed checkout, the completed onboarding, or the completed setup, then any interruption turns into emotional waste.

The user comes back feeling farther away than they actually are.

That is one of the most expensive illusions a product can create.

## Progress has to survive interruption

The reason I keep coming back to Teresa Amabile and Steven Kramer’s piece on [small wins](https://hbr.org/2011/05/the-power-of-small-wins) is that it gets at something growth work often misses.

Progress is motivational when people can feel it.

Not when the analytics team knows it happened.

When the person doing the work can tell that the last effort still counts.

That is the difference between a setup flow that says nothing until the very end and a setup flow that keeps handing the user proof.

Your draft is saved.

Your domain is connected.

Two sources are imported.

Your teammate accepted the invite.

Your preferences are set.

You can continue later without starting over.

Those are small wins.

They are also anti churn infrastructure.

I think a lot of teams only think about proof after the first full success event.

That is too late.

Users often need proof while they are still incomplete.

## Ability gets more important when the finish line moves farther away

BJ Fogg’s [Behavior Model](https://www.behaviormodel.org/home) is useful here for the same reason it is useful in most growth conversations. Behavior needs motivation, ability, and a prompt at the same time.

When a user is midway through a long setup, motivation is usually decaying.

The clock is moving.

The novelty is fading.

A Slack ping arrives.

Dinner is almost ready.

The kid wakes up.

The beautiful, intentional onboarding journey now has to compete with ordinary life.

That is when ability matters more.

Can the user pause safely.

Can they come back to a smaller next move instead of the whole burden.

Can they resume from where they left off.

Can the product tell them what is already done and what remains.

Can the system grant partial credit in a way that reduces the psychological cost of continuing.

If not, the prompt lands on a user whose task just became too heavy.

The growth team may call that weak activation.

I think the more honest label is unfinished design.

## Other crafts preserve work in progress on purpose

Musicians mark passages they need to revisit.

Woodworkers dry fit before final glue.

Game designers use checkpoints.

Tax software saves a return before every section is complete.

Good physical therapists do not tell a patient that the session only counts if they complete the full sequence at full intensity.

They bank the rep that happened.

They preserve the routine.

They set up the next safe move.

That is what mature product systems do too.

They do not confuse interrupted work with worthless work.

They assume continuity is fragile.

Then they design accordingly.

## The artifact I like is a partial credit path

When a team is designing onboarding, activation, checkout, workspace setup, or any other multi step journey, I like writing the partial credit path before launch.

Not as a giant strategy memo.

Just as a small artifact that forces the team to answer one uncomfortable question.

If the user cannot finish in one clean pass, what still counts and how will the product prove it.

## Partial credit path

- What user effort should count even if the full flow is incomplete
- What work is already recoverable in the current system and what work still gets lost
- What visible proof tells the user their partial progress is real
- What smaller valid state can unlock value before full completion
- What exact point should offer save and return, draft mode, or another lighter continuation path
- What prompt should bring the user back, and what should it say about preserved progress
- What information should be prefilled, resumed, or skipped on return
- What metric should distinguish interrupted progress from true abandonment
- What user segment is most likely to need partial credit because their setup context is busy, collaborative, or slow moving
- What team owns the recovery experience after the user leaves mid flow

That is enough to make the problem visible.

The point is not to celebrate half done work forever.

The point is to stop treating every interruption like a reset.

## This changes the growth conversation

Once the partial credit path exists, a better set of questions shows up.

Are we asking for too much before the user can bank a real win.

Do we know which incomplete states still deserve a lifecycle message, a nudge, or a saved draft reminder.

Are we measuring abandonment when we should really be measuring paused progress.

Does the user have a believable reason to return, or are we only sending reminders into a blank emotional space.

Did the product preserve the work, or did the user have to preserve the motivation.

That last question matters more than most dashboards admit.

Strong growth teams do not only remove friction from the happy path.

They also protect the value of effort that happens on an ordinary, interrupted Tuesday.

Before you optimize completion, ask one more question.

What part of the work deserves to count before the finish line.
