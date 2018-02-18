---
layout: post
comments: true
title: The State of Black Characters in Comics
---

<figure>
<center>
   <a href="/images/racial_diversity_plot.png"><img width="3%" src="/images/racial_diversity_plot.png"></a>
</center>
</figure>

---

When I was a little Indian-American kid, I always loved watching action-packed Bollywood movies with my family. At the time, I thought it was mostly because they starred powerful heroes and heroines doing super cool stuff. A little older now, I realize that while this was true, it was crucial that these heroes and heroines looked like me. I realize now that there was something subconscious in my head that said: "This guy looks like me and he's doing some pretty noble and heroic stuff right now, so I must be capable of that same stuff". 

And I'd argue this is true for all kids while growing up. They can watch all the shows and movies, read all the books, have all the best teachers, but the moment they see someone who looks like them doing amazing things, all of a sudden it clicks. The reality clicks that: "Hold on, maybe I can be great too."

As it is currently <a href="https://en.wikipedia.org/wiki/Black_History_Month" target="_blank">Black History Month</a> and the long awaited superhero movie, Black Panther, just came out, I thought it would be a perfect time to look at the historic representation of black characters in an increasingly popular media: comics. Given that the <a href="https://en.wikipedia.org/wiki/Silver_Age_of_Comic_Books" target="_blank">Silver Age of Comics</a> pretty much coincided with the Civil Rights Era in America, I thought it would be really interesting to see how diversity changed in the comics during and outside this time. 

Let's dive in!

# The Data

For this project, I scraped all the data from online wiki pages using the Python web scraping library called BeautifulSoup. It is important to note that the process of reading data from a webpage and putting it into a spreadsheet isn't always clean cut and there are bound to be some errors in the final data. 

Just to point out one known source of error, comic books constantly write and rewrite characters as well as pass on the mantle of one superhero/supervillain to another character. Sometimes, a hero will originally be written as white and many decades later will be rewritten as black, for example. When scraping the wiki page for that character, it is possible that the original publication date will be fetched instead of the rewriting date. All this is to say, note that there will be minor errors although I have tried my best to maintain the accuracy of the scraped data. Whew! Warning over.

I scraped the following wiki pages for this project:

* <a href="https://en.wikipedia.org/wiki/List_of_black_superheroes" target="_blank">List of Black Superheroes</a>
* <a href="https://en.wikipedia.org/wiki/List_of_black_supervillains" target="_blank">List of Black Supervillains</a>
* <a href="https://en.wikipedia.org/wiki/List_of_Marvel_Comics_characters" target="_blank">List of Marvel Comics Characters</a>
* <a href="https://en.wikipedia.org/wiki/List_of_DC_Comics_characters" target="_blank">List of DC Comics Characters</a>






