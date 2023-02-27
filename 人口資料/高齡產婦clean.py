import pandas as pd

df=pd.read_excel("高齡產婦趨勢.xlsx")

usecols=["年份","出生人數","粗出生率","出生嬰兒性別比(女=100)","總生育率(人)","15~19歲婦女生育率","20~24歲婦女生育率","25~29歲婦女生育率","30~34歲婦女生育率","35~39歲婦女生育率","40~44歲婦女生育率","45~49歲婦女生育率"]

df=df.T
df=df.iloc[1:,:]
df.reset_index(inplace=True)
df.columns=usecols
# df.to_excel("高領產婦.xlsx",index=False)

# print(df)