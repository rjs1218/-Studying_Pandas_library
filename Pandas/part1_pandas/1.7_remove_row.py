'''
행 삭제
'''
import pandas as pd

exam_data = {'수학' : [90, 80, 70], '영어' : [98, 88, 78]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print('\n')

# 데이터프레임 df를 복제하여 df2에 저장. df2의 1개 행 삭제
df2 = df[:]
df2.drop('우현', inplace=True)
print(df2)
print('\n')

# 데이터프레임 df를 복제하여 df3에 저장. df3의 2개 행 삭제
df3 = df[:]
df3.drop(['우현', '인아'], axis=0, inplace=True) #  == df3 = df3.drop(['우현', '인아'])
print(df3)