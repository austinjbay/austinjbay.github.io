---
title: "Test the representation, not only the flow"
subtitle: "The same product state can become more useful when it is shown in a form that fits the decision."
description: "A practical representation fit brief for testing whether the form of information helps users make the decision they came to make."
date: 2026-11-24
image: /assets/images/notebook.jpg
layout: post
tags: [Product Discovery]
---

I have spent a fair amount of my career trying to make flows shorter.

Fewer fields. Fewer clicks. A cleaner path from landing page to first useful action. That work often matters. It is also easy to reach for when the real problem sits somewhere else.

Sometimes the user has all the information they need and still cannot see what to do.

Imagine a planning product for small teams. A new manager imports twelve projects, assigns owners, and adds due dates. The setup funnel looks healthy. The next screen shows a tidy list of project names with a status beside each one. Nothing is technically missing.

But the manager came to answer a spatial question about time. Which commitments collide in the same week, and where will the team run out of room?

A list makes every project legible one at a time. It does not make the collision visible. The product has delivered the data without yet delivering the decision.

Growth teams can misread this moment as weak intent. We add a reminder, move the button, or shorten setup again. I have done versions of all three. The better question is whether the product is showing the work in a form that fits the work the person is trying to do.

## Information has a shape

Cartographers have lived with this problem for a long time. A map is not the territory copied onto paper. It is a representation built for a particular extent and use.

