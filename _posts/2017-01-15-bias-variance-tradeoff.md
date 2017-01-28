---
layout: post
title: The Bias-Variance tradeoff
image:
  feature: sample-image-28.jpg
  credit: Berlin, Germany, 2012
---

The Bias-Variance tradeoff is an extremely important concept in statistical modelling which is often misinterpreted or poorly understood. In this post I'll give a gentle introduction to the idea, followed by a deeper and more general discussion from a mathematical perspective. 

We are going to be discussing the general framework of using a statistical model to make predictions. We will have a training set of input data and correct responses, and use this to build a model that allows us to predict the response variable $$Y$$ for new input $$X$$ (in machine learning this is known as *supervised learning*).

Formally, let our model be represented by a function

$$
\begin{align*}
f:\mathbb{R}^p&\to\mathbb{R}\\
X&\mapsto f(X)
\end{align*}
$$

$f$ can represent many different examples. If our expected output $Y$ is continuous, this is the setup for *regression*, and if $Y$ takes discrete (or categorical) values, this is the setup for *classification*. 

In order to know how well our model is doing, we need a way to measure its error. In statisical decision theory, this is known as a *loss function*

$$
\begin{align*}
L:\mathbb{R}\times\mathbb{R}&\to \mathbb{R}\\
(Y,f(X))&\mapsto L(Y,f(X)).
\end{align*}
$$

There are many different possible choices of loss functions, but the most commonly used in machine learning is the squared error $$L(Y,f(X)) = (Y-f(X))^2$$ (the most obvious choice, $$L(Y,f(X)) = \left\|Y-f(X)\right\|$$ is also widely used). 

In theory, deciding on our model is now easy, or at least, the problem is precisely formulated. We need to choose the function $f$ which minimises the expected loss, i.e. minimises $$\mathbb{E}(Y-f(X))^2$$. 

Some manipulation (see here or here) shows that there is a simple solution to this problem: the function which minimises the expected squared loss is given by

$$
f(X) = \mathbb{E}(Y\mid X),
$$

known as the *conditional expectation* or *regression function*. 






