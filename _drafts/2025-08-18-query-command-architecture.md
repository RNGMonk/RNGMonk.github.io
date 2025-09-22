---
layout: post
title: Command Query Architecture
category: blog
---

I'm often struck by the amount of unnecessary complexity in client projects I work on as a contractor. There's often a lot of sophisticated code, doing smart things but the general output of the product is low. Some of this relates to microservice architecture being in vogue, some of this related to popular frameworks we use and some of it is just downright self-imposed.

So what is simple?

It's probably impossible to come up with a definition that could satisfy everyone, but I think there are some properties that I'd like to achieve for my own uses:

1. The complexity of the code should be proportionate to the complexity of the problem.
2. We should rely on relatively simple constructs, in particular I would like to reduce the problem to functions and data as much as possible
3. It should be easy to navigate the code and get a sense of the existing functionality of a project

I once worked on a project that had some of these properties and that project has since become a seed in my mind. One of the key ideas with the project was to separate all functionality in commands and queries. This was loosely inspired by CQRS, but motivated more by code organisation than the ability to be able to decouple and scale reads and writes independently.

Commands represent things the system can do and typically modify the systems state in some way. Queries represent questions that the system can answer. Interestingly almost all request-response style software fits quite neatly into this pattern, but what makes it useful is that it's much easier to think about and get an overview of what can the system do and what can the questions the system can answer.

