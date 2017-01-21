---
layout: post
comments: true
title: How Many Beers Does it Take for Me to Get Bad at Math?
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
      google.charts.load('43', {'packages':['line']});
      google.charts.setOnLoadCallback(drawChart);
      google.charts.setOnLoadCallback(drawTable);
      google.charts.setOnLoadCallback(drawTimeline);

      function drawChart() {

      var data = new google.visualization.DataTable();
      data.addColumn('number', 'Fluid Ounces');
      data.addColumn('number', 'Addition');
      data.addColumn('number', 'Subtraction');
      data.addColumn('number', 'Multiplication');
      data.addColumn('number', 'Division');

      data.addRows([
        [0.0, 7.211799999999999, 10.0178, 13.9512, 23.754200000000004],
        [3.0, 8.6534, 8.779, 10.099400000000001, 20.1162],
        [6.0, 8.4632, 8.7998, 14.707999999999998, 54.842999999999996],
        [9.0, 8.089571428571428, 9.27157142857143, 15.761857142857142, 26.989714285714285],
        [12.0, 9.765714285714285, 9.453999999999999, 16.29042857142857, 35.800000000000004],
        [15.0, 8.717285714285714, 11.168571428571427, 12.827, 15.429142857142859],
        [18.0, 8.025714285714285, 10.050142857142857, 16.57014285714286, 24.246285714285712],
        [21.0, 8.275428571428572, 8.379714285714284, 12.67742857142857, 53.66842857142858],
        [24.0, 8.521571428571429, 10.113142857142858, 15.093571428571428, 30.095428571428574]
        [27.0, 8.633000000000001, 11.726714285714285, 11.533999999999997, 24.44357142857143],
        [30.0, 8.236, 8.467285714285714, 15.249714285714285, 23.27485714285714],
        [33.0, 10.78242857142857, 11.173428571428571, 17.151285714285713, 27.806857142857147]
        [36.0, 7.9479999999999995, 10.388000000000002, 10.040000000000001, 23.692],
        [39.0, 6.571428571428572, 7.807428571428573, 18.093857142857143, 30.108000000000004],
        [42.0, 9.568, 10.078571428571427, 20.98257142857143, 34.21028571428571],
        [45.0, 8.605, 7.799714285714285, 12.615571428571428, 27.83414285714286],
        [48.0, 8.884, 9.368142857142857, 12.717857142857145, 26.12657142857143],
        [51.0, 7.8952857142857145, 7.711142857142858, 17.45942857142857, 48.08257142857143],
        [54.0, 7.892142857142857, 9.461571428571428, 17.050857142857144, 30.052142857142854],
        [57.0, 8.03357142857143, 7.810714285714285, 12.195142857142855, 51.32742857142858],
        [60.0, 7.903999999999999, 9.113714285714286, 13.869285714285715, 28.265000000000004]
      ]);

      var options = {
        width: 900,
        height: 500,
        }
      };

      var chart = new google.charts.Line(document.getElementById('line_ops'));

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
   <div id="line_ops" style="height: 240px;"></div>
</center>
</html>






