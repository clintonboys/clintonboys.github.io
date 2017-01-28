---
layout: post
title: The Bias-Variance tradeoff
image:
  feature: sample-image-28.jpg
  credit: Berlin, Germany, 2012
---

The Bias-Variance tradeoff is an extremely important concept in statistical modelling which is often misinterpreted or poorly understood. In this post I'll give a gentle introduction to the idea, followed by a deeper and more general discussion from a mathematical perspective. 

**Introduction**

We are going to be discussing the general framework of using a statistical model to make predictions. We will have a training set of input data and correct responses, and use this to build a model that allows us to predict the response variable for new input. 

Formally, let our model be represented by a function $$f:\mathbb{R}^p\to\mathbb{R}: X\mapsto Y=f(X).$$