'''
박스 플롯
'''

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', family='AppleGothic')

plt.style.use('seaborn-poster')                    # 스타일 서식 지정
plt.rcParams['axes.unicode_minus'] = False         # 마이너스 부호 출력 설정

df = pd.read_csv(r'/Users/gungo/Documents/GitHub/Data_analsis/Pandas/part4_visualizationTool/auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower',
'weight', 'acceleration', 'model year', 'origin', 'name']

# 그래프 객체 생성(figure에 2개의 서브 플롯 생성)
fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# axe 객체에 boxplot 메소드로 그래프 출력
ax1.boxplot(x=[df[df['origin']==1]['mpg'],
                df[df['origin']==2]['mpg'],
                df[df['origin']==3]['mpg']], 
                labels=['USE', 'EU', 'JAPAN'])

ax2.boxplot(x=[df[df['origin']==1]['mpg'], 
                df[df['origin']==2]['mpg'], 
                df[df['origin']==3]['mpg']], 
                labels=['USE', 'EU', 'JAPAN'],
                vert=False)     # 수평 박스 플롯 옵션

ax1.set_title('제조국가별 연비 분포(수직 박스 플롯)')
ax2.set_title('제조국가별 연비 분포(수평 박스 플롯)')

plt.show()