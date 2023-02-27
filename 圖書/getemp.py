import requests as req
from bs4 import BeautifulSoup
import pandas as pd
import time

header={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

url="https://bid.twincn.com/c.aspx?sn=73278"
nreq=req.get(url,headers=header)
soup=BeautifulSoup(nreq.text,"html.parser")

tab=soup.select("table.table-striped")

j=tab[0].find_all("tr") #tr是每一列

alldf=pd.DataFrame()
for n in j[1:]:
    lis=n.select("td") #td是每一列的值
    for cou,i in enumerate(lis):
        if cou == 0:
            dat=int(str.strip(i.text)) #加上str.strip可以消掉前面的空白值
        elif cou == 1:
            emp=int(str.strip(i.text).replace(",", ""))
        elif cou == 2:
            oremp=int(str.strip(i.text))
        else:
            handicap=int(str.strip(i.text))
    data={"日期":dat,"人數":emp,"原住民":oremp,"身心障礙":handicap,"公司名稱":"龍騰文化"}
    tmpdf=pd.DataFrame(data,index=[0])
    alldf=pd.concat([alldf,tmpdf],ignore_index=True)

alldf.index+=1
alldf.to_excel("龍騰人數.xlsx",encoding="utf-8")
