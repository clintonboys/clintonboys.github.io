---
layout: post
title: Forecasting Australian elections II - Demographic variables and nearest neighbour analysis of electorates
image:
  feature: sample-image-18.jpg
  credit: Cradle Mountain, Tasmania, 2014

---

In this post we'll use census data to cluster Australian federal electorates according to their demographic similarity. This is a good exercise for me to use some basic clustering algorithms, and it's a component I'd like to use in my final model. 

Remember that the important quantity in Australian parliamentary elections is the **swing** in each seat. If we can estimate the swing in each seat, we can assign seats using the Mackerras pendulum and get an election result. 

Suppose we have come up with a nation-wide (or state-wide, or nation-wide but broken down by state) measure of swing. In a basic model, there may be an adjustment on a seat-by-seat basis based on a number of factors. Clustering seats together aims to eliminate this guesswork (such as assigning seats a classification like "rural" or "urban"). We will make small swing adjustments based on which clusters our seats belong to, calibrated by their mean collective swing as cluster at previous contests. As we mentioned in a previous post, this is all made much more complicated by [redistributions](http://www.clintonboys.com/aus-election-model-4/). 

Here I just want to choose the demographic variables we want to feed into the clustering algorithm, and come up with a sensible number of clusters. 