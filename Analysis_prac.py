#%%
import matplotlib
import pandas as pd
import seaborn as sns
df = pd.read_csv('data/exam.csv',index_col = 0)
sns.heatmap(df.corr(),annot = True)

# %%
