'''
데이터 개수 확인
'''

import pandas as pd

df = pd.read_csv('/Users/gungo/Documents/Python/Pandas/part3_data/auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 데이터프레임 df의 각 열이 가지고 있는 원소 개수 확인
print(df.count(), '\n')

# df.count()가 반환하는 객체 타입 출력 -> 시리즈 객체가 출력됨
print(type(df.count()), '\n')

# 데이터프레임 df의 특정 열이 가지고 있는 고유값 확인
# 1은 미국, 2는 유럽, 3은 일본을 나타낸다.
unique_values = df['origin'].value_counts()
print(unique_values, '\n')
print(type(unique_values))

