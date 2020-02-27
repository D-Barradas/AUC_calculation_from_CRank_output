#!/usr/bin/env python
# coding: utf-8

# In[1]:


from optparse import OptionParser
import sys , os 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
# %matplotlib inline 
import numpy as np


# In[ ]:


def Warning_to_nan(x) :

    if isinstance(x, float):
        return x

    elif isinstance(x, str):
        try:
            if float(x):
                return (float(x))
            elif x == "0.0":
                 return 0.0

        except:
            return -1.0


# In[ ]:


def split_the_column_10(x):
    total = x.split("/")[0]
    number = x.split("/")[1].split("*")[0]
    return int(number)


# In[ ]:


##Parse the options
usage = "USAGE: python plot_the_columns.py --f1 excelfile\n"
parser = OptionParser(usage=usage)
parser.add_option("--f1",help="ExcelFile", dest="f1")


# In[ ]:


(options, args) = parser.parse_args()

if (options.f1):
    print ("%s"%(options.f1.split(".")[0]))

else:

    print ("Not enough input arguments supplied")
    print (usage)
    quit()

#cwd = os.getcwd()
#os.system("mkdir "+cwd+"/"+out_folder)


# In[ ]:


# df_excelfile = pd.read_excel("../../Tz_files/DidierExample.xlsx",sheet_name=None)
os.system("mkdir -p figures")
df_excelfile = pd.read_excel(options.f1,sheet_name=None)
full_table = pd.DataFrame()
for name, sheet in df_excelfile.items():
    print(name , sheet.columns.values[0])
#     print ( sheet.columns.values[0] )

    sheet['Target'] = sheet.columns.values[0]

    full_table = full_table.append(sheet[["AUC", "NL on 20%" , "NL on 20" ,"NL on 50" , "NL on 10" ,"Target" ,"iteration step"]])


# In[ ]:


full_table["AUC_num"] = full_table["AUC"].apply(Warning_to_nan)


# In[ ]:


full_table["New_total"] = full_table["NL on 10"].apply(split_the_column_10)


# In[ ]:


sns.lineplot(data=full_table , x='iteration step', y='AUC_num', hue="Target")
plt.grid(True)
plt.title("AUC")
plt.ylim(-0.01,1.05)
plt.ylabel("AUC")
plt.savefig("figures/AUC.png",format="png",transparent=True)
plt.clf()


# In[ ]:


sns.lineplot(data=full_table , x='iteration step', y='NL on 50', hue="Target")
plt.grid(True)
plt.title("NL on 50")
plt.savefig("figures/NL_on_50.png",format="png",transparent=True)
plt.clf()


# In[ ]:


sns.lineplot(data=full_table , x='iteration step', y='NL on 20', hue="Target")
plt.grid(True)
plt.title("NL on 50")
plt.savefig("figures/NL_on_20.png",format="png",transparent=True)
plt.clf()


# In[ ]:


sns.lineplot(data=full_table , x='iteration step', y='NL on 20%', hue="Target")
plt.grid(True)
plt.title("NL on 50")
plt.savefig("figures/NL_on_20_percent.png",format="png",transparent=True)
plt.clf()


# In[ ]:


sns.lineplot(data=full_table , x='iteration step', y='NL on 10 total', hue="Target")
plt.grid(True)
plt.title("NL on 10")
plt.savefig("figures/NL_on_10.png",format="png",transparent=True)
plt.clf()

