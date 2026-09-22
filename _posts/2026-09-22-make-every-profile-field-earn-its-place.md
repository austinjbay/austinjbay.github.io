---
title: "Make every profile field earn its place"
subtitle: "Why growth teams should treat requested data as inventory rather than a free byproduct of signup."
description: "A practical field rent review for deciding which profile questions belong in a growth journey, when to ask them, and how to test whether they create enough value to stay."
date: 2026-09-22
image: /assets/images/notebook.jpg
layout: post
---

I have a small allergy to required fields whose only defense is that the information might be useful someday.

Company size.

Job title.

Phone number.

Industry.

How did you hear about us.

Each one can sound harmless in a planning meeting. Together they turn signup into a customs form.

The usual growth conversation asks whether removing a field will improve conversion. That is worth asking, but it is too narrow. A field does not stop costing the user once they submit the form. The product now has data to store, explain, protect, refresh, and avoid misusing. The user has also received a clue about whose needs the journey serves.

I think every requested field should pay rent.

It should change something useful for the person giving it to us, satisfy a real operational need, or leave the form.

## A profile is not free inventory

Teams often talk about profile data as if an empty database column were a missed opportunity.

If we know the role, we can personalize later.

If we have the phone number, sales can follow up.

If we know the industry, reporting will be cleaner.

Sometimes those are good reasons. Often they are unpriced wishes from different parts of the company, collected in one form because the signup owner has no clean way to refuse them.

The user pays first.

They have to interpret the question, decide how exact to be, wonder why it is being asked, and predict what the answer will trigger. A founder choosing between consultant and business owner is doing product taxonomy work before receiving any value. A person entering a phone number is also deciding whether they just invited a call.

That is not merely form friction. It is a negotiation.

Privacy practice offers a useful constraint here. The UK Information Commissioner's Office describes [data minimisation](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/data-minimisation/) as holding information that is adequate, relevant, and limited to what is necessary. I like that standard even when a legal review is not the immediate issue. It makes the burden of proof sit with the team asking, not the person typing.

## Good questions have a visible job

A field earns its place when the answer changes the experience in a way the user can reasonably understand.

Asking for a delivery address before showing a local arrival estimate has a visible job.

Asking for a team size before anyone has seen the workspace is murkier, especially if every answer produces the same screen.

This is where form design starts to resemble inventory management. Shelf space is finite, carrying costs continue, and stock that never moves is not an asset just because somebody once requested it.

The comparison is not perfect. Data is not a box in a warehouse. It can be copied cheaply. That cheapness is exactly why teams underprice it. Collection is easy while stewardship and interpretation are not.

