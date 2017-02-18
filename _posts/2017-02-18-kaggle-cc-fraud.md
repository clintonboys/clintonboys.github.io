---
layout: post
title: Detecting credit card fraud in R and Python
image:
  feature: sample-image-45.jpg
  credit: Paphos, Cyprus, 2016
---

I have been trying recently to find an example dataset which takes me out of my comfort zone for classification problems a little bit by having a large imbalance in the sizes of the target groups. The classic example of this is credit card fraud: if you have thousands of credit card transactions, probably a very small percentage (say 1%) are fraudulent, so the stupidest model possible (saying no transactions are fraudulent) will result in 99% accuracy!

I found a great dataset on [Kaggle](https://www.kaggle.com/dalpozz/creditcardfraud/kernels) which precisely illustrates this problem. The dataset consists of data on 284,807 credit card transactions in which only 492 (0.172%) were fraudulent. As the problem description on Kaggle points out, usual confusion matrix techniques for computing model accuracy are not meaningful here, which means we will need another way of measuring our model's success. 

## Dataset

The dataset consists of 284,807 rows of credit card transaction data, which is given as 28 anonymised and normalised features (apparently obtained from a set of original features using principal component analysis, a standard method of feature normalisation) as well as two additional features: the time the transaction occurred, and its dollar amount. This final feature allows for an additional layer on top of the analysis to understand the cost of fraud and the value of fraud detection. 

## Measuring success of a model

In a simple binary classification problem, one often speaks of the *confusion matrix* for a model. This is the 2x2 matrix 

```
|-----------------|-----------------| 
| true positives  | false negatives |
| false positives | true negatives  | 
```

which allows us to compute three important quantities:

- the accuracy (the percentage of correct responses)
- the sensitivity or recall (the percentage of actual positives which were detected)
- the specificity (the percentage of actual negatives which were detected)

In unbalanced classification, accuracy is not meaningful since the "null model" will have very high accuracy. However since detection of a positive is usually meaningful and critical (i.e. detecting fraud), high recall is a useful metric in evaluating the model's usefulness (provided it does not come at the expense of too much accuracy). 

Another useful metric is [Cohen's kappa coefficient](https://en.wikipedia.org/wiki/Cohen's_kappa), which essentially weights the accuracy measure to account for the imbalance in the data. 





