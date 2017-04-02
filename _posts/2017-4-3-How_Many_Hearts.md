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

Thus, we say that **two hearts beat in sync if they have the same heartrate and same offset.**

We will be using a half-empirial, half-theoretical approach to answering our question about how many hearts beat with yours.

First the statistics!

From Statistics Canada, Canada's National Statistics Agency, we gather data on the <a href="http://www.statcan.gc.ca/pub/82-626-x/2013001/t004-eng.htm" target="_blank">distribution of resting heart rates</a> for people ages 6 to 79. This data gives the 5th, 10th, 25th, 50th, 75th, 90th and 95th percentile for resting heart rate. 

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

What we are after is the mean of $S$, also called the expected value of $S$ and denoted as $\mathbf{E}(S)$.

If we index each person in the world as $i=1,2,3 ... , N$ where you are person $i=N$, then we have that:

$$
S = B_{1} + B_{2} + ... + B_{N-1} = \sum_{n=1}^{N-1} B_{i}
$$

Why? Well $S$ is the number of people in the world whose hearts beat with yours and $B_{i}$ is 1 if and only if person i's heart beats in sync with yours. So, summing up all the $B_{i}$'s we will get exactly the count of how many people whose hearts are in sync with yours. 

So we want:

$$
\mathbf{E}(S) = \mathbf{E}(\sum_{n=1}^{N-1} B_{i}) = \sum_{n=1}^{N-1} \mathbf{E}(B_{i}) = \sum_{n=1}^{N-1} \mathbf{P}(B_{i}=1)
$$

using in the last equality the fact that the mean of an indicator variable is the probability that this variable is 1.

We can go one step further if we make another assumption:

{:center: style="text-align: center"}
**Assumption 2: Heart rates are independent between people.**
{:center}

This is likely much easier to swallow than Assumption 1 but of course is still not completely true as people who work out together, attend the same sporting event, etc. will have more similar heart rates. Still, on a global level, we should be safe with this assumption.

Then, our independence assumption allows us to reduce the result to:

$$
\mathbf{E}(S) = \sum_{n=1}^{N-1} \mathbf{P}(B_{i}=1) = (N-1) \mathbf{P}(B_{i}=1)
$$

so that we need only to find $\mathbf{P}(B_{i}=1)$.

Exiting the math-o-sphere for a moment, we only need to find the probability that someone's heart is in sync with yours.

Now, under what conditions would someone's heart be in sync with yours? As noted earlier, we need only that both your heart rates are the same and your offsets are the same. For example, both your heart rates could be 55 BPM and you have the same offset, or perhaps your heart rates are 77 BPM and you have the same offset, or perhaps you both share a heart rate of 90 BPM with the same offset. In fact, there are infinitely many heart rates that you can share, any number between 40 and 100! How do we simplify this? Well, we will make another assumption here:

{:center: style="text-align: center"}
**Assumption 3: We will treat the continuous range of heart rates as a large range of integer values.**
{:center}

That is, if we are considering heart rates between 40 BPM and 52 BPM, we choose to split this interval up into 12 allowable integer heartbeats. Why do we do this? Looking at the way heart rate is typically reported by medical equipment, it is given in intgeger valued beats per minute.

Now, given that two pepople have the same heart rate, how do we measure whether they have the same offset?

Let's think about this with an example. Say both you and your friend have a heart rate of 40 BPM which is the same as 40 beats per 60 seconds which implies that your hearts beats once every 1.5 seconds. 

Now, the probability that your friend's heart beats *exactly* when yours does is 0 because there are infinitely many possible offsets in a fininte amount of time. Thus, we will need to make a final assumption in order to conduct a meaningful analysis going forward.

{:center: style="text-align: center"}
**Assumption 4: Two hearts with the same heart rate will be considered as having the same offset if their beats are within some error tolerance of one another.**
{:center}

Essentially, if your friend's heart beats just a tiny fraction of a second afters yours does, we will consider the offsets to be the same. We will denote the error tolerance as $\epsilon$. Going back to our 40 BPM example, we allow that your friend's heart beats in any of the green regions in the figure below. Note that the probability that your friend's heart beats in the green region is $\frac{2\epsilon}{1.5}$.

<figure>
<center>
   <a href="/images/eps_beat.png"><img width="90%" src="/images/eps_beat.png"></a>
</center>
</figure>

So, if two hearts beat at $K$ Beats per Minute, they each beat once every $\frac{60}{K}$ seconds the probability that they have the same offset is $\frac{K\epsilon}{30}$.

 We will let $\epsilon$ be 1% of $\frac{60}{K}$ going forward which implies that the probability that two hearts with the same heart rate share an offset is $\frac{0.01K\frac{60}{K}}{30} = 0.02$ regardless of the heart rate.
 
 Now, we are ready to finish our calculation!
 
 Recall that we are looking for  $\mathbf{P}(B_{i}=1)$, the probability that someone's heart beats in sync with yours.
 
 Note that:
 
 $$
 \mathbf{P}(B_{i}=1) = \sum_{i=40}^{100} \mathbf{P}(\textrm{Your Heart Rate = j and Their Heart Rate = j and Offset's match})
 $$
 
 
 
 
 

 
 


