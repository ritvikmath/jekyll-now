---
layout: post
comments: true
title: The Curse of Casual Dating
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
			['Prefers Shared Interests', 'Chose Shared Interests', 1],
['Prefers Fun', 'Chose Sincerity', 4],
['Prefers Fun', 'Chose Attractiveness', 8],
['Prefers Attractiveness', 'Chose Fun', 22],
['Prefers Shared Interests', 'Chose Ambition', 1],
['Prefers Fun', 'Chose Fun', 2],
['Prefers Shared Interests', 'Chose Sincerity', 3],
['Prefers Attractiveness', 'Chose Attractiveness', 76],
['Prefers Sincerity', 'Chose Shared Interests', 1],
['Prefers Intelligence', 'Chose Sincerity', 30],
['Prefers Attractiveness', 'Chose Shared Interests', 3],
['Prefers Ambition', 'Chose Fun', 1],
['Prefers Sincerity', 'Chose Attractiveness', 41],
['Prefers Intelligence', 'Chose Shared Interests', 4],
['Prefers Ambition', 'Chose Intelligence', 3],
['Prefers Sincerity', 'Chose Ambition', 9],
['Prefers Shared Interests', 'Chose Attractiveness', 4],
['Prefers Intelligence', 'Chose Fun', 7],
['Prefers Sincerity', 'Chose Fun', 11],
['Prefers Intelligence', 'Chose Attractiveness', 37],
['Prefers Attractiveness', 'Chose Sincerity', 69],
['Prefers Sincerity', 'Chose Sincerity', 32],
['Prefers Attractiveness', 'Chose Intelligence', 63],
['Prefers Sincerity', 'Chose Intelligence', 25],
['Prefers Intelligence', 'Chose Ambition', 4],
['Prefers Attractiveness', 'Chose Ambition', 12],
['Prefers Fun', 'Chose Intelligence', 10],
['Prefers Ambition', 'Chose Sincerity', 1],
['Prefers Shared Interests', 'Chose Intelligence', 1],
['Prefers Fun', 'Chose Ambition', 2],
['Prefers Intelligence', 'Chose Intelligence', 35]
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





