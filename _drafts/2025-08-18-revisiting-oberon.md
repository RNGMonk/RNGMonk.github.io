---
layout: post
title: Revisiting Oberon
category: blog
---

I originally learnt about Project Oberon from a Hacker News post about Niklaus Wirth's article "A Plea for Lean Software". I'd never really used Pascal or come into intellectual contact with any of Wirth's work before that but as I dug more deeply I become increasingly interested in what he had to say.

The thing that impressed me about Project Oberon was that it included not only a full operating system and compiler, but also a desktop environment and other graphics and utility application all in about 10k lines of code that could run on real hardware.

For context, real production operating systems and even web browsers run into the 10s of millions of lines of code, more than 3 orders of magnitude larger and well beyond the hope of being comprehended by a single individual.

A more fair comparison would be with xv6, a unix like educational operating system of a similar size. The difference is that for the same weight xv6 provides a very bare bones command line experience with a few command line tools.

The Oberon operating system is clearly making some very different trade offs and decisions and I was curious how they're able to achieve a lot with so little.

A few years ago I spent about 6 weeks trying to understand the project and port it to the Raspberry Pi 3. I learnt a fair amount but was ultimately unsuccessful and then life happened and I moved onto other interests and projects.

Looking back at it now, a few things were much more challenging than I expected.

1. Oberon has no common unix heritage which I realise now I sort of took for granted. It's hard to run Oberon the programming language on a host machine not running Oberon OS. There are some options but there tend to be small differences that need adjustments between the host and target machine.

2. Oberon OS typically needs to be run in a custom emulator. The best one is by Peter de Wagter and is enough to get started but is another non-standard piece of software that has it's own ways of bootstrapping the actual environment. Unfortunately the original FPGAs that Wirth used have been discontinued.

3. Project Oberon comes with an accompanying book describing much an overview of much of the workings of the system using a top down approach. While the book is very useful, it's not sufficient to understand much of the low level details of the system required for porting.

4. Oberon is foreign, the OS itself, the conventions, the programming style and especially the terminology in the book are all very foreign but presented in a way that assumes they are common knowledge.

