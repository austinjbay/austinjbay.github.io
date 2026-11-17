---
title: "Count the promises your growth win creates"
subtitle: "A new behavior can improve the funnel while quietly expanding what the product has to keep working."
description: "A growth Product field note on counting the durable promises created by adoption before a local win becomes a permanent obligation."
date: 2026-11-17
image: /assets/images/notebook.jpg
layout: post
---

I once worked on a feature that made recurring reports much easier to create.

The launch looked healthy. More people scheduled a report, more teammates received one, and the accounts that used the feature were more likely to return. It was the kind of result a growth team wants to find.

Then we tried to change the report.

A field that seemed unimportant turned out to feed someone’s Monday meeting. A naming cleanup broke a filter in a spreadsheet. A sensible change to delivery time made the report arrive after another team had already started its review. What looked like one product surface had become a collection of small agreements with people we could not see.

The adoption win was real. So was the obligation it created.

I think growth teams are usually better at counting the first than the second.

## Adoption creates an installed promise

Most growth work is discussed as movement.

A person publishes a page, connects an integration, saves a template, creates a shared link, schedules a digest, or invites a teammate. The funnel advances and the feature gains an active user.

But some actions do more than move a person forward. They create something the product is now expected to keep honoring.

The shared link needs to keep resolving. The integration needs to keep returning a recognizable shape. The template needs to survive an editor change. The scheduled digest needs to arrive when the receiving team has built its routine around it.

This is an installed promise.

It is not the same as maintenance work for the user. It is the product’s obligation to preserve, migrate, or deliberately retire a behavior it encouraged people to depend on.

That distinction matters because growth tactics can multiply promises quickly. A prominent template can create thousands of documents with the same structure. A default can put one notification schedule into every new workspace. A sharing loop can spread links far beyond the people represented in the account dashboard.

The winning surface may be small. Its installed base may not be.

## The conversion event is also a commitment event

This changes how I read a growth result.

Suppose a new onboarding step increases the number of people who publish a public dashboard. We might measure completion, later visits, sharing, and paid conversion. Those are useful outcomes.

I also want to know what we committed ourselves to when the dashboard went live.

Does its URL now appear in a customer’s documentation. Do other people bookmark it. Does an executive use a screenshot in a monthly review. Does an external team read its fields through an unofficial script. Would changing access rules break an expectation that the activation chart never recorded.

None of this makes the feature a bad idea. It means the unit of growth is not only a completed action. It is an action plus the future states that action creates.

