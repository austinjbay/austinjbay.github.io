---
title: "The same steps in a different order are a different product"
subtitle: "Growth funnels often treat sequence as plumbing, even when each step changes how the next one is understood."
description: "A growth Product field note on path dependence, sequence audits, and testing whether the order of a journey changes its outcome."
date: 2026-10-24
image: /assets/images/notebook.jpg
layout: post
---

I have sat through plenty of funnel reviews where everyone agreed on the steps and nobody talked about their order.

A person picked a template, connected a data source, invited a teammate, and published a report. All four events were green. The activation chart counted a completed setup. The journey looked healthy from far enough away.

Then we watched a few sessions.

People who connected real data before choosing a template understood what the template was for. People who chose first often spent time decorating an example that did not fit their work. People who invited a teammate before publishing had to explain an unfinished thing. Some recovered. Others left behind a technically complete setup that nobody trusted.

The steps were identical. The product was not.

Growth teams are good at asking whether a person reached an event. We are less disciplined about asking what the earlier events made the later ones mean. That is a problem whenever onboarding, lifecycle, SEO, or collaboration contains choices that change the user's frame for the next choice.

Order is not always interface plumbing. Sometimes order is part of the intervention.

## A checklist hides the journey

Funnels make a useful simplification. They turn a messy stream of behavior into a small set of milestones that a team can discuss.

The simplification gets dangerous when we read it as a faithful account of experience.

Imagine a research product that asks a new user to import notes, choose a synthesis method, and generate a summary. Importing first lets the method screen refer to the user's own material. Choosing the method first turns the same screen into an abstract taxonomy. Generating a demo summary before either step may create confidence, or it may anchor the user on a polished example their real material cannot match.

None of those paths is inherently right. They simply make different bets about uncertainty.

