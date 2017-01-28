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

The local density $$\rho_{i}$$ is defined as

$$
\begin{equation}
    \rho_{i}=\sum_{j}\chi(d_{ij}-d_{c})
\end{equation}
$$

where

$$
\begin{equation}
\chi(x) = 
    \begin{cases}
        1 & x<0 \\
        0 & \text{otherwise}
    \end{cases}
    \label{aa}
\end{equation}
$$
