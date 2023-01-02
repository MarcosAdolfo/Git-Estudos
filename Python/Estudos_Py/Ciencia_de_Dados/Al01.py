import pandas as pd


base = pd.read_csv('titanic_train.csv')
base.tail()
base.shape
print(base)

display(base)
base.dtypes
base.info()
base.isnull()
base.isnull().sum()

dados = {'X':[0,10,100]}
dados = pd.DataFrame(dados)
dados.mean()
dados.count()
dados.median()
dados.std()

dados.describe()

base.describe()
base['Survived']
base['Survived'].value_counts()
base[['Survived', 'Sex', 'Age']]

base.head()
base[base.Fare > 100]
base[(base.Fare < 100) & (base.Survived == 1)]

base.loc[(base.Fare < 100) & (base.Survived == 1),['PassengerId','Survived','Age','Fare']].head()
base.iloc[45:65]
base.iloc[40:60,0:5]

import matplotlib.pyplot as plt

base.Fare.hist(bins=50);

base.Pclass.plot.bar();
base.Pclass.value_counts().plot.bar();
