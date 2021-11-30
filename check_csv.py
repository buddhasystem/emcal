#!/usr/bin/env python
# A quick check of the EMCal data
# formatted in CSV
##################################
import numpy as np
from numpy import loadtxt

import matplotlib.pyplot as plt

##################################
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input",   type=str, help="Name of the CSV file to read", default='')

args    = parser.parse_args()

# Files -----------------
input  = args.input

if input=='':
    print('Please specify a filename')
    exit(-1)

# Load the dataset
dataset = loadtxt(input, delimiter=',')
x = np.linspace(0, 30, 31)

plt.style.use('seaborn-whitegrid')

plt.plot(x, dataset[0], 'o', color='black')
plt.plot(x, dataset[1], 'o', color='red')
plt.plot(x, dataset[2], 'o', color='blue')
plt.plot(x, dataset[3], 'o', color='magenta')
plt.show()

exit(0)
