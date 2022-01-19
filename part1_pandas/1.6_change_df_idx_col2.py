'''
행 인덱스 / 열 이름 변경
'''
import pandas as pd

# 행 인덱스 / 열 이름 지정하여 데이터프레임 만들기
df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],\
    index = ['준서', '예은'], columns = ['나이', '성별', '학교']) # !!!열로 입력이 되는 딕셔너리와 달리 행으로 입력이 됨!!!

print(df)
print('\n')

# 열 이름 바꾸기
df.rename(columns={'나이':'연령', '성별':'남녀', '학교':'소속'}, inplace=True) # inplace=True 옵션을 안 넣으면 원본 객체를 수정하는 것이 아닌, 새로운 데이터프레임 객체를 반환함.

# 행 이름 바꾸기
df.rename(index={'준서':'학생1', '예은':'학생2'}, inplace=True)

print(df)