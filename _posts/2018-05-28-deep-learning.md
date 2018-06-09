---
layout: post
title: Deep learning and the universal approximation theorem
image:
  feature: sample-image-49.jpg
  credit: Eden, New South Wales, 2018
---

Deep learning, and in particular deep neural networks, is one of the most popular and 
powerful tools of modern data science. Using analogies from neuroscience, neural networks
provide a framework for building predictive models whose predictive power is seemingly 
limitless. They are at the heart of modern "artificial intelligence" wonders like smart 
assistants (Siri, Cortana, Google Assistant), smart speakers, self-driving cars and most 
modern image detection algorithms (Google image search, IBM Watson). 

This post will give a mathematically-slanted overview to neural networks, with the goal
of proving what could be referred to as the "Fundamental Theorem of Neural Networks". This
remarkable theorem is fairly accessible, and explains beautifully and precisely why neural 
networks are so powerful. 

## The mathematics of neural networks

A neural network is essentially a function approximation algorithm, modelled at a basic level
on the behaviour of neurons in the human brain. Although it is not a particularly common 
way of thinking as a data scientist, from a mathematical perspective machine learning 
is nothing more than function approximation with a probabilistic flavour. Under the assumption 
that the "true" relationship between a set of features $$X$$ and an output variable $$y$$ can be specified
by a function $$f(X, \theta)$$ which may depend further on some parameters $$\theta$$, the problem
of machine learning can be expressed as an attempt to approximate $$f$$ in a way which minimizes
a specified cost function (the choice of cost function is usually motivated probabilistically). 

A *neural network with a single hidden layer* is a finite linear combination of the form

$$
\sum_{j=1}^N\alpha_j\sigma(y_j^TX+\theta_j)
$$

where $$N,\alpha_j\in \mathbb{R}$$, and $$\sigma$$ is a special type of non-linear function we will discuss later. 

![Neural network](https://github.com/clintonboys/clintonboys.github.io/blob/master/_posts/nn.png?raw=true)

- deep learning introduction
- motivation of neural network
- definition; purely mathematical
