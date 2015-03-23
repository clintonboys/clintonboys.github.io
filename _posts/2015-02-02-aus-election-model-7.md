---
layout: post
title: Forecasting Australian elections II - Economic index
image:
  feature: sample-image-12.jpg
  credit: Newtown, New South Wales, 2012

---

In this post we'll create a simple economic index to include in our model. The underlying idea is that a strong economy tends to help the incumbent party. This is an idea we've taken from the FiveThirtyEight model: I haven't done a huge amount of research but I would assume this assumption is weaker in Australian parliamentary elections than in American presidential elections. 

The FiveThirtyEight model uses only a few variables to come up with an economic index:

- nonfarm payrolls (this variable measures unemployment)
- personal income
- industrial production
- personal consumption expenditure
- inflation
- forecasted GDP
- stock market

I want to use similar data to this, from the ABS and the ASX. My economic index will consist of:

- unemployment rate (monthly)
- average weekly income (monthly)
- income from industrial production (monthly)
- retail turnover (monthly)
- inflation (quarterly)
- GDP data (quarterly)
- ASX500 data (daily)


