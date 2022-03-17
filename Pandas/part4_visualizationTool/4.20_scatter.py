'''
산점도
'''

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')        # 스타일 서식 지정

df = pd.read_csv(r'/Users/gungo/Documents/GitHub/Data_analsis/Pandas/part4_visualizationTool/auto-mpg.csv', header = None)

# 열 이름 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower',
'weight', 'acceleration', 'model year', 'origin', 'name']

# 연비와 차중 열에 대한 선점도 그리기
df.plot(kind='scatter', x='weight', y='mpg', c='coral', s=10, figsize=(10, 5))
plt.title('Scatter Plot - mpg vs weight')
plt.show()