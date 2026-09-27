---
title: "A green check does not grant authority"
subtitle: "A growth funnel can finish every product step while the real decision still belongs to somebody else."
description: "A growth PM field note on the gap between product permissions and real decision rights, with an authority gap map for finding false completion."
date: 2026-09-26
image: /assets/images/notebook.jpg
layout: post
---

I once worked on a flow where the final screen looked unusually healthy.

People connected the account, chose an audience, built the thing, and reached the green check. In the funnel, they were done. A surprising number still did nothing with what they had made.

We first reached for the usual explanations. Maybe the last button was timid. Maybe the reminder arrived too late. Maybe people needed more reassurance.

The interviews were less convenient.

One person could build the campaign but was not allowed to send it. Another could schedule the report but could not commit the team to the recommendation. A third had the product permission and the job title, but knew that an informal owner would object if the work went live without a look.

Nobody was confused about the interface. The product had finished. The organization had not decided.

That distinction has stayed with me.

## Permission and authority are different things

Software is good at granting permission.

A role can view, edit, approve, publish, invite, export, or pay. Role-based access control exists to make those permissions systematic. The [NIST overview of role-based access control](https://csrc.nist.gov/projects/role-based-access-control) describes permissions being associated with roles and users being assigned to the appropriate roles.

That is necessary security machinery. It is not a complete account of authority.

Authority is whether the decision will hold in the world around the product.

An office manager may have permission to buy software but not the standing to add a recurring expense. A marketer may have the publish button but not the mandate to change the offer. A teacher may be able to assign a tool while a district policy still governs whether students can use it. A clinician may be able to enter an order while a protocol, payer, or patient decision determines what happens next.

The interface knows what the account allows. It rarely knows which choices colleagues will recognize, which precedent matters, who carries the downside, or who can quietly undo the decision tomorrow.

When growth teams collapse those two layers, we create false completion. The user crosses the product finish line while the consequential decision remains unsettled.

## The funnel hides constitutional questions

That sounds grander than it is.

Every group has some way of deciding who may make which call. Some of it is written down. Much of it lives in habit, trust, budgets, professional norms, and the memory of what happened last time.

Political economist Elinor Ostrom spent decades studying how groups govern shared resources without relying on one universal arrangement. Her Nobel lecture on [polycentric systems for coping with collective action](https://www.nobelprize.org/uploads/2018/06/ostrom_lecture.pdf) is far removed from a SaaS funnel. The useful connection is modest. Decision rights are part of an institutional arrangement, and workable arrangements depend on context rather than a single neat center of control.

A product quietly enters that arrangement whenever it lets somebody spend shared money, expose shared work, contact shared customers, change a shared record, or commit other people to a process.

We tend to model this as a conversion problem owned by one user.

It may actually be a governance problem involving several people who do not appear in the event stream.

This is why a faster interaction can leave time to consequence unchanged. Cutting four screens may save ninety seconds. It does not help if the choice still needs Tuesday's budget meeting, a policy interpretation, or the blessing of the person everyone treats as the real owner.

Interaction speed measures how quickly the product can be operated.

Decision time measures how quickly a choice can become legitimate enough to act on.

Those clocks can move independently.

## I would not turn this into another waiting-state exercise

There is an important collision to avoid here.

I have already written about making delayed work legible and about mapping backstage dependencies in supposedly self-serve flows. Those frames ask what process, person, or system must finish after the user acts.

This is a different failure.

The missing ingredient may not be work in a queue. It may be an unresolved right to decide. Nobody is processing the request because the group has not agreed that this person can make it. A more accurate progress bar would only decorate the ambiguity.

The intervention is different too. Status messages help with known work. Authority gaps may need a narrower action, a visible boundary, a lightweight consent, or an explicit transfer of the decision.

## Decision design has more roles than approve or reject

Many products reduce group decisions to a requester and an approver.

Real decisions are messier.

Somebody recommends. Somebody supplies facts. Somebody absorbs the risk. Somebody can block. Somebody has to carry out the result. Somebody becomes accountable when the choice ages badly.

Bain's description of the [RAPID decision model](https://www.bain.com/insights/rapid-tool-to-clarify-decision-accountability/) separates recommending, agreeing, performing, providing input, and deciding. I would not paste that framework into every product. Its value here is showing how much organizational structure disappears when a UI offers only an approval checkbox.

The same lesson appears in incident response. The [FEMA National Incident Management System](https://www.fema.gov/sites/default/files/2020-07/fema_nims_doctrine-2017.pdf) makes command, coordination, and assigned responsibility explicit because a pile of capable people does not automatically produce a legitimate decision under pressure.

Growth products usually operate at lower stakes. The coordination problem still travels.

If the recommender is mistaken for the decider, the product nudges the wrong person. If the person who carries the risk is absent, an approval can be reversed later. If execution belongs to another team, a completed choice can sit untouched even after everyone agrees.

The product should not reproduce an org chart. It should know enough about the consequential choice to avoid pretending that a click settles it.

## The artifact I want is an authority gap map

Pick one moment the funnel currently calls complete. Then map the decision around it.

| Product moment | Consequence outside the product | Product permission holder | Recognized decider | Who carries the downside | Evidence the decision will hold |
| --- | --- | --- | --- | --- | --- |
| Campaign scheduled | Customers receive a new offer | Lifecycle marketer | Marketing lead | Sales and support | Offer owner named and send boundary agreed |
| Vendor connected | Recurring spend and data access begin | Operations manager | Budget owner and security owner | Finance and security | Budget threshold and data scope accepted |
| Report shared | Team changes weekly allocation | Analyst | Regional lead | Account owners | Decision recorded with an effective date |

These are illustrative rows, not benchmarks.

Add four fields beneath each row.

- The rule the product currently assumes
- The rule people actually use
- How often a product-complete action is delayed, reversed, or quietly ignored
- The smallest product change that could make authority explicit without adding ceremony to every case

That last constraint matters. The goal is not to put a committee in front of every button.

Sometimes the answer is a spending threshold below which the user truly owns the call. Sometimes it is a preview link that asks a specific person for one bounded decision. Sometimes it is separating recommendation from commitment. Sometimes it is letting an administrator delegate a right for a defined period. Sometimes the honest answer is that this action should not be called complete yet.

## Measure consequence, not button speed

I would begin with an observational pass before changing the flow.

Choose a meaningful action such as publishing, paying, inviting a whole team, changing a policy, or accepting a recommendation. Record the product completion time and the first observable consequence. Then sample the long gaps and ask what was unresolved.

Do not label every gap as approval latency. Separate at least these cases.

- A known decider had not responded
- The identity of the decider was disputed
- The user lacked a clear boundary for acting alone
- The decision was made but execution belonged elsewhere
- The action was reversed because an affected person entered late

My hypothesis would read this way.

> If we show who owns the consequential decision, state the boundary of that decision, and route one bounded request to that person, the median time from product completion to real-world action will fall without increasing reversals or unauthorized actions.

That statement can be wrong.

Run the test only on cases where the map shows an authority gap. Compare it with the current flow using time to consequence as the primary measure. Keep reversal rate, disputed-action reports, support contacts, and the share of decisions completed without an extra meeting as guardrails.

Segment by decision size. A lightweight delegation pattern may help a routine campaign and be reckless for a new annual contract. Also inspect the tail. A lower median can hide a small group trapped indefinitely because the product routed the choice to a formal approver while the informal decider remained invisible.

If the change improves clicks but not time to consequence, the authority diagnosis was probably wrong or incomplete. If time falls while reversals rise, the product accelerated action without making it legitimate. Neither result is a win.

## A completed flow should survive contact with the organization

I still care about interaction speed. Slow tools waste attention, and needless steps deserve removal.

I just do not want a quick green check to stand in for a decision the user cannot actually make.

The stronger growth question is not only whether somebody reached the end of the flow. It is whether the choice became durable enough for the next person to act, spend, publish, change course, or take responsibility.

When it did not, another reminder to the original user may be noise. Another celebratory completion event may be fiction.

Map the authority gap instead.

The product does not need to settle every organizational argument. It does need to stop confusing access to a button with the right to make the call.
