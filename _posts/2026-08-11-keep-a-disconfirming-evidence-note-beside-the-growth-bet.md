---
title: "Keep a disconfirming evidence note beside the growth bet"
subtitle: "Why growth teams should name the evidence that would make them stop believing before the dashboard starts telling a flattering story."
description: "A growth PM field note on disconfirming evidence, rollout judgment, and a simple note that helps teams separate conviction from attachment."
date: 2026-08-11
image: /assets/images/notebook.jpg
layout: post
---

I think one of the easiest traps in growth product work is that we get much better at writing the case for an idea than the case against it.

We write the hypothesis.

We define the segment.

We pick the surface.

We decide the metric.

We launch the test.

Then the numbers start moving and the room quietly becomes a courtroom for the idea we already wanted to win.

Every uptick becomes encouraging.

Every flat read becomes inconclusive.

Every concerning signal becomes something to explain away.

I do not think this happens because growth teams are dishonest.

I think it happens because once an idea has design time, engineering time, review time, and political attention sunk into it, the burden of proof starts shifting without anyone saying so out loud.

Now the question is no longer whether the bet is strong.

The question becomes whether the evidence against it is strong enough to slow us down.

That is a much riskier posture.

## Good teams still need a way to disagree with themselves

One reason I keep borrowing from research practice is that research has had to confront this exact human tendency more directly than most product teams have.

