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
<font size="5"><b>Mastering the Mechanics of the Dating Market</b></font>
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
      google.charts.load('43', {'packages':['sankey']});
      google.charts.setOnLoadCallback(drawChart);

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
      
      </script>
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

Let's see how the accuracy and precision of our Random Forest model compare to just plain old random guessing.

<figure>
<center>
   <a href="/images/gain.png"><img width="100%" src="/images/gain.png"></a>
</center>
</figure>

We see that our Random Forest model performs much better than random guessing and has fairly high accuracy and precision levels. With this confidence in our model, we are now ready to list the top five factors in predicting whether you will get a second date.

## Top 5 Factors in Getting a Second Date

<figure>
<center>
   <a href="/images/important_features.png"><img width="100%" src="/images/important_features.png"></a>
</center>
</figure>

Note that the length of the bars is proportional to how strong of a predictor that factor is.

**Key Takeaways:**

* The **top factor in determing whether you get a second date is simply how much your date liked you overall**. This naturally matches up with our intuition
* The next three are how attractive, fun, and involved in their interests, they think you are, respectively. Here we already get **indications that attractiveness, above all other traits, determines how much someome wants to see you again**, at least upon first impression
* Intrestingly, the fifth most important factor is how likely your date thinks it is that you will say 'yes' to a second date. It seems like **people judge whether they want a second date not only by how they percieve their date, but also how they think their date percieves them**

---
<a name="value"></a>

# Can You Accurately Predict Your Own Value in the Dating Market?

In addition to a bunch of opportunities for "love at first sight", **we can also view our data as a two-sided economic market**, where **value is determined by other participants in the market**. If this seems a bit abstract, let's break it down. You, as a person, have a certain social value on five traits we have data for: **Attractiveness, Intelligence, Ambition, Fun, and Sincerity**. That **value is determined by a combination of the scores that all your dates give you** for these traits. 

For example, if you go on five dates, and they score your attractiveness as: 7/10, 8/10, 9/10, 8/10, 7/10, then we take the **average** of these and say that your **"dating market value"** for attractiveness is 7.8/10. We do the same for the other traits.

The key question is **whether the value you assign to yourself, before the study begins, is close to your actual value** or very far from it. If we find that, on average, the self-assigned values and the dating market values are close, people generally have a good idea of their worth in the dating market. On the other hand, if the self-assigned values are far from the dating market values, we need to ask whether the self-assigned values are higher or lower and why this might be. **We report the results below.**

<figure>
<center>
   <a href="/images/self_others.png"><img width="100%" src="/images/self_others.png"></a>
</center>
</figure>

**Interesting!** So we see that on **all five traits, people percieve their own value to be at least 13% higher than the dating market percieves their value to be**. We see that the **greatest discrepency happens with "fun"**. That is, people percieve themselves to be much more fun than the dating market does. This might be because **"fun" is so subjective** and each person will believe the things he or she is interested in to be fun while an outsider may find these things mundane or dull. Other **high discrepency traits include attractiveness and sincerity**. 

Interestingly, the **lowest discrepencies occur with intelligence and ambition**, both of which are **more measurable than the other three traits**. That is, **intelligence can be measured by way of IQ tests, or school grades, etc**. Ambition can be pseudo-measured by how well you did in school, how "good" of a job you have, etc. On the other hand, **beauty is in the eye of the beholder**, and it can be argued that fun and sincerity are as well. Of course, these are just the ***thoughts of this author***. Feel free to come up with your own theories for why these discrepencies might be the way they are and **post your thoughts in the comments below!**

---
<a name="type"></a>

# Do You have a 'Type' When it Comes to Dating?

Tall, dark, and handsome. Green-eyed brunettes. Fitness freaks. When it comes to dating, we often hear about people having "types". That is, we are often told (maybe by our annoying friends) that we **over and over go for the same type of person**, whether we accept it or not. Can we use our data to help answer the question of **whether people are attracted to certain "types" of other people?** 

