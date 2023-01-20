# -*- coding: utf-8 -*-
"""Internet Access Project Py.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eYCFprjCnD3iO_Q0-lmNLjCeRt5CCGAd
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#from google.colab import drive
#drive.mount(‘/content/drive’)

bd = pd.read_csv("broadband.csv")
idf = pd.read_csv("internet.csv")
p_df = pd.read_csv("people.csv")
classdf = pd.read_excel("CLASS.xlsx")

bd.head()

idf.head()

p_df.head()

classdf.head(5)

p_df.columns

idf.describe(include='all')

internetTop5 = idf[idf['Year']==2019]
internetTop5 = internetTop5.groupby('Entity')['Internet_Usage'].sum().sort_values(ascending = False)

internetTop5 = internetTop5.head(5)
internetTop5

"""2. How many people had internet access in those countries in 2019?"""

internet_access_2019 = p_df[p_df['Entity'].isin(internetTop5.index)]

internet_access_2019 = internet_access_2019[internet_access_2019['Year'] == 2019].sort_values(ascending=False,by='Users')

internet_access_2019.head(5)

sns.catplot(data=internet_access_2019,x="Entity",y='Users',kind='bar',size=8).set(ylabel="Internet Users",xlabel="Country",title="Number of Users in 2019")
plt.savefig("Top5bar.png", format="png", dpi=600)
plt.show()

classdf['Region'].unique()

"""The regions given are :- 'Middle East & North Africa', 'Latin America & Caribbean', 'East Asia & Pacific', 'South Asia', 'North America', 'Europe & Central Asia'

