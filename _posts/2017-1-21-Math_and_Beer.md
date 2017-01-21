---
layout: post
comments: true
title: How Many Beers Does it Take for Me to Suck at Math?
---

<figure>
<center>
   <a href="/images/decbeer.jpg"><img width="100%" src="/images/decbeer.jpg"></a>
</center>
</figure>

<center>
<font size="5"><b>Math vs. Alcohol</b></font>
</center>

---

<html>
<head>
  <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':["line"]});
      google.charts.setOnLoadCallback(drawChart);

    function drawChart() {

      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Fluid Ounces');
      data.addColumn('number', 'Addition');
      data.addColumn('number', 'Subtraction');
      data.addColumn('number', 'Multiplication');
      data.addColumn('number', 'Division');

      data.addRows([
         ['0', 7.2, 10.0, 13.9, 23.7],
         ['3', 8.6, 8.7, 10.0, 20.1],
         ['6', 8.4, 8.7, 14.7, 54.8],
         ['9', 8.0, 9.2, 15.7, 26.9],
         ['12', 9.7, 9.4, 16.2, 35.8],
         ['15', 8.7, 11.1, 12.8, 15.4]
         ['18', 8.0, 10.0, 16.5, 24.2]
         ['21', 8.2, 8.3, 12.6, 53.6]
      ]);
     
     var options = {
       
        width: 800,
        height: 400,
       
      };

      var chart = new google.charts.Line(document.getElementById('line_top_x'));

      chart.draw(data, options);
    }
  </script>
</head>
</html>

---

# Why Would I Do This?

Something I've found going out to bars or restaurants with a large group of people is that it gets increasingly harder to calculate how much each person should pay (including tip, tax, etc.) after I've had increasingly many drinks. That really got me thinking just how much alcohol affects mathematical ability. And, so this experiment was born!

---

# The Experiment

As a mathematician, I don't get to design a lot of experiments, but given this chance, I wanted to do it as precisely as possible. The setup was pretty simple. I would start sober and take a random 28 question math test which I had programmed into my computer. This test consisted of 7 addition, 7 subtraction, 7 multiplication, and 7 division questions, each of which was timed. I would work out the answer on some scratch paper and then my results (if I was correct and how much time it took) was sent to a spreadsheet.

Then, I would drink 3 fluid ounces (floz) of beer, wait a couple of minutes, and then repeat the random 28 question test. All in all, I worked my way up through the night from 0 fluid ounces of beer to 60 fluid ounces of beer, taking the test each 3 fluid ounces (20 tests taken total). 

<figure>
<center>
   <a href="/images/cups.jpg"><img width="100%" src="/images/cups.jpg"></a>
</center>
</figure>

---

# TestGraph

<br>

<html>
<style>
.google-visualization-table-td {
text-align: center !important;
}
</style>
<center>
   <div id="line_top_x"></div>
</center>
</html>






