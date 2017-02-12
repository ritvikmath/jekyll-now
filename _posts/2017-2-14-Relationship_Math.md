---
layout: post
comments: true
title: The Length and Strength of Romantic Relationships
---

<figure>
<center>
   <a href="/images/title_hearts.png"><img width="80%" src="/images/title_hearts.png"></a>
</center>
</figure>

<center>
<font size="5"><b>Analyzing Why Couples Break Up</b></font>
</center>

---

Quick Links: 

* [Motivation](#mot)  
* [The Data](#dat)  
* [What are Commonalities within Dating vs. Married Couples?](#com)  
* [At What Age Do People Meet their Significant Others?](#age)  
* [Where Do Couples Meet?](#where)  
* [When is a Couple Most Likely to Break Up?](#len)  
* [What are the Breakup Rates Based on Race, Religion, etc.?](#break)
* [How Likely is a Couple to Break Up Based On Where They Met?](#met) 
* [Can We Build a Model to Predict Breakup?](#model)
* [Notes](#not)  

---
---

<a name="mot"></a>

# Motivation

Romantic relationships, including their formation, continuation, and dissolution, are often percieved as mysterious processes eluding rationalization. Indeed, so some extent they surely are, but in another light, there must be underlying statistical trends to these processes as there are for all of the world's other happenings.

By getting to the root of the trends underlying the dissolution of romantic relationships, we can understand the main factors that lead a couple to break up or not break up. Then, given these factors, we can begin to build a model designed to measure the strength of a romantic relationship. We can then use this strength measure in predicting whether or not this couple will dissolve within some specified future period. 

---

<a name="dat"></a>

# The Data

The data used in this analysis comes from the <a href="https://data.stanford.edu/hcmst" target="_blank">Stanford University Social Science Data Collection</a> and is cited in the [Notes](#not) section. This is a dataset containing individual level survey answers from a sample of 4002 adults in the United States. It contains a great variety of columns which range over a multitude of personal questions about the person and their current relationship and questions about their significant other, if they have one. 

What makes this data extra valuable is that there were follow up surveys of these individuals in the subsequent years. That is, the original survey took place in 2009 and was followed by a second wave in 2010, a third in 2011, a fourth in 2013 and a final fifth between 2014 and 2015. This adds a great depth of value because we not only get a static snapshot of the survey particpants, but also a follow up history. Indeed, it is this time component that allows us to identify couples that broke up and start asking questions about what factors might have been correlated with this dissolution.

---
---

<a name="com"></a>

# What are Commonalities within Dating vs. Married Couples?

We start by looking at the similarities between two people who are dating and two people who are married. Dating is often percieved as a stepping stone to a long term commitment and eventually marriage. We would thus expect there to be some stronger similarities, possibly even demographically, between married couples compared to dating couples. Let's look at these similarities on four axes: race, religion, political party, and college education.

---

## Dating Couples

<figure>
<center>
   <a href="/images/dating.png"><img width="100%" src="/images/dating.png"></a>
</center>
</figure>

---

## Married Couples

<figure>
<center>
   <a href="/images/married.png"><img width="100%" src="/images/married.png"></a>
</center>
</figure>

---

There are some very interesting key takeaways from comparing these two diagrams:

* More than 3 out of every 4 dating couples are the same **race** and that proportion jumps by over 10% when we look at married couples. It seems, from these figures, that same-race couples tend to stay together and get married at a higher rate than do different-race couples.

* The story with **religion** is similar in terms of proportion increase from dating to married couples but varies in one important way. Namely, whereas most couples were same race, most couples are actually different in terms of their religious beliefs. 

* Looking at **political party**, we see that about half of all dating couples share a political party and interestingly, this number does not go up by much when we look at married couples. It seems, thus, that we have some shreds of evidence supporting that political party is not a major factor in couple dissolution. We will come back to that point during the back half of this post.

* Lastly, we see that for dating couples, the proportion who attended the same **university** is quite low at just around 15% but when we look at dating couples, this number more than doubles. This is an indication that couples who did not attend the same college or university tend to break up at a higher rate than those who did. This perhaps makes sense due to shared experiences, geographic proximity, etc.

---
<a name="age"></a>

# At What Age Do People Meet their Significant Others?

Another question we can ask is at what age people meet their significant other. We first split up our population into four groups: dating males, dating females, married males, married females. We then ask, for each group, when each person met the person they are currently dating / married to, and analyze the results. The histograms below outline the results.

<figure>
<center>
   <a href="/images/age_met_histo.png"><img width="100%" src="/images/age_met_histo.png"></a>
</center>
</figure>

Well, one of these graphs is not like the other three. Let's discuss the results:

* Looking just at married couples, we can see the clear difference between females and males is that **most females meet their future spouse around age 22-23** while **most males meet their future spouse around age 25-26**. This is best attributable to the fact that the male is older than the female in a majority of heterosexual couples. 

* We see some really surprising resluts looking now at the dating population. Namely, **dating females have a lower chance of meeting their partner later in life** whereas **dating males have a higher chance of meeting their partner later in life**. We can try to attribute this to the same trend as before, but given the huge difference between these tro graphs, there must be some other force at play. One idea is to attribute this to the social stigma against women dating when they get older, a stigma which seems to be weaker towards men dating later in life. 

* There are also some easy-to-miss subtleties in these graphs. It is best illustrated with the Dating Female chart. We see that although the bars decline on average as the age gets larger, there seems to be an up-and-down pattern to the bars. Translating this to real-talk, it seems that the probability of meeting a parter goes up and down through a woman's 30's and 40's. It is unclear, at least to this author, what a possible cause might be. If you have an idea, post in the comments below!


---

<a name="where"></a>

# Where Do Couples Meet?

Another question we can ask is where couples tend to meet. We've all heard of  various ways couples meet including college romances, online dating, and workplace relationships. But, what proportion of relationships fall into each of these buckets? And, to go a bit further, what proportion of eventual marriages started in each of these buckets? Let's defer to the data.

<figure>
<center>
   <a href="/images/datmarbars.png"><img width="100%" src="/images/datmarbars.png"></a>
</center>
</figure>

Cool stuff! :

* We see that **the most popular places to meet a current partner are at work or a bar/nightclub** if we ignore the "Other" category.

* But, **the most likely places for an eventual married couple to meet are at work or at school** again ignoring the "Other" bin.

* These two findings together imply something that we will see proof of a bit later one, which is that the locations for which the blue married bar is lower than the grey dating bar should have a higher breakup rate. Furthermore, the relative sizes of these bars should provide an indication of how severe the breakup rate is. Just as one example, not many people meet their significant other at church, but relationships that start there tend to stay together, as evidenced by the corresponding marriage bar being nearly three times the height of the dating bar in the "Church" bin.

Stay tuned for more on this later in this post!

---
---

<a name="len"></a>

# When is a Couple Most Likely to Break Up?

This second portion of the post will focus on dissolution rates in dating couples (so we will not consider married couples here). We really want to find out forces make or break a couple so that in the third part of this post, we can use that information to build a predictive model for couple dissolution. 

The first question on our minds concerns the tendency for a couple to break up based on how long they have already been together. Now, some of you might be saying, "well obviously the longer they have been together the less likely they are to break up!" Let's see what the data has to say.

## Probability of Breakup Within 1 Year Based on Length of Relationship

---

<figure>
<center>
   <a href="/images/prob_breakup_overtime.png"><img width="100%" src="/images/prob_breakup_overtime.png"></a>
</center>
</figure>

Hmm ... :

* It seems you were mostly right! The probability of breakup does indeed tend to decrease with the length of the relationship, especially after 3 or more years, where the breakup rate is only at 14%! But, let's not ignore the elephant in the graph. What's up with that spike at 1-3 Months? This author believes this is attributable to the **"Honeymoon Phase"** where any real problems underlying a relationshps have not manifseted or are simply buried under the excitement of a new romance. This would explain the jump from the "Less than 1 Month" bin to the "1-3 Months Bin"

* It is still worth noting though that breakup rates remain well above 50% for any relationship 3 months or newer.

* Another point worth noting is that the breakup probability goes down by a good **5%** after the 1 Year mark but the  1-2 Years and 2-3 Years break up rates are nearly identical, indicating some sort of marginal returns to time. That is to say: **perhaps the probability of breakup continues to decrease as the relationship progresses, but decreases by less and less for each additional month of dating**. Put an even simpler way: The fact that a relationship lasts one year drives the breakup probability down a lot but the fact that it lasts another year after that doesnt drive the breakup probability down as much. And it goes down even less for each subsequent year thereafter.

---

<a name="break"></a>

# What are the Breakup Rates Based on Race, Religion, etc.?


---

<a name="met"></a>

# How Likely is a Couple to Break Up Based On Where They Met?


---

<a name="model"></a>

# Can We Build a Model to Predict Breakup?


---

<a name="not"></a>

# Notes


Thanks for reading and please leave comments!



