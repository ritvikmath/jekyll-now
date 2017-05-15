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
***What are the patterns in Chance of Admission vs. MCAT and Chance of Admission vs. GPA?***
{:center}

{:center: style="text-align: center"}
***Given these patterns, can we build an all-encompassing model to predict chance of admission given MCAT and GPA?***
{:center}

{:center: style="text-align: center"}
***Given this model, can we reccomend a path for prospective medical school students to optimize their chance of admission?***
{:center}

# Let's Start Simple. How Does Chance of Admission changed based on MCAT and GPA?

We all expect the chance of admission or **admit rate** to increase with increasing MCAT and GPA scores, but in what? Linearly? Quadratically? Or something else altogether?

Let's first look at the change in admit rate due to changes in GPA with MCAT held constant at various levels. Note that the **MCAT is scored between 472 and 528 with a median score of 500**. Below, we fix the MCAT to three ranges: *514-517 (High)*, *498-501 (Medium)*, *486-489 (Low)*. For each range, we plot the **Chance of Admission vs. GPA**.

<figure>
<center>
   <a href="/images/gpa_change.png"><img width="90%" src="/images/gpa_change.png"></a>
</center>
</figure>

The key takeaways are:

* There seems to be a (roughly) linear trend in Chance of Admission vs. GPA. 
* The slope of this linear relationship increases with increasing MCAT scores. Put another way, the higher your MCAT score is, the more that each additional GPA point boosts your chance of admission. This is some preliminary edvidence of a link between GPA and MCAT in determining chance of admission.
* Given a low enough MCAT score, no GPA can make up for it in gaining admission to medical school. That is, looking at the bottom red line, where MCAT is between 498 and 501, a GPA of 2.5 vs 3.9 gives the same chance of admission.


