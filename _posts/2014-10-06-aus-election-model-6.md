---
layout: post
title: Difficulties in forecasting elections in Australia VI - Poll reliability
image:
  feature: sample-image-11.jpg
  credit: Blue Mountains, New South Wales, 2011. 

---

I wanted to come up with a Nate Silver-style pollster reliability weighting to include in a future model. The first step was to collect all the final polls for the major polling firms before federal elections in the past: because modern polling is quite different to the pre-Internet and mobile phone era, I just chose the federal elections in 2013, 2010, 2007 and 2004. 

As a preliminary measure of accuracy while I come up with a better one, I just want to use the federal two-party preferred (TPP) result and compare the absolute difference between a pollster's predicted TPP and the actual TPP. I then want to take an average over the four elections and obtain an average error rate. 