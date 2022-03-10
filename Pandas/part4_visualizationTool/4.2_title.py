'''
차트 제목, 축 이름 추가
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

# matplotlib 한글 폰트 오류 해결
rc('font', family='AppleGothic')

# 서울에서 경기도로 이동한 인구 데이터 값만 선택
sr_one = df_seoul.loc['경기도']
plt.plot(sr_one)

# 차트 제목 추가
plt.title('서울 -> 경기 인구 이동')

# 축 이름 추가
plt.xlabel('기간')
plt.ylabel('이동 인구수')

plt.show()