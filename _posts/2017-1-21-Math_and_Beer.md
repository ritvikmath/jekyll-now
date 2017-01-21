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
      google.charts.load('current', {'packages':['line']});
      google.charts.setOnLoadCallback(drawChart);

    function drawChart() {

      var data = new google.visualization.DataTable();
      data.addColumn('number', 'Day');
      data.addColumn('number', 'Guardians of the Galaxy');
      data.addColumn('number', 'The Avengers');
      data.addColumn('number', 'Transformers: Age of Extinction');

      data.addRows([
        [1,  37.8, 80.8, 41.8],
        [2,  30.9, 69.5, 32.4],
        [3,  25.4,   57, 25.7],
        [4,  11.7, 18.8, 10.5],
        [5,  11.9, 17.6, 10.4],
        [6,   8.8, 13.6,  7.7],
        [7,   7.6, 12.3,  9.6],
        [8,  12.3, 29.2, 10.6],
        [9,  16.9, 42.9, 14.8],
        [10, 12.8, 30.9, 11.6],
        [11,  5.3,  7.9,  4.7],
        [12,  6.6,  8.4,  5.2],
        [13,  4.8,  6.3,  3.6],
        [14,  4.2,  6.2,  3.4]
      ]);

      var options = {
        chart: {
          title: 'Box Office Earnings in First Two Weeks of Opening',
          subtitle: 'in millions of dollars (USD)'
        },
        width: 900,
        height: 500,
        axes: {
          x: {
            0: {side: 'top'}
          }
        }
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






