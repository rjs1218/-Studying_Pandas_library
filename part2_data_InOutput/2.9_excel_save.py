'''
Excel 파일로 저장
'''

import pandas as pd

data = {'name' : [ 'Jerry', 'Riah', 'Paul'],
        'algol' : [ "A", "A+", "B"],
        'basic' : [ "C", "B", "B+"],
        'c++' : [ "B+", "C", "C+"],
        }

df = pd.DataFrame(data)
df.set_index('name', inplace=True)
print(df)

# to_excel() 메소드를 이용해서 Excel 파일로 내보내기.
df.to_excel(r"/Users/gungo/Documents/Python/Pandas/part2_data_InOutput/df_sample.xlsx")