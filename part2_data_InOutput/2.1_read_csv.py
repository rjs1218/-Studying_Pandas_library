'''
CSV 파일 읽기
'''

import pandas as pd

file_path = '/Users/gungo/Documents/Python/Pandas/part2_data_InOutput/read_csv_sample.csv'

# read_csv() 함수로 데이터프레임 변환.
df1 = pd.read_csv(file_path)
print(df1, '\n')

# csv파일에 ,대신 다른 구분자가 사용되었다면(ex: 탭이나 공백 등)
# sep또는 delimiter 옵션을 알맞게 입력(ex: 구분자가 |라면, sep='|' 옵션 입력)

# header = None 옵션
df2 = pd.read_csv(file_path, header=None)
print(df2, '\n')

# index_col = None 옵션
df3 = pd.read_csv(file_path, index_col=None)
print(df3, '\n')

# index_col = 'c0' 옵션
df4 = pd.read_csv(file_path, index_col='c0')
print(df4)