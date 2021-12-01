#!/usr/bin/env python
# A quick check of the EMCal data
# formatted in CSV
##################################
import numpy as np
from numpy import loadtxt
from numpy.polynomial import Chebyshev

import matplotlib.pyplot as plt

##################################
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input",    type=str, help="Name of the CSV file to read", default='')
parser.add_argument("-d", "--display",  action='store_true', help="Display a set of input data and exit ")

args    = parser.parse_args()

# ----------------
input   = args.input
display = args.display  # Display and exit

if input=='':
    print('Please specify a filename')
    exit(-1)

# Load the dataset
X = loadtxt(input, delimiter=',')
x = np.linspace(0, 30, 31)

plt.style.use('seaborn-whitegrid')

if display:
    plt.plot(x[7:25], X[0][7:25], 'o', color='black')
    plt.plot(x[7:25], X[1][7:25], 'o', color='red')
    plt.plot(x[7:25], X[2][7:25], 'o', color='blue')
    plt.plot(x[7:25], X[3][7:25], 'o', color='magenta')
    plt.show()
    exit(0)

poly0 = np.polyfit(x[12:17], X[0][12:17], 6)

x1 = np.linspace(x[12], x[16], 100)

answer0 = np.polyval(poly0, x1)

#print(answer)
#print(X[0])

plt.plot(x[12:17], X[0][12:17], 'o', color='black')
plt.plot(x1, answer0, '+', color='red')
plt.show()

exit(0)
