---
title: "Write the waiting-state brief before you ask the user to be patient"
subtitle: "Why growth teams should design the period between user effort and user payoff with the same care they give the click that started it."
description: "A growth PM field note on delayed value, waiting-state design, and a simple artifact that helps teams turn uncertainty into legible progress."
date: 2026-07-28
image: /assets/images/desk.jpg
layout: post
---

I think growth teams often talk as if value arrives right after the click.

The page persuades.

The user signs up.

The setup starts.

The workflow begins.

The product wins.

But a lot of real products do not work like that.

The import needs time.

The data has to sync.

The teammate has to reply.

The payment has to clear.

The AI draft has to process.

The approval has to come back.

The account has to warm up enough for the product to actually prove itself.

That stretch matters more than many teams admit.

I think a lot of early growth loss happens in the waiting state.

Not because the product failed to start the job.

Because it failed to explain what was happening while the user was waiting for the job to finish.

## A delayed outcome is still part of the product

This feels obvious when you say it plainly, but teams still behave as if the digital part of the experience ends at submission.

GOV.UK has a useful line in its guidance on [measuring user satisfaction](https://www.gov.uk/service-manual/measuring-success/measuring-user-satisfaction). Sometimes the end of a transaction is not the end of the user’s experience with the service.

I think that idea should show up in more growth reviews.

The user completed the form.

Fine.

The user connected the source.

Fine.

The user clicked generate.

Fine.

None of that means the product has delivered value yet.

If the meaningful outcome lands later, the waiting period is not dead space.

It is part of the product promise.

That is where expectation either matures into trust or curdles into suspicion.

A lot of products still treat that period like a loading spinner plus hope.

That is thin design.

## The wait is where motivation gets converted into interpretation work

This is the part I keep noticing.

Once a user has already made an effortful move, they start asking a new set of questions.

Did it work.

How long should this take.

Is the system actually doing something.

What should I do while I wait.

Will I lose my place if I leave.

What happens if this fails.

Can I trust the result when it appears.

If the product does not answer those questions, the user has to do interpretation work instead.

They refresh.

They retry.

They wonder whether the product is stuck.

They open support.

They hesitate to bring teammates in.

They decide the tool feels shaky even if the underlying system is technically fine.

I think this is one reason some activation wins look weaker in the wild than they did in the funnel.

The team improved starts.

It did not improve waiting confidence.

## Infrastructure teams are often more honest about waiting than product teams are

I like borrowing from payments here because the logic is so clean.

Stripe’s documentation on [payment methods](https://docs.stripe.com/payments/payment-methods?locale=en-GB) distinguishes between immediate confirmation and delayed notification. Some methods stay in `processing` until the payment actually succeeds or fails, and Stripe recommends holding the order in a pending state until the outcome is real.

That is not just payment plumbing.

It is product truth.

The system should be honest about what is known, what is not known yet, and what happens next.

I think a lot of growth surfaces blur those states.

They celebrate too early.

They imply success when the job is merely underway.

They hide uncertainty because they are afraid it will hurt conversion.

Then the user experiences the correction later, which usually costs more trust than a candid waiting state would have.

There is a product lesson in that.

Do not collapse started, processing, succeeded, and failed into one mushy emotional message.

Those are different realities.

The user can handle the truth better than the ambiguity.

## Good waiting states make the system legible

Apple’s guidance on [displaying progress](https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/DisplayProgress.html) is old, but it still makes the right point. Long operations should not run invisibly. Progress information should tell the user what is happening and what work remains.

That matters outside software tooling too.

A good restaurant pickup counter tells you whether your food is being prepared, bagged, or ready.

A good airport gate tells you whether boarding is delayed, whether the delay is weather, crew, or maintenance, and when the next update will come.

A good package tracker does not merely say not yet.

It leaves a trail of state changes that help you understand where your thing is and whether the system is behaving normally.

Products should do the same.

I do not mean every wait needs a detailed progress bar.

Some jobs are not predictable enough for that.

But the product should still make four things clear.

What just happened.

What the system is doing now.

What the user should expect next.

What the user can safely do in the meantime.

That is enough to calm a lot of unnecessary doubt.

## Waiting time has its own hidden math

This is where operations thinking becomes useful.

John Little’s discussion of [Little’s Law](https://www.nationalacademies.org/read/1867/chapter/22) is about queuing systems, but the product intuition travels well. More work inside a system usually means more time spent waiting inside it.

I think growth teams run into a user facing version of that all the time.

We add more setup checks.

We add more enrichment.

We add more generated options.

We add more approval steps.

We add more background jobs because the product is becoming more capable.

Then we still design the user experience as if the output should feel immediate.

That mismatch creates a strange product lie.

The system grows more complex.

The interface keeps pretending nothing has changed.

Soon the user is sitting in a bigger queue with less explanation than before.

I do not think every queue needs to be shorter before it becomes more usable.

Often it first needs to become more legible.

## A vague wait can poison retention before the user even decides whether the product is good

This is one of the more underdiscussed growth problems.

When a user is waiting, they are not only waiting for the output.

They are learning what kind of relationship this product is going to have with uncertainty.

Does it go quiet when things take longer than expected.

Does it preserve my work if I leave.

Does it explain who has the baton now.

Does it know the difference between progress and completion.

Does it give me a safe next move if the wait stretches out.

Those signals shape future willingness.

A product with great waiting behavior often feels more trustworthy than a faster product with poor waiting behavior.

That sounds backwards until you live it.

A calm tracker can beat a fast but opaque workflow.

A believable pending state can beat a fake instant success that gets revised later.

A clear note that a teammate must act next can beat a generic dashboard that hides the dependency.

I think this matters a lot in collaborative products, AI products, and any product where the first real payoff depends on work happening off screen.

## The artifact I like is a waiting-state brief

When a team keeps losing momentum between user effort and user payoff, I would write a waiting-state brief.

Not a giant journey map.

Not a full service blueprint.

Just a small working artifact for one important flow with delayed value.

An import.

An AI generation path.

A trial setup that depends on data backfill.

An invite flow that needs another person.

A payment or approval path with real processing time.

## Waiting-state brief

- The user action that starts the wait
- What outcome the user believes they are waiting for
- What the system is actually doing during that period
- What states are real and distinct
- What the user should see immediately after submission
- What level of timing confidence is honest
- What proof shows the job is still alive
- What the user can do next without breaking anything
- What should happen if they leave and come back later
- What message appears if the wait is normal but long
- What message appears if the job fails or needs intervention
- Evidence from support, analytics, research, or replay
- Owner

That is usually enough to surface the gaps.

You find places where the product is saying success when it only means accepted.

You find places where the system has rich internal state and the user gets none of it.

You find places where lifecycle messages are compensating for a weak in product wait.

You find places where users are retrying not because they are impatient, but because the product gave them no reliable signal that patience was safe.

## This changes how I think about activation

I still care about getting users to start.

Obviously.

But I trust an activation moment more when the product can carry the user through the period after the start without dropping the thread.

If the first meaningful win depends on waiting, the activation design is incomplete until the wait is designed too.

That can mean better status language.

It can mean clearer state restoration.

It can mean email or in product updates when the job completes.

It can mean telling the user to come back tomorrow instead of pretending everything will resolve in thirty seconds.

It can mean being more candid about dependencies that sit with a teammate, a bank, a model, or a back office process.

The point is not to romanticize slowness.

The point is to stop treating waiting as a blank space between the important moments.

For a lot of products, especially the more ambitious ones, the wait is one of the important moments.

If the product handles it badly, users do not only learn that the system is slow.

They learn that the product is hard to trust when the answer is not immediate.

That is a deeper problem.

And it usually starts earlier than the retention chart makes it look.
