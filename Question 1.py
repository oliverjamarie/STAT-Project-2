import xlrd
import Read
import matplotlib.pyplot as plt
import numpy as np
import math


data_set = Read.Reader().get_data()

women_countHealthy = 0
women_countCHD = 0
women_total = 0

men_countHealthy = 0
men_countCHD = 0
men_total = 0

for item in data_set:
    if (data_set[item]['sex']) == 2.0: #if it's a woman
        if (data_set[item]['chdfate'] == 1.0): #if they have the disease
            women_countCHD +=1
        else:
            women_countHealthy +=1
    else: #if it's a man
        if (data_set[item]['chdfate'] == 1.0): #if they have the disease
            men_countCHD +=1
        else:
            men_countHealthy +=1

women_total = women_countCHD + women_countHealthy
men_total = men_countCHD + men_countHealthy

pMin = 0
pMax = 0
p_median = 0 #p~
p_estimate = 0 #p^
q_estimate = 0 #q^
normal = 0
n = 0

# Find a 95% confidence interval for the true US population proportion of women
# who develop coronary heart disease
# In the formula to find a confidence interval for a population proportion p
#   Let
#       n = total number of women
#       P^ (estimation of p) = (women with CHD)/n
#       q^ = 1 - p^
#       Z(alpha/2) = |1.96|

n = women_total
p_estimate = women_countCHD / n
q_estimate = 1 - p_estimate

normal = (math.pow(1.96,2))

nominator = p_estimate + (normal / (2 * n)) #nominator
denominator = (1 + (normal / n))
p_median = nominator / denominator

nominator = p_estimate * (q_estimate / n)
nominator += normal / (4 * math.pow(n,2))
nominator = math.sqrt(nominator)


denominator = 1 + (normal/n)

frac = nominator / denominator

pMax = round (p_median + (1.96 * frac),3)
pMin =  round (p_median - (1.96 * frac),3)
print("The 95% confidence interval for the true US population proportion of women who develop coronary heart disease is between", pMin, "and", pMax)

# Find a 95% confidence interval for the true US population proportion of men
# who develop coronary heart disease
# In the formula to find a confidence interval for a population proportion p
#   Let
#       n = total number of women
#       P^ (estimation of p) = (women with CHD)/n
#       q^ = 1 - p^
#       Z(alpha/2) = |1.96|
pMin = 0
pMax = 0
p_median = 0 #p~
p_estimate = 0 #p^
q_estimate = 0 #q^
normal = 0
n = 0

n = men_total
p_estimate = men_countCHD / n
q_estimate = 1 - p_estimate

normal = (math.pow(1.96,2))

nominator = p_estimate + (normal / (2 * n)) #nominator
denominator = (1 + (normal / n))
p_median = nominator / denominator

nominator = p_estimate * (q_estimate / n)
nominator += normal / (4 * math.pow(n,2))
nominator = math.sqrt(nominator)

denominator = 1 + (normal/n)

frac = nominator / denominator

pMax = round (p_median + (1.96 * frac),3)
pMin =  round (p_median - (1.96 * frac),3)
print("The 95% confidence interval for the true US population proportion of men who develop coronary heart disease is between", pMin, "and", pMax)
