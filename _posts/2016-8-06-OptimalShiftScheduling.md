---
layout: post
comments: true
title: Building an Efficient Job Shift Scheduler
---

<figure>
<center>
   <a href="/images/header_shifts.jpg"><img width="90%" src="/images/header_shifts.jpg"></a>
</center>
</figure>

<center>
<font size="5"><b>A Fast and Simple Scheduling Method</b></font>
</center>

<script type="text/x-mathjax-config">
  MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});
</script>
<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_CHTML">
</script>

---


Quick Links: 

* [Motivation and Background](#mot)  
* [The Current System](#curr)
* [What are the Variables?](#var)
* [Hard Constraints](#hard)

---

<a name="mot"></a>

# Motivation and Background

<figure>
<center>
   <a href="/images/ra_hero.jpg"><img width="70%" src="/images/ra_hero.jpg"></a>
</center>
</figure>

I currently work as as a Resident Assistant (RA) at my university. My responsibilities include organizing engaging and fun events for residents who live on my floor, serving as an academic and emotional resource for these students, and completing nighttime work shifts, which RAs call "duties", on a rotating basis. These duties are divided into two types, ON duties and IN duties. 

If I am assigned to an ON duty on a given night, I am responsible for patroling various floors of my building multiple times, ensuring that students are not violating housing policies, and checking for maintainance issues. These ON duties last from 7PM until 7AM during which time I can be contacted at any time to respond to anything from an innocuous noise complaint to an unconcious resident who needs immediate medical attention. From my experience, these shifts can be taxing and too many of them in a short time frame can impact sleep patterns, alertness, and even academic performance.

On the other hand, if I am assigned to an IN shift on a given night, I am not responsible for patrolling any part of the building and will only be contacted to respond to an incident if all the people with ON shifts that night are busy dealing with incidents. 

The number of people scheduled for ON and IN shifts each night varies with the size of the particular building. Larger buildings have three ON duties and three IN duties per night with smaller ones having fewer of each type of shift. Furthermore the particular number of the ON shift makes a difference. For example, in my building the shifts are designated ON 1, ON 2, and ON 3 and are responsible for patrolling, among other areas, the lobby, the basement, and the courtyard, respectively. It is apparent that during the winter, it is much more prefereable for RAs to patrol indoors than outdoors.

<a name="curr"></a>

# The Current System

These ON and IN shifts are not randomly assigned. Every three to four weeks, RAs fill out preferences for the coming weeks about which days they would prefer to have an ON shift, which days they would prefer to have an IN shift, which days they cannot have any shift (perhaps because they have other plans that night), and which days they are ambivalent about getting assigned a shift. 

<figure>
<center>
   <a href="/images/sched_hard.jpg"><img width="90%" src="/images/sched_hard.jpg"></a>
</center>
</figure>

Once these preferences are recorded, a team of two or three RAs attempts to create a harmonious schedule which balances the workload for each RA, ensures ample time between ON shifts, ensures a reasonable time between IN shifts, and balances the types of ON shifts accross the board. This is no simple task and it can often take hours to iron out all the inefficiencies in the resulting schedule. Additionally, it is somewhat worrisome that the RAs creating the schedule are resonsible also for scheduling themselves, a potential conflict of interest. 

But worry not!

This problem, creating an optimal schedule subject to many hard, and some softer constraints, belongs nicely to a family of problems called Constraing Satisfaction Problems (CSPs) which computers are really really good at solving fast. 

The only challenge for us is to take this very human problem, and translate it into a problem that a computer can understand and then solve. If you think this sounds crazy complicated, don't worry. I promise it will be much easier than you think. Let's get started!

<a name="var"></a>

# What are the Variables?

In order to translate this scheduling problem into something a computer can solve, we need to figure out what our variables are going to be. At first thought, this seems to be too broad of a problem. Should we think about how many shifts each RA gets? Should we try and use the number of days between shifts as our variables? How about the order of the shifts by RA? 

In fact, the choice of variables is even more basic and will implicitly be able to take all these questions into account. Given some number of RAs in the building, let's say 24 for now, and some number of days to schedule, let's say 27 days, we will define:

$$
ON_{i,j} = 
\left\{
\begin{array}{ll}
      1 & \text{if RA i scheduled ON for day j} \\
      0 & \text{if not} \\
\end{array} 
\right
.$$

and 

$$
IN_{i,j} = 
\left\{
\begin{array}{ll}
      1 & \text{if RA i scheduled IN for day j} \\
      0 & \text{if not} \\
\end{array} 
\right
.$$

So, assume we have the following list of 24 RAs

<figure>
<center>
   <a href="/images/RAs.jpg"><img width="90%" src="/images/RAs.jpg"></a>
</center>
</figure>

and we want to schedule them for the 27 day period **Sunday May 15th 2016 - Friday June 10th 2016**.

If we know that 

$$ON_{Bruce, Jun 1} = 1 \text{   and   } IN_{Clark, Jun 1} = 0$$

then we know that Bruce is ON duty on the night of June 1st and Clark is **not** IN duty on the night of June 1st. 

How many of these variables are there? Well there are 24 possibilities for the RA and 27 possibilities for the day so we get a total of 24 times 27 or 648 variables. *Whoa! I thought we said this would be simple!* Don't stress, it will be, and it's all because these variables, as many of them as we have, can only be 0 or 1, which is the key structure we will take advantage of when formulating our problem. Let's turn our attention to the different kinds of constraints we have for these variables.

<a name="hard"></a>

# Hard Constraints

There are a couple of hard constraints when we try and solve this scheduling problem. Let's define what this means/

**Hard Constraint**: A rule that, if violated, makes for an invalid schedule

Let's go through each constraint and see how a human would state it and how we can express it with our variables.

## Sufficient Staff Constraint

{:center: style="text-align: center"}
**We need exactly three RAs with ON shifts and three RAs with IN shifts each night**
{:center}

Hmm ... how do we express this with our variables. Well, starting simple, we can choose a day, say May 15th. We know that exactly (no more, no less) than three RAs need to have ON shifts on May 15th. How do we count how many people will be ON for May 15th? Well since  $ON_{i, May 15} = 1$  if RA i is ON and 0 if not, all we need to do is sum up 

$$ON_{Ash, May 15} + ON_{Bruce, May 15} + ... + ON_{Xavier, May 15} + ON_{Zeus, May 15}$$

and that will tell us how many RAs have ON shifts for May 15th. 

