---
layout: post
comments: true
title: Analyzing the UCLA Swipes Black Market
---
# Disclaimer

The purpose of this post is to analyze, elucidate, and understand the market for UCLA Dining swipes through the years. The author DOES NOT endorse the selling of swipes as this is a clear violation of UCLA On Campus Housing Regulations, Section C.7.a, copied below:

*The only person authorized to use a UCLA Dining Meal Plan card is the owner of the card. UCLA Housing and Hospitality Services is the sole vendor of meal plans and dining meals. Dining Plan meals are non-transferable. Meal plan holders may not pass, loan, trade or sell meals or their ID card to anyone for any reason.*

# Motivation

## Background

<figure>
<center>
   <a href="/images/dining_hall2.png"><img width="80%" src="/images/dining_hall2.png"></a>
</center>
</figure>

At UCLA, students living in the residential dorms use a unit of currency called swipes, loaded onto their student IDs, to get access to dining halls and quick service restaurants. 

There are two fundamentally different meal plan styles that students are able to choose between, standard and premier. 

Standard meal plans allocate a set number of swipes at the start of each week (11, 14, or 19), and allow the student to swipe at most one time per meal period (Breakfast, Lunch, Dinner, Late Night). All unused swipes at the end of the week are lost and the student will be allocated another set of swipes at the start of the following week.

In contrast, premier meal plan holders pay a cash premium which gives them increased flexibility in using their swipes. For example, a student who has meal plan 14P (P for premier) is allocated 154 swipes (14 swipes per week for the 11 weeks of the quarter) all at the start of the quarter, with no restriction on when or how many swipes s/he can use per dining period. One reason students often elect to purchase this premier plans is to allow for visiting family or friends to enter dining facilities with them. 

## The Problem

<figure>
<center>
   <a href="/images/dining_hall.jpg"><img width="80%" src="/images/dining_hall.jpg"></a>
</center>
</figure>

All too often, students who purchase premier meal plans find themselves with an extreme surplus of swipes with no chance of using them all by the quarter’s end, when all remaining swipes are lost. Faced with this situation, students elect to sell their remaining swipes, and there is more than enough demand in this black market for swipes. Students living off campus, without access to a meal plan, make up a large chunk of the consumers in the market for swipes. 

With an adequate number of suppliers and demanders for any product, a structured market is bound to arise. This market for swipes will be the focus of analysis for the remainder of this post.

# The Data

Data for this analysis was scraped from a Facebook group designed to connect buyers and sellers of swipes. The data, consisting of ~17000 posts ranging from 2013-2016, includes fields such as when a post was written and the content of the post. The crux of the following analysis relied on a careful and methodical extraction of various fields from the text portion of each Facebook post. In particular, the following features were extracted from each post: whether the post was by a buyer or seller of swipes, how much the author aimed to buy/sell swipes for, how many swipes the post author (typically in the case of a buyer) wanted, which dining facility the post author wanted to buy/sell swipes for.

This all boils down to a problem in Natural Language Processing (NLP), the art of extracting relavant and accurate information from everyday speech. As a gentle introduction to this process, we will share an easy, medium, and hard post to extract information from.

## Easy Case

{:center: style="text-align: center"}

**buying 3 swipes at De neve at 12, $5 each, PM me~**
{:center}



We wish all posts were as easy to analyze as the one above. This post is nice for many reasons including: 

* The post clearly starts with 'buying' indicating that this person wishes to buy a swipe
* The post clearly mentions that '3 swipes' are needed
* The post clearly mentions the name of the dining hall, De neve dining hall
* The post uses a '$' symbol and the word 'each' to clearly convey how much the swipe will be for

## Medium Case

{:center: style="text-align: center"}
**Anyone need Late night Swipes? I have 7 swipes i got to get rid of. $5 - Los Angeles, CA (90024)**
{:center}


The post above is more confusing for a few reasons:

* It is clear to human that this person wants to sell swipes, as indicated by "Anyone need ... ?" but the word "sell" is nowhere mentioned, making this task more difficult for a computer
* Furthremore, the word 'need' is used, which is typically used by buyers i.e. "I need swipes"
* It is clear again to a human that this person is willing to sell 7 swipes at $5 each but the word 'each' is never explicitly used which, is not properly checked, might cause a naive computer to believe this author is selling 7 swipes for a total of $5, clearly not the case
* Still we can manage to work this one out with some clever rules such as picking up on the fact that the word 'need' is used but that the sentence ends in a '?' or that it is probabaly illogical for someone to sell 7 swipes at $5 total, yielding a value of less than $1 per swipe.
 
## Hard Case

{:center: style="text-align: center"}
**swipes bplate 1pm, $5 - los angeles california, help me raise money for my friend's unicamp project! thanks!**
{:center}


This post is very clear to a human but very hard for a computer to understand for a few reasons:

* Even for a human, just reading the first part is a bit confusing. That is, if we just read up to: "...los angeles california" we are not really use if this person is in need of swipes at at bplate (a dining hall) at 1pm or will be selling swipes at bplate at 1pm. We might lean towards selling
* After reading the latter half of the post, it is clear to a human that this person is raising money for their friend's project and thus must be selling swipes, as we might have suspected. But, this is a very very special case and a computer will find it very hard to pick up on this nuance. For this reason, posts such as these are tagged neither with a 'b' for buyer or 's' for seller but rather  with an 'n' for 'not sure', in order to avoid misclassification. 

# Whew. Enough of all the words, let's see some Graphs!

All this data begs some immediate (and some not so immediate) questions. Let's ask each one and answer it with a cool graph!

## What is the activity of the swipe market over time?

