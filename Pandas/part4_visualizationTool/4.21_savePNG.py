'''
그림 파일로 저장
'''

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')        # 스타일 서식 지정

df = pd.read_csv(r'/Users/gungo/Documents/GitHub/Data_analsis/Pandas/part4_visualizationTool/auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower',
'weight', 'acceleration', 'model year', 'origin', 'name']

# cylinders 개수의 상대적 비율을 계산하여 시리즈 생성
cylinders_size = df.cylinders/df.cylinders.max() * 300

# 3개의 변수로 산점도 그리기
df.plot(kind='scatter', x='weight', y='mpg', marker='+', figsize=(10, 5),
        cmap='viridis', c=cylinders_size, s=50, alpha=0.3)

plt.savefig("/Users/gungo/Documents/GitHub/Data_analsis/Pandas/part4_visualizationTool/scatter.png")
plt.savefig("/Users/gungo/Documents/GitHub/Data_analsis/Pandas/part4_visualizationTool/scatter_transparent.png", transparent=True)

plt.show()