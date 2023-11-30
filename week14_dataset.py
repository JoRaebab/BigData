"""
1)생존자와 사망자 수를 구하시오.
2)남성과 여성의 생존률을 비교하시오.
3) 객실 등급별 생존자 수를 구하시오.
4) 나이별 생존자 수를 구하시오.
"""
import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
# print(titanic.describe())
#print(titanic.head(10))
#print(titanic.info())

#1
survived_human = titanic[titanic['survived'] == 1]['survived'].count()
dead_human = titanic[titanic['survived'] == 0]['survived'].count()
print(f"생존자 수 : {survived_human}명")
print(f"사망자 수 : {dead_human}명")

#2
man_survived = titanic[(titanic['sex'] == 'male') & (titanic['survived'] == 1)]['survived'].count()
woman_survived = titanic[(titanic['sex'] == 'female') & (titanic['survived'] == 1)]['survived'].count()
man_count = titanic[(titanic['sex'] == 'male')]['sex'].count()
woman_count = titanic[(titanic['sex'] == 'female')]['sex'].count()
print(man_survived, man_count, woman_survived, woman_count)
print(man_survived/man_count, woman_survived/woman_count)

#3
pclass1_survived = titanic[(titanic['pclass'] == 1) & (titanic['survived'] == 1)]['survived'].count()
pclass2_survived = titanic[(titanic['pclass'] == 2) & (titanic['survived'] == 1)]['survived'].count()
pclass3_survived = titanic[(titanic['pclass'] == 3) & (titanic['survived'] == 1)]['survived'].count()
pclass_survived = titanic.groupby('pclass')['survived'].sum()
print(pclass_survived)

#4
age_survived = titanic.groupby(pd.cut(titanic['age'], bins=range(0, 81, 10)))['survived'].sum()
print(age_survived)
