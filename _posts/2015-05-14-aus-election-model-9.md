---
layout: post
title: Forecasting Australian elections III - Emma Chisit v1.0
image:
  feature: sample-image-31.jpg
  credit: Kosziusko National Park, New South Wales, 2012

---

I've spent the last few months of my spare time writing code for a [model](http://www.clintonboys.com/emma-chisit/) to forecast Australian elections. I'm calling the model Emma Chisit. A very basic first version of the model is finished, and I wanted to write up a few things about how it works, mainly so I can explain the current shortcomings, and the improvements I want to make down the line. 

**The data used by the model**

The model uses the following data:

- poll data obtained from two main sources: The Phantom Trend's github repo which contains a nearly complete database of federal polling data from this century, and my own (incomplete but continuing) efforts at scraping the web for state polling data. At the moment I'm concentrating on federal elections, so my model is only using the federal polling data. 
- election results data from the AEC results page. The model uses the primary votes by polling place data for each polling place in the country
- preference data from Antony Green. I'm using Antony Green's calculations of preference flows in the 2013 election. 

**Poll aggregator to swings**

The current heart of the model is a poll aggregator. I'm using the same code that I wrote for my [Israeli poll aggregator](http://www.clintonboys.com/israel-poll-aggregator-1/), which accounts for pollster reliability (measured across my entire poll database, including state polls) and recency. The model computes a poll aggregate (which has a much greater historical tendency for accuracy than the individual pollsters) and then the implied swing (percentage change) from the previous election's results. 

**Four-party model and runoff simulator**

The model then takes the swing estimate and applies it to each individual seat. At this stage, the model assumes the system is ostensibly four parties, the Coalition, the Labor Party, the Greens and a generic "Others" label that encompasses everyone else. This was a decision I made early on because these are the only four options reliably included in all polls. It's also the biggest shortcoming of the model in predicting recent elections, mainly because of the rise of PUP. 

- Discussion of output

- Problems:
    + Contests which aren't LP/NP-ALP
    + Strong independent candidates
    + PUP
    + More data (pref flows)