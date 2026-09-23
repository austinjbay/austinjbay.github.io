---
title: "Price the uncertainty before you test the price"
subtitle: "With usage-based billing, the frightening number is often not the rate. It is the bill a customer cannot predict."
description: "A growth PM field note on metering, household budgeting, and testing whether a bill estimate makes usage-based pricing understandable."
date: 2026-09-19
image: /assets/images/desk.jpg
layout: post
---

I think pricing tests often assume the customer is reacting to a number.

$20 per seat.

Eight cents per minute.

$3 for every thousand jobs.

But usage-based products ask customers to evaluate two things at once. They have to judge the rate and predict the quantity. If quantity feels unknowable, even a fair rate can feel expensive.

The customer is not only asking what does this cost. They are asking what will I discover I spent after it is too late to change my behavior.

Before testing the price, I want to price that uncertainty.

## Metering creates a forecasting job

Usage billing can align price with value. It can also transfer forecasting work to the customer.

Stripe's guide to [usage-based billing](https://docs.stripe.com/billing/subscriptions/usage-based) describes tracking usage through meters and applying a pricing model at the end of a billing period. That machinery is necessary. It does not by itself make the eventual bill predictable to the person creating usage.

A household budget offers a useful analogy. Knowing electricity costs a certain amount per kilowatt-hour does not immediately tell a family what this month's bill will be. They need a sense of appliance use, weather, billing days, fees, and how today's behavior compares with an ordinary month.

A software customer faces the same translation problem. They may know the API rate but not how many calls one workflow produces, which retries are billable, whether failed jobs count, or how a busy week changes the total.

The analogy does not prove customers will behave like utility consumers. It does reveal that rate comprehension and bill comprehension are different product jobs.

## A worked invoice is part of the interface

Imagine a hypothetical document-processing product.

The plan charges $12 each month plus $0.04 per processed page after 500 included pages. A small property manager expects 40 documents a week with an average of 12 pages.

Here is a worked invoice for a four-week month.

| Line item | Calculation | Amount |
| --- | --- | --- |
| Base plan | One month | $12.00 |
| Pages processed | 40 × 12 × 4 | 1,920 pages |
| Included pages | 500 | $0.00 |
| Billable pages | 1,920 − 500 | 1,420 pages |
| Usage charge | 1,420 × $0.04 | $56.80 |
| Estimated subtotal | Base plus usage | $68.80 |

Now make uncertainty visible. If average documents range from 9 to 15 pages, the same workload produces 1,440 to 2,400 pages. The estimated subtotal ranges from $49.60 to $88.00 before tax.

That range is more useful than false precision. It also tells the team which assumption matters. Page count, not the posted rate, drives most of this customer's uncertainty.

I would show the assumptions next to the estimate and let customers change them. An unexplained range is only a different kind of mysterious number. People should not have to reconstruct unavoidable charges from scattered fragments.

## The artifact I want is a bill predictability brief

Write it for a real usage shape, not an abstract average.

**Metered unit**

A page successfully processed. Retries caused by system errors do not count.

**User translation**

One ordinary 12-page document usually creates 12 metered pages. Show where exceptions occur.

**Known inputs**

Documents processed so far, observed average pages, included allowance, and days left in the billing period.

**Estimate**

Expected bill, plausible range, assumptions, last refresh time, and taxes or fees not included.

**Control points**

Usage notification at a customer-chosen amount, exportable meter history, and a clear explanation of disputed or delayed events.

**Trust failures**

Late meter events, duplicated usage, silent definition changes, and estimates that present a point value when the range is wide.

The [FinOps Foundation's guidance on forecasting](https://www.finops.org/framework/capabilities/forecasting/) emphasizes using historical spend and planned changes to anticipate cloud costs. Customers do not need an enterprise finance practice to buy a product. The transferable lesson is that a forecast should connect observed history, known change, and explicit uncertainty.

## Test estimate usefulness, not only estimate exposure

I would not call an estimator successful because users opened it.

My hypothesis would be more demanding.

> If customers see a bill range translated into their ordinary documents, they will predict the final invoice more accurately and report greater confidence without materially suppressing valuable usage.

For a comprehension study, ask customers what they expect the bill to be before and after seeing an estimate, then compare both with the final invoice. That alone does not establish a causal effect on usage. For that question, randomly assign eligible accounts to the estimator or the existing pricing experience, keep rates unchanged, and observe a complete billing cycle. Track absolute forecast error, confidence, support contacts about billing, surprise at invoice time, and whether users avoid clearly valuable work.

An estimate can reduce usage by frightening customers with a poorly explained upper bound. It can increase usage by making a safe range legible. Either behavior matters more than clicks on the widget.

I would also test comprehension with scenarios. If usage doubles for one week, can the customer identify the likely range. Do they know whether a failed job counts. Can they explain when the meter updates.

## Predictability is part of the price

A low rate with a mysterious quantity can feel riskier than a higher rate attached to a stable bill. That does not mean usage pricing is wrong. It means the product has to help customers do the forecasting job its model creates.

The rate card tells people how the meter works. A predictability brief tells the team whether a customer can turn that meter into a household or company decision.

Before moving the price point, I would measure the space between the customer's expected invoice and the one we actually send. That gap is part of what they experience as price.
