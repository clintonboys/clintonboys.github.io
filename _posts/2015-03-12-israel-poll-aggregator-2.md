---
layout: post
title: Aggregating Israeli opinion polls II: the aggregator 
image:
  feature: sample-image-14.jpg
  credit: Agmon HaHula, Israel, 2014

---

Having produced a series of reliability weightings, I scraped Wikipedia for opinion polls for this year's election in the last thirty days (following methodology from 538 where polls beyond this period lose their utility) (israeli_2015_polls.csv). We have to combine the reliability weightings with a recency weighting: more recent polls are weighted more highly. We're going to use the brilliant datetime package to sort out all the dates. 

    import datetime
    import numpy as np
    import pandas as pd

    polls = pd.read_table('israeli_2015_polls.csv',delimiter=',')
    polls['date'] = pd.to_datetime(polls['date'],dayfirst=True)
    poll_ratings = pd.read_csv('poll_weights.csv',delimiter=',')
    poll_ratings.columns = ['pollster','rating']

    today = datetime.datetime(2015,3,12)

The following function weights polls in the average according to their recency. 

    def exp_decay(days):
        days = getattr(days,"days",days)
        return .5 ** (days/30.)

We now inner-merge the poll data with the pollster reliability ratings to get a single table, and add in the recency weights to each poll (I briefly forgot the nice pandas way to add columns like this and did )

    polls = polls.merge(poll_ratings, how="inner", on="pollster")

    recency_weights = []
    for i in range(0,len(polls['date'])):
        recency_weights.append(exp_decay(pd.to_datetime(today,dayfirst=True)-polls['date'][i]))

    polls['recency_weights']=recency_weights

Now we put everything together and add up the average to get a nice poll aggregate:

    parties = ["L", "YB", "YA", "ZC", "BY", "S", "UTJ", "M", "A", "Y", "K"]

    for party in parties:
        print party+": " + str(np.round(np.sum(polls['rating']*polls['recency_weights']*polls[party]/(polls['rating']*polls['recency_weights']).sum()),2))

This produced the following output on March 12, five days before the election:

    L: 23.25
    YB: 5.61
    YA: 11.58
    ZC: 23.67
    BY: 12.41
    S: 6.78
    UTJ: 6.87
    M: 5.32
    A: 12.38
    Y: 3.9
    K: 8.25
    [Finished in 0.4s]

There's a few other intricacies I'd like to add to the model in the coming days if I have time:

- performing the aggregate on votes rather than seats and then assigning seats using the Knesset method, including surplus-vote agreements
- adding in weighting for sample sizes (these are very hard to come by for Israeli polls which doesn't sit well with me)
- adjusting for trends to give a forecast for election day (the current model gives a snapshot of what would happen if the election were held today)
- change to a probabilistic model which simulates 10 000 elections and gives probabilities of winning
- add some sort of analysis of Phase 2 of the electoral process, including potential coalitions etc (this is fraught with difficulty however)
