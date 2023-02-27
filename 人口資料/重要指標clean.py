import pandas as pd

usecols=["年份","總人口數","男性人口數","女性人口數","男女比(女=100)","人口增加率","自然增加率","社會增加率"]
usecols2=["總扶養比","幼扶養比","老扶養比","老化指數"]
df=pd.read_excel("人口重要指標.xlsx")
df2=df.copy()
df=df.iloc[:7,:]
df=df.T
df=df.iloc[1:,:]
df.reset_index(inplace=True)
df.columns=usecols
# print(df)

#扶養比資料
df2=df2.iloc[[13,14,15,17],:]
df2=df2.T
df2=df2.iloc[1:,:]
df2.reset_index(inplace=True)
df2=df2.iloc[:,1:]
df2.columns=usecols2
# print(df2)

dfall=pd.concat([df,df2],axis=1)
# dfall.to_excel("1960-2022人口重要指標.xlsx",index=False)