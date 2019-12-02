import xlrd
import Read
import matplotlib.pyplot as plt
import numpy as np
import math


data_set = Read.Reader().get_data()

count_CHD = 0
count_healthy = 0
total_SCL_Healthy =  0
total_SCL_CHD = 0

for item in data_set:
    if (data_set[item]['scl'] != ''):
        if (data_set[item]['chdfate'] == 1.0):
            count_CHD += 1
            total_SCL_CHD += data_set[item]['scl']
        else:
            count_healthy += 1
            total_SCL_Healthy += data_set[item]['scl']

mean_SCL_CHD = total_SCL_CHD / count_CHD
mean_SCL_Healthy = total_SCL_Healthy / count_healthy

pMin = 0
pMax = 0
normal = 0
n = 0
s2 = 0 #s^2
s = 0

# From the study data, determine a 95% confidence interval for the true US
# population scl mean for those with chd
# In the formula to find a large sample confidence interval for mu
#   Let
#       n = total number of people with CHD
#       S = ?
#       Z(alpha/2) = |1.96|

n = count_CHD

normal = 1.96

for item in data_set:
    if data_set[item]['chdfate'] == 1.0 and data_set[item]['scl'] != '':
        temp = data_set[item]['scl'] - mean_SCL_CHD
        s2 += math.pow(temp,2)

print(s2)
s = math.sqrt(s2)
print (s)