We have all the regions we need from the given class xlsx file.
"""

south_asia = list(classdf[classdf['Region'] == 'South Asia']['Economy'])
lAmerica_Caribbean = list(classdf[classdf['Region'] == 'Latin America & Caribbean']['Economy'])
europe_central_asia = list(classdf[classdf['Region'] == 'Europe & Central Asia']['Economy'])
east_asia_pacific = list(classdf[classdf['Region'] == 'East Asia & Pacific']['Economy'])
middle_east_north_africa = list(classdf[classdf['Region'] == 'Middle East & North Africa']['Economy'])
north_america = list(classdf[classdf['Region'] == 'North America']['Economy'])

print(south_asia,lAmerica_Caribbean,europe_central_asia,east_asia_pacific,middle_east_north_africa,north_america)

sa_i_a = idf[idf['Entity'].isin(south_asia)].groupby('Entity')
sa_i_ax = sa_i_a.apply(lambda x : x[x['Year']==2017])
print(sa_i_ax.sort_values(ascending=False,by='Internet_Usage')[['Entity','Internet_Usage']].reset_index(drop=True))
print(len(sa_i_ax))
top_5_sa = sa_i_ax.sort_values(ascending=False,by='Internet_Usage').head(5)
top_5_sa

mena = idf[idf['Entity'].isin(middle_east_north_africa)].groupby('Entity')
menax = mena.apply(lambda x : x[x['Year']==2017])
print(menax.sort_values(ascending=False,by='Internet_Usage')[['Entity','Internet_Usage']].reset_index(drop=True))
print(len(menax))
top_5_mena = menax.sort_values(ascending=False,by='Internet_Usage').head(5)
top_5_mena

lmc = idf[idf['Entity'].isin(lAmerica_Caribbean)].groupby('Entity')
lmcx = lmc.apply(lambda x : x[x['Year']==2017])
print(lmcx.sort_values(ascending=False,by='Internet_Usage')[['Entity','Internet_Usage']].reset_index(drop=True))
print(len(lmcx))
top_5_lmc = lmcx.sort_values(ascending=False,by='Internet_Usage').head(5)
top_5_lmc

eca = idf[idf['Entity'].isin(europe_central_asia)].groupby('Entity')
ecax = eca.apply(lambda x : x[x['Year']==2017])
print(ecax.sort_values(ascending=False,by='Internet_Usage')[['Entity','Internet_Usage']].reset_index(drop=True))
print(len(ecax))
top_5_eca = ecax.sort_values(ascending=False,by='Internet_Usage').head(5)
top_5_eca

eap = idf[idf['Entity'].isin(east_asia_pacific)].groupby('Entity')
eapx = eap.apply(lambda x : x[x['Year']==2017])
print(eapx.sort_values(ascending=False,by='Internet_Usage'))
print(len(eapx))
top_5_eap = eapx.sort_values(ascending=False,by='Internet_Usage').head(5)
top_5_eap

na = idf[idf['Entity'].isin(north_america)].groupby('Entity')
nax = na.apply(lambda x : x[x['Year']==2017])
print(nax.sort_values(ascending=False,by='Internet_Usage'))
print(len(nax))
top_5_na = nax.sort_values(ascending=False,by='Internet_Usage').head(5)
top_5_na

top5sa = idf[idf['Entity'].isin(top_5_sa['Entity'])]
top5mena = idf[idf['Entity'].isin(top_5_mena['Entity'])]
top5lmc = idf[idf['Entity'].isin(top_5_lmc['Entity'])]
top5eca = idf[idf['Entity'].isin(top_5_eca['Entity'])]
top5eap = idf[idf['Entity'].isin(top_5_eap['Entity'])]
top5na = idf[idf['Entity'].isin(top_5_na['Entity'])]

def drawMultiLineGraphTop5(data_r,regionName,palette='rocket'):
  fig, ax = plt.subplots(figsize=(12, 8 ))
  sns.set_palette(palette)
  sns.lineplot(x = "Year", y = "Internet_Usage", data = data_r, hue = "Entity", style = "Entity", dashes = False,  legend="brief",ax=ax).set(ylabel="Internet Usage",xlabel="Country",title="Top 5 Countries in Internet Usage in "+regionName)
  plt.savefig("Top5"+regionName+".png", format="png", dpi=600)
  plt.show()

drawMultiLineGraphTop5(top5sa,"South Asia")

drawMultiLineGraphTop5(top5mena,"Middle East and North Africa")

drawMultiLineGraphTop5(top5lmc,"Latin America and Caribbean")

drawMultiLineGraphTop5(top5eap,"East Asia & Pacific")

drawMultiLineGraphTop5(top5eca,"Europe & Central Asia")

drawMultiLineGraphTop5(top5na,"North America")

iT5 = pd.DataFrame(internetTop5.index,internetTop5).reset_index()
iT5

otherList = ['World', 'Asia', 'Upper-middle-income countries',  'High-income countries', 'Lower-middle-income countries', 'Europe', 'North America' , 'South America', 'Africa']
top5InternetUsers = p_df[(p_df['Year']==2020)]
top5InternetUsers = top5InternetUsers[~top5InternetUsers['Entity'].isin(otherList)]
top5InternetUsers = top5InternetUsers.groupby('Entity').agg(np.sum).sort_values(ascending=False,by="Users").head(5)
top5InternetUsers['Entity'] = top5InternetUsers.index
top5InternetUsers

sns.catplot(data=top5InternetUsers,x="Entity",y='Users',kind='bar',size=8).set(xlabel="Country",ylabel="Users",title="Top 5 Countries in Internet Usage (Population Share)")
plt.savefig("Top5Users.png", format="png", dpi=600)
plt.show()

mergeData = idf.merge(bd)
mergeData = mergeData[mergeData['Year']==2019]

x = mergeData['Internet_Usage']
y = mergeData['Broadband_Subscriptions']
print(round(x.corr(y),2))

sns.scatterplot(x,y).set(xlabel ="Internet Usage", ylabel = "Broadband Subscriptions", title ='Correlations between both')
plt.savefig("CorrelationWithoutLine.png", format="png", dpi=600)
plt.show()

sns.regplot(x,y).set(xlabel ="Internet Usage", ylabel = "Broadband Subscriptions", title ='Correlations between both')
plt.savefig("CorrelationWithLine.png", format="png", dpi=600)
plt.show()