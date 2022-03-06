'''
데이터프레임에 숫자 더하기
'''

import pandas as pd
import seaborn as sns

# titanic 데이터셋에서 age, fare 2개 열을 선택해서 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.head(), '\n')      # 첫 5행만 표시
print(type(df))

# 데이터프레임에 10 더하기
addition = df + 10
print(addition.head(), '\n')
print(type(addition))
