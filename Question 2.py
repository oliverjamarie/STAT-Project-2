import xlrd
import xlsxwriter
import Read
import matplotlib.pyplot as plt
import numpy as np

file_path = "C:/Users/Oliver Marie/OneDrive/Documents/STAT 400/"
write_book = xlsxwriter.Workbook(file_path + "Question 2.xlsx")
write = write_book.add_worksheet()

data_set = Read.Reader().get_data()

bound = [100,125,150,175,200,225,250]
histogram = []

bound_count = [] #used to keep track of how many patients are within a bound

#initilises bound_count based on array size of bound
for index in bound:
    bound_count.append(0)


for item in data_set:
    if data_set[item]['chdfate'] == 1.0:
        bound_index = 0
        for i in bound:
            if data_set[item]['sbp'] < i:
                print ("%d \t %d" %(i,data_set[item]['sbp']))
                bound_count[bound_index] += 1
                break
            bound_index += 1
        histogram.append(data_set[item]['sbp'])

print ("\n\n")

for i in bound_count:
    print (i)

write_book.close()

plt.hist(histogram, bins = 'auto', histtype = 'bar', rwidth = .8)

plt.title('Distribution of Systemic Blood Pressure of the sample population')
plt.show()

plt.boxplot(histogram)
plt.show()
