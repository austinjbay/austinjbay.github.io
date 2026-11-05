---
title: "Choose the unit before you optimize the flow"
subtitle: "A product can make every step easier while drawing the boundary around the wrong piece of work."
description: "A growth PM field note on finding the unit of work users actually carry, with a practical unit boundary sketch and a test for choosing where completion belongs."
date: 2026-10-27
image: /assets/images/notebook.jpg
layout: post
---

I once worked on a product that made it very easy to create one thing at a time.

That was a problem because almost nobody arrived with one thing.

They had a launch with several assets, a research project with a pile of interviews, or a client job with work that belonged together. We had polished the create button, shortened the form, and celebrated each finished item. The user still had to remember which items formed the actual job.

Our flow was efficient at the wrong scale.

This is easy to miss in growth product. Funnels need a countable object, so the product quietly chooses one. A task is completed. A report is published. A receipt is filed. An appointment is booked. Once that object has an event name, the team starts improving the path to it.

The object may be real and still be smaller or larger than the work the user is trying to carry.

Before I optimize a flow now, I want to know whether the product has chosen the right unit.

## Product boundaries are product behavior

A unit is the piece of work the product treats as belonging together.

It determines what shares a name, an owner, a due date, a price, a history, and a finished state. It also determines what gets separated.

Consider a field service product that treats every visit as an independent appointment. That works for a boiler inspection. It works less well when three visits, two parts orders, and a customer call all belong to one repair. The team can reduce booking time for each appointment while the customer keeps asking whether the repair itself is on track.

Or imagine an expense product organized around individual receipts. The user may experience the work as a trip. Policies, currency conversion, approval, and reimbursement all make more sense at that larger boundary. Perfect receipt capture does not remove the job of rebuilding the trip.

The reverse mistake happens too. A learning product can define a course as the unit even when someone only needs one technique before tomorrow's meeting. A heavy container makes a small useful job look like a commitment.

This is not mainly an information architecture question. The boundary changes behavior. People postpone work that is too large to begin, fragment work that is too small to coordinate, and invent naming conventions when the product will not hold the grouping they need.

## Other fields make the unit explicit

