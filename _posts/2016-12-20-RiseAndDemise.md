
---
layout: post
comments: true
title: The Rise and Demise of College Majors
---

<figure>
<center>
   <a href="/images/major_sun.png"><img width="100%" src="/images/major_sun.png"></a>
</center>
</figure>

<center>
<font size="5"><b>Analyzing the Boom and Bust of College Majors Over Time</b></font>
</center>

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

---

Quick Links: 

* [Motivation](#mot)  
* [The Data](#data)
* [Is Your Major On the Rise or On the Demise?](#rod)
* [Can We Group Majors by GPA Requirements and Admission Rates?](#group)
* [Which Majors are Getting Farther From Reach?](#diff)
* [Notes](#notes)

---

<a name="mot"></a>

# Motivation

All undergraduate students are, at some point in their college careers, required to select a major, or field of study, which they would like to specialize in. This major is often a reflection of genuine passion, percieved lucrativeness, and even global shifts in interest. With that said, we might guess that demand for particular majors is not necisarrily stable over time. 

By identifying the majors for which demand is rapidly rising and those for which demand is rapidly declining, we can ask questions about what factors are causing this systematic education shift. All this begs the natural question of how to measure demand for a particular major. Should we look at college side admissions statistics? Should we look at student side application statistics? Is GPA a good indicator of demand? Well, they all seem like great ideas! 

In this post, we will look at college applications to each major, college admissions by major, as well as the corresponding applicant  admitee GPAs, in order to analyze which majors are on the rise and which are on the demise.

---

<a name="data"></a>

# The Data

We will use admissions statistics from a major US University, the University of California at Los Angeles (UCLA) for our analysis. The data comes from the <a href="https://www.admission.ucla.edu/prospect/adm_tr/Tr_Prof03_mjr.htm" target="_blank">UCLA Admissions Website</a> website. 

The data spans the years **2003 until 2016** and includes fields such as counts, GPAs, and units for applicants, admitees, and enrolees. The data for **Fall 2015** and **Fall 2016** contains a more limited view with only data for applicants and admitees. It is important to note that this data pertains to transfer students who transfer into UCLA from other universities, typically community colleges.

---

<a name="rod"></a>

# Is Your Major On the Rise or On the Demise?

<center>
<div>
<iframe src="https://ritvikmath.shinyapps.io/RiseAndDemise/" style="border: none; width: 850px; height: 800px"></iframe>
</div>
</center>

The tool above lets you go wild and explore which majors are on the rise in terms of number of applicants, applicant GPA, admission rate, and admitted student GPA. There is a lot of information contained here but let's just highlight some of the key takeaways.

* Majors which have a growing applicant rate, decreasing admission rate and a growing admission GPA can be thought of as having "increased demand". Indeed, these majors are attracting more and more applicants, which perhaps the university did not prepare for. In response, the university may have accepted a similar number of students from that major as before, which explains the lower admit rate. In addition, the university would have the ability to raise its admitted GPA with so many more applicants.
* We can reverse the above story to find majors which are on the decline. Indeed, if fewer and fewer studentsa re applying to a major, the university might have to raise its admit rate to maintain a similar number of students from that major. It might also have less flexibility to choose very high performing students in this case.
* We can also check the growth rates of applicants over time to find out which majors are attracting the most students over time.

---

<a name="group"></a>

# Is Your Major On the Rise or On the Demise?

<figure>
<center>
   <a href="/images/major_sun.png"><img width="100%" src="/images/major_sun.png"></a>
</center>
</figure>

---

<a name="diff"></a>

# Which Majors are Getting Farther From Reach?

<figure>
<center>
   <a href="/images/colbars.png"><img width="100%" src="/images/colbars.png"></a>
</center>
</figure>

<figure>
<center>
   <a href="/images/colbars_all.png"><img width="100%" src="/images/colbars_all.png"></a>
</center>
</figure>

---

Thanks for reading and please leave comments!




