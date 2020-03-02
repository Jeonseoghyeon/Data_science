import pandas as pd

df = pd.read_csv('data/enrolment_1.csv')

# 코드를 작성하세요.
df['status'] = 'allowed'
condition1 = (df['year'] == 1) 
df.loc[condition1,'status'] == 'not allowed'
# 정답 출력
print(df)