---
layout: post
comments: true
title: Detecting Cheating in Lecture Halls
---

<figure>
<center>
   <a href="/images/coverpiclecture.png"><img width="100%" src="/images/coverpiclecture.png"></a>
</center>
</figure>

<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
  tex2jax: {
    inlineMath: [['$','$'], ['\\(','\\)']],
    processEscapes: true
  }
});
</script>
<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_CHTML">
</script>

I recently got to thinking about how a college professor could detect whether or not students were cheating on a class exam. Of course, the only way to definitively accuse a student of cheating is to observe them cheating in the moment. That is, observe them looking at another student's exam, for example. Still, there had to be some statistical ways to determine whether cheating had occurred during the exam even if you can't prove which students were responsible. 

The idea would be fairly simple. From here on out, pretend you're the professor of your favorite course (and comment that course below!)

**First**, you would randomize students to seats on exam day, perhaps alphabetically or project a randomized seating chart for students to follow.

**Second**, after the exam, you would count how many pairs of students (students sitting right next to each other) had the **exact same score** on their exams. 

**Third**, you would ask yourself if that many pairs with identical scores was "normal" or if it was too high to be a concidence.

Seems simple enough? Cool! Let's talk about some of the details and run through an example.

For this to work, you'll need two assumptions to hold. Good news is that these assumptions aren't far fetched at all. 

First off, you (the professor), need an adequate number of students in the course so that you dont run into issues with too small of a sample size. In reailty, many lower division and some upper division courses at many colleges can get quite large. For our example we will assume a lecture hall which is 15 seats by 20 seats so that it accomodates 300 students on exam day. 

Second, we will assume that you have taught this course multiple times in the past and understand well what the grade distribution should look like. This, again, is realistic for a professor who has been teaching a course for multiple terms. For our example exam, we will assume that the grades are usually distributed normally (as in a bell-curve) with mean 70% and standard deviation 15% with a maximum score of 100%. This distribution is shown below.

## Expectation of Exam Distribution

<figure>
<center>
   <a href="/images/exam_score_distr.png"><img width="100%" src="/images/exam_score_distr.png"></a>
</center>
</figure>



