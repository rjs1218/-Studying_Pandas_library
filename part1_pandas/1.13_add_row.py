'''
행 추가
'''

import pandas as pd

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data)
print(df, '\n')

# 새로운 행 추가 - 같은 원소 값 입력
df.loc[3] = 0
print(df, '\n')

# 원소 값 여러 개의 배열 입력
df.loc[4] = ['동규', 30, 45, 13, 54]
print(df, '\n')

# 기존 행 복사
df.loc['행5'] = df.loc[3]
print(df)