#import pandas as pd
#df = pd.read_csv('C:\Python_Data_Project\TEMP.ade', sep = '\n', header = None,squeeze = True)

import pandas as pd

# Read in the data as a Pandas Series
df = pd.read_csv('C:\Python_Data_Project\TEMP.ade', sep = ';', header = 2, squeeze = True)
read_file.to_excel (r'C:\Python_Data_Project\dat.xlsx', index = None, header=True) 
df
