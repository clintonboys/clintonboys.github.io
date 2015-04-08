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

Below is a list of the census demographic variables (from the 2006 and 2011 censuses) which are most highly correlated with two-party preferred Labor vote (or equivalently with two-party preferred Coalition vote, since COA = 100 – ALP) across 147 electorates (redistribution in the house of representatives means the electorates from the election and those which existed at the time of the census do not quite match up. As a result I had to exclude three electorates from this analysis).

1. Percentage of labour force in electorate aged 45 and above
2. Migrant index (the migrant index is an average of four statistics which are presumably highly interdependent and which all have very similar correlation coefficients: percentage overseas born, percentage non-English speaking born, percentage speaking English badly or not at all, percentage speaking language other than English at home)
3. Percentage of electorate employed in agriculture
4. Percentage of electorate who are unemployed
5. Median age in electorate
6. [Total dependency ratio](http://en.wikipedia.org/wiki/Dependency_ratio)
7. Percentage of electorate aged between 15 and 24
8. Percentage of electorate who are Catholic
9. Logarithm of population density of electorate (The logarithm gives a more intuitive statistic given the highly skewed nature of Australian electorates and the rural/urban divide)
10. Number of years served by current member. 

I thought the most interesting thing on this list was the first statistic, which had the highest correlation coefficient of -0.7267, and is plotted below:

![Labour force and Labor vote](https://github.com/clintonboys/clintonboys.github.io/blob/master/_posts/labour.png?raw=true)

Personally, if I had to guess, I would have thought these two variables were positively correlated – persons over 45 in the labour force would seem to be prime candidates for old-school union movement Labor voters to me. But as you can see, the higher the proportion of the electorate in this category, the lower the Labor vote. And this relationship explains nearly 3/4 of the variance in 2PP Labor vote.

So now we want to cluster seats according to these variables. This should provide a more sophisticated framework for swing and trend adjustment than I've seen in other models, which might take into account the rural/urban divide (which is accounted for mainly in variables 2, 3 and 5 above), "sophomore surges" for members on their first reelection (variable 10 above). 

