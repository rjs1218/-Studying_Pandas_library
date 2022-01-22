'''
Excel 파일 읽기
'''

import pandas as pd

# read_excel() 함수로 데이터프레임 변환
# engine 옵션에
# excel 확장자가 xlsx일 경우 'openpyxl' 지정
# excel 확장자가 xlrd일 경우 'engine' 지정

df1 = pd.read_excel('/Users/gungo/Documents/Python/Pandas/part2_data_InOutput/남북한발전전력량.xlsx', engine='openpyxl')

df2 = pd.read_excel('/Users/gungo/Documents/Python/Pandas/part2_data_InOutput/남북한발전전력량.xlsx', engine='openpyxl', header=None)

print(df1, '\n')
print(df2)