---
layout: post
title: Sentiment analysis of Q&A tweets III - Estimating political affiliations
image:
  feature: sample-image-10.jpg
  credit: Stella Maris, Haifa, Israel, 2014
---

In the [previous](http://www.clintonboys.com/qanda-tweets/) [two](http://www.clintonboys.com/qanda-tweets2/) posts in this series, I came up with a method of scoring the sentiment of tweets from the Q&A program. I now want to put all these pieces together to try and get a feel for the political leanings of Twitter users watching the program. 

The big problem with this analysis, as I said in the last two posts, is that most tweets are negative, so even the positive tweets are comprised of words with negative sentiment. 

![Sentiment scatter](https://github.com/clintonboys/clintonboys.github.io/blob/master/_posts/sent_scatter.png?raw=true)

This diagram shows the real problem; of the 764 tweets I hand-classified as positive or negative, using the basic calculation from the previous post, it's very difficult to separate them by their sentiment score alone. However, if we include **two** variables, namely 

`NormalisedSentiment`: sum of all sentiments for words in the corpus in the tweet, divided by the total number of words in the tweet

    def NormalisedSentiment(tweet):
        score = 0
        for word in tweet.split(' '):
            try:
                score = score + sentiment_dict['rating'][word]
            except KeyError:
                pass
        return score


`NegativePercentage`: number of words with a sentiment less than zero, divided by the total number of words in the tweet

    def NegativePercentage(tweet):
        total_words = 0
        bad_words = 0
        for word in tweet.split(' '):
            try:
                if sentiment_dict['rating'][word] < 0:
                    total_words += 1
                    bad_words +=1
                else:
                    total_words += 1
            except KeyError:
                pass
        return float(bad_words) / float(total_words)

If we do a scatter plot of these two variables and color by classification (blue is positive, red is negative), 

    training_data = pd.DataFrame([tweets_final, normsent, negperc, classes]).transpose()
    training_data.columns = ['tweet', 'normsent', 'negperc', 'class']

    X = training_data[['normsent', 'negperc']].values
    y = training_data['class']

    color_map = []
    for score in classes:
        if score == 1:
            color_map.append('b')
        else:
            color_map.append('r')
    plt.scatter(training_data.normsent, training_data.negperc, c =color_map)
    plt.show()

we get the following picture:

![Sentiment scatter 2](https://github.com/clintonboys/clintonboys.github.io/blob/master/_posts/sent_scatter2.png?raw=true)

I now want to use simple support vector machines (which is just linear regression in this easy case) to train a decision boundary on this training data. Scikit-learn makes this particularly straightforward (I found a function plot_surface to plot the decision boundary as I had a bit of trouble figuring it out myself): 

    est = svm.SVC(kernel = 'linear')
    linear_model = est.fit(X,y)
    ax = plt.gca()
    ax.scatter(training_data.normsent, training_data.negperc, c =color_map)
    plot_surface(est, X[:,0], X[:,1],ax =ax)
    plt.show()

![Sentiment scatter 3](https://github.com/clintonboys/clintonboys.github.io/blob/master/_posts/sent_scatter3.png?raw=true)

We then fit this model to the much larger training set (noting again the model, which currently has about 72% accuracy, will only get better the more tweets I classify):

![Test data](https://github.com/clintonboys/clintonboys.github.io/blob/master/_posts/test.png?raw=true)

Let's see how this classification does with a few examples before we finish up by adding in the basic entity recognition: 




