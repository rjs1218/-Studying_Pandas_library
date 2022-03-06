'''
행, 열 바꾸기
'''

import pandas as pd

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data)
print(df, '\n')

# 데이터프레임 df를 전치하기
df = df.transpose()
print(df, '\n')

df = df.T
print(df)