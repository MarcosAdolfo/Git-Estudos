import pandas as pd # Importando a biblioteca Pandas


#Criando o DataFrame
df = pd.DataFrame(
    {
        "a" : [4,5,0],
        "b" : [6,7,8],
        "c" : [5,6,2]
    }
    ,index=[1,2,3])

df

df1 = pd.DataFrame(
    [
        [4,5,0],
        [6,7,8],
        [5,6,2]
    ]
    ,index=[1,2,3], columns=['a','b','c'])

df1

#Importando um DataFrame
df2 = pd.read_csv('titanic_train.csv')

df2

df2.columns
df2['Name']
df2[df2["Sex"] == 'male']
df2[df2['Fare'] >= 50.0000]
df2[['Name','Sex','Age']]

#Métodos de Entendimento
df2.shape
df2['Sex'].value_counts()
df2['Sex'].value_counts(normalize=True)
