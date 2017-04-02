---
layout: post
comments: true
title: How Many Hearts Beat in Sync With Yours?
---

<figure>
<center>
   <a href="/images/header_rel.png"><img width="90%" src="/images/header_rel.png"></a>
</center>
</figure>

---

<script type="text/x-mathjax-config">
  MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});
</script>
<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_CHTML">
</script>

The idea of two hearts beating in unison has long been a powerful image in poetry, music, and romance. Let us see what the realm of mathematics has to say about this idea. The question we will answer is a natural one, but one which will require careful analysis:

{:center: style="text-align: center"}
***On average, how many hearts beat in sync with yours?***
{:center}

Of course, our first question should be: **What does it mean for two hearts to beat in sync?**

We will define two basic notions in answering this question.

* Heartrate: The number of times a heart beats per minute measured in beats per minute (BPM) 
* Offset: Given that two hearts share a heartrate, the time delay between their beats usually measured in seconds

Thus, we say that **two hearts beat in sync if they have the same heartrate and same offset

We will be using a half-empirial, half-theoretical approach to answering our question about how many hearts beat with yours.

First the statistics!

From Statistics Canada, Canada's National Statistics Agency, we gather data on the <a href="http://www.statcan.gc.ca/pub/82-626-x/2013001/t004-eng.htm" target="_blank">distribution of resting heart rates</a> for people ages 6 to 79. This data gives the 5th, 15th, 25th, 50th, 75th, 90th and 95th percentile for resting heart rate. 

<figure>
<center>
   <a href="/images/heart_perc.png"><img width="90%" src="/images/heart_perc.png"></a>
</center>
</figure>

Since we wish to have finer grained data, we will need to make an assumption here.

{:center: style="text-align: center"}
**Assumption 1: The distribution of heart rates between the provided percentiles is uniformly distributed.**
{:center}

This assumption is surely not fully correct but it will serve us well in the absence of finer grained data. We will also assume that our minimum resting heart rate is 40 BPM and the maximum is 100 BPM. These numbers come from an <a href="http://www.mayoclinic.org/healthy-lifestyle/fitness/expert-answers/heart-rate/faq-20057979" target="_blank">article about normal heart rates</a>.

Given our assumption far, we can generate a histogram of the heart rates.

<figure>
<center>
   <a href="/images/heartrate_histo.png"><img width="90%" src="/images/heartrate_histo.png"></a>
</center>
</figure>

Time for some math!

Let's now dive into the calculation of how many hearts beat with yours.

First we'll define :

$$
S = \textrm{Number of people whose heart beats in sync with yours}
$$

$$
B_{i} = \textrm{A variable which is 1 if person i's heart beats in sync with yours and 0 if not}
$$

$$
O_{j} = \textrm{A variable which is 1 if two hearts beating with heart rate j have the same offset and 0 if not}
$$

What we are after is the mean of $S$, also called the expected value of $S$ and denoted as $\mathbf{E}(S)$.

If we index each person in the world as $i=1,2,3 ... , N$ where you are person $i=N$, then we have that:

$$
S = B_{1} + B_{2} + ... + B_{N-1}
$$

Why? Well $S$ is the number of people in the world whose hearts beat with yours and $B_{i}$ is 1 if and only if person i's heart beats in sync with yours. So, summing up all the $B_{i}$'s we will get exactly the count of how many people whose hearts are in sync with yours. 

So we want:

$$
\mathbf{E}(S) = \mathbf{E}(\sum_{n=1}^{N-1} B_{i}) = \sum_{n=1}^{N-1} \mathbf{E}(B_{i}) = \sum_{n=1}^{N-1} \mathbf{P}(B_{i}=1)
$$
