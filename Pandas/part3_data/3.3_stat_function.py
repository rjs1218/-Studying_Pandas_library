'''
통계 함수
'''

import pandas as pd

df = pd.read_csv('/Users/gungo/Documents/Python/Pandas/part3_data/auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 평균값
print(df.mean(), '\n')
print(df['mpg'].mean(), '\n')
print(df.mpg.mean(), '\n')
print(df[['mpg', 'weight']].mean(), '\n'*2)

# 중간값
print(df.median(), '\n')
print(df['mpg'].median(), '\n'*2)

# 최댓값(문자열 포함)
print(df.max(), '\n')
print(df['mpg'].max(), '\n'*2)

# 최솟값(문자열 포함)
print(df.min(), '\n')
print(df['mpg'].min(), '\n'*2)

# 표준편차 : 자료가 평균을 중심으로 얼마나 퍼져 있는지를 나타내는 수치
print(df.std(), '\n')
print(df['mpg'].std(), '\n'*2)

# 상관계수 : 두 변량 X, Y 사이의 상관관계의 정도를 나타내는 수치
print(df.corr(), '\n')
print(df[['mpg', 'weight']].corr())