---
layout: post
comments: true
title: What is the Probability that a God Exists?
---

<script type="text/x-mathjax-config">
  MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});
</script>
<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_CHTML">
</script>

As seventeenth-centry mathematican, philosopher, and physicist Blaise Pascal described, there are only four possible states of the universe:

* You believe in a god and this god exists (Case A)
* You believe in a god but no god exists (Case B)
* You do not believe in any god but a god exists (Case C)
* You do not believe in any god and no god exists (Case D)

Each case has an associated benefit (Case A and Case D) or cost (Case B and Case C). For example, in case A, you should be rewarded for you belief through some beneficial afterlife, or constructuve reincarnation, etc. But, for example in case C, you might suffer a terrible fate after death or a similarly grave outcome. We can enumerate the benefits and costs in a payoff matrix:

<figure>
<center>
   <a href="/images/payoff.jpg"><img width="90%" src="/images/payoff.jpg"></a>
</center>
</figure>

where

$$
A = \textrm{Benefit from believing in a god when a god exists}

B = \textrm{Loss from believing in a god when no god exists}

C = \textrm{Loss from not believing in a god when a god exists}

D = \textrm{Benefit from not believing in a god when no god exists}
$$

We assume that

$$ A > 0, B < 0, C < 0, D > 0 $$

since you being right about the existence/non-existence of a god is a gain while you being wrong about the existence/non-existence of a god is a loss.

We will also assume that each person has their own personal probability, $ p $, that a god exists:

$$ 
p = \textrm{Your Personal Probability That a God Exists}
$$

Now what is your expected payoff if you choose to believe in a god? Well it should be a probability-weighted average of your reward in the case where you believe in a god and a god exists (Case A) and your loss in the case where you believe in a god but no god exists (Case B). In other words:

$$
\textrm{Expected Payoff from Belief} = p \times A + (1-p) \times B
$$

Similarly,

$$
\textrm{Expected Payoff from Disbelief} = p \times C + (1-p) \times D
$$

Now, assuming that you believe in a god, it should be the case that:

$$
\textrm{Expected Payoff from Belief} > \textrm{Expected Payoff from Disbelief}
$$

otherwise you would choose disbelief over belief (see notes section for a bit more commentary on this inequality).

In other words:

$$
p \times A + (1-p) \times B > p \times C + (1-p) \times D
$$

which simplifies down to:

$$
p > \frac{(D-B)}{(D-B) + (A-C)}
$$

But what is $(D-B)$? It is really the added benefit you get from switching from belief to disbelief in a world where there is no god. Let's say $G_{disbelief} = D-B$.

And what is $(A-C)$? It's just the added benefit you get from switching from disbelief to beleif in a world where there is a god. Let's say $G_{belief} = A-C$.

So, if you choose to believe in a god:

$$
p > \frac{G_{disbelief}}{G_{disbelief} + G_{belief}}
$$

This makes sense since if $G_{belief}$, your gain from believing in a god, gets higher and higher, the quantity $\frac{G_{disbelief}}{G_{disbelief} + G_{belief}}$ will approach $0$ and you will choose to believe in a god even if your personal probability that a god exists, $p$, is small. In more casual terms, *if you think your life will be a lot better by believing in a god, you don't necissarily need great faith in the existence of a god to believe.*

Let's flip that story. If $G_{disbelief}$, your gain from not believing in a god, gets higher and higher, the quantity $\frac{G_{disbelief}}{G_{disbelief} + G_{belief}}$ will approach $1$. In everyday terms this says that *if you think your life will be a lot better by not believing in a god, you would need a lot of faith in the existance of a god to believe.* 











