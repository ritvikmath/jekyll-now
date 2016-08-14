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
* [The Data](#data)
* [Who is paid the most at each school?](#highpay)
* [How to UC campuses compare at a globally?](#global)
* [What is the distribution of salaries for each campus?](#distr)

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

The data spans the years **2010 until 2015** and includes all ten UC Schools as well as the University of California Office of the President. In total there are about **1.5 million rows** in the table, where each row corresponds to a particular employee in a particular year. 

## Brief Notes on the Data

* Employees who are concurrenly students have their names listed as '*****' in order to protect their privacy. For this reason, we will use them when calculating summary statistics for each campus, but must remove them when we try and track certain employees through time since we have no unique identifier for them.
* The job titles are not very specific and usually are limited to things like 'COACH' or 'PROF' without much more detail about which sport, department, etc. the employee is a part of.
* There are a few missing values in the data for salaries. This author chose to use median imputation to fill in these missing values. Basically, the missing values for any column involving salaries is filled in with the median of existing entries in that column.

<a name="highpay"></a>

# Who is paid the most at each school?

One of the burning questions readers probabaly have is *"Who is paid the most at each campus?"*. Let's answer this question before going much deeper into the data as a whole.

<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
      google.charts.load('current', {'packages':['table']});
      google.charts.setOnLoadCallback(drawTable);

      function drawTable() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Campus');
        data.addColumn('string', 'Top Paid Position');
        data.addColumn('number', '2015 Salary');
        data.addRows([
          ['Berkeley', 'Head Coach' , {v: 2038733, f: '$2,038,733'}],
          ['Davis', 'CEO Medical Center' , {v: 1114446, f: '$1,114,446'}],
          ['Irvine', 'Professor - Health Sciences' , {v: 1234771, f: '$1,234,771'}],
          ['Los Angeles', 'Head Coach' , {v: 3514771, f: '$3,514,771'}],
		  ['Merced', 'Chancellor' , {v: 404896, f: '$404,896'}],
		  ['Riverside', 'Dean - School of Medicine' , {v: 698608, f: '$698,608'}],
		  ['San Diego', 'Professor - Health Sciences' , {v: 1569475, f: '$1,569,475'}],
		  ['San Francisco', 'Health Sciences Clinical Instructor' , {v: 1753731, f: '$1,753,731'}],
		  ['Santa Barbara', 'Professor in Residence' , {v: 468571, f: '$468,571'}],
		  ['Santa Cruz', 'Chancellor' , {v: 392076, f: '$392,076'}],
		  ['Office of the President', 'Chief Investment Officer' , {v: 1106688, f: '$1,106,688'}]
        ]);

        var table = new google.visualization.Table(document.getElementById('table_div'));
		
        table.draw(data, {allowHtml: true, showRowNumber: false, width: '100%', height: '150%', alternatingRowStyle: true});
		
      }
</script>
    
<style>
.google-visualization-table-td {
text-align: center !important;
}
</style>
<center>
<div id="table_div"></div>
</center>

By clicking on the column names, you can sort the table by salary, position, or campus. 

Perhaps the most strinking thing about this table is that the sum of the five lowest salaries still is less than the top salary, that of a head coach at UC Los Angeles. 

Let's now step back and look at our plethora of data as a whole.

<a name="global"></a>

# How do UC campuses compare globally? 

There are inherent disparities between salaries at UC campuses and moreover, these disparities change over time. 

Use the tool below to explore for yourself some of these differences in salaries over time and between campuses. 


<center>
<div>
<iframe src="https://ritvikmath.shinyapps.io/NewBubble/" style="border: none; width: 850px; height: 700px"></iframe>
</div>
</center>

There are a few key points about this global data:

* Number of students and employees generally goes up over time, the UC system is growing.
* There is actually a huge difference between median and mean salary.For example, UC Merced's mean salary in 2015 is around \\$28,000 but its median salary is only \\$8,850. Big difference between medians and means usualy indicate strong presence of outliers (high salary earners) pulling the mean to high values.
* The fact that UC San Francisco is a graduate school really shows as it has few students and few employees but makes has by far the highest mean and median salaries.
* There seems to be a somewhat positive correlation between number of students / employees and mean / median campus salary.
* There seems to be a somewhat negative correlation between number of students / employees and unemployment rate. Hmm .... more on this later.

<a name="distr"></a>

# What is the distribution of salaries for each campus?

Let's zoom in a bit and look at the distribution of salaries within each campus and over time. As you play with the tool below think about questions like *"Does the salary distribution shift over time towards higher or lower earners?"*, *"Which campus has the most equality in pay?"*, *"Are there intermediate peaks or valleys in these distributions?"*. 

If there is no graph, give it a second. 1.5 million rows of data takes a bit of time to load!

<center>
<div>
<iframe src="https://ritvikmath.shinyapps.io/TestShiny/" style="border: none; width: 950px; height: 600px"></iframe>
</div>
</center>
    





