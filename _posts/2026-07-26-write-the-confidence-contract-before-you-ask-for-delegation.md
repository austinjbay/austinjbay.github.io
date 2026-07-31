---
title: "Write the confidence contract before you ask for delegation"
subtitle: "Why growth teams should define where the product is reliable, where it is guessing, and what the user should still verify before automation becomes part of the job."
description: "A growth PM field note on AI assisted workflows, overtrust, and a simple confidence contract that helps teams earn delegation instead of assuming it."
date: 2026-07-26
image: /assets/images/desk.jpg
layout: post
---

I think one of the easier ways to damage product trust right now is to ask the user to delegate judgment before the product has earned the role.

The UI looks calm.

The recommendation sounds fluent.

The draft feels complete.

The summary arrives fast.

The ranking looks precise.

The suggested next step appears sensible.

That surface polish is useful right up until it persuades the user to stop checking.

That is the part I think growth teams need to treat with more seriousness.

A lot of modern product growth is no longer about getting the user to click one more button. It is about getting them to hand a piece of thinking to the system.

Pick the leads worth calling.

Draft the follow-up.

Group the feedback.

Recommend the lesson.

Flag the risk.

Choose the next action.

Those are not only convenience features.

They are delegation moments.

And every delegation moment carries a quiet question.

What level of trust is this product asking for right here.

## Delegation is a growth move, not only an AI design detail

I think this gets missed because teams talk about AI as a feature layer when it often behaves more like a growth layer.

If the recommendation is good, the user reaches value faster.

If the draft is strong, the first useful outcome arrives earlier.

If the sorting is reliable, the user experiences competence before they have built their own system.

If the product can shoulder a piece of the job, activation can feel lighter and repeated use can become more likely.

That is growth leverage.

It is also a product judgment problem.

The leverage only holds if the user knows what kind of reliance is safe.