That is familiar in API design. Stripe separates releases with and without breaking changes and gives integrations an explicit version to use. Its [API versioning documentation](https://docs.stripe.com/api/versioning) is a useful reminder that improving the current product and preserving an existing consumer are separate jobs.

Growth surfaces deserve a lighter version of the same thoughtfulness. A customer may never call a saved template an interface contract. It can still function like one.

## Durable goods and city streets have the same awkward lesson

The idea travels beyond software.

A manufacturer does not stop accounting for a product when it leaves the factory. Parts, repair knowledge, warranties, and recalls follow the installed base. Selling more units creates revenue and a larger population that future changes have to consider.

Cities live with a similar asymmetry. Cutting a ribbon is a moment. Maintaining the road, station, or water line is a continuing responsibility. The visible launch and the quiet obligation belong to the same decision even when they sit in different budgets.

Growth teams can accidentally split those two moments across functions. The experiment owns adoption. Platform owns compatibility. Support owns confusion. Lifecycle owns the migration message. Months later, each team sees a fragment of the cost and nobody can connect it back to the original win.

That is how a feature becomes too important to change without ever being important enough to manage deliberately.

The answer is not to stop shipping things that create dependency. Products become valuable partly because people can rely on them. The better question is whether we know which reliability we are selling.

## Keep an installed promise register

For a growth bet that creates a persistent object, repeated output, external link, integration, or team routine, I would keep a small register beside the experiment brief.

## Installed promise register

- Behavior we are trying to grow
- Persistent thing created by that behavior
- People or systems likely to depend on it
- Expectation the current experience establishes
- Product changes that could violate that expectation
- Evidence that dependency has formed
- Cost of preserving the behavior
- Safe migration path if the behavior changes
- Clear retirement condition if the promise is temporary
- Owner after the experiment ends

The point is not to estimate years of maintenance before testing a button. The point is to notice when a button manufactures an installed base.

A one-time export probably needs little ceremony. A public link used in a customer’s own product needs more. A saved filter used by one person is different from a scheduled report delivered to fifty people. The register should make those differences discussable before aggregate adoption turns them into one large number.

I would pay special attention to promises that cross the product boundary. Once an output lands in a deck, a bookmark, a webhook, an inbox rule, or another team’s meeting, ordinary product analytics become a weak map of who depends on it.

## Look for dependency rather than mere use

Usage does not tell us whether a promise exists.

Someone can open a feature every day without depending on its current shape. Someone else can depend heavily on a link they never open themselves because it feeds a process elsewhere.

I would look for evidence in a few places.

- Objects that are old but still receive traffic
- Outputs consumed by people who did not create them
- Repeated schedules that survive across many cycles
- Customer scripts, exports, or forwarding rules built around a stable format
- Support requests that ask the product to restore an earlier behavior
- Release notes that trigger unusually careful questions from a small group
- Features with low visible use but high migration effort whenever they change

The useful observation is not simply that people used the feature. It is that something else began to assume the feature would continue behaving a certain way.

GitHub makes that obligation concrete in its [REST API version policy](https://docs.github.com/en/rest/about-the-rest-api/api-versions). Breaking changes belong in a new version, earlier versions receive a stated support period, and closing versions produce advance signals. That machinery exists because dependency changes the cost of change.

The same principle can guide much smaller product choices without requiring an API governance program.

## Write a hypothesis about the obligation

The growth hypothesis should name both the new behavior and the promise it creates.

Here is one I would be comfortable testing.

> We believe making scheduled project summaries easier to create will increase the share of new workspaces that establish a weekly review habit. If those summaries become an installed promise, then established schedules will be less tolerant of format and timing changes than newly created schedules, visible through higher disablement, manual export, and support contact after the same change.

That second sentence is falsifiable. The old and new schedules may react the same way. The apparent dependency may be mostly in our imagination. Good. Then we have learned that the product has more room to change than the anecdotes suggested.

If the difference is real, we have learned something the activation lift alone could not tell us.

## Run a cohort age change test

I would not manufacture a destructive break to prove this point.

Instead, choose a low-risk change already worth considering, such as a modest layout adjustment, a new default delivery hour, or a renamed field with an easy path back. Compare reactions across cohorts defined by how long the persistent behavior has been established.

Keep exposure comparable. Measure the immediate product outcome and the signs of dependency. Those might include schedule edits, reversions, downloads, manual copying, help visits, support contact, and downstream opens. Read a small sample of qualitative responses to learn what external routine, if any, was disturbed.

The result should inform a decision.

If established cohorts react no differently, make the change and keep watching. If they react much more strongly, preserve the old behavior for existing objects, provide a migration choice, or narrow the change. If the cost of supporting both paths is larger than the value of the behavior, the team has found that out while it can still choose deliberately.

This is observationally useful even when an experiment is not practical. Plot change-related support and workaround behavior by object age, number of consumers, and whether the output crosses into another system. A dependency pattern should become stronger as the promise becomes older, wider, or more embedded.

## Retirement is part of the original product decision

Some promises should not last forever.

That is not a failure. The failure is letting temporary behavior acquire permanent expectations by accident.

Internet infrastructure has a surprisingly humane idea here. The IETF’s [Sunset header specification](https://www.rfc-editor.org/rfc/rfc8594.html) gives a service a way to announce that a resource is expected to become unavailable and to point consumers toward retirement information. The interesting part for product teams is not the header. It is the assumption that an ending deserves a date, a scope, and a mitigation path.

A beta badge is not enough if the product encourages people to build real work on top of the beta. A low-usage feature is not automatically cheap to remove if its few users have embedded it deeply. A new replacement is not a migration plan if existing objects cannot travel there.

When a growth bet creates a lasting thing, I want the team to decide early which of three stories it is telling.

We intend to preserve this behavior.

We intend to evolve it through explicit migration.

We intend for it to expire, and we will make that boundary honest before dependence forms.

Those are all defensible. Drifting among them is not.

## Growth should count what it asks the product to remember

There is a satisfying simplicity to a conversion event. It happened or it did not.

The future created by that event is messier.

A saved object may become a reference. An integration may become infrastructure. A weekly email may become the agenda. A public link may travel somewhere its creator will never see.

This is part of what we want when we work in growth. We want the product to earn a place in real work. But earning that place means the company no longer has complete freedom to treat yesterday’s experience as disposable.

So after a promising test, I would ask one more question before calling the result clean.

What did people just learn they can rely on.

If we cannot answer that, we may have grown more than usage.

We may have grown a promise nobody is yet prepared to keep.
