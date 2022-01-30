import pandas as pd
import numpy as np

headerList  = ["Sample_No", "C"]

df = pd.read_csv('C:\DataCsv\TEMP.ade',sep = ';', squeeze = True)

df.columns=df.columns.str.strip()
df.columns = df.columns.str.replace(' ','_')

for index, row in df.iterrows():
     print(row["Sample_No"], row["C"][3:1000])

#for row in df:
       #print(row['Sample_No'], row['C'])

df







#import pandas as pd
#df = pd.read_csv('C:\Python_Data_Project\TEMP.ade', sep = ';', header = 0, squeeze = True)
#df.info()

#df = pd.read_csv('C:\Python_Data_Project\TEMP.ade',parse_dates=['Date       Time    '], dayfirst=True)


