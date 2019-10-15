import xlrd
import Read
import matplotlib.pyplot as plt
import numpy as np

data_set = Read.Reader().get_data()

bound = [35,45,50,55,65,70,75,80,100 ]#used to keep track of how many patients are within a bound
bound_countM_chd = [] #used to keep track of how many healthy males are within a bound
bound_countF_chd = [] #used to keep track of how many healthy females are within a bound
bound_countM_healthy = [] #used to keep track of how many male CHD patients are within a bound
bound_countF_healthy = [] #used to keep track of how many female CHD patients are within a bound
dataM_chd = []
dataF_chd= []
dataM_healthy = []
dataF_healthy= []


#sum of all ages of men and women with CHD
tot_ageM_chd = 0
tot_ageF_chd = 0

#sum of all ages of healthy men and women
tot_ageM_healthy = 0
tot_ageF_healthy = 0

#count of men and women with CHD
countM = 0
countF = 0

#initilises arrays
for index in bound:
    bound_countM_chd.append(0)
    bound_countF_chd.append(0)
    bound_countM_healthy.append(0)
    bound_countF_healthy.append(0)
    dataM_chd.append(0)
    dataF_chd.append(0)
    dataM_healthy.append(0)
    dataF_healthy.append(0)

#Traverses data_set
for item in data_set:
    if data_set[item]['chdfate'] == 1.0:
        index = 0
        for i in bound:
            if data_set[item]['age'] < i and data_set[item]['sex'] == 1:
                countM += 1
                tot_ageM_chd += data_set[item]['age']
                bound_countM_chd[index] += 1
                dataM_chd.append (data_set[item]['age'])
                break
            elif data_set[item]['age'] < i and data_set[item]['sex'] == 2:
                countF += 1
                tot_ageF_chd += data_set[item]['age']
                bound_countF_chd[index] += 1
                dataF_chd.append(data_set[item]['age'])
                break
            index += 1
    else:
        index = 0
        for i in bound:
            if data_set[item]['age'] < i and data_set[item]['sex'] == 1:
                countM += 1
                tot_ageM_healthy += data_set[item]['age']
                bound_countM_healthy[index] += 1
                dataM_healthy.append (data_set[item]['age'])
                break
            elif data_set[item]['age'] < i and data_set[item]['sex'] == 2:
                countF += 1
                tot_ageF_chd += data_set[item]['age']
                bound_countF_healthy[index] += 1
                dataF_healthy.append(data_set[item]['age'])
                break
            index += 1

avg_ageM = tot_ageM_chd / countM
avg_ageF = tot_ageF_chd / countF

print("\n%d Total Number Of Men\n%d Mean Average Age" % (countM, avg_ageM))
print ( "\n%d Total Number Of Women\n%d Mean Average Age" % (countF, avg_ageF))

#
# plt.hist(dataM_chd, bins='auto', histtype = 'bar',rwidth = .5)
# plt.title ('Age distribution of male sample population')
# plt.show()
