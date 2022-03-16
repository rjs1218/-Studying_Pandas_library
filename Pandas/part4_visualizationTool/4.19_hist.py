'''
히스토그램
'''

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('classic')    # 스타일 서식 지정

df = pd.read_csv(r'/Users/gungo/Documents/GitHub/Data_analsis/Pandas/part4_visualizationTool/auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower',
'weight', 'acceleration', 'model year', 'origin', 'name']

# 연비(mpg) 열에 대한 히스토그램 그리기
df['mpg'].plot(kind='hist', bins=10, color='coral', figsize=(10, 5))

# 그래프 꾸미기
plt.title('Histogram')
plt.xlabel('mpg')
plt.show()