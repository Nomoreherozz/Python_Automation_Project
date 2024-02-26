#! E:\Python Learing\Automation Script\env\Scripts\python.exe
#Import package
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


#Read the Excel file
file_path=input('Your Excel file path: ')
df = pd.read_excel(file_path)

#Input 3 Pivots with Headers in Excel file
pivots_1 = input('Choose the Row: ')
pivots_2 = input('Choose the Column: ')
pivots_3 = input('Choose the Values: ')

#Check if the Headers exist and create new Excel for pivot tables
if pivots_1 and pivots_2 and pivots_3 in df:
 
 list = [pivots_1,pivots_2,pivots_3]
 df = df[list]
 pivot_table=df.pivot_table(index=pivots_1, columns=pivots_2,values=pivots_3,
                           aggfunc='sum').round(0)

 pivot_table.to_excel('pivot_tables.xlsx','Report',startrow=4)
 print("Successfully create pivot_tables.xlsx!!!!")
 end=input("press Enter to exit") 
 
else:
 print("Headers not exist in Excel file!!!!")
 end=input("press Enter to exit") 
 


