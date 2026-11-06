---
title: "Account for the behavior your measurement creates"
subtitle: "A survey, interview, or observed test can become part of the product experience it was meant to study."
description: "A practical measurement footprint review for separating product behavior from behavior created by the act of studying it."
date: 2026-11-06
image: /assets/images/notebook.jpg
layout: post
---

There is a version of product research that feels almost weightless.

We add one question after onboarding. We invite a few new users to an interview. We ask a beta cohort to keep a diary. Then we put their behavior next to everyone else's and talk as if the research merely watched what happened.

I have become less comfortable with that story.

Asking someone whether they plan to make a budget can make budgeting more present in their mind. Asking a new team to explain its goal can help the team sharpen the goal. Inviting a user to a weekly interview can make the product feel more important, more supported, or more accountable than it otherwise would.

Those are not reasons to stop doing research. They are reasons to admit that measurement sometimes joins the experience.

For a growth PM, this matters most when a small, closely studied cohort looks unusually healthy. We may believe we found the right audience or built the right feature. In reality, we may have built a temporary product made of software plus attention from the team.

## The thermometer can warm the room

Health researchers call one version of this measurement reactivity. A review indexed by the National Library of Medicine describes it plainly as measurement producing changes in the people being measured. It found examples where measurement changed later cognition, emotion, and behavior, while also noting that researchers still cannot reliably predict when the effect will appear. That uncertainty is the useful part for product teams. The effect is plausible, not guaranteed. [The review argues that measurement can alter what follows](https://pubmed.ncbi.nlm.nih.gov/20205982/).

A later systematic review examined randomized trials in which people answered questions about health behavior. It found a small overall effect on subsequent behavior, then warned that bias and publication patterns may make even that estimate too generous. [The review treats the question behavior effect as real enough to test and uncertain enough not to assume](https://pubmed.ncbi.nlm.nih.gov/25133835/).

That is a better posture than either extreme I often see in product work.

One extreme treats every conversation as contamination and retreats into event logs. The other assumes a survey or interview cannot matter because it is not a shipped feature.

Both miss the practical question. Did this particular act of learning change the behavior we later used as evidence?

The Office for National Statistics has found that even the order of survey questions can matter. In its testing of loneliness measures, asking the direct question first changed responses to the scale that followed. The recommendation was not to abandon the survey. It was to preserve the order needed for comparable interpretation. [The ONS testing shows that the instrument can shape the answer](https://www.ons.gov.uk/peoplepopulationandcommunity/wellbeing/compendium/nationalmeasurementofloneliness/2018/testingoflonelinessquestionsinsurveys).

Product research deserves the same care. A question is not only a window. Sometimes it is a prompt.

## Research can quietly bundle extra value

Imagine a planning product testing a new weekly review.

Twenty beta users get the feature. Each receives a kickoff call, a short Friday survey, and a follow-up interview after four weeks. The product team watches their sessions closely and answers problems quickly. Beta users complete more weekly reviews and retain better than similar users on the current experience.

The result is encouraging, but the bundle contains several possible causes.

- The feature made the review easier
- The kickoff call clarified why the review matters
- The Friday question served as a reminder
- The interview created a mild sense of accountability
- Fast responses from the team prevented small problems from becoming abandonment
- Selection into the beta identified unusually motivated users

Only the first claim belongs to the feature by itself. The others may still point toward good product ideas. Perhaps the eventual product needs a clear explanation, a well-timed prompt, or visible support. But we should not credit the software for value supplied by the study and then act surprised when the general release underperforms.

This is where qualitative research and experimentation need to talk to each other. Good research practice already recognizes that an observer can change a session. Nielsen Norman Group advises observers not to offer advice, corrections, or accidental clues because those actions can bias the result. It also notes that body language and noise can affect participant behavior and comfort. [Its observer guidance makes the researcher's presence part of the method](https://www.nngroup.com/articles/observer-guidelines/).

Growth work adds another concern. The effect may outlive the session. Attention today can become motivation tomorrow.

## Keep a measurement footprint review

Before I use a researched cohort as evidence for a growth decision, I want a one-page review beside the readout.

### The behavior under study

- The user behavior we hope the product changes
- The later outcome we will use as evidence
- The population and period covered by the claim
- What happened before any research contact

### The research contact

- Every survey, interview, diary entry, test task, and reminder
- When each contact appeared relative to the behavior
- Whether it named the desired action or asked users to predict it
- Whether users knew the team was watching closely
- Any money, early access, status, or special support attached to participation

### The plausible pathways

- Attention that made the product more salient
- Explanation that improved understanding
- Accountability that encouraged follow-through
- Staff help that removed a blocker
- Repeated reflection that helped users notice value
- Selection that made participants different before contact began

### The decision boundary

- What the study can support if contact changed behavior
- What requires evidence from a less contacted population
- Which piece of research-created value should become an intentional product element
- What we will not claim from this cohort

The artifact is not a purity test. A beta without contact is often a bad beta. Researchers need to ask questions, and teams should help people who encounter serious problems.

The point is to keep an honest account of what the cohort received.

## Write a hypothesis about the footprint

For the planning product, I would write this before looking at the final retention chart.

> We believe the Friday research survey increases weekly review completion among beta participants by at least five percentage points because answering the question makes the review more salient, even when the product experience is otherwise unchanged.

That statement is falsifiable. It names the contact, the behavior, a minimum effect, and a mechanism. It also creates a useful fork in the product decision.

If the survey has little effect, we gain confidence that the behavior is not mainly an artifact of that contact. If it has a meaningful effect, the study has discovered something potentially valuable. The question may be functioning as a prompt for reflection. We just have not yet earned the right to call the underlying feature sufficient.

I would validate this with a small randomized encouragement study inside the beta.

All eligible beta users would receive the same feature and the same support policy. Before the first Friday, randomly assign half to receive the weekly research survey and half to receive no research contact until the end of the four-week period. Passive product events would capture review completion for both groups. The delayed-contact group would still have a clear route to request help, and serious issues would be handled consistently across both groups.

The primary readout would be weekly review completion during the study. The later readout would be retained review behavior after the research period ends. I would also compare unsolicited support use so a difference in access to help does not hide inside the result.

This design will not isolate every influence. People who opt into a beta may still differ from everyone else. A closing interview may shape what happens afterward. Passive event tracking has its own limits. But the comparison answers a narrower and important question about whether the recurring measurement created part of the apparent win.

For interviews or usability tests, a perfect silent comparison may be impractical. In that case, stagger the contact. Randomly invite some eligible users before the behavioral window and others after it. Keep the invitation language, incentive, eligibility, and follow-up timing fixed. Compare behavior during the window, then use the later conversations to understand why the difference did or did not appear.

Ethics still outrank experimental neatness. Do not withhold safety information, contractual support, or help a user reasonably expects. The aim is not to strand people for cleaner data. It is to avoid casually giving one cohort a different product and forgetting that we did so.

## The footprint can reveal missing product

There is a tempting response when measurement changes behavior. Exclude the cohort, label it biased, and move on.

Sometimes that is right. Often it wastes the more interesting lesson.

If a weekly question helps people return, perhaps the product does not make the review cadence visible enough. If an interview helps users explain the value to themselves, perhaps the product completes work without helping them recognize progress. If access to a researcher keeps a team moving, perhaps the product lacks a good way to recover when users are uncertain.

The research footprint can act like dye in a plumbing system. It shows where motivation, interpretation, or confidence needed a path and did not have one.

The judgment call is whether to remove that influence from the evidence, translate it into the product, or both.

That translation should be specific. An interview that creates accountability does not automatically justify another notification. A thoughtful human asking about the user's goal may work because it creates reflection, not because it produces an interruption. The product analogue might be a private weekly note, a preview of unfinished work, or a prompt the user schedules for themselves.

Good judgment preserves the function without copying the research ritual.

## Evidence includes the way we collected it

Mid-career product work has made me more suspicious of clean readouts from unusually cared-for groups.

Not cynical. Just slower to separate the result from the conditions that produced it.

We already know that acquisition channels shape who arrives, defaults shape what people do, and incentives shape what gets counted. Research contact belongs on that list. The interview, survey, diary, and observed session can be part of the causal story rather than neutral paperwork around it.

That does not make the learning invalid. It makes the learning more precise.

Sometimes the feature worked.

Sometimes the attention worked.

Sometimes the strongest product idea is hiding in the difference.
