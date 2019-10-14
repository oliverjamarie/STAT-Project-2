import xlrd
import xlsxwriter
import Read


file_path = "C:/Users/Oliver Marie/OneDrive/Documents/STAT 400/"
write_book = xlsxwriter.Workbook(file_path + "Question 3.xlsx")
write = write_book.add_worksheet()

data_set = Read.Reader().get_data()

bound = [150,175,200,225,250,275,300,325,350,375]

bound_count = [] #used to keep track of how many patients are within a bound

#initilises bound_count based on array size of bound
for index in bound:
    bound_count.append(0)

for item in data_set:
    if data_set[item]['chdfate'] == 1.0:
        bound_index = 0
        for i in bound:
            if data_set[item]['scl'] != '' and data_set[item]['scl'] < i:
                print ("%d \t %d" %(i,data_set[item]['scl']))
                bound_count[bound_index] += 1
                break
            bound_index += 1

print ("\n\n")

for i in bound_count:
    print (i)

write_book.close()