The [GOV.UK question page pattern](https://design-system.service.gov.uk/patterns/question-pages/) recommends asking only for information that is really needed and generally starting with one thing per page. That advice comes from public services, where a vague or unnecessary question can keep someone from completing a consequential task. Consumer software usually carries lower stakes, but the design principle travels well. Make the question singular, explain its job, and do not make the user solve the organisation chart behind it.

There is an accessibility argument too. The W3C guidance for [identifying input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html) explains how programmatically identified purposes can let browsers and assistive technology present familiar personal-information fields in more usable ways. A standard field with a clear purpose is easier for people and software to handle than an inventive label that exists mainly for internal segmentation.

Privacy, operations, and accessibility arrive at a similar product judgment from different directions.

Ask less. Ask clearly. Use the answer for the job you implied.

## The artifact I use is a field rent review

I would run this on signup, account creation, lead forms, preference centers, and any lifecycle prompt that asks for more personal information.

For each field, write down the following.

- The exact question and whether it is required
- The user decision or product behavior it changes now
- The person or system that uses the answer
- The consequence of a blank, stale, or inaccurate answer
- What the user is likely to think will happen next
- How long the answer stays reliable
- A less intrusive way to get the same outcome
- The event that would justify asking later
- The removal owner and review date

Then give the field one status.

- Keep now when it unlocks immediate user value or a genuine requirement
- Ask in context when its purpose becomes clear later in the journey
- Infer carefully when a reliable, explainable signal already exists
- Make optional when it helps but should not block progress
- Remove when nobody can name a current use

The review gets uncomfortable in a productive way.

Marketing may discover that source attribution from a self-reported dropdown is mostly decorative. Sales may admit that it calls every qualified account regardless of the phone field. Product may find that the role selector feeds a dashboard but does not alter the experience. Analytics may point out that a required answer looks complete while being full of whatever choice gets people through fastest.

Completeness and truth are not the same thing.

## Put the claim in plain language

Here is the hypothesis I would write before changing a form.

> We believe moving the company-size question from signup to the first team invitation will increase completed signups among solo evaluators without reducing successful team creation, because the reason for the question will be clearer when collaboration becomes relevant.

That statement is more useful than saying fewer fields will convert better.

It names the specific field, the audience carrying the cost, the later moment where the question may belong, the intended behavior, and the outcome we are not willing to damage.

It also leaves room for the change to be wrong.

Maybe company size selects an important account configuration. Maybe it helps route regulated customers to a safer path. Maybe removing it attracts more low-intent signups and creates no additional use. The review should expose those possibilities before the experiment, not after somebody dislikes the result.

## Test the downstream job, not only the form

A clean experiment would randomly assign eligible new visitors to the current form or the reduced form. Keep traffic sources, device mix, eligibility rules, and follow-up treatment stable where possible.

The immediate measure is completed signup per eligible visitor. I would also watch field-level abandonment and time to complete, split by device and important acquisition source.

That is only the front door.

The deciding measures should cover the job the removed field supposedly performed. In the company-size example, I would compare the share that creates a team, invites a colleague, reaches the product's existing value event, and remains active over the team's normal early-retention window. If the field routes sales or support, I would compare routing accuracy and manual correction work too.

I would add two quality checks.

First, inspect the distribution and usefulness of the answers when the question appears in context. A later answer rate may be lower while the answers are more accurate and actionable.

Second, watch for burden moving somewhere less visible. Removing a field is not a win if support agents now spend their day repairing account configuration or if users meet an avoidable dead end later.

Run the test long enough to observe the downstream behavior, not merely the signup bump. Predefine the segment cuts that could change the decision. A field may be wasteful for individual users and essential for administrators in a regulated company. The right result may be a branched request rather than universal removal.

## Timing can be better than deletion

I do not believe every short form is automatically good.

Some questions prevent serious mistakes. Some are necessary for eligibility, tax, safety, compliance, or delivering the service at all. Hiding those needs until late in the journey can feel worse than asking early and explaining why.

There are also cases where one answer saves the user from ten irrelevant choices. That can be a fair trade.

The standard I want is not minimalism for its own sake. It is earned collection.

Ask at the moment when the answer can do honest work. Show the effect when that is practical. Give people a real optional path when the answer is merely helpful. Retire fields whose consumers disappeared two roadmaps ago.

And be careful with inference. Replacing a direct question with a hidden guess can reduce typing while making the product more presumptuous. If the guess affects pricing, access, or a consequential experience, make it inspectable and correctable.

That is the product-judgment part. A spreadsheet can reveal an unused field. It cannot decide whether asking later will feel considerate, evasive, or surprising.

## The form is making a promise

Every question implies that the answer matters.

When nothing changes, the product signals that its questions are for the company's convenience. When the answer triggers an unexplained call, it reveals that a neutral-looking form was actually a lead filter. When a stale answer quietly shapes the experience months later, it makes the profile feel like a trapdoor.

Growth teams should care because forms sit at unusually sensitive boundaries. They turn visitors into accounts, accounts into qualified leads, and individual users into members of a wider system. The questions asked there are part of the product, not clerical prework.

Make each field earn its place.

If the team cannot name the value, the user, the timing, and the owner, the empty column may be the better product decision.
