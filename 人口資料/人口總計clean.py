import pandas as pd



df=pd.read_excel("男女不同歲數人口組成.xlsx")
resetcols=["年份","0~14歲人口數(人)","0~19歲人口數(人)","15~64歲人口數(人)","20~64歲人口數(人)","25~64歲人口數(人)","65歲以上人口數(人)","70歲以上人口數(人)","80歲以上人口數(人)","85歲以上人口數(人)"]


total=df.iloc[:9,1:]
total=total.T

total=total.iloc[1:,:]
total.reset_index(inplace=True)
total.columns=resetcols
# print(total)
#===========================================
men=df.iloc[18:27,:]
men=men.T
men=men.iloc[2:,:]
men.reset_index(inplace=True)
men.columns=resetcols
men["性別"]="男性"
# print(men)
#==========================================
women=df.iloc[36:45,:]
women=women.T
women=women.iloc[2:,:]
women.reset_index(inplace=True)
women.columns=resetcols
women["性別"]="女性"
# print(women)
#==========================================
# mandw=pd.DataFrame()
mandw=pd.concat([men,women],ignore_index=True)
# mandw.to_excel("男女人口個別.xlsx",index=False)
# total.to_excel("人口總計.xlsx",index=False)


