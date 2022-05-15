import numpy as np
import pandas as pd

#
# s=pd.Series([1, 3, 5, np.nan,6,8])
# print(s)
#
s=pd.Series([10,12,18,14], index=['Ala','Marek','Wiesiek','Eleonora'])
print(s)

data={'Kraj':['Belgia','Indie','Brazylia'],
      'Stolica':['Bruksela','New Delhi','Brasilia'],
      'Populacja':[11190846,1303171035,207847528]}
df=pd.DataFrame(data)
print(df)
#
# print(df.dtypes)
#
# daty=pd.date_range('20210324',periods=5)
# print(daty)
#
# df=pd.DataFrame(np.random.randn(5,4),index=daty,columns=list('ABCD'))
# print(df)
# df=pd.read_csv('dane.csv', header=0, sep=';', decimal=',')
# print(df)
# df.to_csv('plik.csv',index=False)

# xlsx=pd.ExcelFile('imiona.xlsx')
# df=pd.read_excel(xlsx, header=0)
# print(df)

# print(s.Wiesiek)
#
# print(df[0:1])
#
# print(df.iloc[[1],[1]])
#
# print(df.loc[[0],['Stolica']])
#
# print('Kraj: '+df.Kraj)
#
# print(df.sample(2))
# print(df.sample(frac=0.5))
#
# print(df.sample(n=10, replace=True))
#
# print(df.head(2))
# print(df.tail(1))
#
# print(df.describe())


print(s[(s>12)])
print(s.where(s>12, 'za male'))