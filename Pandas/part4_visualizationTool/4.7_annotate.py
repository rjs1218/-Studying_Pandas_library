'''
그래프에 대한 설명을 덧붙이는 주석
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

# y축 범위 지정(최솟값, 최댓값)
plt.ylim(50000, 800000)

# 주석 표시 - 화살표
plt.annotate('',
            xy=(20, 620000),        # 화살표의 머리 부분(끝점)
            xytext=(2, 290000),     # 화살표의 꼬리 부분(시작점)
            xycoords='data',        # 좌표체계
            arrowprops=dict(arrowstyle='->', color='skyblue', lw=5),   # 화살표 서식
            )

plt.annotate('',
            xy=(47, 450000),        # 화살표의 머리 부분(끝점)
            xytext=(30, 580000),     # 화살표의 꼬리 부분(시작점)
            xycoords='data',        # 좌표체계
            arrowprops=dict(arrowstyle='->', color='olive', lw=5),   # 화살표 서식
            )

# 주석 표시 - 텍스트
plt.annotate('인구 이동 증가(1970-1995)',  # 텍스트 입력
            xy=(10, 350000),            # 텍스트 위치 기준점
            rotation=25,                # 텍스트 회전 각도
            va='baseline',              # 텍스트 상하 정렬
            ha ='center',               # 텍스트 좌우 정렬
            fontsize=15,                # 텍스트 크기
            )

plt.annotate('인구 이동 감소(1995-2017)',  # 텍스트 입력
            xy=(38, 500000),            # 텍스트 위치 기준점
            rotation=-11,                # 텍스트 회전 각도
            va='baseline',              # 텍스트 상하 정렬
            ha ='center',               # 텍스트 좌우 정렬
            fontsize=15,                # 텍스트 크기
            )            
plt.show()