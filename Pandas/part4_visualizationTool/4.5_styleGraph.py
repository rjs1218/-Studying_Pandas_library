'''
스타일 서식 지정 등

matplotlib 스타일 서식 종류
https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
'''

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

df = pd.read_excel(r'/Users/gungo/Documents/GitHub/Data_analsis/Pandas/part4_visualizationTool/시도별 전출입 인구수.xlsx', engine='openpyxl', header=0)

df = df.fillna(method='ffill')

# 서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)

rc('font', family='AppleGothic')

# 서울에서 경기도로 이동한 인구 데이터 값만 선택
sr_one = df_seoul.loc['경기도']

# 스타일 서식 지정
plt.style.use('ggplot')

# 그림 사이즈 지정
plt.figure(figsize=(14, 5))

# x축 눈금 라벨 회전하기
plt.xticks(size=10, rotation='vertical')

# x, y축 데이터를 plot 함수에 입력
plt.plot(sr_one, marker='o', markersize=10)   # 마커 표시 추가

plt.title('서울 -> 경기 인구 이동', size=30)
plt.xlabel('기간', size=20)
plt.ylabel('이동 인구수', size=20)

plt.legend(labels=['서울 -> 경기'], loc='best', fontsize=15)    # 범례 표시

plt.show()