---
layout: post
title: Sentiment analysis of Q&A tweets III - Estimating political affiliations
image:
  feature: sample-image-10.jpg
  credit: Stella Maris, Haifa, Israel, 2014
---

In the [previous](http://www.clintonboys.com/qanda-tweets/) [two](http://www.clintonboys.com/qanda-tweets2/) posts in this series, I came up with a method of scoring the sentiment of tweets from the Q&A program. I now want to put all these pieces together to try and get a feel for the political leanings of Twitter users watching the program. 

The big problem with this analysis, as I said in the last two posts, is that most tweets are negative, so even the positive tweets are comprised of words with negative sentiment. 

![Sentiment scatter](https://github.com/clintonboys/clintonboys.github.io/blob/master/_posts/sent_scatter.png?raw=true)

This diagram shows the real problem; of the 764 tweets I hand-classified as positive or negative, using the basic calculation from the previous post, it's very difficult to separate them by their sentiment score alone. However, if we include **two** variables, namely 

`NormalisedSentiment`: sum of all sentiments for words in the corpus in the tweet, divided by the total number of words in the tweet

`NegativePercentage`: number of words with a sentiment less than zero, divided by the total number of words in the tweet

If we do a scatter plot of these two variables and color by classification (blue is positive, red is negative), we get the following picture:

![Sentiment scatter 2](https://github.com/clintonboys/clintonboys.github.io/blob/master/_posts/sent_scatter2.png?raw=true)
