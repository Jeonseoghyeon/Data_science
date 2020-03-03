#%%
import matplotlib
import pandas as pd
from itertools import combinations

A= 'Life expectancy at birth- years'
B = 'Internet users percentage of population 2014'
C = 'Forest area percentage of total land area 2012'
D =  'Carbon dioxide emissionsAverage annual growth'

a = [A,B,C,D]
df = pd.read_csv('data/world_indexes.csv',index_col = 0)
z = list(combinations(a,2))
for i in z:
    df.plot(kind='scatter',x=i[0],y=i[1])



# %%
