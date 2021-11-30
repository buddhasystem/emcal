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

