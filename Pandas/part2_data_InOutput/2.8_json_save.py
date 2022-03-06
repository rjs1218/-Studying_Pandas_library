'''
JSON 파일로 저장
'''

import pandas as pd

data = {'name' : [ 'Jerry', 'Riah', 'Paul'],
        'algol' : [ "A", "A+", "B"],
        'basic' : [ "C", "B", "B+"],
        'c++' : [ "B+", "C", "C+"],
        }

df = pd.DataFrame(data)
df.set_index('name', inplace=True)
print(df)

# to_json() 메소드를 사용하여 JSON 파일로 내보내기.
df.to_json(r"/Users/gungo/Documents/Python/Pandas/part2_data_InOutput/df_sample.json")