Survey researchers have a clean name for one version of this problem. Context from an earlier question can change the answer to a later one. An experimental study of [question order and bullying reports](https://pmc.ncbi.nlm.nih.gov/articles/PMC5965535/) found that changing which questions came first changed what respondents reported. A product flow is not a survey, but the transferable lesson is useful. Earlier prompts do not disappear after the click. They can prime a category, set an expectation, or narrow what the person notices next.

This is also familiar in cooking. The ingredient list does not fully specify the dish. Toasting spices before adding liquid produces a different result from dropping the same spices into the finished sauce. Sequence changes what later actions can do.

A growth funnel that records only ingredient possession will miss that.

## Sequence carries product judgment

I used to treat step order mostly as a conversion question. Put the easiest action first. Delay the expensive ask. Get momentum on the page.

Those are reasonable instincts, but they are incomplete.

The better question is what must become true before the next action can do its intended job.

A pricing page visited before a use case is understood feels like a cost inspection. The same page visited after a concrete result feels like an exchange. A request to invite a colleague before there is anything to inspect is distribution. The same request after a useful draft exists is collaboration. A lifecycle email that arrives before a background job finishes creates a broken return. The same email after completion can reopen a live decision.

The UI may be unchanged while the meaning moves.

This is why I would not automatically optimize for the shortest common route. A route can be short because it removed waste. It can also be short because it moved a consequential choice ahead of the evidence needed to make it well.

Apple's guidance on [disclosure controls](https://developer.apple.com/design/human-interface-guidelines/disclosure-controls) recommends keeping essential information available while hiding details until they become relevant. That is usually discussed as interface hierarchy. It is also a sequence decision. Relevance has a before and an after.

Good growth Product work makes that judgment visible instead of letting screen order inherit it by accident.

## Keep a sequence audit

The practical artifact I use is a sequence audit. It is intentionally smaller than a journey map. I only make one when two or three events can occur in different orders and the order could plausibly change the quality of the outcome.

| Event | What becomes true | What it changes downstream | Risk if it happens too early | Risk if it happens too late |
| --- | --- | --- | --- | --- |
| Import real notes | The product has representative material | Methods can be shown against the user's work | Import effort arrives before the value is legible | The user makes abstract choices |
| Choose a method | The product has an intended form of synthesis | The first output can fit the job | The choice is made without evidence | The product may produce an irrelevant default |
| Generate a summary | The user can inspect an output | Collaboration has a concrete object | A demo creates the wrong expectation | The journey withholds proof for too long |
| Invite a teammate | Another person enters the work | The output can become shared work | The inviter has nothing coherent to explain | The work stays private after it becomes useful |

For each event, I write down four things.

- The state change that the event creates
- The later decision that depends on that state
- The user cost of placing it earlier
- The product cost of placing it later

Then I mark the edges where order should matter. Import before method choice is an edge worth testing. Changing an avatar before selecting a color theme probably is not.

This keeps the exercise from becoming a grand theory of every click. Most adjacent events are ordinary navigation. The artifact earns its keep when one action supplies evidence, context, or a shared object that changes the next action.

## Observe paths before prescribing one

I would start with actual event streams rather than the path drawn in a launch document.

Google Analytics describes a path as a specific sequence of nodes and its [path exploration](https://support.google.com/analytics/answer/9317498?hl=en) can work forward from a starting event or backward from an ending event. Whatever tool you use, the backward view is especially helpful. Start with the useful outcome, then inspect the sequences that preceded it.

I would compare a small number of path families rather than every unique trail. For the research product, those might be real material before method choice, method choice before real material, and demo output before either one.

For each family I want more than completion.

Did the first summary use real material. Was it edited heavily. Was it shared. Did a teammate view it. Did the account create another summary after seeing fresh notes. Those signals help distinguish a path that merely reaches the last screen from one that leaves the product in a useful state.

Sequence analysis is observational. Confident users may naturally choose a different order from uncertain users. Teams with clean data may import earlier. A path can correlate with a strong outcome without causing it.

That is why the audit should end in an experiment, not a decree.

## Test the order while holding the work steady

Here is the hypothesis I would use.

> We believe showing a representative import before method selection will increase the share of new workspaces that produce a shared summary from real material within fourteen days, because users will choose with their own work in view, while time to first summary will not increase by more than one day.

Randomly assign eligible new workspaces to two coherent sequences. In one, import precedes method selection. In the other, method selection precedes import. Keep the available methods, import requirements, help, and final summary experience the same.

The primary outcome is a shared summary made from representative material. Time to first summary is the boundary measure. I would also inspect method changes after the first output and large edits to the generated structure. Those are useful signs that an early abstract choice did not survive contact with the work.

Do not compare a carefully rewritten sequence with the old sequence plus three other changes. Then the test says that one package beat another, not that order mattered.

I would also watch sessions from both variants. The numbers can tell us whether a sequence worked. A few sessions can show the mechanism. Perhaps real data makes method labels clear. Perhaps import is too large an opening ask. Perhaps neither order works because the categories do not match how customers think.

The result can be productively mixed. Import first may improve output quality while slowing the first session. That gives the team a real decision about what to shorten inside import rather than a vague instruction to reduce friction everywhere.

## The route is part of the product

Sequence work is easy to dismiss as funnel tuning because it often changes no underlying capability.

I think that undersells it.

Products are experienced in time. Each action leaves the person and the system in a new state. The next screen inherits that state whether the roadmap acknowledges it or not.

This matters across the growth surface.

An SEO landing page can give a visitor the vocabulary that makes comparison useful. Onboarding can create a real object before asking someone to organize it. Lifecycle can wait for a completed job before reopening the product. Collaboration can put something inspectable in the room before asking another person to enter.

The craft is not to force everyone down one immaculate corridor. People will arrive with different context and take different routes. The craft is to notice where order changes meaning, make the intended dependency explicit, and test whether it produces better work rather than prettier progression.

A checklist says the user did the things.

A sequence audit asks whether each thing made the next one more useful.

That is often the difference between a funnel that completes and a product that comes together.
