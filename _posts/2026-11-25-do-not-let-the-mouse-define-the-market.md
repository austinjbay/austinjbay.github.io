---
title: "Do not let the mouse define the market"
subtitle: "A healthy funnel can still exclude people when the product assumes everyone works through the same input device."
description: "A practical interaction parity sheet for finding growth journeys that only work with a mouse, precise touch, or visible feedback."
date: 2026-11-25
image: /assets/images/notebook.jpg
layout: post
---

I once watched a team make a campaign builder much faster.

The old version asked people to choose an item, open a menu, and move it up or down. The new version let them drag items directly into place. It felt immediate. In moderated sessions, people finished sooner. In the experiment, more campaigns reached the review step.

Then someone tried to build one without a mouse.

They could enter every field and add every item with a keyboard. They could not put the items in the required order. The product had not made the journey faster for them. It had removed the journey.

That experience changed how I look at a clean funnel win. We often treat input method as an implementation detail while treating conversion as product truth. But if a meaningful action depends on precise dragging, hovering, seeing a quiet toast, or hitting a small target, the interface has decided who is eligible before the funnel starts counting.

Accessibility is not a special version of growth work. It is part of defining the reachable market.

## A funnel can hide a locked door

Most growth analysis begins after an event arrives.

Someone viewed the builder. Someone added an item. Someone reached review. We compare the steps and look for the largest drop. The person who could not operate the first custom control may appear as an unmotivated visitor or a mysterious bounce. The event stream records absence, not the reason for it.

This is one place where an average conversion rate can be unusually reassuring. A pointer shortcut helps a large group finish faster, while another group loses the ability to finish at all. The blended result can still rise.

I do not think the answer is another segment dashboard. Keyboard use, screen reader use, voice control, zoom, switch access, and touch are not neat customer identities. The same person may use a trackpad at work, a phone on the train, and a keyboard while an injured hand heals. An interaction method is a condition of use, not a marketing persona.

