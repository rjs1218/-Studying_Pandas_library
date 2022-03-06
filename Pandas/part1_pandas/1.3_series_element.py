'''
시리즈 원소 선택
'''
import pandas as pd

# 투플을 시리즈로 변환(인덱스 옵션 지정)
# 투플과 리스트의 차이점은 투플은 원소를 추가하거나 삭제할 수 없음
tup_data = ('rjs1218', '2000-12-18', '남', True)
sr = pd.Series(tup_data, index = ['이름', '생년월일', '성별', '학생여부'])
print(sr)
print('\n')

# 원소 1개 선택
print(sr[0])
print(sr['이름'])
print('\n')

# 여러 개의 원소 선택(인덱스 리스트 활용)
print(sr[[1, 2]])
print('\n')
print(sr[['생년월일', '성별']])
print('\n')

# 여러 개의 원소를 선택(인덱스 범위 지정)
print(sr[1:2])
print('\n')
print(sr['생년월일':'성별'])