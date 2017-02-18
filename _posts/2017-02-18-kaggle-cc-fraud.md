---
layout: post
title: Detecting credit card fraud in Python
image:
  feature: sample-image-45.jpg
  credit: Paphos, Cyprus, 2016
---

I have been trying recently to find an example dataset which takes me out of my comfort zone for classification problems a little bit by having a large imbalance in the sizes of the target groups. The classic example of this is credit card fraud: if you have thousands of credit card transactions, probably a very small percentage (say 1%) are fraudulent, so the stupidest model possible (saying no transactions are fraudulent) will result in 99% accuracy! 

I found a great dataset on [Kaggle](https://www.kaggle.com/dalpozz/creditcardfraud/kernels) which precisely illustrates this problem. The dataset consists of data on 284,807 credit card transactions in which only 492 (0.172%) were fraudulent. As the problem description on Kaggle points out, usual confusion matrix techniques for computing model accuracy are not meaningful here, which means we will need another way of measuring our model's success. 

I'll mention I was surprised how much Kaggle has changed since the last time I was there (probably mid-2015). It has much more of a social feel to it now, and that was always the best part of the site so it seems like they've changed their focus. I learned a few new tricks in the various notebooks people had published about this dataset. 

## Dataset

The dataset consists of 284,807 rows of credit card transaction data, which is given as 28 anonymised and normalised features (apparently obtained from a set of original features using principal component analysis or [PCA](https://en.wikipedia.org/wiki/Principal_component_analysis) , a standard method of feature normalisation) as well as two additional features: the time the transaction occurred, and its dollar amount. This final feature allows for an additional layer on top of the analysis to understand the cost of fraud and the value of fraud detection. 

## Measuring success of a model

In a simple binary classification problem, one often speaks of the *confusion matrix* for a model. This is the 2x2 matrix 

```
|-----------------|-----------------| 
| true positives  | false negatives |
| false positives | true negatives  | 
|-----------------|-----------------|
```

which allows us to compute three important quantities:

- the accuracy (the percentage of correct responses)
- the sensitivity or recall (the percentage of actual positives which were detected)
- the specificity (the percentage of actual negatives which were detected)

In unbalanced classification, accuracy is not particularly meaningful since the "null model" will have very high accuracy. However since detection of a positive *is* usually meaningful or even critical (i.e. detecting fraud), high recall is a useful metric in evaluating the model's usefulness (provided it does not come at the expense of too much accuracy). 

Another useful metric is [Cohen's kappa coefficient](https://en.wikipedia.org/wiki/Cohen's_kappa), which essentially weights the accuracy measure to account for the imbalance in the data. 

## Accuracy-recall tradeoff in some basic models

I'll run a few simple out-of-the-box models on this dataset to demonstrate the tradeoff. 

# Logistic regression

The first thing any data scientist would do with this problem, after checking a few basic sanity plots and maybe throwing away a couple of unncessary features, is to run a logistic regression model. This is the standard method for a binary target variable with multiple features.

```
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, cohen_kappa_score
X = raw.ix[:,1:29]
Y = raw.Class
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.3)
lr = LogisticRegression()
lr.fit(X_train, Y_train)
Y_pred = lr.predict(X_test)
cnf_matrix = confusion_matrix(Y_test, Y_pred)
print cnf_matrix
print 'Accuracy: ' + str(np.round(100*float((cnf_matrix[0]0]+cnf_matrix[1][1])/float((cnf_matrix[0][0]+cnf_matrix[1][1] + cnf_matrix[1][0] + cnf_matrix[0][1])),2))+'%'
print 'Cohen Kappa: ' + str(np.round(cohen_kappa_score(Y_test, Y_pred),3))
print 'Recall: ' + str(np.round(100*float((cnf_matrix[1][1]))/float((cnf_matrix[1][0]+cnf_matrix[1][1])),2))+'%'
```

```
[[85284    15]
 [   50    94]]
Accuracy: 99.92%
Cohen Kappa: 0.743
Recall: 65.28%
```

Here the accuracy is high, but the accuracy of the null model is also high. The recall is fairly poor; we let 35% of fraudulent transactions through the model. 

# Random forest 

A random forest is another model which perfectly suits this problem. A random forest uses decision trees and a clever resampling trick to correct for a common overfitting issue with simpler decision-tree models. 

```
rf = RandomForestClassifier(n_estimators = , n_jobs =4)
rf.fit(X_train, Y_train)
Y_rf_pred = rf.predict(X_test)
cnf_matrix = confusion_matrix(Y_rf_pred, Y_test)
print cnf_matrix
print 'Accuracy: ' + str(np.round(100*float((cnf_matrix[0][0]+cnf_matrix[1][1]))/float((cnf_matrix[0][0]+cnf_matrix[1][1] + cnf_matrix[1][0] + cnf_matrix[0][1])),2))+'%'
print 'Cohen Kappa: ' + str(np.round(cohen_kappa_score(Y_undersampled_test, Y_undersampled_pred),3))
print 'Recall: ' + str(np.round(100*float((cnf_matrix[1][1]))/float((cnf_matrix[1][0]+cnf_matrix[1][1])),2))+'%'
```

```
[[85293    27]
 [    6   117]]
Accuracy: 99.96%
Cohen Kappa: 0.668
Recall: 95.12%
```

The random forest model actual performs very well on this dataset. My guess is that there are a few features which control almost all of the behaviour here. 

## Using undersampling

One final way to improve models with an unbalanced dataset like this is to use undersampling. This means training the model on a training set where the "normal" data is undersampled so it has the same size as the fraudulent data. 

# Logistic regression

```
fraud_records = len(raw[raw.Class == 1])
fraud_indices = raw[raw.Class == 1].index
normal_indices = raw[raw.Class == 0].index
under_sample_indices = np.random.choice(normal_indices, fraud_records, False)
raw_undersampled = raw.iloc[np.concatenate([fraud_indices,under_sample_indices]),:]
X_undersampled = raw_undersampled.ix[:,1:29]
Y_undersampled = raw_undersampled.Class
X_undersampled_train, X_undersampled_test, Y_undersampled_train, Y_undersampled_test = train_test_split(X_undersampled,Y_undersampled,test_size = 0.3)
lr_undersampled = LogisticRegression(C=1)
Y_full_pred = lr_undersampled.predict(X_test)
cnf_matrix = confusion_matrix(Y_test, Y_full_pred)
print cnf_matrix
print 'Accuracy: ' + str(np.round(100*float((cnf_matrix[0][0]+cnf_matrix[1][1]))/float((cnf_matrix[0][0]+cnf_matrix[1][1] + cnf_matrix[1][0] + cnf_matrix[0][1])),2))+'%'
print 'Recall: ' + str(np.round(100*float((cnf_matrix[1][1]))/float((cnf_matrix[1][0]+cnf_matrix[1][1])),2))+'%'
```

```
[[82625  2674]
 [   11   133]]
Accuracy: 96.86%
Recall: 92.36%
```

Note that the recall for logistic regression is much better now. Undersampling will not improve the random forest performance since the subtlety is already built into this model. 



