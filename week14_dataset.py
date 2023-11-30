"""
1)생존자와 사망자 수를 구하시오.
2)남성과 여성의 생존률을 비교하시오.
3) 객실 등급별 생존자 수를 구하시오.
4) 나이별 생존자 수를 구하시오.
5) 생존자와 사망자의 나이 분포를 시각화해보시오.
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

titanic = sns.load_dataset('titanic') #data loading
# print(titanic.describe())
#print(titanic.head(10))
#print(titanic.info())
titanic = titanic.drop(['who', 'deck', 'embark_town', 'alive', 'class', 'adult_male', 'alone'], axis=1) #column drop
titanic = titanic.dropna() #결측치가 있는 행 제거
# 수치 데이터가 아닌 feature를 숫자로 변환
titanic['sex'] = titanic['sex'].map({'male' : 0, 'female' : 1})
titanic['embarked'] = titanic['embarked'].map({'S' : 0, 'C' : 1, 'Q' : 2})
# 특성, 타겟 분리
X = titanic.drop('survived', axis=1)
y = titanic['survived']
# 훈련, 테스트 셋 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
# 모델 생성
model = LogisticRegression(solver='liblinear') #로지스틱 회귀 모델 적용
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f"정확도 : {accuracy_score(y_test, y_pred)}")



#1
survived_human = titanic[titanic['survived'] == 1]['survived'].count()
dead_human = titanic[titanic['survived'] == 0]['survived'].count()
#print(f"생존자 수 : {survived_human}명")
#print(f"사망자 수 : {dead_human}명")

#2
man_survived = titanic[(titanic['sex'] == 'male') & (titanic['survived'] == 1)]['survived'].count()
woman_survived = titanic[(titanic['sex'] == 'female') & (titanic['survived'] == 1)]['survived'].count()
man_count = titanic[(titanic['sex'] == 'male')]['sex'].count()
woman_count = titanic[(titanic['sex'] == 'female')]['sex'].count()
#print(man_survived, man_count, woman_survived, woman_count)
#print(man_survived/man_count, woman_survived/woman_count)

#3
pclass1_survived = titanic[(titanic['pclass'] == 1) & (titanic['survived'] == 1)]['survived'].count()
pclass2_survived = titanic[(titanic['pclass'] == 2) & (titanic['survived'] == 1)]['survived'].count()
pclass3_survived = titanic[(titanic['pclass'] == 3) & (titanic['survived'] == 1)]['survived'].count()
#pclass_survived = titanic.groupby('pclass')['survived'].sum()
#print(pclass_survived)

#4
age_survived = titanic.groupby(pd.cut(titanic['age'], bins=range(0, 81, 10)))['survived'].sum()
#print(age_survived)

#5
survived_ages = titanic[titanic['survived'] == 1]['age'].dropna() #나이에 nan값을 제거
dead_ages = titanic[titanic['survived'] == 0]['age'].dropna()
plt.hist(survived_ages, bins=20, label='Survived', alpha=0.5) #bin = 구간을 설정
plt.hist(dead_ages, bins=20, label='Dead', alpha=0.5)
plt.xlabel('Age')
plt.ylabel('Count')
#plt.legend()
#plt.show()

