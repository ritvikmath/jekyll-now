---
layout: post
comments: true
title: Your Friends Have More Friends Than You
---

<script type="text/x-mathjax-config">
  MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});
</script>
<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_CHTML">
</script>

If you're like me, you know keep down that your friends definitely have more friends than you and you wanted to find out why. We'll look at three different explanations: a talk-y verbal one, a visual one, and a hardcore math one for all of you who still aren't convinced.

# Verbal Explanation

Let's say you sort all the people in the world by how many friends they have. At the top of the list you have people with *tons* of friends and then at the bottom you have people who have very few friends. Which of these people are you more likely to have as friends? Well, its not the people at the bottom of the list because if they each have one friend then its really unlikely that *you* are that friend. 

On the flip side, if you look around the top of the list, it's much more likely that you have one of these people as a friend. Why? Just because they have more friends in total and you have much better odds of being one of their friends than of someone at the bottom of the list. 

Put in fewer words:

***People with more friends are more likely to have you as a friend***

Not buying it? Let's see the visual explanation!

# Visual Explanation

Let's say you have a network of six people, with some random links between them representing friendship:

<figure>
<center>
   <a href="/images/f1.png"><img width="90%" src="/images/f1.png"></a>
</center>
</figure>

Now, let's just count the number of friends each of these people have as well has how many friends their friends have:

<figure>
<center>
   <a href="/images/f2.png"><img width="90%" src="/images/f2.png"></a>
</center>
</figure>

So, overall, we get that:

<figure>
<center>
   <a href="/images/f3.png"><img width="90%" src="/images/f3.png"></a>
</center>
</figure>

Maybe you still believe that this is just one example and doesn't hold in general. Let's go to the hardcore math explanation!

# Definitive Math Explanation (Warning: Maths Ahead!)

We will treat the network of all friendships in the world as a graph, which is a network of vertices connected by edges. Here, each person is a vertex and an edge between people means that they are friends. (Yes, friendship has to be mutual)

Let $$V$$ be the set of all vertices (people) and let $$E$$ be the set of all edges (friendships). Also $$|V|$$ is the number of people in the world and $$|E|$$ is the number of connections between people. To proceed, we will calculate two values and compare them.

First, we will calculate ***the average number of friends that someone has**. Second, we will calculate ***the average number of friends that a someone's friend has***. If the second value is bigger than the first value, then we have shown that, on average, your friends have more friends than you do. 

The first value is fairly straightforward to calculate. We will add up all the friendships in the world and then divide by the number of people in the world to get the average number of friendships per person. The total number of friendships is $$2|E|$$ since each connection between two people represents two friendships, one from person A's point of view and one from person B's point of view. The total number of people in the world is simply $$|V|$$. So, the average numer of friends that someone has, which we will designate by $$\mu = \frac{2|E|}{|V|}$$

