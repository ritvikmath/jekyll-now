---
layout: post
comments: true
title: Salary Dynamics in the University of California
---

<figure>
<center>
   <a href="/images/sankey.jpg"><img width="100%" src="/images/sankey.jpg"></a>
</center>
</figure>

<center>
<font size="5"><b>Exploring Salaries throughout the UC System</b></font>
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

# Disclaimer

The raw data used for this analysis is publically available and contains names, job titles, and salaries for all University of California Employees from 2010 until 2015. Before performing any analysis on the data, this author encrypted all names. If this data is released, the encryption will remain in place and no names will be published.

Although all the data is available online, there is a fundamental difference between having to search for data, point by point, in a database and having all the data aggregated into a spreadsheet where searching is much more simple. 

---


Quick Links: 

* [Background](#back)  


---

<a name="back"></a>

# Background

The University of California (UC) system is a public university system comprising of ten campuses, with the oldest being UC Berkeley, founded in 1868 and the newest being UC Merced, founded in 2005. The UC System was allocated a budget of **\\$25.5 billion** in 2015, **\\$13.1 billion** of which went towards paying its around **180,000 employees**. Of course, there are various factors that impact each individual employee's salary such as position and years of experience. 

But, there may be more, underlying, factors which impact employee salary, all else held constant, such as UC Campus, city unemployment rate, and cost of living. This post aims to dive deep into the intricacies of the distribution of salaries throughout the UC system, offering an interactive way to explore the key dynamics at play.

<a name="data"></a>

# The Data

The data for this analysis came from the [Compensation at the University of California](https://ucannualwage.ucop.edu/wage/) website. The data includes employee names, campus of employment, job title, and gross pay. A snapshot of the data is shown below.

<figure>
<center>
   <a href="/images/data_sal.jpg"><img width="100%" src="/images/data_sal.jpg"></a>
</center>
</figure>

The data spans the years 2010 until 2015 and includes all ten UC Schools as well as the University of California Office of the President. In total there are about 1.5 million rows in the table, where each row corresponds to a particular employee in a particular year. 

## Brief Notes on the Data

* Employees who are concurrenly students have their names listed as '*****' in order to protect their privacy. For this reason, we will use them when calculating summary statistics for each campus, but must remove them when we try and track certain employees through time since we have no unique identifier for them.
* The job titles are not very specific and usually are limited to things like 'COACH' or 'PROF' without much more detail about which sport, department, etc. the employee is a part of.
* There are a few missing values in the data for salaries. This author chose to use median imputation to fill in these missing values. Basically, the missing values for any column involving salaries is filled in with the median of existing entries in that column.