The Center for Open Science explains [preregistration](https://www.cos.io/initiatives/prereg) as specifying the research plan in advance so planned and unplanned work stay distinct. I like that framing because it protects a team from using the same data to generate and test the story at the same time.

Product teams do a milder version of that mistake constantly.

We say the test will help us decide.

Then we watch the early data.

Then we adjust the interpretation standard while pretending we are only adjusting our understanding.

Now the same result that would have worried us before launch somehow feels acceptable after launch because we can see a different bright spot nearby.

That is not rigorous learning.

That is motivated reading.

I am not arguing that growth teams need academic preregistration.

I am arguing that they need a simpler discipline that protects judgment before attachment takes over.

## A lot of growth bets become too easy to rescue in the readout

This is especially true when the idea is directionally plausible.

The prompt feels more contextual.

The paywall feels cleaner.

The onboarding step feels shorter.

The lifecycle message feels sharper.

The collaboration ask feels more timely.

Nothing about the concept sounds obviously foolish.

That is exactly why it becomes easy to keep rescuing it.

The clickthrough rate went up, even if the downstream quality slipped.

The conversion step improved, even if the segment we really care about stayed flat.

The usage spike was small, but maybe the test was underpowered.

The guardrail moved the wrong way, but maybe it was noise.

I think a lot of teams tell themselves they are being nuanced in moments like this.

Sometimes they are.

Sometimes they are just negotiating with the evidence.

Microsoft’s guidance on [trustworthy experimentation before a test starts](https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-pre-experiment-stage/) says the hypothesis should be falsifiable by the metrics considered. That sounds obvious. It is also more demanding than many product organizations behave in practice.

A metric set does not really make a hypothesis falsifiable if the team can reinterpret every inconvenient movement after the fact.

## Medicine has a healthier respect for rival explanations

This is one reason I like reading outside product.

In diagnosis, the risk of early certainty is expensive enough that other fields have built explicit habits to interrupt it.

The Agency for Healthcare Research and Quality describes [process-focused checklists](https://www.ahrq.gov/diagnostic-safety/resources/issue-briefs/dxchecklists-3.html) that try to trigger more deliberate thinking, including prompts like asking what else the case could be.

I do not want to stretch the analogy too far.

Product teams are not diagnosing heart attacks.

Still, the cognitive problem is familiar.

The first story arrives.

The story feels coherent.

The confirming details become more visible.

Alternative explanations become harder to see because the team is now organizing attention around the favored interpretation.

Growth work does this all the time.

We think the new onboarding explainer improved activation.

Maybe it did.

Maybe higher-intent traffic arrived that week.

Maybe support quietly compensated for the confusing edge cases.

Maybe the headline metric rose because more people complied with the flow while fewer understood the product.

Maybe the treatment worked for evaluators and weakened the experience for eventual operators.

If the team never writes down what would count as evidence against the idea, it becomes much easier to treat those rival explanations as annoyances instead of decision inputs.

## The hardest part of growth judgment is not shipping

It is unshipping your favorite explanation.

I think this is the part early career product work under-teaches.

We talk a lot about conviction.

We talk a lot about clear bets.

We talk a lot about moving fast.

We talk much less about the craft of withdrawing belief cleanly.

That is a real craft.

It matters because growth work is full of ideas that are believable enough to survive a weak standard of proof.

The prompt probably helps some people.

The checklist probably clarifies something.

The email probably catches a few users at the right time.

The pricing page probably removes a little friction.

Almost any reasonable idea will help somewhere for someone under some condition.

That does not make it a good ship decision.

The bar is higher.

Would we still believe this is the right move after looking directly at the strongest inconvenient evidence it produced.

If the answer is only yes because the team can keep finding escape hatches, I get cautious fast.

## I like a small artifact called a disconfirming evidence note

When a team is about to launch a growth bet that already has a persuasive internal story, I like writing one page before the test starts.

Not a giant review deck.

Not a legal brief for why the team should never take risk.

Just a small note that makes one thing explicit.

What evidence would make us stop believing the current story.

## Disconfirming evidence note

- The hypothesis in one sentence
- The main metric that would support the bet
- The strongest metric or behavior that would argue against it
- The segment whose negative result would matter most
- The rival explanation most likely to produce a flattering but misleading win
- The guardrail movement we are least willing to explain away
- The qualitative evidence that would make the result feel less trustworthy
- The threshold at which a rerun, rollback, or narrower rollout becomes more responsible than a full ship
- What decision we expect to make if the result is mixed rather than clean
- Owner

I like this note because it changes the emotional geometry of the readout.

Instead of asking whether the team can defend the idea, you ask whether the actual result clears the standard the team agreed to when it was still capable of being sober.

That is a better argument.

## This is different from writing a hypothesis

A lot of teams will hear this and say that the hypothesis already does the job.

I do not think it does.

A hypothesis tells me what you believe.

A disconfirming evidence note tells me what could take that belief away.

Those are different documents.

The first one creates forward motion.

The second one protects the decision from becoming a loyalty test.

I have found that many teams are pretty good at the first move and suspiciously weak at the second.

That weakness shows up in familiar ways.

The readout spends most of its time on the metric that moved in the desired direction.

The team describes the negative segment as an edge case even when that segment matters strategically.

The rollout plan is framed as prudent while quietly assuming the organization will never actually use the additional time to invalidate the idea.

The next iteration gets defined before the current interpretation is honestly settled.

That is how a maybe turns into policy.

## It also makes mixed results easier to handle without theater

One thing I appreciate in Microsoft’s [post-experiment guidance](https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-post-experiment-stage/) is the acknowledgement that ship decisions often involve tradeoffs among overall evaluation criteria and guardrails, and that those tradeoffs should be predetermined rather than improvised around a specific result.

That is exactly the spirit I want from a growth team.

Not rigidity.

Predetermined honesty.

Mixed results are normal.

The OEC improves and a guardrail slips.

A new user segment benefits and a return segment does not.

The local conversion lift is real and the downstream quality is murky.

That does not mean the team failed.

It means the team has to decide whether the mixed result matches the standard it agreed to beforehand or only the story it prefers now.

Without that earlier standard, the meeting becomes improv theater.

Every person argues from their current emotional relationship to the bet.

That is rarely where the best product judgment lives.

## Other crafts know how to separate exploration from commitment

A woodworker can dry fit the joints before the glue.

A film editor can try a cut before locking picture.

A scientist can distinguish exploratory work from confirmatory work.

A surgeon can pause for a checklist before the incision.

The common move is not caution for its own sake.

It is preserving a moment where reversal is still psychologically and operationally possible.

That is what I want for growth teams too.

The problem with a lot of modern experimentation culture is not that teams test too much.

It is that they sometimes lose the ability to be surprised by their own counterevidence.

## Before the next growth win gets narrated into inevitability

I think mid-career product judgment gets sharper when you stop asking only whether a bet has a case for it.

Most decent bets do.

The better question is whether you have written down the evidence that would make you stop telling yourself the case still holds.

That is the note I want sitting beside the dashboard.

Not because pessimism is noble.

Because interpretation is slippery and success stories are cheap.

A growth team does not become rigorous when it learns how to argue for its idea with more confidence.

It becomes rigorous when it can meet inconvenient evidence without immediately hiring itself as defense counsel.
