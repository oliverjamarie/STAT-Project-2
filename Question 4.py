import xlrd
import xlsxwriter
import Read
import matplotlib.pyplot as plt
import numpy as np

file_path = "C:/Users/Oliver Marie/OneDrive/Documents/STAT 400/"
write_book = xlsxwriter.Workbook(file_path + "Question 4.xlsx")
write = write_book.add_worksheet()

data_set = Read.Reader().get_data()

bound = [35,45,50,55,65,70,75,80,100 ]#used to keep track of how many patients are within a bound
bound_countM = [] #used to keep track of how many male patients are within a bound
bound_countF = [] #used to keep track of how many female patients are within a bound
histogramM = []
#initilises bound_count based on array size of bound


#sum of all ages of men and women with CHD
tot_age_M = 0
tot_age_F = 0

#count of men and women with CHD
countM = 0
countF = 0

#initilises bound_countF and bound_countM
for index in bound:
    bound_countM.append(0)
    bound_countF.append(0)

#Traverses data_set
for item in data_set:
    if data_set[item]['chdfate'] == 1.0:
        bound_index = 0
        for i in bound:
            if data_set[item]['age'] < i and data_set[item]['sex'] == 1:
                countM += 1
                tot_age_M += data_set[item]['age']
                bound_countM[bound_index] += 1
                histogramM.append (data_set[item]['age'])
                break
            elif data_set[item]['age'] < i and data_set[item]['sex'] == 2:
                countF += 1
                tot_age_F += data_set[item]['age']
                bound_countF[bound_index] += 1
                break
            bound_index += 1

avg_ageM = tot_age_M / countM
avg_ageF = tot_age_F / countF

print ("\n\nMen")

for i in bound_countM:
    print (i)

print("\n%d Total Number Of Men\n%d Mean Average Age" % (countM, avg_ageM))

print ("\n\nWomen")

for i in bound_countF:
    print (i)

print ( "\n%d Total Number Of Women\n%d Mean Average Age" % (countF, avg_ageF))

write_book.close()


plt.hist(histogramM, bins='auto', histtype = 'bar',rwidth = .5)

plt.title ('Age distribution of male sample population')
plt.show()
