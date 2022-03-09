'''
선 그래프 그리기
'''
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel(r'/Users/gungo/Documents/GitHub/Data_analsis/Pandas/part3_data/남북한발전전력량.xlsx', engine = 'openpyxl')

df_ns = df.iloc[[0, 5], 3:]             # 남한, 북한 발전량 합계 데이터만 추출
df_ns.index = ['South', 'North']        # 행 인덱스 변경
df_ns.columns = df_ns.columns.map(int)  # 열 이름의 자료형을 정수형으로 변경
print(df_ns.head(), '\n')

# 선 그래프 그리기
df_ns.plot()

# 행, 열 전치하여 다시 그리기
tdf_ns = df_ns.T
print(tdf_ns.head(), '\n')
tdf_ns.plot()

# !!!중요!!!
plt.show()      # 맥북은 왜 그런지 모르겠지만 이걸 적어야 그래프가 보임
