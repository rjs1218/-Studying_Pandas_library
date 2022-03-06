'''
행 선택
'''
import pandas as pd

exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print('\n')

# 행 인덱스를 사용하여 행 1개 선택
label1 = df.loc['서준']
position1 = df.iloc[0]
print(label1)
print()
print(position1)
print('\n')

# 행 인덱스를 사용하여 행 2개 선택
label2 = df.loc[['서준', '우현']]
position2 = df.iloc[[0, 1]]
print(label2)
print()
print(position2)

# 행 인덱스의 범위를 지정해서 행 선택
label3 = df.loc['서준':'우현']
position3 = df.iloc[0:1]
print('\n', label3)
print('\n', position3)