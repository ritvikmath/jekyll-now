---
layout: post
comments: true
title: Citywide Disparties in SAT Scores
---

<figure>
<center>
   <a href="/images/sat_cover.png"><img width="40%" src="/images/sat_cover.png"></a>
</center>
</figure>

<center>
<font size="5"><b>Identifying Reasons for SAT Score Differences Among Neighboring Schools</b></font>
</center>

---

Quick Links: 

* [Background and Data](#back)  
* [How Does SAT Scores Vary Based on Subject, Family Income, School Size, etc.?](#corr)
* [Do High Schools Cluster Geographically by SAT Score?](#loc)
* [Can We Build a Model to Predict SAT Scores?](#model)
* [Summarizing Features of High and Low Performing Schools](#summ)
* [References](#refs)

---
---

<a name="back"></a>

# Background

<figure>
<center>
   <a href="/images/test_img.jpg"><img width="75%" src="/images/test_img.jpg"></a>
</center>
</figure>

Every year, about **1.7 million** college bound high school seniors take the SAT exam, often cited as a major factor in college admittance. Prior to 2016 this exam consisted of 3 sections: reading, math, and writing and was graded out of a maximum possible score of **2400**. From 2016 onward, the exam has changed in <a href="http://sat.ivyglobal.com/new-vs-old/" target="_blank">various ways</a> but since the data we use is from before 2016, we will disregard these recent changes. While students can and do study extensively for the SAT, there are other factors at play which make this test less than fair for all students.

The most common of these is **family income**. It is known that **students coming from richer families perform better on average than students coming from poorer familes**. This should not be a great surprise given that wealthier students are more readily able to enroll in *very expensive* SAT preparation courses or hire private tutors. Income disparities can also have less overt implications. For example, students from poorer familes might need to work a **part time job while in high school** to meet family income needs, detracting from study time for the SAT and school in general. These are indeed theories which are backed by **evidence**: <a href="https://www.washingtonpost.com/news/wonk/wp/2014/03/05/these-four-charts-show-how-the-sat-favors-the-rich-educated-families/?utm_term=.706068ac11eb" target="_blank">here</a> and <a href="https://economix.blogs.nytimes.com/2009/08/27/sat-scores-and-family-income/" target="_blank">here</a>. 

Of course, other factors can also have an effect on SAT score including **school size (maybe larger schools have more resources)**, **school hours (maybe it helps to be at school longer)**, **the SAT score of neighboring schools (maybe schools cluster geographically by SAT score)**, etc. We will analyze data from the New York City Department of Education and the College Board to check for these patterns accross the ***puclic high schools in New York City for the 2014-2015 school year***. The data can be found at <a href="https://www.kaggle.com/nycopendata/high-schools" target="_blank">here</a>. Each row of the data represents one public high school in New York City and inclues features such as total school enrollment, school latitude and longitude, percent of students who took the SAT at this school, racial composition of the school, school hours, and average school scores in SAT math, reading, and writing.

We join this data to **another dataset about <a href="https://izahoina.carto.com/tables/nyc_income_compiled/public/map" target="_blank">median family income</a> in various regions within New York City**. This will allow us to perform an income analysis later on.

---

<a name="corr"></a>

# How Does SAT Scores Vary Based on Subject, Family Income, School Size, etc.?

We want to first understand how SAT scores vary by various school dimensions namely: **school size, percent of students who took the SAT, and median family income of the neighborhood the school is in**. For each of these dimensions, we categorize a school as either **high, medium, or low** and look at the average SAT **math, reading, and writing** score in each bucket. 

## School Size

We start with total school enrollment. **Is is more likely that a larger school or smaller school will have better average SAT scores?** We can argue for either side. Perhaps larger schools have more resources to provide students. On the other hand, perhaps smaller schools offer a more intimate learning environment with a better student to teacher ratio. Let's turn to the data.

<figure>
<center>
   <a href="/images/SAT_Enrollment_Scores.png"><img width="75%" src="/images/SAT_Enrollment_Scores.png"></a>
</center>
</figure>

* We see that in general, the score rise as the size of the school increases, possibly due to our theory of larger schools having more resources to give students. Or **perhaps larger schools are just located in more high income areas**.
* Note also that SAT math seems to increase faster than the other subjects.

## Percent Tested

We turn our attention now to the variance in SAT scores based on what **percent of students at a given school took the SAT exam**. We expect that if a large fraction of students at the school take the exam, the school is likely **more academically advanced** in general than if a low proportion of students take the exam and so we **expect higher scores in this case**. What does the data say?

<figure>
<center>
   <a href="/images/SAT_Pct_Tested_Scores.png"><img width="75%" src="/images/SAT_Pct_Tested_Scores.png"></a>
</center>
</figure>

* We see that **math is actually lower in the < 33% case, but grows at a much faster rate**, eventually beating the other subjects by a large margin.
* We see that there is a **bit of a change between the first and second school groups** but a **very large change between the second and third**. That is, **having more than 66% of students take the SAT at a school seems to be correlated with relatively very high SAT scores**. 

## Family Income

Saving the best for last, we now look at how SAT scores change based on median family income in the region that the school is in. Following our discussion in the introduction, we **expect that higher income leads to higher SAT scores**. Again we partition the schools into low, medium, and high income bins. What's the data tell us?

<figure>
<center>
   <a href="/images/SAT_FamilyIncome_Scores.png"><img width="75%" src="/images/SAT_FamilyIncome_Scores.png"></a>
</center>
</figure>

* Note that the combined average SAT score for the high income schools is nearly **100 points more** than the combined average score of the low income schools.
* We see that the **ratio between reading, math, writing remains roughly constant regardless of income bin**.
* Note that this income **might be off the mark since it is aggregated for the region that the school is in**, meaning that there will still be some low income students at schools in high income areas and high income studnets at schools in low income areas. Also, the **school itself might be underfunded** even if it is in a high income area, or vice versa. It is thus important to **take these results with a grain of salt**.
* Still, we see a clear **positive correlation between SAT score (all subjects) and median family income of the region that a school falls in**.

## Correlations Between Subjects

It is no surprise that the three SAT subjects seem to "move together" in all the dimensions above. If we just compute the correlation coefficent between each pair of the three subjects, we get the following results. It is intuitive that math and reading, which share certain skills, are more correlated than either is to math.

<figure>
<center>
   <a href="/images/stscorrs.png"><img width="75%" src="/images/stscorrs.png"></a>
</center>
</figure>



<figure>
<center>
<iframe src="/images/us_states.html" style="border: none; width: 800px; height: 500px"></iframe>
</center>
</figure>











