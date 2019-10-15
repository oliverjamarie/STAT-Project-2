import xlrd
import xlsxwriter
import Read
import matplotlib.pyplot as plt
import numpy as np

file_path = "C:/Users/Oliver Marie/OneDrive/Documents/STAT 400/"
write_book = xlsxwriter.Workbook(file_path + "Question 1.xlsx")
write = write_book.add_worksheet('Question 1')

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

histogram = []

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
            #appends patients id to corresponding column based on sex
            write.write(indexM_row,indexM_col,item)
            indexM_row += 1
            countM_chd += 1
        else :
            write.write(indexF_row,indexF_col,item)
            indexF_row += 1
            countF_chd += 1
        histogram.append(data_set[item]['sex'])

total_Sample_size = countM + countF
propM_sample = countM / total_Sample_size #proportion of men in sample
propF_sample = countF / total_Sample_size #proportion of women in sample

total_num_chd = countM_chd + countF_chd
propM_chd = countM_chd / total_num_chd #proportion of men with CHD
propF_chd = countF_chd / total_num_chd #proportion of women with CHD

write.write('G10',"Men")
write.write('G11',"Women")
write.write('G12',"Total")

write.write('H9',"Sample")
write.write('I9',"Proportion In Sample")
write.write('J9',"Number Of People Who Have CHD")
write.write('K9',"Proportion Of People Who Have CHD")

write.write('H10',countM)
write.write('I10',propM_sample)
write.write('J10',countM_chd)
write.write('K10',propM_chd)

write.write('H11',countF)
write.write('I11',propF_sample)
write.write('J11',countF_chd)
write.write('K11',propF_chd)

write.write('H12',total_Sample_size)
write.write('I12',propM_sample + propF_sample)
write.write('J12',total_num_chd)
write.write('K12',propM_chd + propF_chd)

write_book.close()


plt.hist(histogram, bins = 'auto', histtype = 'bar')

plt.title ('Gender distribution of sample population')
plt.show()
