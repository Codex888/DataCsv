import pandas as pd
import pyodbc
import pyexcel
fields = ['value']

df = pd.read_csv('C:\DataCsv\TEMP.ade',skipinitialspace=True, usecols=fields,sep = ';',  header = 0,)
read.to_excel (r'C:\DataCsv\data.xlsx', index = None, header=True) 
df