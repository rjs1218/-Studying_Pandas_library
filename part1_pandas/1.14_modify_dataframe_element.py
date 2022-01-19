'''
원소 값 변경
'''

import pandas as pd

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data)

# '이름' 열을 새로운 인덱스 지정
df.set_index('이름', inplace=True)
print(df, '\n')

# 데이터프레임 특정 원소 변경
df.iloc[0][3] = 80
print(df, '\n')

df.loc['서준']['체육'] = 90
print(df, '\n')

df.loc['서준', '체육'] = 100
print(df)

# 데이터프레임 원소 여러 개 변경
df.loc['서준', ['음악', '체육']] = 50
print(df, '\n')

df.loc['서준', ['음악', '체육']] = 100, 50
print(df)