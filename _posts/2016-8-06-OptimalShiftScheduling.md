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
**Hard Constraint 1: We need exactly three RAs with ON shifts and three RAs with IN shifts each night**
{:center}

Hmm ... how do we express this with our variables. Well, starting simple, we can choose a day, say May 15th. We know that exactly (no more, no less) than three RAs need to have ON shifts on May 15th. How do we count how many people will be ON for May 15th? Well since  $ON_{i, May 15} = 1$  if RA i is ON and $0$ if not, all we need to do is sum up the May 15 variable for all the RAs:

$$ON_{Ash, May 15} + ON_{Bruce, May 15} + ... + ON_{Xavier, May 15} + ON_{Zeus, May 15}$$

and that will tell us how many RAs have ON shifts for May 15th. 

For some proposed schedule, if the sum is 2, we reject that schedule since not enough RAs are staffed ON that night. If that sum is 4, we also reject that schedule since too many RAs are staffed ON that night. We need it to be exactly 3. So we need 

$$ON_{Ash, May 15} + ON_{Bruce, May 15} + ... + ON_{Xavier, May 15} + ON_{Zeus, May 15} = 3$$

and similarly, 

$$IN_{Ash, May 15} + IN_{Bruce, May 15} + ... + IN_{Xavier, May 15} + IN_{Zeus, May 15} = 3.$$

But, we can just do this for each of the 27 days since we have the same constraint every night. So, in a nutshell

$$ON_{Ash, j} + ON_{Bruce, j} + ... + ON_{Xavier, j} + ON_{Zeus, j} = 3$$

and

$$IN_{Ash, j} + IN_{Bruce, j} + ... + IN_{Xavier, j} + IN_{Zeus, j} = 3$$

where $j$ is each day from May 15th to June 10th. 

Cool, that wasn't too painless, and now we have our first constraint. Let's press on!

## Equal Work Constraint ##

Let's do a quick calculation of roughly how many ON shifts each RA should have in this time period. There are 27 days with 3 ON shifts per day for a total of 81 ON shifts spead accross 24 RAs for a total of **3.375 ON shifts per RA**. Well, we cant give partial ON shifts to an RA, so we want that each RA has either 3 or 4 ON shifts. The same holds for IN shifts. 

{:center: style="text-align: center"}
**Hard Constraint 2: Each RA has either 3 or 4 ON shifts and either 3 or 4 IN shifts**
{:center}

We could imagine that even with this constraint, Bruce, for example, might get lucky with 3 ON and 3 IN duties and Clark might get very unlucky with 4 ON and 4 IN constraints. This seems a bit unfair so we want the total number of duties (ON + IN) for each RA to be either 7 or 8. This is basically saying that no RA should get away with having 3 ON shifts and 3 IN shifts. 

{:center: style="text-align: center"}
**Hard Constraint 3: Each RA has either 7 or 8 total shifts**
{:center}

Now, how do we translate these using our variables? The number of total ON shifts any given RA has is calculated by adding up their $$ON$$ variables (which is 1 if they have an ON shift on a given day and 0 if not) for 27 days. For example, if we want to know how many ON shifts Vader has for the 27 day period, we need to sum:

$$ON_{Vader, May 15} + ON_{Vader, May 16} + ... + ON_{Vader, Jun 9} + ON_{Vader, Jun 10}$$

and ensure that this sum is either 3 or 4. We do the same for IN shifts. 

To satisfy Hard Constraint 3, we need only do ensure that: 

$$7 \le (ON_{Vader, May 15} + IN_{Vader, May 15}) + ... + (ON_{Vader, Jun 10} + IN_{Vader, May 15}) \le 8.$$

## Burnout Constraint

Even if we assure that two RAs have the same number of ON shifts, let's say three each, we say nothing about how those shifts are spread out. For example, if Clark has three ON shifts on May 15, May 30, and June 10, he enjoys a relatively spead out workload. If Bruce, on the other hand, has three ON shifts on May 15, May 16, and May 17, he faces three continuous days of work and has a much greater stress level. We thus want the following three hard constraints:

{:center: style="text-align: center"}
**Hard Constraint 4: Each RA has at least 7 days between ON shifts**
{:center}

{:center: style="text-align: center"}
**Hard Constraint 5: Each RA has at least 7 days between IN shifts**
{:center}

{:center: style="text-align: center"}
**Hard Constraint 6: Each RA has at least 2 days between an ON shift and an IN shift**
{:center}

You're probabaly asking, where did these numbers come from? For a specific instance of this problem, with some historical shift preference data, I found that these were the highest numbers that still resulted in a valid schedule. For this reason, the fine tuning of these numbers is built into the model and it will keep trying to build schedules until it maximizes each of these three numbers. More on this later on. 

The question for now is how to express these constraints using our variables. It seems a bit difficult at first since our variables only tell us whether or not an RA is working on a given day, not the time between shifts. But, we can be a little creative here. Let's start simple. 

Let's say we wan't to enforce Hard Constraint 4 for Elsa. We know that for the first seven days of the scheduling period, May 15 - May 21, she can have at most ON shift. If she had two or more, then these shifts would be less than 7 days apart and we would be violating the constraint. So we need:

