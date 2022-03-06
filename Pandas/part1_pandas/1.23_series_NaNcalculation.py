'''
NaN 값이 있는 시리즈 연산
'''

import pandas as pd
import numpy as np

student1 = pd.Series({'국어':np.nan, '영어':80, '수학':90})
student2 = pd.Series({'수학':80, '국어':90})

print(student1, '\n')
print(student2, '\n')

# 두 학생의 과목별 점수로 사칙연산 수행(시리즈 vs 시리즈)
addition = student1 + student2          # 덧셈
subtraction = student1 - student2       # 뺄셈
multiplication = student1 * student2    # 곱셈
division = student1 / student2          # 나눗셈
print(type(division), '\n')

# 사칙연산 결과를 데이터프레임으로 합치기(시리즈 -> 데이터프레임)
result = pd.DataFrame([addition, subtraction, multiplication, division], index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)
