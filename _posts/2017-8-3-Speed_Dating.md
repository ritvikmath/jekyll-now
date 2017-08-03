---
layout: post
comments: true
title: How to Get a Second Date
---

<figure>
<center>
   <a href="/images/"><img width="100%" src="/images/"></a>
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

<html>
<head>
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('43', {'packages':['sankey', 'table', 'timeline']});
      google.charts.setOnLoadCallback(drawChart);
      google.charts.setOnLoadCallback(drawTable);
      google.charts.setOnLoadCallback(drawTimeline);

      function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'From');
        data.addColumn('string', 'To');
        data.addColumn('number', 'Number of People');
        data.addRows([
			['Prefer Shared Interests', 'Chose Shared Interests', 1],
['Prefer Fun', 'Chose Sincerity', 4],
['Prefer Fun', 'Chose Attractiveness', 8],
['Prefer Attractiveness', 'Chose Fun', 22],
['Prefer Shared Interests', 'Chose Ambition', 1],
['Prefer Fun', 'Chose Fun', 2],
['Prefer Shared Interests', 'Chose Sincerity', 3],
['Prefer Attractiveness', 'Chose Attractiveness', 76],
['Prefer Sincerity', 'Chose Shared Interests', 1],
['Prefer Intelligence', 'Chose Sincerity', 30],
['Prefer Attractiveness', 'Chose Shared Interests', 3],
['Prefer Ambition', 'Chose Fun', 1],
['Prefer Sincerity', 'Chose Attractiveness', 41],
['Prefer Intelligence', 'Chose Shared Interests', 4],
['Prefer Ambition', 'Chose Intelligence', 3],
['Prefer Sincerity', 'Chose Ambition', 9],
['Prefer Shared Interests', 'Chose Attractiveness', 4],
['Prefer Intelligence', 'Chose Fun', 7],
['Prefer Sincerity', 'Chose Fun', 11],
['Prefer Intelligence', 'Chose Attractiveness', 37],
['Prefer Attractiveness', 'Chose Sincerity', 69],
['Prefer Sincerity', 'Chose Sincerity', 32],
['Prefer Attractiveness', 'Chose Intelligence', 63],
['Prefer Sincerity', 'Chose Intelligence', 25],
['Prefer Intelligence', 'Chose Ambition', 4],
['Prefer Attractiveness', 'Chose Ambition', 12],
['Prefer Fun', 'Chose Intelligence', 10],
['Prefer Ambition', 'Chose Sincerity', 1],
['Prefer Shared Interests', 'Chose Intelligence', 1],
['Prefer Fun', 'Chose Ambition', 2],
['Prefer Intelligence', 'Chose Intelligence', 35]
        ]);

        // Sets chart options.
        var options = {
          width: 725,
		  sankey:{
			  node: {
				label: {
				  fontSize: 12,
				  bold: true
				}},
	
			link: {colorMode: 'source',
				color: {fillOpacity: 1,  strokeWidth: 1}
			}
			}
		  
        };
        
        

        // Instantiates and draws our chart, passing in some options.
        var chart = new google.visualization.Sankey(document.getElementById('sankey_basic'));
        chart.draw(data, options);
      }
      
</head>
</html>

---


Quick Links: 

* [Background and Data](#bdat)  
* [How to Get a Second Date](#secdate)
* [Can You Accurately Predict Your Own Value in the Dating Market?](#value)
* [Do You have a 'Type' When it Comes to Dating?](#type)
* [All Roads Lead to Attractiveness](#tranfs)
* [How Does Your Behavior Change as You Date More People?](#order)
* [Notes](#notes)

---
<a name="bdat"></a>

# Background and Data

Dating has long been regarded as a simultaneously rule-driven and mysterious game. You need to **dress well, seem interested in everything your date says**, but all the while, **"be yourself"**. You need to come off as **fun and exciting** but **not share the most important and intimate parts of yourself so soon**. Indeed, a first date can often be a mixture of **exciting, confusing, and scary** and can leave you wondering if you did "enough" to get a second date with the other person. This problem has long been studied from a psychological and biological standpoint, but now we will tackle it in the **data science** arena.

For this analysis we will use **<a href="https://www.kaggle.com/annavictoria/speed-dating-experiment" target="_blank">speed dating data</a>** compiled by professors at the **Columbia Business School in 2002-2004**. They invited waves of attendees to come in an participate in the study. Each wave consisted of a variable number of attendees, but there were the **same number of males and females per wave**. The study would then progress as follows. Each attendee would fill out a preliminary questionaire with several questions, including their **preferences in potential dates along six traits**: ***Attraction, Intelligence, Sincerity, Fun, Ambition, and Shared Interests***. In addition, **each attendee would rank themselves** on five attributes: ***Attraction, Intelligence, Sincerity, Fun, and Ambition***. Each male-female pair would then go on a **quick 4 minute "speed date"** and would have the chance to **rank their partners on the previously mentioned six attributes** as well as **indicate wheter or not they would like to schedule a second date with their partner**.

Viewing this study as a plethora of opportunities for two people to feel **"love at first sight"**, we can start asking many of the age old questions when it comes to dating and specifically first dates. 

---
<a name="secdate"></a>

# How to Get a Second Date

If we **analyze all the dates in our study where someone requested a second date**, and **compare them with those where no second date was requested**, we should be able to **tease out the factors which make or break whether your date will ask to go out with you again**. We do just that by using a machine learning model called the **<a href="https://en.wikipedia.org/wiki/Random_forest" target="_blank">Random Forest</a>**. This model basically works by trying to answer the question: **"Will someone request to go on a second date?"** and arrives at its final answer by **asking a series of yes or no questions**. Furthermore, **the earlier a question is asked, the more important it is in determining whether you'll get a second date or not**. Just for example, if the first question asked is "Does the other person rank my attractiveness above 50/100?", and the fourth question asked is "Does the other person prefer someone of the same race as themselves?", then the first question is more effective in determining whether the other person requests a second date.

But, it's not exactly that easy. **We can trust the results of our Random Forest model only if it is able to give us a 'good' accuracy** in predicting whether or not someone will request a second date. If it gives a sub-par predictive power, then we really have no reason to trust the model at all. We will judge our Random Forest model on two metrics, **accuracy and precision**. **Accuracy is simply the number of dates where the model correctly predicts whether or not there will be a second date divided by the total number of dates**. **Precision**, a related but different measure, **is the proportion of dates where the model gives a correct predicion out of only the dates where the model predicts that there will be a second date**. That is, precision measures how "correct" the Random Forest model is when it predicts that you will get a second date.




