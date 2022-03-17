'''
titanic 데이터셋
'''

import seaborn as sns

# titanic 데이터셋 가져오기
titanic = sns.load_dataset('titanic')

# titanic 데이터셋 살펴보기
print(titanic.head(), '\n')
print(titanic.info())