########## Module 1 ##########
# Introduction to ML Strategy#

# 1/26/2020 
# Orthogonalization 

# Chian of assumption in ML
# Fit training set well on cost function 
# Fit dev set well on cost function 
# Fit test well on cost function 
# Perform well in real world

########## Module 2 ##########
#    Setting Up Your Goal    #

# Single Number Evaluation Metric 
# Precision-Accuracy on labelled data
# Recall-Accuracy on test data
# F-1 score
# Harmonic Mean #
# 2/(1/P+1/R)

# Satisficing and Optimization Metric 
# Accuracy and running time 
# N metric: 1 optimizing, 1 satisficing 
# Waken words/ trigger words 
# Number of true positive
# Number of false positive 

# Train/dev/test distribution 
# How to set them up?
# Guideline 
# Choose a dev set and test set to reflect the data you expect to get in the future 
# Consider to do well on 

# 1/27/20
# Old way od splitting data

# Size of test set 
# Set your test set to be big enough to give high confidence in the overall performance


# When to CHnage dev/test and Metrices #
# Orthogonalization for cat picturess: anti-porn 
# 1. Metric to evaluate classifier: plant target 
# 2. How to do well on this metric

########## Module 3 ##########
#   Human Level Performance  #

# Human, Bayes Optimal Error 
# As long as ML is worse than human, you can:
# 1. Get labeled data from humans
# 2. Gain insight from manual error analysis: Why did a person get right?
# 3. Better analysis of bias/variance


#      Avoidable Bias      #
# 1/28/2020
# Human-level error as a proxy for Bayes error 


# Surpassing Human-level Performance #

# Problem where ML significantly surpasses human-level performance 
# On-line advertising 
# Product recommendation 
# Logistics
# Loan approval 
# Speech recognition 
# Medical 

# Human are not completely task-based 

# Improve Your Model Peroformance #
# Fit the training set well 
# The training set performance generalizes pretty well to the dev/test set 

# Avoid bias (Human-level and Traing-error)
# - Train bigger model 
# - Train longer/better optimization algorithm
# - NN architecture/hyperparameter search 

# Variance (Training error and Dev error)
# -More data 
# -Regularization 
# - NN architecture/hyperparameter search 