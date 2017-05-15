---
layout: post
comments: true
title: Optimizing Your Chances of Medical School Admission
---

<figure>
<center>
   <a href="/images/coverbeat.jpeg"><img width="90%" src="/images/coverbeat.jpeg"></a>
</center>
</figure>

---

<script type="text/x-mathjax-config">
  MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});
</script>
<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_CHTML">
</script>

In 2016 there were **27,772** students who applied to Medical Schools across the United States. Of these students, **8,883** were granted admission, **an admit rate of 32%**. But of course, the overall admit rate is not very enlightening. The data we are really interested in for this post is about **how that admit rate changes based on GPA and MCAT (Medical College Admission Test) score**.

We of course know roughly that a higher GPA and/or a higher MCAT score will lead to a higher chance of admission, all else held constant, but we want to really get down into the details here. Our analysis will progress by asking a **series of questions**:

{:center: style="text-align: center"}
1. ***What are the patterns in Admit Rate vs. MCAT and Admit Rate vs. GPA?***
{:center}

{:center: style="text-align: center"}
2. ***Given these patterns, can we build an all-encompassing model to predict admit rate given MCAT and GPA?***
{:center}

{:center: style="text-align: center"}
3. ***Given this model, can we reccomend a path for prospective medical school students to optimize their chance of admission?***
{:center}

# Let's Start Simple. How Does Admit Rate changed based on MCAT and GPA?

We all expect the chance of admission or **admit rate** to increase with increasing MCAT and GPA scores, but in what? Linearly? Quadratically? Or something else altogether?

Let's first look at the change in admit rate due to changes in GPA with MCAT held constant at various levels. Note that the **MCAT is scored between 472 and 528 with a median score of 500**. Below, we fix the MCAT to three ranges: *514-517 (High)*, *498-501 (Medium)*, *486-489 (Low)*. For each range, we plot the **Admit Rate vs. GPA**.

<figure>
<center>
   <a href="/images/gpa_change.png"><img width="90%" src="/images/gpa_change.png"></a>
</center>
</figure>

The key takeaways are:

* There seems to be a (roughly) linear trend in Admit Rate vs. GPA. 
* The slope of this linear relationship increases with increasing MCAT scores. Put another way, the higher your MCAT score is, the more that each additional GPA point boosts your chance of admission. This is some preliminary edvidence of a link between GPA and MCAT in determining admit rate.
* Given a low enough MCAT score, no GPA can make up for it in gaining admission to medical school. That is, looking at the bottom red line, where MCAT is between 498 and 501, a GPA of 2.5 vs 3.9 gives the same admit rate of around 3%.

Now let's turn to a more interesting trend, that of Admit Rate vs. MCAT for some fixed values of GPA. Here we fix the GPA at three levels: *3.8-4.0 (High)*, *3.4-3.6 (Medium)*, *3.0-3.2 (Low)*. Note here that even though a GPA of 3.0 is labeled as *low*, you should take that to mean relatively low rather than absolutely low. Indeed, even those with a GPA in the *low* range can achieve a peak admit rate of 50% given a high enough MCAT score. 

<figure>
<center>
   <a href="/images/mcat_change.png"><img width="90%" src="/images/mcat_change.png"></a>
</center>
</figure>

The most striking thing about this figure is that the curves do not follow a linear or quadratic trend but rather follow a **mathematical shape called a sigmoid**. Sigmoids, generally S-shaped curves, appear in many other contexts, perhaps most popularly in population models. They describe some process which is **slow to pick up** (a slow growth at the beginning), **then gains momentum** (fast growth in the middle), before **finally capping off at some level** (slow growth at the end). 

Indeed they make perfect sense in our context too! Given a very low MCAT score, boosting that score by a little bit will **help a bit in the beginning but not much**. Once you keep boosting the MCAT score, you **realize greater and greater gains**, causing your admit rate to increase faster and faster. Finally, when your MCAT score is already fairly high, **additional gains in your MCAT score do not help much**.

Note also that the sigmoid shape is more defined for higher values of GPA. We also see the effect of different GPA levels on the sigmoid by, for example, looking at the admit rate for the highest value of MCAT for the three GPA bands. We see for the low GPA curve, the admit rate here is around 50%, for the middle GPA curve it is around 60%, and for the highest GPA curve it is around 85%.

# Cool Trends! But Can we Fit Models to Them?

Now that we some some idea of the trends in admit rate based on GPA and MCAT, we would like to know if we can fit a (not too complex) mathematical model to these trends to predict admit rate for any combination of GPA and MCAT score with a decent degree of accuracy. Before tackling the whole problem, let's just see how good we can do at predicting those sigmoids from the last figure.

<figure>
<center>
   <a href="/images/sigmoid_preds.png"><img width="90%" src="/images/sigmoid_preds.png"></a>
</center>
</figure>

Here we took the three Admit Rate vs. MCAT curves from the last section and **chose (carefully) some sigmoids to best fit this data**. The sigmoid fits are shown with a red dotted line. Recall that the three curves represent **High, Medium, and Low GPA bands**. We see that at least **for the high GPA band, our prediction is almost prefect**. As we get to lower GPA bands, the **prediction is not as strong but still captures the dynamics of the data**. 

Using the fact that our model seems to predict well for higher values of GPA, we will **limit our prediction to applicants whose GPA was 3.1 and higher**.

# A Full Model

All the pieces are here. But we need to figure out how to put them together in order to create an all-encompassing model which, given your GPA and MCAT score, will give a (hopefully accurate) prediction of your chance of admission to medical school in the United States. Seems like a daunting task but let's list out what we know such a model needs to include:

* Given some fixed value of GPA, the model needs to be sigmoidal for changing values of MCAT score. 
* Given some fixed value of GPA, the properties of this sigmoid (slope, offset, etc.) need to change as a function of GPA.
* Given some fixed value of MCAT score, the model needs to be (roughly) linear for changing values of GPA.
* The model will be limited to applicants with a GPA of 3.1 or higher.

Taking all these rules into account, and using some mathematical fitting techniques to minimize our error, we arrive at the following function.

$$
p(G,M) = \frac{-1.5 + 0.61 \times G}{1+e^{-0.2 \times (M - 512.75 + 2.5G)}}
$$



