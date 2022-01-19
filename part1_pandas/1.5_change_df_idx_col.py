'''
행 인덱스 / 열 이름 설정
'''
import pandas as pd

# 행 인덱스 / 열 이름 지정하여 데이터프레임 만들기
df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],\
    index = ['준서', '예은'], columns = ['나이', '성별', '학교']) # !!!열로 입력이 되는 딕셔너리와 달리 행으로 입력이 됨!!!

print(df)
print(df.index)     # 행 인덱스
print(df.columns)   # 열 인덱스
print('\n')

# 행 인덱스, 열 이름 변경하기
df.index = ['학생1', '학생2']
df.columns = ['연령', '남녀', '소속']

print(df)
print(df.index)     # 행 인덱스
print(df.columns)   # 열 인덱스
