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

<a name="com"></a>

# What are Commonalities within Dating vs. Married Couples?

We start by looking at the similarities between two people who are dating and two people who are married. Dating is often percieved as a stepping stone to a long term commitment and eventually marriage. We would thus expect there to be some stronger similarities, possibly even demographically, between married couples compared to dating couples. Let's look at these similarities on four axes: race, religion, political party, and college education.

---

## Dating Couples

<figure>
<center>
   <a href="/images/dating.png"><img width="75%" src="/images/dating.png"></a>
</center>
</figure>

---

## Married Couples

<figure>
<center>
   <a href="/images/married.png"><img width="75%" src="/images/married.png"></a>
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

Another question we can ask is at what age people meet their significant other. We first split up our population into four groups: dating males, dating females, married males, married females. We then ask, for each group, when each person met the person they are currently dating / married to, and analyze the results. The histograms below outline the results.

<figure>
<center>
   <a href="/images/age_met_histo.png"><img width="100%" src="/images/ge_met_histo.png"></a>
</center>
</figure>

Well, one of these graphs is not like the other three. Let's discuss the results:

* Looking just at married couples, we can see the clear difference between females and males is that **most females meet their future spouse around age 22-23** while **most males meet their future spouse around age 25-26**. This is best attributable to the fact that the male is older than the female in a majority of heterosexual couples. 

* We see some really surprising resluts looking now at the dating population. Namely, **dating females have a lower chance of meeting their partner later in life** whereas **dating males have a higher chance of meeting their partner later in life**. We can try to attribute this to the same trend as before, but given the huge difference between these tro graphs, there must be some other force at play. One idea is to attribute this to the social stigma against women dating when they get older, a stigma which seems to be weaker towards men dating later in life. 

* There are also some easy-to-miss subtleties in these graphs. It is best illustrated with the Dating Female chart. We see that although the bars decline on average as the age gets larger, there seems to be an up-and-down pattern to the bars. Translating this to real-talk, it seems that the probability of meeting a parter goes up and down through a woman's 30's and 40's. It is unclear, at least to this author, what a possible cause might be. If you have an idea, post in the comments below!

# At What Age Do People Meet their Significant Others?


---

<a name="where"></a>

# Where Do Couples Meet?


---

<a name="len"></a>

# When is a Couple Most Likely to Break Up?


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


