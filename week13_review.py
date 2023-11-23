import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')

# print(type(titanic))


print(titanic.isnull().sum())
# fillna함수는 nan값을 다른값으로 대입할수있게 함
# inplace = true는 불러온 데이터셋에 바로 수정하는 옵션
print(titanic['age'].fillna(titanic['age'].median(), inplace=True))
print(titanic.isnull().sum())
titanic['deck'] = titanic['deck'].cat.add_categories('Unknown')
titanic['deck'].fillna('Unknown', inplace=True)
# print(titanic.tail())
print(titanic['deck'])

# print(titanic.describe())
# print(titanic.info)
