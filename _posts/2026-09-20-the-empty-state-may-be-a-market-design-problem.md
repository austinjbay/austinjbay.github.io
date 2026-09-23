---
title: "The empty state may be a market design problem"
subtitle: "A marketplace can have plenty of supply in aggregate and still show no useful match where and when a user needs one."
description: "A growth PM field note on perishable inventory, local liquidity, and mapping the geographic and time windows where matching actually happens."
date: 2026-09-20
image: /assets/images/notebook.jpg
layout: post
---

I think product teams sometimes treat an empty marketplace screen as a copy problem.

We add a friendlier illustration. We suggest broadening the filters. We promise that new options arrive every day. We ask for an email so we can notify the user later.

All of that can be reasonable.

It can also hide the more important diagnosis. The marketplace has supply, but not supply that can meet this demand in this place and time.

The empty state may be a market design problem.

## Aggregate supply can be locally useless

Imagine a hypothetical marketplace for last-minute music lessons.

The team reports 2,000 active teachers and 3,500 weekly student searches. Those totals sound healthy. A parent in north Austin searches for a beginner piano teacher within five miles on Tuesday between 5 and 7 p.m. The result is empty.

There are teachers in Dallas, guitar teachers nearby, piano teachers available at noon, and one Tuesday teacher whose slot was booked ten minutes ago. None of them is a match.

Marketplace liquidity is local to the dimensions that make a transaction possible. Geography, time, category, price, trust, and service level all fragment the headline pool.

In [Harvard Business School's interview about market design](https://www.library.hbs.edu/working-knowledge/how-to-fix-a-broken-marketplace), Alvin Roth explains why marketplaces need enough participants, enough room to consider transactions, and safe conditions for participation. A local services app is not a labor matching theorem. The useful connection is that bringing participants together is not enough. The rules and timing of matching shape whether compatible pairs find each other.

## Time makes inventory perishable

A lesson slot at 6 p.m. disappears at 6 p.m. An available ride, restaurant table, or same-day delivery window cannot be stored for next Tuesday.

That makes time-bound marketplace inventory perishable. The product is not only searching a catalog. It is coordinating expiring opportunities.

Uber's explanation of [marketplace matching](https://www.uber.com/us/en/marketplace/matching/) describes why the closest driver is not always the quickest and why considering a batch of nearby requests can improve matching. The mechanisms of ride hailing differ from lessons, care, reservations, or rentals. Still, the core constraint travels. A participant elsewhere or later may do nothing for the request in front of us.

This is why expanding the map can make a marketplace dashboard look healthier while making matching worse. A thousand new teachers across the country add supply. They do not change Tuesday piano liquidity in north Austin.

## Fragmentation deserves its own diagnosis

An empty result can come from several fractures.

- Enough providers exist, but not inside the travel radius.
- Enough local providers exist, but their open hours do not overlap demand.
- Time and location overlap, but category or qualification does not.
- Compatible options exist, but stale availability makes them look bookable when they are not.
- Matches exist, but ranking hides them behind preferences users would relax if the trade were clear.

Each failure suggests a different move.

Recruiting more general supply will not fix a narrow schedule gap. Asking users to widen distance may help only if travel remains practical. Moving demand can help a flexible student, while a school pickup schedule may make Tuesday at six nonnegotiable. Better availability sync can unlock inventory without adding a single provider.

This differs from a total capacity problem. A market may have enough lesson hours for every request yet fail because the hours and requests do not line up. Capacity asks whether the system can serve the volume. Liquidity asks whether compatible parties can find each other before the opportunity expires.

## The artifact I want is a liquidity map

Build the map at the resolution of the promise.

| Segment | Weekly searches | Compatible live slots | Search-to-match | Main fracture |
| --- | --- | --- | --- | --- |
| North Austin, piano, Tue 5–7 | 48 | 9 | 19% | Too few overlapping hours |
| North Austin, piano, Sat 9–12 | 31 | 42 | 71% | Ranking and price fit |
| South Austin, guitar, Tue 5–7 | 26 | 33 | 65% | Stale calendars |
| Austin-wide, all lessons | 620 | 910 | 58% | Aggregate hides local gaps |

These are hypothetical numbers, not benchmark claims.

For each cell, add the maximum distance or delivery radius, freshness of availability, minimum trust requirement, time until inventory expires, and the next-best alternative users actually accept.

My hypothesis might read this way.

> If Tuesday-evening piano searches first show verified openings within five miles and then offer a clearly labeled Wednesday alternative, more families will make a suitable match without increasing cancellations or travel regret.

The test changes sequencing and transparency, not total supply. If it fails because neither window contains enough compatible options, the map points toward targeted provider acquisition or schedule creation in that cell.

A forecast can help position supply, but it does not remove the need to choose the right local unit. A precise citywide forecast can still miss a neighborhood dinner gap. Nor should a test ignore competition for the same lesson slot. If one family's treatment changes the choices available to another, assignment and analysis need to account for that shared inventory.

## Design the market before decorating the gap

Empty-state design matters. People deserve a truthful explanation, a useful alternative, and a way forward.

But the interface should not be asked to apologize indefinitely for a fragmented market.

I would start by mapping where compatible demand and perishable supply overlap at the time and geographic resolution of the job. Then I would decide whether to recruit a specific kind of supply, shift flexible demand, improve freshness, change ranking, or narrow the promise.

The goal is not to make emptiness feel nicer. It is to learn which boundary prevented a match and redesign the market around that reality.
