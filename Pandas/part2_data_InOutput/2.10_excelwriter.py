'''
ExcelWriter() 활용
'''

import pandas as pd

data1 = {'name' : [ 'Jerry', 'Riah', 'Paul'],
         'algol' : [ "A", "A+", "B"],
         'basic' : [ "C", "B", "B+"],
          'c++' : [ "B+", "C", "C+"]}

data2 = {'c0':[1,2,3], 
         'c1':[4,5,6], 
         'c2':[7,8,9], 
         'c3':[10,11,12], 
         'c4':[13,14,15]}

df1 = pd.DataFrame(data1)
df1.set_index('name', inplace=True)
print(df1, '\n')

df2 = pd.DataFrame(data2)
df2.set_index('c0', inplace=True)

# df1을 'sheet1'으로, df2를 'sheet2'로 저장
writer = pd.ExcelWriter(r"/Users/gungo/Documents/Python/Pandas/part2_data_InOutput/df_excelwriter.xlsx")
df1.to_excel(writer, sheet_name="sheet1")
df2.to_excel(writer, sheet_name='sheet2')
writer.save()