The activity of any economic market, even a black market, relies on supply being available and demand being high. The supply side is easy. Students only have meal premier plans during academic quarters, Fall, Winter, and Spring. So we expect a huge drop (theoretically) down to zero between quarters and in the summer. The demand side is a bit more nuanced. Obviously, students demand swipes mainly during academic quarters but there are more subtleties going on here. 

For example, at the beginning of the quarter, students are likely less dependent on buying swipes and have their fridges stocked (with health food for their ephemeral diets). But, as any student knows, when midterms, and especially finals come around, cooking is not a top priority. A potentially cheap all you can eat meal at a dining hall sounds like a great option. Indeed, we expect demand for swipes to rise at the end of each quarter. Expanding on the supply side, we also expect more meal-plan-equipped students to realize their daunting surplus of swipes and so supply shoots up around the end of the quarter as well. Are we right with our expectations ? Lets find out.

### Number of Posts to Facebook Page by Day

<figure>
<center>
   <a href="/images/post_volume.jpg"><img width="100%" src="/images/post_volume.jpg"></a>
</center>
</figure>

Indeed our predicitons were right! The green vertical lines indicate the end of each academic quarter and are indeed the naturaly stopping points for upward trends in the graph. We see that the 2014 - 2015 academic year saw a huge growth in the swipe market with a potential decline in the 2015 - 2016 academic year.

## Where are buyers eating?

One often cited problem with schools that use the swipe system for meals is that a swipe at one dining location will buy a completely different dining experience than a swipe at another dining location. For example, one swipe at the popular quick service restaurant Bruin Cafe will can buy a carton of Thrifty ice cream, which I can pick up for $2.50, at my local RiteAid. One swipe will also get me access to an all-you-can-eat dining hall such as De Neve, where I can indulge in college student (not so) guilty pleasure food such as pizza, burgers, fries, and as much ice cream as my heart desires, valued at $14.50 for non-meal-plan-carrying folk. 

Also, given the choice between paying UCLA Dining $14.50 for an all-you-can-eat experience and paying $5 to a freshman who grossly miscalculated how many swipes she would need this quarter, it is evident what students are choosing. We thus expect the high-value dining halls, Covel (CO), De Neve (DN), Bruin Plate (BP), and Feast (FE) to dominate the locations which swipe buyers frequent. The three quick service restaurants, Rendevous (RN), Cafe 1919 (19), and Bruin Cafe (BC) should make up a very small fraction of the swipe market.

### Demand for UCLA Restaurants

<figure>
<center>
   <a href="/images/pie_loc.jpg"><img width="80%" src="/images/pie_loc.jpg"></a>
</center>
</figure>

From the chart, we see that altogether the three quick service restaurants, where the dollar value of a swipe is relatively low, are frequented only 4% of the time. The Big 4 Dining Halls make up the overwhelming majority of the locations in the market for swipes. Feast (Asian Cuisine) is frequented most often, then Bruin Plate (Healthy Food), followed by De Neve (Tasty Junk Food), with Covel (In my opinion, improving) coming in last. 

## How much does UCLA Dining lose?

As with many black markets (illegal music, pirated DVDs, etc.) the original creator of the product never sees revenue from underground transactions. The natural question is then: how much revenue does UCLA Dining lose from the operation of the swipe market?

Better yet, let's think about how much revenue is lost and when it is lost. We know that in times between quarters, winter, spring, and summer breaks, there are fewer transactions taking place and thus there is less revenue being lost. But, we also know that around the end of academic quarters, especially in finals week, we see a surge of trades in the market, and should thus expect to see a surge of lost revenue. But, then again, maybe not ... Maybe students who are buying swipes at the end of quarters are mostly buying swipes to quick service restaurants because it takes up less valuable study/sleep time during finals week. If that is the case, we might not see a surge in lost revenue around finals week. 

To answer the question we will focus only on people who buy swipes to dining halls (the Big 4 in the donut plot above) and use the following pricing information provided by UCLA dining:

<figure>
<center>
   <a href="/images/dining_prices.png"><img width="80%" src="/images/dining_prices.png"></a>
</center>
</figure>

We use the prices from Non-OCH (On Campus Houising) Residents since these make up the bulk of consumers, UCLA students without meal plans of their own.

Let's see what our data says:

### Lost Revenue Over Time

<figure>
<center>
   <a href="/images/lost_rev.jpg"><img width="100%" src="/images/lost_rev.jpg"></a>
</center>
</figure>

The upper plot shows three estimates: Low, Middle, and High. The Low estimate is the lost revenue if all the people in the data who bought Dining Hall swipes bought breakfast swipes, which have the cheapest value at $11.00 each. This is clearly not close to accurate. The green High estimate is the lost revenue if all the people in the data who bought Dining Hall swipes bought dinner swipes, valued at $14.50 each, which is also not realistic but likely more realistic than the Low estimate case. The yellow curve in the middle takes is the Middle estimate, simply an average of prices of a Breakfast, Lunch, and Dinner swipe and comes out to $13.08 each. 

We see that indeed lost revenues stagnate in the breaks betweeen academic quarters but also rise sharply in finals week, as we predicted. 

Looking at the bottom chart, we see that lost revenue per academic year is also on the rise, rising in a roughly linear fashion. 

The exact values of lost revenue by year are:

* **$2276** for the 2013-14 Year
* **$12256** for the 2014-15 Year
* **$23567** for the 2015 - 16 Year

If lost revenues continue to follow this pattern, a naive, back-of-the-envelope estimate says that UCLA Dining should expect to lose **$36209** worth of revenues in the 2016-17 Year.


