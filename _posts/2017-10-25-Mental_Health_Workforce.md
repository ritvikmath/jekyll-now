---
layout: post
comments: true
title: Top 5 Most Toxic Workplace Combinations for Mental Health
---

<figure>
<center>
   <a href="/images/mh_cover.jpg"><img width="90%" src="/images/mh_cover.jpg"></a>
</center>
</figure>

# Motivation

**Fact 1:** Two-thirds of all Americans report being disengaged at work or actively despise their job

**Fact 2:** Americans spend one third of their day at work

These two facts coupled together don't spell out a positive outlook for the nation's mental health. Let us find out which types of workplaces breed, or perhaps attract, the most workers who report that a mental health issue hinders their productivity at work. Perhaps by identifying these toxic factors in workplaces, we as a nation can build more mentally hospitable, and thereby more productive, corporate environments. 

# The Data

The data comes from a 2016 OSMI (Open Sourcing Mental Health) survey which asked respondents to answer a series of questions related to their workplace inculding its mental health policies. Respondents were also asked to answer questions about whether they have a mental health issue, and if so, whether it impedes their performance at work. 

It is imporant to note that since this is a survey, we will inherently have some bias. For example, given that this survey is about mental health issues in workplace, we can expect that people with strong feelings about this topic (such as those with mental health issues) are probabaly more likely to respond. In addition, it is very possible that multiple people from the same company respond to the survey together, causing that company to be overrepresented. Still, we should be somewhat safe from these biases since, as we will see shortly, we are measuring relative magnitudes of the differences in certain percentages, ignoring the biased percentages themselves.

# So What Are We Going to Measure?

Our method is very simple. We are going to take each possible pair of factors in our dataset and first compute, independently, what percent of people responding "Yes" to each factor also report that a mental health issue gets in the way of their work. 

For example, we look at people who say ***"Yes, my employer discussed mental health with me"*** and compute what proportion of them report a mental health issue getting in the way of work. Then, we look at those who say ***"Yes, I feel comfortable discussing a mental health issue with my supervisor"***, and see what proportion of them report a mental health issue interfering with work.


We then look at all the workplaces with a combination of the two factors (***"Yes, my employer discussed mental health with me"*** and ***"Yes, I feel comfortable discussing a mental health issue with my supervisor"***) and compute the proportion of people that report a mental health issue interfering with work. 

Last, we compute the average difference between the combined proportion and the two individual proportions and find the highest such differences. In more intuitive terms, we are finding the workplace factors which, perhaps alone are not toxic, but when combined in a workplace, create a destructive dissonance for employee mental health.  



