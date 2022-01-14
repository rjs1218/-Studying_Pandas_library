'''
딕셔너리 -> 시리즈 변환
'''
import pandas as pd

# key : value로 이루어진 딕셔너리 만들기
dict_data = {'a' : 1, 'b' : 2, 'c' : 3}

# 판다스 Series() 함수로 dictionary를 Series로 변환
series = pd.Series(dict_data)

# series 자료형 출력
print(type(series))
print('\n')

# 변수 series에 저장되어 있는 시리즈 객체 출력
print(series)
