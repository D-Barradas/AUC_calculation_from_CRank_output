#!/usr/bin/env python
# coding: utf-8

# In[29]:


# %load ../calculate_auc_from_CR_out_file.py
#!/usr/bin/env python


import string
import sys
from math import *
from scipy import *
from sklearn import metrics



def read_zscore_file(zscore_file):
    #Inizio di lettura
    f = open(zscore_file).readlines()
    g = open("%s.auc.temp"%(zscore_file) ,"w")
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
        if "I" in F or "G" in F or "R" in F :
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

#         g.write("line:{} TP:{} FP:{} TTP:{} TFP:{}\n".format(line, TP, FP, TTP, TFP))
    #    print line, TP, FP, TTP, TFP
        new_file_with_columns.append((line, TP, FP, TTP, TFP))
    g.write("{} {}\n".format(TTP, TFP))
    for m in new_file_with_columns:
        new_line = " ".join(m[0].split("_"))
        TP2, FP2, TTP2, TFP2 = m[1],m[2],m[3],m[4]
        g.write("{} {} {} {} {}\n".format(new_line, TP2, FP2, TTP2, TFP2))
    return ( TTP,TFP , new_file_with_columns, name)
    # print >>g, TTP,TFP



# In[30]:


# In[110]:


def calculate_auc (new_file_with_columns,TTP ,TFP ):
    totalPositive = float(TTP)
    totalNegative = float(TFP)     
    if totalPositive == 0 or totalNegative == 0:
        print ("Warning ! totalPositive = {}  totalNegative = {} ".format(totalPositive,totalNegative))
    else : 
        tprs = []
        fprs = []
        predictedTruePositiveSofar = 0
        predictedFalsePositiveSofar = 0  

        for d in new_file_with_columns:
#             tprs.append(float(d[3])/float(totalPositive))
#             fprs.append(float(d[3])/float(totalPositive))
            
#             print (n,d)
            true_col = float(d[1])
            false_col = float(d[2])
            if true_col == 1 :
                predictedTruePositiveSofar +=1
            if false_col == 1:
#             else :

                predictedFalsePositiveSofar +=1

            tprs.append(float(predictedTruePositiveSofar)/float(totalPositive))
            fprs.append(float(predictedFalsePositiveSofar)/float(totalNegative))
        return ( metrics.auc(fprs, tprs) )





# In[31]:


# In[127]:


# file = "only_zscore/CP57/Zscore.txt"
# file = "/Users/barradd/Desktop/AUC/test-Zscore"
file = "%s"%(sys.argv[1])
# file = "../data/T26_Zscore5.0.txt"


# In[128]:


my_TTP, my_TFP, my_data , name =  read_zscore_file(file)


# In[129]:


# print (my_TTP, my_TFP)


# In[130]:


print ( "file:", name, "AUC:" , calculate_auc(my_data,my_TTP, my_TFP))


# In[32]:


# !head ../data/T26_Zscore5.0.txt*


# In[ ]:




