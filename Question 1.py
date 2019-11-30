import xlrd
import Read
import matplotlib.pyplot as plt
import numpy as np

# Find a 95% confidence interval for the true US population proportion of women
# who develop coronary heart disease
# In the formula to find a confidence interval for a population proportion p
#   Let
#       n = total number of women
#       P^ (estimation of p) = (women with CHD)/
#       q^ = 1 - p^
#       Z(alpha/2) = |1.96|




data_set = Read.Reader().get_data()

women_countHealthy = 0
women_countCHD = 0

men_countHealthy = 0
men_countCHD = 0

for item in data_set:
    if (data_set[item]['sex']) == 2.0: #if it's a woman
        if (data_set[item][chdfate] == 2.0): #if they have the disease
            women_countCHD +=1
        else
            women_countHealthy +=1
    else #if it's a man
        if (data_set[item][chdfate] == 2.0): #if they have the disease
            men_countCHD +=1
        else
            men_countHealthy +=1
