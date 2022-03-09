'''
산점도
'''

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r'/Users/gungo/Documents/GitHub/Data_analsis/Pandas/part3_data/auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']

df.plot(x='weight', y='mpg', kind='scatter')

plt.show()