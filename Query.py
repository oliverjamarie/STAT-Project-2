#Used to get information on the data_set

import xlrd
import Read
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

data_set = Read.Reader().get_data()

def get_num_men ():
    count = 0
    for item in data_set:
        if data_set[item]['sex'] == 1:
            count += 1
    return count

def get_num_women ():
    count = 0
    for item in data_set:
        if data_set[item]['sex'] == 2:
            count += 1
    return count

def get_total_pop_size ():
    return len(data_set)

def get_num_men_chd ():
    countM = 0
    for item in data_set:
        if data_set[item]['chdfate'] == 1.0:
            #If a man
            if data_set[item]['sex'] == 1.0:
                countM += 1
    return countM

def get_min_sbp():
    min = 1000.0
    for item in data_set:
        if data_set[item]['sbp'] < min :
            min = data_set[item]['sbp']

    return min

def get_num_sbp_less (num):
    count = 0

    for item in data_set:
        if data_set[item]['sbp'] < num and data_set[item]['sbp'] != 0.0 :
            count += 1

    return count

def get_spb_percentiles ():
    percentile = math.ceil(get_total_pop_size()/10)
    print (percentile)
    pos = 1
    count = 0

    for item in data_set:
        if pos > 0 and pos % percentile == 0:
            print(pos)
            count += 1

        pos += 1

#generates histogram based off age
def generate_hist_age ():
    bin = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
    age =[]

    for item in data_set:
        age.append(data_set[item]['age'])
    plt.hist(age, bins='auto', histtype = 'bar', rwidth = 0.8, normed = True)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title ('Age Distribution of sample population')
    plt.show()

def testSCL ():
    for i in data_set:
        print(i)

testSCL()
