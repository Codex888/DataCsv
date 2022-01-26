#import pandas as pd

#df = pd.read_csv('C:\Python_Data_Project\TEMP.ade', sep = ';', header = 1, squeeze = True)
#print (df)

#import pandas as pd
#import csv
#from openpyxl import Workbook

#def convert_csv_to_xlsx(self):
#    wb = Workbook()
#    sheet = wb.active

 #   CSV_SEPARATOR = "#"

 #   with open("C:\Python_Data_Project\TEMP.ade") as f:
 #       reader = csv.reader(f)
 #       for r, row in enumerate(reader):
   #         for c, col in enumerate(row):
   #             for idx, val in enumerate(col.split(CSV_SEPARATOR)):
    #                cell = sheet.cell(row=r+1, column=idx+1)
     #               cell.value = val
#
   # wb.save("C:\Python_Data_Project\dat.xlsx")

#import pandas as pd
#import pyexcel


#df = pd.read_csv('C:\Python_Data_Project\TEMP.ade', sep = ';', header = 1, squeeze = True)

#sheet = pyexcel.get_sheet(file_name="C:\Python_Data_Project\TEMP.ade", delimiter=",")
#sheet.save_as("C:\Python_Data_Project\dat.xlsx")

import pandas as pd

#df = pd.read_csv('C:\Python_Data_Project\TEMP.ade',nrows= 100, sep = ';', header = 1, squeeze = True)
df = pd.read_csv('C:\Python_Data_Project\TEMP.ade', sep = ';', header = 0, squeeze = True)

df.to_excel("C:\Python_Data_Project\dat1.xlsx", index=None, header=True)
