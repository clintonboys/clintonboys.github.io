---
layout: post
title: Forecasting Australian elections IV - Marginal seat polls and the strong transition model
image:
  feature: sample-image-2.jpg
  credit: Cradle Mountain National Park, Tasmania, 2014. 

---

As I've recently (and finally) become gainfully employed, I haven't been able to devote a huge amount of time to my [model](http://www.clintonboys.com/emma-chisit/) for forecasting Australian elections. I have spent some time rewriting my sloppy code, fixing some redundancies and bugs, and improving the model to include the first few things on my [to-do list](http://www.clintonboys.com/aus-election-model-9/). 

The major theoretical improvement I've been thinking about over the last month is the [strong transition model](http://www.electoralcalculus.co.uk/strongmodel.html) which I learnt about while reading about the May 2015 UK general election (I was planning to write a post about why the polls failed so miserably to predict the result but I read so many good summaries of this I don't really think it's necessary). 

This model of voter behaviour at multi-party elections caught my eye after my initial model performed poorly in seats where the PUP candidate had a particularly strong showing. The thinking behind the model is that political parties generally have a two-tiered system of support: their dyed-in-the-wool followers who will vote for the party no matter what, and othet supporters, who are more flakey and prone to switching teams. The proportion of a party's supporters in the former group is an unknown, and difficult to estimate, parameter of the model: the May2015 website put it at 20%. When a party loses support in the polls, it loses it from the *non-strong* group first. 