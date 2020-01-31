########## Module 1 ##########
##       Error Analysis     ##

#  Evaluate multiple ideas in parallel #
# Ideas for cat detection:
# - Fix pictures of dogs being recognized as catss
# - Fix great cats being misrecognized 
# - Improve performance on blurry images 

# Cleaning up incorrectly labeled data #
# Correcting incorrect dev/test set examples
# -Apply same process to your dev and test sets to make sure they continue to come from the same distribution 
# -Consider examining examples your algorithm got right as wekk as ones it got wrong 
# -Train and dev/test data may now come from slightly different distributions

# Build your system quickly, the iterate #
# Speech recognition example
# -Noisy background 
# -Accented speech 
# -Far from micphone
# -Stuttering


# Steps 
# 1. Set up dev/test set and metric 
# 2. Build initial system quickly 
# 3. Use Bias/Variance analysis & Error analysis to prioritize next stops


########## Module 2 ##########
## Mismatched Training and dev/test set ##
# Cat app example 
# Data from webapges 

# Data from mobile app

# Speech recognition example 
# Traning: Purchased data/Smart speaker control/Voice control 
# Dev/test: Speech activated research mirror

# 1/30/20 #
# Bias and Variance with mismatched data distributions #
# Training-dev set: 
# Same distribution as training set, but used for training 

# data distrbution: training error and training-dev error
# mismatch;: training-dev set and test set 

# More general formulation 

# Addressing data mismatch #
# - Carry out manual error analysis to try to understand difference between training and dev/test sets 
# - Make training data more similar; or collect more data similar to dev/test sets


########## Module 3 ##########
## Learning from multiple tasks ##

# Transfer Learning #
# Use the model of one to solve another

#  Example: Radiology diagonis 

# Multi-task Learning #
# When multi-task learning makes sense 
# - Training on a set of tasks that could benefit from having shared lower-level features 
# -Usually: Amount of data you have for each task is quite similar 

########## Module 34 ##########
# End-to-end Deep Learning # 
# Example 
# Facial Recoginition 
# Machine translation 

# Whether to use end-to-end machine learning #
# Pros and cons

# Pros 
# - Let the data speak 
# - Less hand-desinging of comonents needed 

# Cons 
# May need amount of data 
# Exclude possible useful hand-designing components
