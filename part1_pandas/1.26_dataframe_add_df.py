'''
데이터프레임끼리 더하기
'''

import pandas as pd
import seaborn as sns

# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.tail(), '\n')    # 마지막 5행 표시
print(type(df), '\n')

# 데이터프레임에 10 더하기
addition = df + 10
print(addition.tail(), '\n')
print(type(addition), '\n')

# 데이터프레임끼리 연산하기(addtion - df)
subtraction = addition - df
print(subtraction.tail(), '\n')
print(type(subtraction))