Database systems do not assume that every statement should stand alone. The PostgreSQL documentation describes a [transaction as a bundle of steps that succeeds or fails as one operation](https://www.postgresql.org/docs/current/tutorial-transactions.html). The boundary matters because a half-finished transfer is not a smaller successful transfer. It is an invalid state.

Product work is rarely that crisp, but the idea travels. Sometimes completion belongs to a set of actions because the partial result cannot honestly carry the outcome.

Health care has a more contested version of the same choice. The Centers for Medicare and Medicaid Services defines an [episode of care as a set of services and supplies for a condition over a defined period](https://www.cms.gov/priorities/innovation/key-concepts/bundled-payments). The episode can cross tests, procedures, providers, and settings. Where that episode begins and ends affects what gets paid for and what people are encouraged to coordinate.

Archives offer another useful view. The National Archives explains that a records series contains materials [accumulated and used together for a specific purpose](https://www.archives.gov/research/start/how-records-grouped.html). The useful grouping comes from the work that produced the records, not merely from the fact that every page can be cataloged on its own.

Those domains have very different stakes. What they share is an admission that a unit is chosen, and that the choice shapes what the system can preserve, coordinate, and call complete.

Software often hides that judgment behind a data model.

## Look for the object people reconstruct

The fastest clue is usually the grouping users rebuild outside the product.

They put the same prefix on twelve project names. They keep a spreadsheet that says which orders belong to a customer move. They paste several report links into one document. They ask support to close a whole case even though the product only knows how to close its tickets.

That shadow object is interesting. It suggests the product stores the parts while the user carries the whole.

I would still be careful. Repeated grouping does not automatically mean the product should add a new container. Sometimes the grouping is temporary, personal, or already handled well by another system. A sales team may assemble links in an account plan because the plan properly belongs in its CRM. Pulling that object into an analytics product could create duplicate ownership rather than relief.

The question is whether the missing boundary is causing consequential work.

Can people tell what is finished without reconstructing the group. Can they assign responsibility at the scale where someone can act. Do changes to one item alter the meaning or status of its siblings. Does pricing or permission split something that the user must manage as one commitment.

If the answers are mostly no, a folder may be enough. If the answers are yes, the unit is part of the product model.

## Draw a unit boundary sketch

The artifact I use is a unit boundary sketch. It fits on one page and describes one recurring job.

**The user-held unit**

Name the thing the person believes they are moving forward. Use their noun if one exists, such as a trip, repair, hiring round, campaign, or claim.

**The product-held unit**

Name the object the product currently creates, counts, prices, assigns, and closes. These may be different objects, which is useful to show.

**The natural edges**

Write down what starts the work, what makes an item belong, and what makes the work meaningfully finished. Avoid using the current interface as the definition.

**The shared consequences**

Note what the grouped items should inherit together. Good candidates include ownership, access, status, budget, history, and a change that affects the rest of the group.

**The reconstruction work**

Record what people do today to recover the missing whole or break apart an oversized one. Include coordination time, duplicate entry, abandoned starts, and mistakes at the boundary.

**The dangerous edge cases**

Name examples that do not fit the proposed unit. A receipt can span two trips. A repair can reveal a second fault. One interview can inform several studies. If the model only works for the tidy example, it is not ready to become infrastructure.

The sketch is deliberately not a request for a hierarchy. Its job is to expose the boundary before the team commits to projects, folders, workspaces, parent records, or another permanent layer of navigation.

## Test the boundary without building the container

I would begin with observed work rather than a new object in the interface.

Take a sample of recent completed jobs and ask users to group the product records the way they experienced the work. Do not supply the grouping rule. Compare where people draw the edges, which attributes they expect the group to share, and what they mean when they say the job is done.

Then run a concierge test for one narrow use case. Behind the scenes, let the team assemble related items into a proposed unit. Give users a group-level view or summary and allow a few consequential actions at that level, such as assigning an owner, seeing the outstanding work, or closing the job. Keep item creation unchanged.

The hypothesis should make the boundary falsifiable.

> For multi-visit repairs, treating the repair rather than the appointment as the unit of coordination will reduce time spent reconstructing status and increase repairs completed without a missed dependency, without increasing incorrectly grouped visits.

I would compare eligible work with and without the group-level treatment. The primary outcome belongs at the proposed unit, such as repairs completed without a missing part or unowned follow-up. I would also measure reconstruction time and incorrect grouping. Those harms matter because a neat container that puts unrelated work together can be worse than no container.

The interviews still matter after the test. I want to hear whether the proposed unit matches how people discuss ownership and completion when the researcher is gone. A metric lift can show that the treatment helped. It cannot by itself tell us that the boundary will remain intelligible across the messy cases.

## A better unit can still be the wrong product move

There are several ways to get this wrong.

The first is turning every relationship into a container. Flexible tags or saved views may be better when membership overlaps and changes often. A rigid parent object can force the organization to choose one truth where several are legitimate.

The second is choosing the unit that makes reporting convenient. A company account may be easy for a dashboard while the actual work happens by location, household, classroom, or case. Administrative neatness is weak evidence about the user's boundary.

The third is making the unit too large. Bundling can improve coordination and also hide partial progress, create permissions problems, or make a small job feel impossible to start. The right whole should not erase useful parts.

The fourth is assuming one boundary can serve every decision. Creation, billing, collaboration, and analysis may need different grains. A receipt can remain an editable item while a trip becomes the unit for approval. The goal is not one universal object. It is an explicit choice about which consequences belong together.

Sometimes the current unit is right. Users may group things only for occasional reporting, the groups may disagree wildly, or the cost of a wrong grouping may exceed the coordination benefit. In that case I would improve cross-item views rather than change the product's center of gravity.

## The growth judgment is where completion belongs

Growth teams inherit units from event schemas, database tables, and existing screens. We should not confuse inheritance with truth.

If the product unit is too small, the funnel can fill with local completions while the user's real job remains open. If it is too large, activation can demand a body of work that no sensible new user wants to finish at once.

The judgment is where to place a meaningful finish line and which things should cross it together.

That choice will affect onboarding, collaboration, pricing, lifecycle messages, and what the team calls retained value. It deserves to be made before we shave another step off the flow.
