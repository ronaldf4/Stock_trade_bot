# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import os
import glob

# %%
print('hello')

# %%
os.getcwd()
# %%
file_list = []
os.chdir("C://Users//Ron//Desktop//Shalini Menon//FE800//Data_new")
for file in glob.glob("*.xlsx"):
    print(file)
    file_list.append(file)

for file in glob.glob("*.csv"):
    print(file)
    file_list.append(file)
    


# %%
# df = pd.read_excel('FDTR_daily.xlsx',skiprows = 5)
# df.iloc[:]

# %%
df = {}
for file_name in file_list:
    df_name = file_name[0:3]
    print(df_name)
    if file_name[-1] == 'x':
        temp = pd.read_excel(file_name, encoding = "ISO-8859-1")
        start_index = temp.iloc[:,0].ne('Date').idxmin()
        #print(start_index)
        df[df_name] = pd.read_excel(file_name, encoding = "ISO-8859-1",skiprows = (start_index + 1),usecols = [0,1]).dropna()
        df[df_name].columns = ['Date',str(df_name)]

    else:
        temp = pd.read_csv(file_name, encoding = "ISO-8859-1")
        start_index = temp.iloc[:,0].ne('Date').idxmin()
        #print(start_index)
        df[df_name] = pd.read_csv(file_name, encoding = "ISO-8859-1",usecols = [0,1]).dropna()
        df[df_name].columns = ['Date',str(df_name)]

    print('done')

# %%
df['deb']

# %%
df['dxy']['Date'] = pd.to_datetime(df['dxy']['Date'])
# %%
date_range = np.array(sorted(pd.date_range(start='12/30/2005', end='12/31/2019'),reverse=True))
#date_range
date_df = pd.DataFrame(date_range,columns = ['Date']).set_index('Date')

# %%
#date_df
# %%
final_df = date_df
for index in df.keys():
    final_df = final_df.join(df[index].set_index('Date'))


final_df.fillna(method='bfill',inplace = True)
final_df.dropna(inplace = True)

# %%
final_df.info()

# %%
final_df.drop(final_df.tail(1).index,inplace = True)
final_df = final_df.sort_index()
final_df


# %%

final_df.to_csv('../merged_data.csv')

# %%
