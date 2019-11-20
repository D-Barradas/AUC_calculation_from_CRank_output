#!/usr/bin/env python
# coding: utf-8

# In[59]:


import string
import sys
from math import *
from scipy import *
from sklearn import metrics


# In[109]:


def read_zscore_file(zscore_file):
    #Inizio di lettura
    f = open(zscore_file).readlines()

#     name = sys.argv[1].split(".")
    name = zscore_file.split(".")[0]

    # total number of models in the file
    NL  = 0

    # results values according to L_rmsd values
    TTP = 0
    TFP = 0

    # Everything set, starting reading file
    new_file_with_columns = []
    for line in f:
#     for line in f.readlines():
        line = line.rstrip()
        NL = NL + 1
## Uncomment the line below to change the way the file is read
#         F= line.split("\t")[0].split("-")[-1]
#
        F= line.split()[0].split("-")[-1]
#         print ("HERE",F)


    # check if this line is a HQ model. In the case, store it
        TP = 0
        FP = 0
        if "I" in F or "G" in F :
            FP =1
            TFP += 1
            
        else :
#             print (line)
            TP =1 
            TTP += 1 
            
            
#         if F[2] == "A" or F[2] == "M" or F[2] == "H":
#             TP = 1
#             TTP = TTP + 1
#         else :
#             FP = 1
#             TFP = TFP + 1

    #    print line, TP, FP, TTP, TFP
        new_file_with_columns.append((line, TP, FP, TTP, TFP))
    return ( TTP,TFP , new_file_with_columns, name)
    # print >>g, TTP,TFP


# In[110]:


def calculate_auc (new_file_with_columns,TTP ,TFP ):
    totalPositive = TTP
    totalNegative = TFP     
    if totalPositive == 0 or totalNegative == 0:
        print ("Warning ! totalPositive = {}  totalNegative = {} ".format(totalPositive,totalNegative))
    else : 
        tprs = []
        fprs = []
        predictedTruePositiveSofar = 0
        predictedFalsePositiveSofar = 0    
        for n,d in enumerate(new_file_with_columns):
            true_col = int(d[1])
            false_col = int(d[2])
            if true_col == 1 :
                predictedTruePositiveSofar +=1
            else :
                predictedFalsePositiveSofar +=1

            tprs.append(float(predictedTruePositiveSofar)/totalPositive)
            fprs.append(float(predictedFalsePositiveSofar)/totalNegative)
        return ( metrics.auc(fprs, tprs) )


# In[127]:


# file = "only_zscore/CP57/Zscore.txt"
# file = "/Users/barradd/Desktop/AUC/test-Zscore"
file = "%s"%(sys.argv[1])
#file = "/Users/barradd/Desktop/AUC/T26_Zscore5.0.txt"


# In[128]:


my_TTP, my_TFP, my_data , name =  read_zscore_file(file)


# In[129]:


#print (my_TTP, my_TFP)


# In[130]:


print ( "file:", name, "AUC:" , calculate_auc(my_data,my_TTP, my_TFP))



