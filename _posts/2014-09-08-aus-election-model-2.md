---
layout: post
title: Difficulties in forecasting elections in Australia II - Constituency sizes
image:
  feature: sample-image-8.jpg
  credit: Blue Mountains, New South Wales, 2014

---


It is worthwhile noting that FiveThirtyEight does **not** attempt to forecast US congressional elections on a district-by-district basis (instead providing a probabilistic model for the Congressional makeup as a whole). For presidential elections, which generate by far the most interest, his job is made a lot easier by the [electoral college](http://en.wikipedia.org/wiki/Electoral_College_(United_States)), a fairly ridiculous system which means that the first-past-the-post winner of state gains **the full** number of points that state has up for grabs. 

If we wanted to come up with a model for the most interesting Australian elections, we need need a way of modelling the result in each **seat**, the same way Silver models the result in each **state**. Except on an occasional, one-off basis, individual seats are not polled in Australia, so seat-by-seat data is non-existent (and when it is available, is too sporadic to be worthwhile).

The most robust and accurate opinion polling is conducted on a **countrywide** basis and especially in recent years is actually quite good. Often these countrywide results are broken down into states, but never into electoral districts. 

Somewhat inspired by Silver, my main idea for overcoming this issue is to use nearest-neighbour analysis on demographic data to obtain extrapolated polling estimates for individual districts. Imagine taking the countrywide polls, which give a two-party-preferred vote for the whole country, and then, based on previous elections and previous polls as training data, come up with an adjustment to this two-party-preferred figure for each seat. We could then simulate elections at a seat-by-seat level, with the requirement that in each simulation the total two-party-preferred vote is equal to that given by (a weighted average of) the countrywide polling data. 

For example, suppose we have come up with a weighted average of various polls and we estimate that, if the election were held today, the countrywide result would be a two-party-preferred vote of 50-50. The most simple-minded approach would be to work out what this translates to as a swing from the previous election, let's say that swing was +2% to the ALP, and then add two points to the ALP's results in each seat in the last election and come up with a result that way (for greater accuracy I'd actually like to use primary vote information and preference data and obtain my own two-party preferred estimate; see the next post in this series). 

Looking at past data though, swings are completely non-uniform across the country, and are tightly correlated with a bunch of demographic variables like household income, people born overseas, etc. Using past election data and nearest neighbour analysis, we can come up with swing estimates for individual seats with some level of confidence: computing these estimates for each seat simulates an election, and simulating an election a whole number of times would hopefully give a nice normal distribution with an estimated seat makeup for the lower house. 
