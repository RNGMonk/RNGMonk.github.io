---
layout: post
title: One Step Forward, Two Steps Back
category: blog
---

I'm re-reading Jacob Lund Fisker's poorly titled "Early Retirement Extreme". I say poorly titled because it's much less about about retiring early, and more about re-thinking modern life from first principles and through system's thinking. I like to re-read the book every few years because I find most of his ideas apply well beyond the realm of personal finance and one of my favourite is his concept of "Web of Goals".

There are two important concepts here:
1. You tend to have multiple goals at once and they can counteract each other
2. Goals tend to have first and second order effects, and we tend to neglect second order effects in our thinking.

So far example, if you have a goal to lose weight and a goal to go on holiday to Italy (where you'll probably put on weight) then you'll be less effective at losing weight.

Another example is say, aiming to get a high paying job. The first order effect of the job would be increased income. But a second order effect might be that your more stressed out, and they you feel like you need to go on holiday which costs money. So the first order and second order effects interact resulting in less money than you might have expected.

So the key idea is to try align your goals and their first and second order effects such that they're mostly pointing in the same direction, minimsing the amount counteracting interactions.

This idea applies very directly to software development, where we tend to have a lot of waste due to counteracting forces. Here are some examples.

# React

When React was first introduced it promised to reduce the complexity of interactive frontend applications by essentially providing the same mental model of declaratively rendering state as server rendered web sites and to save us all from jQuery spaghetti.

The problem was that now we had to worry about server side rendering for SEO and first render performance reasons. Sever side rendering can be quite complex based on your use case and so new React frameworks were introduced, such as Nextjs to save us from the complexity of SSR.

But Nextjs similarly comes with it's on host of problems, primarily being focused on a serverless request response model which makes some use cases like setting a db connection pool and using websockets much more complicated.

# Containerisation

Containers solve the problem of "works on my machine" by creating reproducable environments that bundle all the required dependencies and can be shared and deployed. 

# Microservices