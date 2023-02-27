import pandas as pd
import io

#<民國轉西元?=========================

# df=pd.read_excel("龍騰.xlsx")


# dat=[]
# for i in df["公告日期"]:
#     k=str(int(i[:3])+1911)+i[3:]
#     dat.append(k)

# df["date"]=dat


# df=df.iloc[:,1:]

# df.to_excel("/proced/龍騰.xlsx",encoding="utf-8",index=False)

#============================
# df=pd.read_excel("originfile\公司人數\康軒人數.xlsx")
# df=df.iloc[:,1:]

# dat=[]
# for i in df["日期"]:
#     if len(str(i)) == 5:
#         k=str(int(str(i)[:3])+1911)+"/"+str(i)[3:]
#         dat.append(k)
#     if len(str(i)) == 4:
#         k=str(int(str(i)[:2])+1911)+"/"+str(i)[2:]
#         dat.append(k)

# df["date"]=dat
# df.to_excel("./proced/康軒人數.xlsx",encoding="utf-8",index=False)

#</民國轉西元>===============================

alldf=pd.DataFrame()
file=["全華","翰林","三民","南一","康軒","龍騰"]



for i in file:
    readdf=pd.read_excel("proced/"+str(i)+"人數.xlsx")
    alldf=pd.concat([alldf,readdf],ignore_index=True)
    


alldf.to_excel("all人數.xlsx",index=False)