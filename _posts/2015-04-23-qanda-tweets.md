---
layout: post
title: Sentiment analysis of QandA tweets
image:
  feature: sample-image-27.jpg
  credit: Amsterdam, The Netherlands, 2012
---

For a while I've been keen to learn how to use the Twitter API to scrape tweets. In this post I'll do some basic sentiment analysis on tweets I scraped during the Monday 20/4 airing of QandA, an Australian current affairs panel show which has become infamous in Australia for its lively Twitter feed. 

The panel for this program consists of five people, together with the host Tony Jones. The panel this episode consisted of 
 
- Derryn Hinch, a journalist and former radio personality who is famous for his outspoken views on child molestation rings (he has often defied court orders against naming child abusers)
- Andrew Robb, a member of the current conservative government who is the minister for trade and investment
- Anna Burke, a member of the centre-left opposition who used to be the house speaker
- Dave Hughes, a popular comedian
- Jane Burns, CEO of a research group that studies how technology affects the lives of young people 

As the program is political in nature, the ABC usually provides a breakdown of the political identifications of their audience, and attempts to make this breakdown as similar as possible to the true voting intentions of the Australian public.

I wanted to try and assess the political leanings of the Twitter users using the hashtag #QandA during the episode's broadcast. This required a number of steps.

**1. Scraping Twitter for tweet data**

Twitter has a very usable API and there's a great Python package called `tweepy` that allows you to automate everything using a Python script. I fiddled around with the default tweepy script to scrape the Twitter stream live for a certain search term, using the term `QandA`. The free API is limited to only providing 1% of the Firehose (Twitter's in house term for the live feed of all tweets), but since Q&A only get around 20 000 tweets per episode, there's no way this data is going to exceed 1% of the 6000 tweets per second in the Firehose. So I set the script to run from 9.30PM to 10.30PM AEST on Monday April 20 and saved only the body text of all tweets using the hashtag. 

**2. Devising sentiment analysis**

The analysis I want to do is a little different to the usual textbook Twitter sentiment analysis problem of classifying a tweet as happy or sad. Classifying a tweet as right or left is quite hard, so rather than that I want to to do the following process:
- identify if a tweet contains a single pertinent political keyword ('Tony Abbott', 'Coalition', 'ALP', etc. etc.) which has a particular alignment on the political spectrum
- assess the sentiment of the other words in the tweet
- come up with a corresponding political ranking (right or left will do; it's hard to quantify beyond that)

For example, the tweet 

`I don't understand how the Coalition can be so cruel towards asylum seekers #QandA`

would be rated as left-wing, since it contains the keyword `Coalition` and the negative-sentiment marker `cruel`.

This is a pretty crude model, but I imagine it will do a decent first job. 