The Google PAIR chapter on [Explainability and Trust](https://pair.withgoogle.com/guidebook-v2/chapter/explainability-trust/) is useful here because it keeps returning to trust calibration, not trust maximization. I like that distinction. The job is not to make the user trust the system as much as possible. The job is to help them trust it to the right degree for the task in front of them.

That difference matters a lot in growth product.

A lot of teams still celebrate the moment the user adopts the AI assistance without asking whether the user adopted the right posture toward it.

Did they understand what the system was actually good at.

Did they know what still needed human judgment.

Did they have a way to verify the output when the stakes were real.

Did the product make the boundaries visible before the failure taught the lesson the hard way.

If not, the activation may be real and still fragile.

## Products often ask for one kind of trust and earn another

I have seen this pattern in products that summarize calls, draft emails, score accounts, recommend content, generate plans, and rank opportunities.

The product earns trust on fluency.

The user interprets that fluency as correctness.

Then the team is surprised when a miss creates a disproportionate trust drop.

That trust drop is not irrational.

It is often the first moment the user realizes the contract was never stated clearly.

The review article [How transparency modulates trust in artificial intelligence](https://pmc.ncbi.nlm.nih.gov/articles/PMC9023880/) is helpful because it separates trust from trustworthiness and points out two opposite failure modes. People can under-trust a useful system or over-trust a fallible one. Growth teams usually worry more about the first problem because adoption is visible on the dashboard. The second problem is just as expensive. It hides until the user delegates too much, gets burned, and becomes harder to win back.

This is why I keep thinking about restaurant menus.

Good menus do not only try to sell you the dish.

They help you understand what kind of dish it is.

Rich or light.

Spicy or mild.

Small plate or main course.

Shared or individual.

The menu is not dumping kitchen details on you.

It is helping you make the right use of the recommendation.

AI product surfaces need the same quality.

Not more explanation for its own sake.

Better framing for the decision the user is about to outsource.

## The dangerous moment is when confidence gets inferred instead of communicated

When teams say users need to trust the system, I think what they usually mean is users need to know how to use the system safely.

Those are different things.

The first is emotional.

The second is operational.

The automation bias review in the [Journal of the American Medical Informatics Association](https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/) still travels well outside healthcare because it shows the same human pattern you see in product work. People can over-accept automation, especially under complexity, time pressure, and high workload. One of the useful details in that review is that mitigations included better presentation, clearer confidence cues, and stronger user accountability.

That sounds academic.

It is also deeply practical.

A user moving fast through an inbox triage tool, a CRM copilot, or a lesson generator is living in exactly the kinds of conditions that make uncritical acceptance more likely.

They are busy.

They want relief.

The product sounds sure of itself.

Why would they slow down unless the product gave them a reason to.

That is why I think the most dangerous confidence signal in an AI product is often the one you never explicitly designed.

It is the confidence the user infers from tone, speed, formatting, or placement.

The recommendation sits at the top of the page, so it feels blessed.

The draft appears fully formed, so it feels reviewed.

The summary uses clean prose, so it feels faithful.

The score has decimals, so it feels precise.

The task label says best next step, so it feels validated.

None of those cues are neutral.

They are all part of the confidence contract whether the team writes the contract down or not.

## Other disciplines are stricter about what delegation means

Pilots use autopilot without confusing it for a substitute for situational awareness.

Clinicians use decision support without pretending the interface owns the whole diagnosis.

Editors use spellcheck without assuming it understands the sentence better than they do.

Ops teams use dashboards without assuming every green light means the system is healthy.

Those disciplines are not anti-automation.

They are clearer about the boundary between assistance and authority.

That boundary is where a lot of product growth work still feels underdesigned.

I think that is partly because the local metric makes the handoff look successful.

The user used the feature.

The task completed faster.

The assisted workflow retained better than the manual workflow.

Good.

Keep all of that.

Then ask the harder question.

What kind of decision power did the user quietly hand over in order to get that lift.

If the team cannot answer that clearly, the product may be scaling convenience faster than judgment.

## The artifact I like is a confidence contract

When a team is adding AI help to a core path and the conversation starts drifting into vibes, I would write a confidence contract.

Not a policy memo.

Not a trust principles deck.

Not a giant responsible AI framework.

Just a small working artifact that forces the product team to be specific about the delegation they are asking for.

## Confidence contract

- The user decision this output is trying to influence
- What the system is actually good at in this context
- What the system is still weak at
- What evidence the product can show with the output
- What the user should verify before acting
- What level of consequence exists if the output is wrong
- Whether the output should guide, recommend, draft, rank, or act
- What fallback path exists when confidence is soft
- What language should lower certainty instead of implying authority
- What telemetry would tell us users are over-relying or ignoring wisely
- Owner

That is usually enough to improve the product conversation.

The point is not to generate compliance theater.

The point is to make the delegation legible before the user has to reverse engineer it from a failure.

## This changes the product choices you make

Once the confidence contract exists, a few things usually get easier.

You get clearer about where AI belongs in the journey.

Some moments want automation.

Some want recommendation.

Some want a draft.

Some want the human to stay fully in charge.

You get less attached to polished certainty.

Sometimes the better experience is a recommendation with visible reasons, alternatives, and an easy path to edit.

Sometimes the better experience is a rough first pass that clearly says review me.

Sometimes the better experience is no AI at all on the first run because the user has not built enough context to judge whether the help is good.

You also get better at sequencing proof.

The UK government guidance on [ethics, transparency, and accountability for automated decision making](https://www.gov.uk/data-ethics-guidance/ethics-transparency-and-accountability-framework-for-automated-decision-making) is written for a very different environment, but I think one of its lessons travels well. Teams should be explicit about purpose, limitations, oversight, and routes for review. Consumer and B2B products may not need the same formal machinery, but they do need the same habit of naming what the system is doing, where it should be trusted, and how a person can contest or correct it.

That is not bureaucracy.

That is product clarity.

It also tends to improve experimentation quality.

If a treatment lifts assisted usage, you can ask more intelligent follow-up questions.

Did the lift come from reducing effort.

Did it come from better decision quality.

Did it come from stronger perception of competence.

Did it come from users over-delegating in a way that will create future distrust.

Without the contract, those outcomes can look the same at first.

## The signal to watch is not only adoption

I think one of the bigger traps in AI flavored growth work is to stop the analysis at usage.

People clicked accept.

People sent the draft.

People used the recommended path.

People kept the default.

Fine.

Now I want to know a few more things.

How often did they edit before accepting.

How often did they reverse the action later.

How often did they seek a second source.

How often did the assisted output get used in higher consequence cases than the team intended.

How often did trust collapse after the first obvious miss.

Those are not secondary details.

They are part of the core growth truth of the feature.

A product that accelerates first use by borrowing against future trust has not solved the right problem.

It has just front-loaded the feeling of progress.

## Before you ask for one more act of delegation

I think good growth teams are going to get more comfortable with a slightly less glamorous question than how do we increase AI adoption.

The better question is what kind of delegation have we earned.

That question is slower.

It is also more honest.

If the product can reliably take a low consequence sorting job off the user’s plate, great.

If it can draft something useful that still needs review, say that.

If it can spot patterns but not make the final call, design for that boundary.

If it cannot yet support safe delegation in a core workflow, do not let tone and polish pretend otherwise.

The confidence contract will not make the system smarter.

It will make the team more precise about the trust it is requesting.

That precision is a growth advantage.

It helps users adopt the feature with clearer expectations.

It protects the product from brittle overtrust.

And it gives the team a better chance of earning a role in the workflow that lasts longer than the novelty of the demo.
