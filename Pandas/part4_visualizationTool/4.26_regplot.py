'''
회귀선이 있는 산점도
'''

import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

# 스타일 테마 설정(5가지 : darkgrid, whitegrid, dark, white, ticks)
sns.set_style('darkgrid')

fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# 그래프 그리기 - 선형회귀선 표시(fit_reg=True)
sns.regplot(x='age',
            y='fare',
            data=titanic,
            ax=ax1)

# 그래프 그리기 - 선형회귀선 미표시(fit_reg=False)
sns.regplot(x='age',
            y='fare',
            data=titanic,
            ax=ax2,
            fit_reg=False)      # 회귀선 미표시

plt.show()