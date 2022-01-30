import pandas as pd

df = pd.read_csv('C:\DataCsv\TEMP.ade',skipinitialspace=True,sep = ';',  header = 0,)
#read.to_excel (r'C:\DataCsv\data.xlsx', index = None, header=True) 
df


import csv
with open('C:\DataCsv\TEMP.ade', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))



import csv
with open('C:\DataCsv\TEMP.ade', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Time'], row['Quality'])




import csv, json
import pandas as pd

raw_data = {}
with open('C:\DataCsv\TEMP.ade', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    raw_data['Date Time'] = []
    raw_data['Method_Name (Filter_Name)'] = []    
    raw_data['Calc_Mode'] = []
    raw_data['Quality'] = []
    raw_data['Sample Id'] = []
    for row in spamreader:
        raw_data['Date Time'].append((row[0]).split(',')[1])
        raw_data['Method_Name (Filter_Name)'].append((row[0]).split(',')[2])
        raw_data['Calc_Mode'].append((row[0]).split(',')[3])
        raw_data['Quality'].append((row[0]).split(',')[5])
        raw_data['Sample Id'].append((row[0]).split(',')[6])
   

df = pd.DataFrame(raw_data, columns = ['Date Time', 'Method_Name (Filter_Name)', 'Calc_Mode', 'Quality']).replace('','NaNs')
df.to_csv('output_dataframe.csv')