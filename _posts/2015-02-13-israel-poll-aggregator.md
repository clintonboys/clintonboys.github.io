---
layout: post
title: Aggregating Israeli opinion polls
image:
  feature: sample-image-22.jpg
  credit: Royal National Park, New South Wales, 2014

---

The Israeli electoral system is completely different to the Australian system. 120 representatives are elected to the Knesset from a single at-large electorate. Members must be registered to a party; parties submit lists of candidates in an order they want them to be elected, candidates are then elected to the Knesset from these lists based on a proportion of votes received by each party, provided the vote is greater than the electoral threshhold (currently 3.25%, a significant increase from the previous election). 

It is difficult to provide a probabilistic model of what the Israeli government will look like after the election, even with the significant amount of polling that exists, because Israel's proportional representation system has meant, like many European countries in the post-war period, majority governments never occur. Rather, the election is just the first phase of a process that is followed by political wrangling and deals behind closed doors to form a coalition government (and these are often very unstable: the current election is more than twelve months early because of the breakdown of a previous coalition). 

In this post I just want to come up with a simple poll aggregator that adjusts for accuracy in previous contests. There's a whole bunch of opinion polls floating around but most aggregators (like the one on HaAretz) just seem to take a simple average (although I imagine there's plenty of sites in Hebrew that I can't read yet). I want to look at the final poll all the polling firms did before the 2013, 2009, 2006 and 2003 elections and come up with an accuracy score for each polling firm which will then translate into a weight in the aggregator. 

I looked at the Wikipedia pages for each election, which contain a lot of opinion polling information, and compiled them into tables. For example, the following table has the election result, together with the final polls of six top pollsters:

**Poll** | Kadima | Likud | Labor | Shas | UTJ | HaBayit | UAL | Hadash | Balad | Meretz | Yesh Atid | Otzman | Am Shalem | Hatnuah
--- | --- | ---
*Election* | *2* | *31* | *15* | *11* | *7* | *12* | *4* | *4* | *3* | *6* | *19* | *0* | *0* | *6* 
Dahaf | 2 | 32 | 17 | 11 | 6 | 12 | 4 | 4 | 3 | 6 | 13 | 2 | - |  8
