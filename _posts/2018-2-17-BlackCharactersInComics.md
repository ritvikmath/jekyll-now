---
layout: post
comments: true
title: The State of Black Characters in Comics
---



---

# Motivation

When I was a little Indian-American kid, I always loved watching action-packed Bollywood movies with my family. At the time, I thought it was mostly because they starred powerful heroes and heroines doing super cool stuff. A little older now, I realize that while this was true, it was crucial that these heroes and heroines looked like me. I realize now that there was something subconscious in my head that said: "This guy looks like me and he's doing some pretty noble and heroic stuff right now, so I must be capable of that same stuff". 

And I'd argue this is true for all kids while growing up. They can watch all the shows and movies, read all the books, have all the best teachers, but the moment they see someone who looks like them doing amazing things, all of a sudden it clicks. The reality clicks that: "Hold on, maybe I can be great too."

As it is currently <a href="https://en.wikipedia.org/wiki/Black_History_Month" target="_blank">Black History Month</a> and the long awaited superhero movie, Black Panther, just came out, I thought it would be a perfect time to look at the historic representation of black characters in an increasingly popular media: comics. Given that the <a href="https://en.wikipedia.org/wiki/Silver_Age_of_Comic_Books" target="_blank">Silver Age of Comics</a> pretty much coincided with the Civil Rights Era in America, I thought it would be really interesting to see how diversity changed in the comics during and outside this time. 

<figure>
<center>
   <a href="/images/blackpanther.png"><img width="100%" src="/images/blackpanther.png"></a>
</center>
</figure>

Let's dive in!

# The Data

For this project, I scraped all the data from online wiki pages using the Python web scraping library called BeautifulSoup. It is important to note that the process of reading data from a webpage and putting it into a spreadsheet isn't always clean cut and there are bound to be some errors in the final data. 

Just to point out one known source of error, comic books constantly write and rewrite characters as well as pass on the mantle of one superhero/supervillain to another character. Sometimes, a hero will originally be written as white and many decades later will be rewritten as black, for example. When scraping the wiki page for that character, it is possible that the original publication date will be fetched instead of the rewriting date. All this is to say, note that there will be minor errors although I have tried my best to maintain the accuracy of the scraped data. Whew! Warning over.

I scraped the following wiki pages for this project:

* <a href="https://en.wikipedia.org/wiki/List_of_black_superheroes" target="_blank">List of Black Superheroes</a>
* <a href="https://en.wikipedia.org/wiki/List_of_black_supervillains" target="_blank">List of Black Supervillains</a>
* <a href="https://en.wikipedia.org/wiki/List_of_Marvel_Comics_characters" target="_blank">List of Marvel Comics Characters</a>
* <a href="https://en.wikipedia.org/wiki/List_of_DC_Comics_characters" target="_blank">List of DC Comics Characters</a>

In the end, I produced a dataset with the following six columns: **Alignment (Hero, Villain, or Unsure), Character Name, Comic (Marvel or DC), Length of Wiki Page, Black or Nonblack, Year When Introduced**. A snapshot of the data is shown below.

<figure>
<center>
   <a href="/images/comics_data.png"><img width="100%" src="/images/comics_data.png"></a>
</center>
</figure>

Let's ask some questions and see the answers to them!

# How Has Racial Diversity in Comics Changed Through Time?

Since we are focussing on black characters here, we will define something called the **racial diversity score** as shown below:

<figure>
<center>
   <a href="/images/RDS.png"><img width="100%" src="/images/RDS.png"></a>
</center>
</figure>

Now that we know what the racial diversity score is, let's see how it has changed through time.

<figure>
<center>
   <a href="/images/blog_diversity_chart.png"><img width="100%" src="/images/blog_diversity_chart.png"></a>
</center>
</figure>

**Key Points:**

* We see that the diversity score starts at 0 while Marvel and DC did not have any black characters. Then, upon the addition of their respective first black characters, the score initially spikes and then gradually falls since it likely was not a plan to continue regularly introducing black characters in the 1950's. 

