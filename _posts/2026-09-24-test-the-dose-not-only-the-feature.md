---
title: "Test the dose, not only the feature"
subtitle: "A feature can be useful once and exhausting ten times, which makes intensity part of the product decision."
description: "A growth PM field note on dose response, product intensity, and testing how much of a useful intervention users can actually absorb."
date: 2026-09-24
image: /assets/images/desk.jpg
layout: post
---

I think a lot of product experiments test the noun and ignore the amount.

Show the recommendation or do not show it.

Send the reminder or keep quiet.

Add the assistant or leave the workflow alone.

That binary choice is clean enough for a slide. It is often incomplete as a product decision.

A recommendation can help when there are three and become homework when there are thirty. A reminder can rescue a forgotten task on Tuesday and feel like pestering by Friday. An assistant can remove one tedious step, then make the whole product feel strangely crowded when it appears beside every field.

The feature may work. The dose may be wrong.

## More is a different treatment

Medicine has a much higher burden of proof than product work, and I do not want to flatten that difference. Still, dose finding offers a useful piece of judgment.

The International Council for Harmonisation guidance on [dose response information](https://database.ich.org/sites/default/files/E4_Guideline.pdf) separates evidence that a treatment has an effect from evidence about how effect and harm change across doses. That distinction travels surprisingly well.

In product work, dose can mean frequency, volume, duration, prominence, or how much of a task the product takes over. A weekly summary and seven daily alerts are not just two delivery settings for the same idea. They create different demands on attention and may teach different behavior.

Apple's guidance for [notifications](https://developer.apple.com/design/human-interface-guidelines/notifications) makes a related product point. It recommends avoiding multiple notifications for the same thing because people may turn off all notifications from the app. Relevance is partly about content, but it is also about restraint.

This matters for growth because teams can mistake a local lift for permission to increase the treatment.

One reminder raises completion, so we send three. A carousel earns clicks, so we add more cards. Suggested replies speed up a message, so we put them in every conversation. Each move sounds like scaling a win. At some point the product is no longer scaling the original intervention. It is testing a stronger one without admitting it.

## Product intensity has a curve

I picture most interventions as having a response curve, even when I do not have enough data to draw it yet.

At a very low dose, users may not notice the feature or receive enough help to change what they do. As the dose rises, the benefit can grow. Then it may flatten. Past that point, more exposure can create fatigue, dependence, clutter, mistakes, or opt-outs.

The curve will not be the same for everyone.

A daily reminder may be appropriate for a time-sensitive medication log and absurd for an annual tax checklist. A novice may benefit from more guidance than an expert. A person who asked to be notified has a different relationship with the message than someone whose permission was buried in setup.

This is where product judgment matters more than a universal benchmark. The job is not to find the maximum amount a channel permits. It is to find the smallest dose that reliably helps with the user's job, then learn where additional intensity stops earning its cost.

That is a more useful growth question than asking whether engagement keeps rising. Engagement can rise because the product created more surfaces to touch. It does not tell us whether each additional touch improved the outcome.

## The artifact I want is a dose brief

Before launching an intervention that can vary in intensity, I would write a compact dose brief.

| Decision | Working answer |
| --- | --- |
| User job | Finish a weekly expense review before Friday close |
| Active ingredient | A reminder that names the unfinished review and opens it directly |
| Dose dimensions | Messages per week, delivery channel, and number of unfinished items shown |
| Candidate doses | No message, one message, or up to three messages that stop after completion |
| Intended response | More reviews completed by Friday without extra correction work |
| Benefit measure | Share of eligible reviews completed on time |
| Burden measures | Notification disablement, dismissals, corrections, and support complaints |
| Stop condition | Completion, explicit dismissal, or Friday close |
| Groups likely to differ | New reviewers, experienced reviewers, and people with one versus many open reports |

The phrase active ingredient is deliberate. It forces the team to say what part of the intervention is expected to help.

If the team believes the value comes from restoring context, the deep link and named unfinished task may matter more than another send. If the value comes from timing, adding messages at random hours is not a stronger version of the same idea. It is a blurrier one.

The dose dimensions also keep a common experiment mistake visible. Frequency is not the only form of intensity. A single full-screen interruption may be a higher dose than three quiet items in an inbox. Five recommendations that require separate decisions may be heavier than one summary containing the same information.

## Write the hypothesis around the curve

For the expense review example, I would write the hypothesis this way.

> **Hypothesis** If eligible reviewers receive one contextual reminder while a review is unfinished, more reviews will be completed by Friday than with no reminder. Increasing the dose to as many as three reminders will produce little additional completion and more notification disablement.

That statement makes two claims visible. The intervention may help, and the incremental dose may not.

A clean test could randomly assign eligible reviewers to no reminder, one reminder, or a sequence capped at three. Everyone should face the same eligibility rule and the messages should stop when the job is done. I would compare on-time completion across groups, but I would also inspect correction rates, disablement, dismissals, and next-week completion.

The last measure matters. A heavy dose might pull work forward this week while teaching users to wait for pressure next week. That would be a real behavioral effect, just not the one we intended.

The [review of challenges in online controlled experiments](https://arxiv.org/abs/2212.11366) is a useful reminder that metric choice, novelty, user learning, and longer-term effects can all complicate a tidy readout. A dose test does not remove those problems. It gives the team a more honest treatment definition and a better chance of seeing where benefit bends into burden.

I would resist collapsing the result into one blended average too quickly. New and experienced users may have different curves. People with one unfinished report may need a nudge, while people with twenty need workflow help rather than louder reminders. Segments should come from a plausible difference in the job, not a fishing trip after the result.

## Restraint can be a growth capability

Mid-career product work has made me less impressed by a team that can make a metric move and more interested in whether it knows what the movement cost.

That is especially true when the mechanism is repeatable. Once a notification, prompt, recommendation, or generated suggestion works once, the system makes it very cheap to do it again. Cheap repetition can outrun good judgment.

The United Kingdom Government Service Manual guidance on [sending emails and text messages](https://www.gov.uk/service-manual/design/sending-emails-and-text-messages) advises teams to send messages when users need to know something and to let them act on it. I like the practical standard underneath that guidance. A message has work to do. It is not free attention simply because the address is available.

Sometimes the right result of a dose test will be more. A second prompt may genuinely help. More examples may improve a recommendation. A longer guided mode may help a new user succeed independently.

But more should earn its way into the product.

The growth thesis is not that teams should become timid. It is that intensity is part of the intervention, not a setting to optimize after the important decision has already been made.

Test whether the feature helps. Then test how much help the user can absorb before the product starts creating a second problem.
