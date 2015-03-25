---
layout: post
title: Forecasting Australian elections I - Poll reliability
image:
  feature: sample-image-11.jpg
  credit: Blue Mountains, New South Wales, 2011. 

---

In a series of posts last year (starting [here](http://www.clintonboys.com/aus-election-model-1/)) I discussed the difficulties in building a model for predicting Australian elections. In the next series of posts, I want to build a few basic pieces of this model. 

<<<<<<< HEAD
The first piece of the model I want to build is a series of reliability weights for pollsters. First let's have a look at who the main pollsters are in Australian elections.

**Newspoll** - The best-known and most influential pollster. Polls Federal and State elections since 1985, using random telephone number selection. Only calls landlines. 

**Morgan** - The oldest pollster. Has polled Federal elections since the 1940s, and also polls State elections. Traditionally a door-to-door pollster, in recent years has updated its model to include SMS and internet sampling. 

**Galaxy** - Fairly recent pollster, polling Federal elections since 2004, and some recent state elections. Uses random telephone number selection and includes mobile phones. 

**Nielsen / Ipsos** Nielsen used to conduct polls for Fairfax newspapers but stopped in 2014. It has been replaced by Ipsos. Telephone pollster that calls landlines and mobiles (Nielsen used to only call landlines).  

**ReachTEL** - Automated dialling pollster. Polls both Federal and State elections. 

**Essential** - The pollster used by Crikey. Polls using email. Only polls Federal elections. 

There are other minor pollsters floating around but we won't have enough data on them to create a weighting. We'll have to come up with a rule to assign polls not on this list a weight in the model.

Let's look at elections in Australia in the last ten years. There have been eighteen elections for either the Federal government or the state governments in NSW, QLD, VIC, SA and WA since then (we exclude the territories, and TAS because its system is compeltely different to the others).

I want to calculate accuracy for the firms above for whenever polled these elections; we will just use the final poll they released before election day. We'll use primary and TPP (two-party-preferred) data for our calculations. Some pollsters won't have all eighteen data points because they only poll federal elections. 

Collecting the state polling data took a really long time. Federal data has been collected and curated by Phantom Trend and is available in a Github repo. There's no such luck for state data though, so I had to get it all myself. 

Newspoll data is all available on their website in a fairly accessible form. Morgan data is also available but hidden in single media releases for each poll so it's a bit of a pain. The other pollsters are much more opaque with their data. Galaxy was helpful and actually responded to an email request with a whole bunch of data. 
=======
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
>>>>>>> b370c6e8d371b63588f03d806aa1b4885593dd46
