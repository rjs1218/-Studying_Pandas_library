'''
딕셔너리 -> 데이터프레임 변환
'''
import pandas as pd

dict_data = {'c0':[1, 2,3 ], 'c1':[4, 5, 6], 'c2':[7, 8, 9]}

# 딕셔너리를 데이터프레임으로 변환. 변수 df에 저장.
df = pd.DataFrame(dict_data)

# df 자료형 출력.
print(type(df))
print('\n')
# df에 저장되어 있는 데이터프레임 출력.
print(df)
