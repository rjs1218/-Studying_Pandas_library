'''
막대 그래프
'''
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel(r'/Users/gungo/Documents/GitHub/Data_analsis/Pandas/part3_data/남북한발전전력량.xlsx', engine='openpyxl')

df_ns = df.iloc[[0, 5], 3:]
df_ns.index = ['South', 'North']
df_ns.columns = df_ns.columns.map(int)

tdf_ns = df_ns.T
print(tdf_ns.head(), '\n')
tdf_ns.plot(kind='bar')

plt.show()