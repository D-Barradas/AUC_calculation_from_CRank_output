#!/usr/bin/env python

#This script give the distance between the CA of two proteins partner and give a matrix and a plot

import string
import sys
from math import *
from scipy import *

#Inizio di lettura
f = file(sys.argv[1], "r")
g = file("rock.tmp1", "w")

name = sys.argv[1].split(".")

# total number of models in the file
NL  = 0

# results values according to L_rmsd values
TTP = 0
TFP = 0

# Everything set, starting reading file

for line in f.readlines():
    line = line.rstrip()
    NL = NL + 1
    F = line.split()
#    F = line.split()[0].split("_")[-1].split(".")[0]
#    print F
# L_rmsd analysis
# check if this line is a HQ model. In the case, store it
    TP = 0
    FP = 0
    if F[2] == "A" or F[2] == "M" or F[2] == "H":
    #if F == "A" or F == "M" or F == "H":
       TP = 1
       TTP = TTP + 1
    else :
       FP = 1
       TFP = TFP + 1
    print line, TP, FP, TTP, TFP
print >>g, TTP,TFP
