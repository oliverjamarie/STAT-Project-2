import xlrd
import Read
import matplotlib.pyplot as plt
import numpy as np


data_set = Read.Reader().get_data()

bound = [75,100,125,150,175,200,225,250,275]
data_chd = [] #Stores the sbp of patients with CHD
data_healthy = [] #Stores the sbp of the patients without CHD

for item in data_set:
    if data_set[item]['chdfate'] == 1.0:
        data_chd.append(data_set[item]['sbp'])
    else:
        data_healthy.append(data_set[item]['sbp'])

plt.hist(data_chd, bound, histtype = 'bar', rwidth = .8)
plt.title('Distribution of Systemic Blood Pressure (SBP)\n of the sample population diagnosed with CHD')
plt.show()

plt.hist(data_healthy, bound, histtype = 'bar', rwidth = .8)
plt.title('Distribution of Systemic Blood Pressure (SBP)\n of the sample population NOT diagnosed with CHD')
plt.show()

plt.boxplot(data_chd)
plt.title("Box And Whiskers Plot of SPB\n of the sample population diagnosed with CHD ")

plt.boxplot(data_healthy)
plt.title("Box And Whiskers Plot of SPB\n of the sample population NOT diagnosed with CHD ")
plt.show()
