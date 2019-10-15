import xlrd
import xlsxwriter
import Read
import matplotlib.pyplot as plt
import numpy as np

data_set = Read.Reader().get_data()
data_chd = []  #Stores the scl of patients with CHD
data_healthy = [] #Stores the scl of healthy patients

count_chd = 0 #Number of people with CHD
count_healthy = 0 #Number of healthy patients
pop_size = 0 #Size of sample population

bound = [150,175,200,225,250,275,300,325,350,375]

for item in data_set:
    if data_set[item]['chdfate'] == 1.0:
        data_chd.append(data_set[item]['scl'])
    else:
        data_healthy.append(data_set[item]['scl'])

count_chd = len (data_chd)
count_healthy = len(data_healthy)
pop_size = len(data_set)

plt.hist(data_chd, bound, histtype = 'bar', rwidth = .8, orientation = 'horizontal')
plt.title('Distribution of SCL\n of the sample population diagnosed with CHD')
plt.show()
