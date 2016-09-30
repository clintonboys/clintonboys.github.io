---
layout: post
title: Generating cricket scoreboards I
image:
  feature: sample-image-44.jpg
  credit: Corfe Castle, England, 2016
---

I've always loved the sport of cricket, specifically the 5-day test match format, and been in awe of its ability to generate statistics. Experienced commentators and writers on the game are usually able to find **some** record being broken in every single game being played, whether it is based on a well-known statistic (highest individual or team score), or a more obscure one (most runs conceded by a bowler in the fourth innings for no wickets). 

I started to wonder about automatically "simulating" cricket matches. I quickly understood that doing this properly is an extremely demanding exercise in statistics and modelling that people have done PhDs in. This is for two reasons:

- there are an astounding amount of variables at any given moment in a cricket match (pitch, ground, home team, crowd, day, weather, fatigue, bowler skill, bowler handedness, ball speed, ball condition, batter skill, batter handedness, etc etc...)
- there are several points in a cricket match where teams may have to make a strategic decision to declare or to enforce the follow-on and these decisions are very difficult to model as they depend mostly on captains' "intuition" or "feel" for the state of the match (and can include information about future weather or player injuries)

With a full simulator out of the question I decided the first step was to develop a basic simulation engine in Python which could produce logically accurate test match scorecards 