The Web Content Accessibility Guidelines make the underlying product requirement quite concrete. [W3C says functionality should be operable through a keyboard when the underlying job does not truly depend on a freehand path](https://www.w3.org/WAI/WCAG22/Understanding/keyboard). Moving an item between two positions qualifies. The drag gesture is one implementation, not the job itself.

That distinction is useful far beyond a compliance review. It asks a product team to name the durable action underneath the fashionable interaction.

## Equivalent work matters more than identical gestures

I used to hear accessibility discussions get stuck on imitation.

How do we recreate drag and drop from a keyboard. How do we make a screen reader describe the same animation. How do we preserve the clever interaction everywhere.

Those questions start too close to the interface.

The job in the campaign builder is not dragging. The job is putting one message before another. A move earlier button, a position menu, or cut and paste might complete that job more clearly than a simulated drag. The keyboard route does not have to look identical. It has to offer comparable control and a legible result.

This reminds me of good operations design. A warehouse may let a worker scan a package, enter its code, or choose it from an exception list. The physical moves differ. The system still needs to identify the same package, apply the same rule, and confirm the same state change. Redundant routes are not ornamental when the work has to survive real conditions.

The confirmation matters as much as the control. A sighted pointer user may notice that a card moved and a small success message appeared. Someone using a screen reader needs the changed position and result to reach them another way. [W3C guidance on status messages says important changes should be available to assistive technology without unnecessarily moving focus](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html). An action that technically fires but leaves its result silent is not a complete route.

Touch introduces a related mistake. We can preserve the action and still make the control practically unusable. [W3C guidance on target size calls for sufficient size or spacing and explains how cramped controls increase accidental activation](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum). A tiny reorder handle may exist on mobile while remaining an optimistic fiction for someone with limited dexterity, a tremor, or a moving bus underneath them.

The product judgment is not whether every route feels the same. It is whether each route preserves agency, consequence, and feedback.

## Keep an interaction parity sheet

For a consequential journey, I want one small artifact beside the funnel. I call it an interaction parity sheet.

Each row holds one meaningful job rather than one screen or component.

| Job | Pointer route | Non-pointer route | Result feedback | Focus after action | Failure evidence |
| --- | --- | --- | --- | --- | --- |
| Put a message first | Drag the card to the top | Choose move to first | New position is visible and announced | Returns to the moved card | Repeated move attempts or exit before review |
| Remove a recipient | Select the remove control | Reach the named button by keyboard | Recipient count changes and is announced | Moves to the next sensible recipient | Count changes visually but not programmatically |
| Publish the campaign | Select the publish button | Reach and activate the same control | Success and next state are available | Lands at the published campaign | Focus disappears or confirmation is silent |

I would fill it out with a designer, an engineer, and the person who owns the growth readout. That mix matters. The designer can distinguish the job from the gesture. The engineer can explain what the accessibility tree and focus actually do. The growth owner can show where failure becomes invisible in the data.

The sheet should answer a few practical questions.

- Can someone reach the action without a precise pointer
- Can they understand the control before activating it
- Can they perform the same underlying job
- Can they tell what changed afterward
- Does focus move somewhere predictable
- Can they recover from an error without changing input method
- What evidence would show that one route is failing

The last question keeps this from becoming a component inventory. A journey may pass a static inspection and still be exhausting in use. Twenty unnecessary tab stops, a reorder action that requires dozens of key presses, or a confirmation announced too late can technically preserve access while making completion much less likely.

## Test the route without voting on access

Automated checks are useful, but they cannot tell us whether the whole job makes sense. The [GOV.UK Service Manual recommends combining automated checks, manual testing, assistive technology testing, and research with disabled users](https://www.gov.uk/service-manual/helping-people-to-use-your-service/testing-for-accessibility). That is a good model for growth teams because each method catches a different kind of failure.

I would begin with the interaction parity sheet and a manual keyboard pass through the complete journey. Then I would inspect names, roles, states, focus order, announcements, zoom behavior, and touch targets. I would test with the assistive technologies that matter for the product and bring in people who actually use them.

The product experiment comes after we have established an accessible floor. We should not randomize people into a route we know they cannot operate just to prove that exclusion lowers conversion.

For the campaign builder, I would test two conforming reorder approaches. Both groups keep drag and drop. One also gets visible move controls that work from a keyboard. The other gets a position menu that works from a keyboard. Assignment can happen at the builder level, with enough time for repeated use rather than one polished demo.

The hypothesis would read this way.

> We believe visible move controls will increase successful campaign review by at least fifteen percent among people who begin reordering with a keyboard, compared with a keyboard-operable position menu, because each move and its result remain in the working context. Pointer-user completion will not fall by more than two percentage points, and median reorder time will not increase by more than ten percent.

That claim can fail. The menu may be faster. Visible controls may add noise. The improved route may help completion but make large lists tedious. The guardrails also prevent the team from calling parity successful when it creates a confusing default for everyone.

I would read task completion, wrong-order reviews, reorder time, repeated actions, abandonment after the first move, and successful correction of a deliberate mistake. I would separate results by observed interaction route without pretending that route defines a permanent kind of user. A short usability study with keyboard and screen reader users would explain failures the events cannot.

If neither design supports the job well, the decision is not to return to drag only. It is to design a better accessible route.

## The fastest path is not the whole product

There is a familiar growth instinct to remove every extra control and make the dominant gesture feel effortless. Sometimes that is exactly right. A clean direct manipulation can be satisfying and fast.

The trouble starts when we confuse the dominant route with the underlying capability.

A product is more durable when meaningful work can survive a change of device, input method, vision, dexterity, or environment. That resilience often improves the ordinary experience too. Named controls are easier to discover. Clear feedback reduces duplicate actions. Generous targets help on a crowded train. Predictable focus helps a power user move quickly.

Those benefits are welcome, but they are not the price accessibility must pay to earn a place. A person should not need to improve the average funnel before they get a usable product.

The growth lesson is narrower and more demanding. Before celebrating a faster path, check who still has a path.
