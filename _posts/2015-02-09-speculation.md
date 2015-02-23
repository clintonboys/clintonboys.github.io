---
layout: post
title: Media speculation and leadership spills
image:
  feature: sample-image-9.jpg
  credit: Cascade Mountains, Oregon, 2013

---

There's been a lot of discussion lately about the media's role in the leadership problems which have become a common feature of the Australian political landscape in recent years. I wanted to try and quantify media speculation in some (probably fairly crude) way and try and get a nice visualisation of the build-up and release cycle that accompanies these events. 

I scraped the Sydney Morning Herald for headlines containing the string "leadership" and plotted them against a time axis which contains markers for the following (federal or NSW) leadership changes or attempted changes in the past years (only interested in government leadership, not opposition leadership):

- February 9, 2015: spill motion against Abbott (unsuccessful)
- June 27, 2013: spill motion against Gillard (successful)
- March 21, 2013: spill motion against Gillard (unsuccessful)
- June 24, 2010: spill motion against Rudd (successful)
- December 3, 2009: spill motion against Rees (successful)

To scrape the website I used the smhscraper tool by (name) that I found on github. It's a great basic tool but it needs a bit of work to clean up the data and make it useful. I'm using the brilliant datetime and pandas python packages for this. 
