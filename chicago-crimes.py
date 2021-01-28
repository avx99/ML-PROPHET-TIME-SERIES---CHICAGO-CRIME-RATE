import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# https://www.kaggle.com/currie32/crimes-in-chicago?select=Chicago_Crimes_2012_to_2017.csv
# https://www.kaggle.com/currie32/crimes-in-chicago?select=Chicago_Crimes_2008_to_2011.csv
# https://www.kaggle.com/currie32/crimes-in-chicago?select=Chicago_Crimes_2005_to_2007.csv
# https://www.kaggle.com/currie32/crimes-in-chicago?select=Chicago_Crimes_2004_to_2001.csv

df1 = pd.read_csv('Chicago_Crimes_2001_to_2004.csv',error_bad_lines= False,nrows=10000)
df2 = pd.read_csv('Chicago_Crimes_2005_to_2007.csv',error_bad_lines= False,nrows=10000)
df3 = pd.read_csv('Chicago_Crimes_2008_to_2011.csv',error_bad_lines= False,nrows=10000)
df4 = pd.read_csv('Chicago_Crimes_2012_to_2017.csv',error_bad_lines= False,nrows=10000)
# sns.pairplot(df)
# shape of df = (7941282, 23)
df = pd.concat([df1,df2,df3,df4])

plt.figure(figsize=(10,10))
sns.heatmap(df.isnull(), cbar=False,cmap='YlGnBu')

df.drop(['Unnamed: 0','IUCR','Case Number','ID','X Coordinate','Y Coordinate','Updated On','Year','FBI Code','Beat','Ward','Community Area','Location','District','Longitude','Latitude'],inplace = True,axis=1)

df.Date = pd.to_datetime(df.Date,format='%m/%d/%Y %I:%M:%S %p') 
