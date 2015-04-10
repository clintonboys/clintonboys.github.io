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

Below is a list of the census demographic variables which for the 2006 census are most highly correlated with two-party preferred Labor vote at the 2007 Federal election (or equivalently with two-party preferred Coalition vote, since COA = 100 – ALP). 

1. Percentage of labour force in electorate aged 45 and above
2. Migrant index (the migrant index is an average of four statistics which are presumably highly interdependent and which all have very similar correlation coefficients: percentage overseas born, percentage non-English speaking born, percentage speaking English badly or not at all, percentage speaking language other than English at home)
3. Percentage of electorate employed in agriculture
4. Percentage of electorate who are unemployed
5. Median age in electorate
6. [Total dependency ratio](http://en.wikipedia.org/wiki/Dependency_ratio)
7. Percentage of electorate aged between 15 and 24
8. Percentage of electorate who are Catholic
9. Logarithm of population density of electorate (The logarithm gives a more intuitive statistic given the highly skewed nature of Australian electorates and the rural/urban divide)

I thought the most interesting thing on this list was the first statistic, which had the highest correlation coefficient of -0.7267, and is plotted below:

![Labour force and Labor vote](https://github.com/clintonboys/clintonboys.github.io/blob/master/_posts/labour.png?raw=true)

Personally, if I had to guess, I would have thought these two variables were positively correlated – persons over 45 in the labour force would seem to be prime candidates for old-school union movement Labor voters to me. But as you can see, the higher the proportion of the electorate in this category, the lower the Labor vote. And this relationship explains nearly 3/4 of the variance in 2PP Labor vote. There's probably some confounding going on to explain this. 

There is an obvious issue here that I'm only using data from 2006, which is nearly 10 years ago. I'm in the process of obtaining the 2011 census data by electoral district to see how these variables look at the 2013 election, but the ABS doesn't make it as easy as it could. For the moment let's just use these as a proof-of-concept. 

So now we want to cluster seats according to these nine variables. This should provide a more sophisticated framework for swing and trend adjustment than I've seen in other models, which might take into account the rural/urban divide (which is accounted for mainly in variables 2, 3 and 5 above). They also usually take into account "sophomore surges" for members on their first reelection (variable 10 above); this is something I'll talk about in another post. 

I just want to use simple *k*-means clustering, and I'm going to use R. The main difficulty with *k*-means clustering is to choose the right value of *k*, the number of clusters. This requires a bit of trial-and-error to get right and needs to be calibrated against my own knowledge of Australian electorates.

    census <- read.csv('2006_census_data_by_division.csv')
    summary(census)
    pop <- as.numeric(as.character(census$Total_population[1:150]))
    Var1 <- as.numeric(as.character(census$Labour_force_aged_45_years_and_over22[1:150]))/pop
    Mig1 <- as.numeric(as.character(census$Overseas[1:150]))
    Mig2 <- as.numeric(as.character(census$NonEngBorn.[1:150]))
    Mig3 <- as.numeric(as.character(census$Persons_who_speak_English_not_well_or_not_at_all[1:150]))/pop
    Mig4 <- as.numeric(as.character(census$Persons_speaking_a_language_other_than_English_at_home[1:150]))/pop
    Var2 <- (Mig1+Mig2+Mig3+Mig4)/4
    Var3 <- as.numeric(as.character(census$Persons_employed_in_agriculture[1:150]))/pop
    Var4 <- as.numeric(as.character(census$Unemployed_persons[1:150]))/pop
    Var5 <- as.numeric(as.character(census$Median_age[1:150]))
    Var6 <- as.numeric(as.character(census$Total_dependency_ratio3[1:150]))
    Var7 <- as.numeric(as.character(census$Persons_aged_15_to_24_years[1:150]))/pop
    Var8 <- as.numeric(as.character(census$Catholic.[1:150]))
    Var9 <- log(as.numeric(as.character(census$Population_density1[1:150])))
    divs <- census$division[1:150]
    df = data.frame(divs, Var1, Var2, Var3, Var4, Var5, Var6, Var7, Var8, Var9)
  

