'''
웹에서 표 정보 읽기
'''

import pandas as pd

url = '/Users/gungo/Documents/Python/Pandas/part2_data_InOutput/sample.html'

tables = pd.read_html(url)

# 표(table)의 개수 확인
print(len(tables), '\n')

for i in range(len(tables)):
    print("tables[%s]" % i)
    print(tables[i], '\n')


df = tables[1]

# 'name' 열을 인덱스로 지정
df.set_index(['name'], inplace=True)    # inplace=True 옵션을 안 넣으면 원본 객체를 수정하는 것이 아닌, 새로운 데이터프레임 객체를 반환함.
print(df)