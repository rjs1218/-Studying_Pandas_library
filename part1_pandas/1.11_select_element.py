'''
원소 선택
'''

import pandas as pd

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data)

# '이름' 열을 새로운 인덱스로 지정
df.set_index('이름', inplace=True)
print(df)

# 데이터프레임 원소 1개 선택
a = df.loc['서준', '음악']
print(a)
b = df.iloc[0, 2]
print(b)

# 데이터 프레임 원소 2개 선택
c = df.loc['서준', ['음악', '체육']]
d = df.iloc[0, [2, 3]]
e = df.loc['서준', '음악':'체육']
f = df.iloc[0, 2:]
print(c)
print(d)
print(e)
print(f)