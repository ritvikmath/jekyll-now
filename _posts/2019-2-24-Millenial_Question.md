---
layout: post
comments: true
title: Where Can You Afford a House AND Avocado Toast?
---

<figure>
<center>
   <a href="/images/fcover2.png"><img width="100%" src="/images/fcover2.png"></a>
</center>
</figure>

<script type="text/x-mathjax-config">
  MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});
</script>
<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_CHTML">
</script>

---

We all know that millenials love avocado toast. We all also know that millenials can't afford a house. Well worry not! This post will answer the question of where you should move for the best chances of buying both a house AND your precious avocado toast.

# The Data
---

The final dataset used in this post is a combination of data from three sources. The first dataset is from the Hass avocado board and contains information about avocado prices and quantities sold over time and in each U.S. region.

http://www.hassavocadoboard.com/retail/volume-and-price-data

The second two datasets from rom the U.S. Census Bureau and contain information on average income by U.S. county and average house prices by U.S. county.

We join these three datasets together to get a final dataset which gives us information about average avocado prices over time in each U.S. region as well as average income and average housing price information for those regions.

Note that we will be considering Large Hass Avocados here, as they are the most popular and we dont want interference in our data from different types of avocados.

# Methodology
---

Let's start by recognizing that getting our answers isn't as simple as ranking each U.S. region by avocado price or house price. It really depends on your income too. For example, if avocados are twice as expensive in City B as in City A, but your income in City B would be four times as much, you'd be better off living in City B since you can afford twice as many avocados, all else held constant.

So let's define two sensible scores for each U.S. region:

$$
Housing Score = \frac{\text{Average Income}}{\text{Average House Price}}
$$

$$
Avocado Score = \frac{\text{Average Income}}{\text{Average Avocado Price}}
$$

So we really want to find the U.S. cities where both **Housing Score** and **Avocado Score** are maximized. But how do we maximize two metrics at once? Well suppose we are comparing two cities, City A and City B and we plot their Housing Score and Avocado Score on a grid.

<figure>
<center>
   <a href="/images/avoTutorial.png"><img width="100%" src="/images/avoTutorial.png"></a>
</center>
</figure>

We see that City A has a *slightly higher* Housing Score than City B but City B has a *much higher* Avocado Score than City A. So, we go with City B here. Another, more graphical way, to describe our decision is that we went with the city which was furthest from the origin, (0,0).

This is a good place to note that we will be normalizing the Housing Score and Avocado Score for this analysis. That is, for a fair comparrision we will be bringing those two scores into the same ballpark since houses tend to be more expensive than avocados. 

Let's see the results using our real data!

<figure>
<center>
   <a href="/images/houseAvoToastGraphic.png"><img width="100%" src="/images/houseAvoToastGraphic.png"></a>
</center>
</figure>

We see here the five worst cities to live in when it comes to buying a house *and* avocado toast are cloest to the origin and the five *best* cities are furthest from the origin. Note that the top city, Detroit, is actually off this chart, which is why there are just four green points circled. 
