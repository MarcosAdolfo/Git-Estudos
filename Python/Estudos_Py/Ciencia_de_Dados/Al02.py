import pandas as pd

base = pd.read_csv('titanic_train.csv')
base.head(3)
base.tail(3)
base.shape

base.isnull().sum()
base.nunique()

import matplotlib.pyplot as plt
x = base.Fare
fig, ax = plt.subplots()
ax.hist(x, bins=10, linewidth=0.5, edgecolor="white")
plt.show()

x = base[base.Fare <= 100].Fare
fig, ax = plt.subplots()
ax.hist(x, bins=50, linewidth=0.5, edgecolor="white")
plt.show()

import pandas as pd
from pandas_profiling import ProfileReport
base = pd.read_csv('titanic_train.csv')
profile = ProfileReport(base, title="Pandas Profiling Report")
#profile #error 
profile.to_file("relatorio.html")
