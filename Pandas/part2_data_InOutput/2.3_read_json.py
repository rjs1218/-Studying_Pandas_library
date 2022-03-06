'''
JSON 파일 읽기
'''

import pandas as pd

file_path = '/Users/gungo/Documents/Python/Pandas/part2_data_InOutput/read_json_sample.json'

# read_json() 함수로 데이터프레임 변환
df = pd.read_json(file_path)

print(df, '\n')
print(df.index)