$$ON_{Elsa, May 15} + ON_{Elsa, May 17} + ... + ON_{Elsa, May 20} + ON_{Elsa, May 21} \le 1$$

Then, if we move this seven day window forward by 1, to get the range May 16 - May 22, we know that she can also have at most one ON shift in this range, for the same reason as before.

$$ON_{Elsa, May 16} + ON_{Elsa, May 18} + ... + ON_{Elsa, May 21} + ON_{Elsa, May 22} \le 1$$

We just keep rolling this seven day window through the full 27 days and set the same less than or equal to 1 ON shift constraint for each window.

This can be confusing with just words so let's see some pics. The first window looks like this:

<figure>
<center>
   <a href="/images/FirstRoll.jpg"><img width="70%" src="/images/FirstRoll.jpg"></a>
</center>
</figure>

Then we add another day to the end of the window and remove one from the beginning:

<figure>
<center>
   <a href="/images/SecondRoll.jpg"><img width="70%" src="/images/SecondRoll.jpg"></a>
</center>
</figure>

And then continue ...

<figure>
<center>
   <a href="/images/ThirdRoll.jpg"><img width="70%" src="/images/ThirdRoll.jpg"></a>
</center>
</figure>

We make sure that in each seven day window, each RA has no more then one ON shift.

We do the analysis for IN shifts in the same way since Hard Constraint 5 requires also 7 days. To meet Hard Constraint 6, we need to make sure that the sum of all the $ON$ and $IN$ variables for each RA for each two day window is no more than 1. For example, for Elsa, we need that:

$$(ON_{Elsa, May 15} + IN_{Elsa, May 15}) + (ON_{Elsa, May 16} + IN_{Elsa, May 16}) \le 1$$

$$(ON_{Elsa, May 16} + IN_{Elsa, May 16}) + (ON_{Elsa, May 17} + IN_{Elsa, May 17}) \le 1$$

$$...$$

$$(ON_{Elsa, Jun 9} + IN_{Elsa, Jun 9}) + (ON_{Elsa, Jun 10} + IN_{Elsa, Jun 10}) \le 1$$

### Serendipitous Sidenote

Even though it is evident to a human that we cannot assign the same person for two different shifts in a given day, the computer will not know that unless we state it as a constraint. We have "accidentally" set this constraint implicit in Hard Constraints 4 through 6. For example, if we propose a schedule where Elsa is scheduled to be ON and IN for June 10, we will have that  

$$(ON_{Elsa, Jun 9} + IN_{Elsa, Jun 9}) + (ON_{Elsa, Jun 10} + IN_{Elsa, Jun 10}) \eq 2$$

which violates the final constraint in the preceding section. 

## Preference Constraints

So far, we have only encoded constraints that are globally applicable accross all RAs. But, as we said before, RAs submit preferences about which shifts they would like to have on each day. These preferences are as follows:

**ON Preference**: I would prefer to have an ON shift this day 
**IN Preference**: I would prefer to have an IN shift this day but if not, do **NOT** schedule me to work this day at all
**OFF Preference**: I cannot work this day 
**NO Prference**: Anything you assign to me this day is fine

We care right now about the IN and OFF Preferences, which give rise to our two last Hard Constraints.

{:center: style="text-align: center"}
**Hard Constraint 7: Never schedule someone for an ON shift if they put an IN preference**
{:center}

{:center: style="text-align: center"}
**Hard Constraint 8: Never schedule someone for an ON or IN shift if they put an OFF preference**
{:center}

These are pretty simple to encode. For example, if Yoda put an IN Preference on May 15, we simply need that:

$$ON_{Yoda, May 15} = 0.$$

And if Patrick had put an OFF preference on June 10, we simply need that:

$$ON_{Patrick, Jun 10} = 0$$

and 

$$IN_{Patrick, Jun 10} = 0.$$

And with that, we have all our Hard Constraints. Any proposed schedule that meets all eight of these Hard Constraints is a perfectly acceptable schedule and we can use it for the next 27 days. 

<a name="soft"></a>

# Soft Constraint

But, there are probabaly many such perfectly acceptable schedules and we want to be a bit picky. We wan't to pick the one which maximizes some value which is linked to how many ON Preference and IN Preferences we satisfy. That is, out of all the acceptable schedules, we want to pick the one which gives the most RAs their preferred choice of shift accross the 27 days. 

We encode this preference through a Soft Constraint, defined below.

**Soft Constraint**: A rule that says how to pick the best schedule out of all acceptable ones

We want this rule to be some function of how many times we match up an ON preference with an ON shift and how many times we match up an IN preference with an IN shift accross all RAs and all days. To make this a bit easier, we will define a new measure for each RA as follows:

$$A_{i} = \text{Number of ON shifts for RA $i$ which s/he had put an ON preference for}$$
$$B_{i} = \text{Number of IN shifts for RA $i$ which s/he had put an IN preference for}$$

Given these two new measures, we can define the following function:

$$ (A_{Ash} + A_{Bruce} + ... + A_{Zeus}) + (B_{Ash} + B_{Bruce} + ... + B_{Zeus} $$

What does this measure? This sum tells us how many total shift preference matches there were for an acceptable schedule 









