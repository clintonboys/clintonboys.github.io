---
layout: post
title: Forecasting Australian elections I - Poll reliability
image:
  feature: sample-image-11.jpg
  credit: Blue Mountains, New South Wales, 2011. 

---

In a series of posts last year (starting [here](http://www.clintonboys.com/aus-election-model-1/)) I discussed the difficulties in building a model for predicting Australian elections. In the next series of posts, I want to build a few basic pieces of this model. 

I wanted to come up with a Nate Silver-style pollster reliability weighting to include in my future model. The first step was to collect all the final polls for the major polling firms before federal elections in the past: because modern polling is quite different to the pre-Internet and mobile phone era, I just chose the federal elections in 2013, 2010, 2007, 2004 and 2001.  

As a preliminary measure of accuracy while I come up with a better one, I just want to use the federal two-party preferred (TPP) result and compare the absolute difference between a pollster's predicted TPP and the actual TPP. I then want to take an average over the four elections and obtain an average error rate. This is just a preliminary analysis: considering the results I am wary of including the resultant weights in my model. 

I'm only going to look at the four main pollsters: Morgan, Nielsen, Newspoll and Galaxy. ReachTEL has only become a player quite recently; in particular they only have a single data point for pre-election polling (where their estimate was off by only 0.49%). 

Although I like Python and R, this is easy enough to accomplish in the Excel spreadsheet I used to input the data. 

We obtain the following average TPP% absolute error among the major four pollsters:

    Morgan   2.60
    Nielsen  1.78
    Newspoll 1.38
    Galaxy   0.50

I found this very surprising: Galaxy has nearly a third of the error of the best of the other three pollsters.

We need to be conservative when we convert these numbers into weights though, because the national TPP figure is **not** the best indicator of the election result. The average error in a pre-election poll is 1.52; using this to create weights we get 

    Morgan    0.58
    Nielsen   0.85
    Newspoll  1.10
    Galaxy    3.02

These weights are giving far too much to Galaxy. I'm not sure what the best workaround is here; Galaxy is getting off the hook a bit for its phenomonal prediction in 2010 (it predicted 50.2, the result was 50.12) which must have been a bit of a fluke. I would suggest weightings more like

    Morgan    0.80
    Nielsen   0.90
    Newspoll  1.10
    Galaxy    1.50

would be more useful