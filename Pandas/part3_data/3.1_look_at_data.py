'''
데이터 살펴보기
'''

import pandas as pd

df = pd.read_csv(r'/Users/gungo/Documents/Python/Pandas/part3_data/auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

print(df.head(), '\n')
print(df.tail(), '\n')

# df의 모양과 크기 확인(행과 열의 개수)를 투플로 반환
print(df.shape, '\n')

# 데이터프레임 df의 내용 확인
print(df.info(), '\n')

# 데이터프레임 df의 자료형 확인
print(df.dtypes, '\n')

# 시리즈 mpg 열의 자료형 확인
print(df.mpg.dtypes)

# 데이터프레임 df의 기술 통계 정보 확인
print(df.describe(), '\n')          # 산술 데이터만
print(df.describe(include='all'))   # 문자열 데이터도 포함