The U.S. Geological Survey explains that cartographic generalization reduces detail so the right amount of information can be shown clearly at a given scale. Roads, streams, and buildings may all be present in the underlying data, yet they cannot all receive equal treatment on every map. [The USGS overview of multiscale representation describes selection and simplification as part of making a usable map](https://www.usgs.gov/centers/cegis/science/multiscale-representation).

That is a useful correction for product teams. We often treat a table, feed, calendar, map, graph, and board as interchangeable containers with different visual styling. They are not. Each one makes certain relationships cheap to perceive and others expensive.

A table is good at exact lookup. A timeline makes overlap and sequence easier to see. A map makes distance and adjacency available at a glance. A board can expose concentration and movement. The underlying records may be identical while the work required from the user changes substantially.

Information systems research gives this idea a more formal footing. Iris Vessey's work on cognitive fit argues that performance improves when the representation emphasizes the kind of information a task requires. Graphs tend to foreground spatial relationships while tables foreground symbolic values. The important claim is not that graphs are better. It is that a representation should be judged against the task. [The original cognitive fit paper connects matched representations with faster and more accurate problem solving](https://onlinelibrary.wiley.com/doi/10.1111/j.1540-5915.1991.tb00344.x).

Air traffic control makes the stakes easier to see. Controllers do not need information arranged according to whichever database table was easiest to expose. They need a display that supports a time-sensitive job. The Federal Aviation Administration's human factors standard says information used in a spatial or chronological order should preserve that order on screen. It also recommends integrating data that must be used together rather than scattering it across separate displays. [The FAA standard ties display arrangement directly to the task being performed](https://hf.tc.faa.gov/publications/2016-12-human-factors-design-standard/full_text.pdf).

Most growth products are not control towers. Still, the same design mistake appears at lower stakes. We make the user mentally join information that the product already has. Then we measure the hesitation created by that translation and call it friction.

## The default view is part of the value proposition

Return to the planning product.

The list view is not bad. It may be exactly right for changing an owner or finding a project by name. It is simply a poor first representation for spotting a crowded week.

This distinction matters because a common growth response would be to add a calendar as another view and let users choose. Choice sounds respectful. It can also move the representation problem onto the person who knows the product least.

An experienced operator may know to switch views before checking capacity. A new manager may assume the default view is the product. If the value is only visible after discovering a control, naming an unfamiliar view, and translating the task into product language, our acquisition message has promised something our first experience has hidden.

The default is therefore not neutral. It is a claim about what matters now.

I would not make every interface dynamic or personalize a view from a thin signal. That creates its own confusion. I would start by naming the decision behind the session and asking which representation makes the evidence for that decision easiest to perceive.

This also changes how I think about empty states. A blank calendar and a blank list ask for different first inputs. One invites placement in time. The other invites record creation. Before optimizing the call to action, we should know which mental operation helps the user encounter the product's value.

## Keep a representation fit brief

I would put a small brief beside the growth hypothesis before changing the flow.

### The decision

- The question the user is trying to answer
- The action that follows when the answer is clear
- The evidence the user needs to make that call
- The cost of a slow or wrong answer

### The current form

- The representation shown by default
- The relationships it makes easy to notice
- The mental sorting, joining, or comparison still left to the user
- The other views available and the effort needed to find them

### The candidate form

- The representation that should better fit the decision
- The information it will emphasize and suppress
- The user situations where that emphasis should help
- The tasks that may become harder in return

### The proof

- A realistic decision task with a knowable answer
- Time to a correct decision
- Decision accuracy
- The next meaningful product action
- A later outcome that shows whether the decision was useful

The tradeoff line matters most. Every representation edits reality.

A timeline can reveal collisions while making exact metadata harder to scan. A map can reveal local density while making rank harder to compare. A graph can make a trend obvious while hiding the value of a single point. If the brief claims only benefits, it is probably describing decoration rather than a representation choice.

## Test the decision before the preference

For the planning product, I would write the hypothesis this way.

> We believe that showing managers with at least eight dated projects a weekly timeline rather than a project list on their first planning review will increase correct identification of the most overloaded week from under half to at least two thirds, because the timeline makes overlapping commitments directly visible. We expect those managers to rebalance at least one project more often during the same session without increasing mistaken owner or date changes.

This is falsifiable in a way that a claim about making planning feel intuitive is not. It names the population, representation, task, mechanism, threshold, action, and a guardrail.

I would begin with a task-based prototype comparison before running a broad product test. Give managers a realistic project set and ask them to identify the week most likely to exceed team capacity. Randomly show the current list or the proposed timeline first. Keep the underlying data, labels, and available actions the same. Measure whether they choose the correct week, how long the choice takes, and what evidence they use.

Then reverse the order with a second scenario so the team can see whether the result survives familiarity with both formats. Ask participants to change the owner of one named project as well. That lookup task should favor neither version too severely, and it makes the cost of the timeline visible.

The GOV.UK Service Manual recommends usability tasks with clear goals that are relevant and believable without giving away the answer. [Its guidance on moderated usability testing is a good method for this early comparison](https://www.gov.uk/service-manual/user-research/using-moderated-usability-testing). Preference can be captured afterward, but it should not be the primary result. People can like a polished view and still make a worse decision with it.

If the candidate representation improves accuracy without a large lookup penalty, I would run a product experiment among eligible managers. The primary behavioral outcome would be a capacity adjustment during the planning session. The later check would be whether fewer projects from the identified week become overdue. I would keep import completion and unintended edits as guardrails.

If people identify the busy week but do not rebalance anything, the representation may have solved perception without solving action. That is still useful learning. It points toward authority, confidence, or the cost of moving work rather than another round of visual polish.

If accuracy does not improve, the mechanism is wrong. Perhaps project effort is missing. Perhaps managers reason about individual specialists rather than total team capacity. Perhaps the weekly level is too coarse. The team should revise the task model before shipping a prettier timeline.

## Better visibility is not automatically more engagement

There is a growth trap hiding here.

A useful representation can help someone decide not to act. A pricing comparison may show that the current plan is sufficient. A portfolio view may reveal that no change is needed. A scheduling view may help a manager close the product after confirming the week is safe.

That can lower clicks while improving the product.

The right measure begins with the decision, not interaction with the representation. Correctness and time can matter more than view toggles. The downstream behavior should be appropriate action, which includes informed restraint when the state does not call for a change.

There is another trap in letting the winning view spread everywhere. A timeline that helps with capacity planning does not become the best home for editing project names, reviewing notes, or finding an owner. Cognitive fit is local to the task. Growth craft means knowing where the representation earns its place and where it does not.

I find this idea reassuring because it gives product teams another option besides adding persuasion or removing steps.

Sometimes the path is already short enough.

The user does not need more motivation. They do not need another tooltip. They need the product to arrange what it knows in the shape of the decision they came to make.
