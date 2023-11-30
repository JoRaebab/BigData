import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
# print(titanic.describe())
# print(titanic.head(10))
print(titanic['age'].fillna(titanic['age'].median(), inplace=True))
titanic['deck'] = titanic['deck'].cat.add_categories('Unknown')
titanic['deck'].fillna('Unknown', inplace=True)
titanic['embarked'].fillna('Unknown', inplace=True)
titanic['embark_town'].fillna('Unknown', inplace=True)
print(titanic.info())
