import pandas as pd


base = pd.read_csv('titanic_train.csv')
base.head()
base.info()
base = base.drop('Cabin',axis=1)
base.info()
base = base.dropna()
base.info()
base.dtypes.values
colunasDp = base.dtypes[base.dtypes.values == 'object'].index
base = base.drop(colunasDp, axis = 1)
base.info()

x = base.drop('Survived',axis=1)
y = base.Survived

from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors = 3)
neigh.fit(x, y)
neigh.score(x, y)

from sklearn import tree
clfArvore = tree.DecisionTreeClassifier()
clfArvore = clfArvore.fit(x, y)
clfArvore.score(x, y)

from sklearn.linear_model import LogisticRegression
clfLog = LogisticRegression(random_state=0,max_iter=1000).fit(x, y)
clfLog.score(x, y)