* Interestingly, we see that in the period from about **1965-1978** there is a rapid growth in the diversity score for both Marvel and DC. It happens to be that this period immediately followed and somewhat intersected with the **Civil Rights Era in the U.S.**, which spanned from about **1954-1968**.

* Since 1980, the diversity score has still been growing, which is a good sign, but at a **much slower rate** than in the aforementioned boom period. Looking at the graph, we see that the **diversity score went from about 2% to 7% (5% rise) in the 14 years we mentioned before** but since then, it has **only gone up about 3% in the last 40 years**.

* Another feature of this graph is that the lines for Marvel and DC intersect quite often, which we can read as a good sign since neither publisher seems to be consistenly outperforming the other in terms of writing black comic book characters. Still, it is worth noting that in the boom period (1965-1978), Marvel had a steeper growth in diversity score than did DC. And, in the modern era, DC seems to have a slight lead in diversity score over Marvel.

* If the proportion of black characters in comics were the same as actual black people in the US, <a href="https://www.census.gov/quickfacts/fact/table/US/PST045217" target="_blank">13%</a>, the diversity score should be around 0.23. Seeing as it is currently just over 0.1, we still have some work to do if we aim to represent our populace fairly in the comics.

How about we take a quick look at some of the key black comic characters which made that period from 1965-1978 so prosperous.

<figure>
<center>
   <a href="/images/blog_highlight_chars.png"><img width="100%" src="/images/blog_highlight_chars.png"></a>
</center>
</figure>

# Are Black Characters Represented as Heroes or Villains?

Now that we have analyzed the rate at which black characters have been added to comics over time, a deeper question would be whether these characters are usually the good guys or the bad guys. Let's look at a time series of what percent of characters are heroes for black and all comic book characters.

<figure>
<center>
   <a href="/images/frac_heroes.png"><img width="100%" src="/images/frac_heroes.png"></a>
</center>
</figure>

**Key Points:**

* The most striking thing about this chart is that the line for black heroes is always above the line for all heroes. This means that black characters are represted as heroes at a consistently higher rate than for comic characters in general. This seems to be a good sign.

* We also see that the line for black heroes is always above 50%, meaning that so far, half of all black comic book characters have always been heroes. We see this is not true for all comic book heroes. From about 1960 to 1995, the line for all heroes dipped below 50% meaning that during that time period, most comic book characters were either villains or neither (some characters are more ambiguous than either heros or villains or I just wasn't able to tell by scraping the wiki pages).

* A possible explanation for the decline in the hero rate for both series until about 1990 might be because most major comic book heroes have a whole gallery of bad guys. For every Spider Man, there are 15-20 solid bad guys.

Let's lastly look at how many days, on average, readers need to wait for a new black character vs a new non-black character.

# Waiting Time for New Black Characters vs New Non-Black Characters

<figure>
<center>
   <a href="/images/avg_rate.png"><img width="100%" src="/images/avg_rate.png"></a>
</center>
</figure>

**Key Points:**

* Right away, we see that the average wait time for a black character is much more than the average wait time for a non-black character accross all time periods. We are more interested in how the ratio of the wait time for a black vs. nonblack character changes over time. The ratio, shown in the bottom plot, starts very high, at 66. This means that in the 1960's there were on average 66 new nonblack characters for every new black character in comics.

* We see that this ratio gets a lot better in the coming decades and is now around 12, meaning that there are on average 12 nonblack characters for each black character. Based on the current U.S. population demographics, we would expect this ratio to ideally be about 7 new nonblack characters per new black character.

* When I saw this plot, I was trying to explain the sudden spike in wait times in the 2010's for both black and nonblack characters. My two guesses are either that in recent years the focus has been on comic book films rather than movies (although I don't have a good enough grasp on comic books to know if this is true), or that there is simply a lag time between characters appearing in comics and their wiki pages being created (I think more likely).

# Wrapping Up


