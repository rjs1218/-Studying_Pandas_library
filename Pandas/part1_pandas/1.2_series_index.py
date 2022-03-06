'''
시리즈 인덱스
'''
import pandas as pd

# 리스트를 시리즈로 변환하여 변수 sr에 저장
list_data = ['2000-12-18', 23, 'gg', True]
sr = pd.Series(list_data)
print(sr)
print('\n')
# idx에 sr의 인덱스 배열 저장
idx = sr.index
# val에 sr의 데이터 값 배열 저장
val = sr.values

print(idx)
print('\n')
print(val)