To make this more concrete, we will consider our "types" as our six attributes: **Attractive, Intelligent, Ambitious, Fun, Sincere, and Sharing of Interests**. We proceed by **taking a look at the correlation between these attributes**. Why? Well, imagine that when we look at the data for how intelligent people scored their dates, we find that it is highly correlated with how sincere they scored their dates. That is, **we find that people, whether conciously or subconciously, think of intelligent people as also sincere**. This gives us evidence that perhaps intelligence and sincerity are not separate, but are **really part of one global "type"**.

To be clear, we will be using an **arrow from one trait to another if the latter trait is the most correlated with the former trait**. Here is a visual example with our intelligence->sincerity example.

<figure>
<center>
   <a href="/images/ex_graph.png"><img width="100%" src="/images/ex_graph.png"></a>
</center>
</figure>

When we apply this method to all six traits, we get the following surprising result.

<figure>
<center>
   <a href="/images/groups.png"><img width="100%" src="/images/groups.png"></a>
</center>
</figure>

We see **two disjoint groups with three traits each**. Let's take a look at each one in turn. We see that the **group on the left consists of fun, shared interets, and attractiveness**. Intuitively, this means that **people group these traits together very tightly when scoring their dates**. **On the right**, we see the other three traits: **intelligence, sincerity, and ambition**. 

There is a very **natural story behind this divide**. It seems natural that **intelligent people might be ambitious** since they would be able to apply their intellect towards their goals. We can also make a case for **intelligent people seeming to be very knowledgeable about facts, therefore coming off as sincere**. 

On the other side, we **often associate people we find physically attractive with being fun-loving or exciting**. We are also very likely to **consider people fun because they like doing the same things as us**, therefore giving them a high score in shared interests.

So it seems like, coarsely, there are two "types" of people: the **attractive, fun-loving ones**, and the **intelligent, ambitious ones**. Of course, **this is only given the six traits we have data for**, and **only uses the top correlated trait with each other trait**, but it definitely seems natural and informative that the **data reflects the social constructs we are used to**.

---
<a name="type"></a>

# All Roads Lead to Attractiveness

Do you have that friend who says they're looking for something in a potential romantic partner and then **always ends up picking people who are the exact opposite**? Maybe you are that friend ... Either way, it's no surprise that **what we say we want in a romantic parter and what our actions say are often two completely different things**. 

Luckily, our data gives us the ability to **see what people say they prefer** in a partner (in terms of our six attributes) and then **compare that to what they actually want**, based on the prevalent traits of the people they request to go on a second date with. 

As an example, **suppose that you rank intelligence as your top desired trait** before going on any of the speed dates. Suppose after going on 10 speed dates, you request to have a second date with 5 of them. Suppose furthermore that **among those 5 chosen people, the trait with the highest average score was ambition**. We will then say that **you prefer intelligence but end up choosing to go on second dates with ambitious people**.

We do this for all the attendees and produce the Sankey diagram below. **Hover over the links** to find out **how many people who initially preferred a certain trait ended up requesting second dates with people of a predominantly second trait**.

<html>

<div id="sankey_basic" style="width:400px; height: 500px;"></div>

</html>

There are two key takeaways from this diagram.

First off, we see that a large majority of people initially prefer attractiveness. Still, after all the dates are said and done, people seem to diversify in terms of the people they request a second date with. That is, attractiveness takes up a smaller share of the chosen traits on the right than the preferred traits on the left. 

Secondly, we see that in some sense "all roads lead to attractiveness". If we look at all the preferred traits on the left and trace where most of the attendees end up on the right hand side, the answer is attractivenss for four of the six traits. We thus have evidence which says that no matter what people claim to want in a romantic partner, they typically end up going for attractive people based on first impressions. This makes some sense. After all, on a first date, it is much easier to judge someomes attractiveness than it is to judge their sincerity of intelligence.




