'''
정수형 위치 인덱스로 초기화
'''

import pandas as pd

dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

df = pd.DataFrame(dict_data, index = ['r0', 'r1', 'r2'])

print(df, '\n')

# 행 인덱스를 정수형으로 초기화
ndf = df.reset_index()
print(ndf)