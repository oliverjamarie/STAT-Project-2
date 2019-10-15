import xlrd
import Read
import matplotlib.pyplot as plt
import numpy as np


data_set = Read.Reader().get_data()

#Row index for Male and Females !! Set to first empty cell
indexM_row = 3
indexF_row = 3

#Col index for Male and Females !! constant
indexM_col = 0
indexF_col = 2

#Counters
countM_chd = 0
countF_chd = 0
countM = 0
countF = 0

plot = []

for item in data_set:
    #counts number of men and women in sample
    if data_set[item]['sex'] == 1.0:
        countM += 1
    else :
        countF += 1

    #counts number of men and women in sample who have CHD
    if data_set[item]['chdfate'] == 1.0:
        #If a man has CHD
        if data_set[item]['sex'] == 1.0:
            plot.append(1)
            indexM_row += 1
            countM_chd += 1
        else :
            plot.append(2)
            indexF_row += 1
            countF_chd += 1


total_Sample_size = countM + countF * 1.0
propM_sample = countM / total_Sample_size #proportion of men in sample
propF_sample = countF / total_Sample_size #proportion of women in sample

total_num_chd = countM_chd + countF_chd *1.0
propM_chd = countM_chd / total_num_chd #proportion of men with CHD
propF_chd = countF_chd / total_num_chd #proportion of women with CHD

#Histogram for whole sample population
rel_freq = [0,0] #Relative Frequency

rel_freq[0] = propM_sample
rel_freq[1] = propF_sample

group = ['Male', 'Female']

plt.bar(group, rel_freq, align = 'center', alpha = 0.5)

plt.title ('Gender distribution of sample population')

plt.show()


#Histogram for people with CHD
rel_freq = [0,0] #Relative Frequency

rel_freq[0] = propM_chd
rel_freq[1] = propF_chd

group = ['Male', 'Female']

plt.bar(group, rel_freq, align = 'center', alpha = 0.5)

plt.title ('Gender distribution of sample population with CHD')


plt.show()
