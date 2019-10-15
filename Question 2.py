import xlrd
import Read
import matplotlib.pyplot as plt
import numpy as np

data_set = Read.Reader().get_data()

bound = [100,120,140,160,180,200,220,240,260]
data_chd = [] #Stores the sbp of patients with CHD
data_healthy = [] #Stores the sbp of the patients without CHD

for item in data_set:
    if data_set[item]['chdfate'] == 1.0:
        data_chd.append(data_set[item]['sbp'])
    else:
        data_healthy.append(data_set[item]['sbp'])

count_chd = len(data_chd)
count_healthy = len(data_healthy)
total_Sample_size = len(data_set)

rel_freq = []

for i in bound:
    rel_freq.append(0)

index = 0
for i in data_healthy:
    index = 0
    for x in bound:
        if i < x:
            rel_freq[index] += 1
            break
        index += 1

index = 0
for i in bound:
    rel_freq[index] = rel_freq[index]/count_healthy
    index += 1

plt.bar(bound, rel_freq, align = 'edge', alpha = 0.8,width = 10)
plt.title('Distribution of Systemic Blood Pressure (SBP)\n of the sample population NOT diagnosed with CHD')
plt.show()

for i in rel_freq:
    i = 0

index = 0
for i in data_chd:
    index = 0
    for x in bound:
        if i < x:
            rel_freq[index] += 1
            break
        index += 1

index = 0
for i in bound:
    rel_freq[index] = rel_freq[index]/count_chd
    index += 1



plt.bar(bound, rel_freq, align = 'edge', alpha = 0.8,width = 10)
plt.title('Distribution of Systemic Blood Pressure (SBP)\n of the sample population diagnosed with CHD')
plt.show()

plt.boxplot(data_chd)
plt.title("Box And Whiskers Plot of SPB\n of the sample population diagnosed with CHD ")
plt.show()

plt.boxplot(data_healthy)
plt.title("Box And Whiskers Plot of SPB\n of the sample population NOT diagnosed with CHD ")
plt.show()
