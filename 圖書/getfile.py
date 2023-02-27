import requests as req
from bs4 import BeautifulSoup
import pandas as pd
import time

#如果要測試header,user-agent,ip可以用httpbin檢查(如果有輸入paramaters的話)


header={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

#===================================================
# url="https://bid.twincn.com/c.aspx?sn=73278"
# nreq=req.get(url,headers=header) 
# soup=BeautifulSoup(nreq.text,"html.parser")
# articles=soup.select("table")
# cols=articles[1].select("strong")[0:8]
# row=soup.find_all(class_="row")
#==================================================

alldf=pd.DataFrame()
for page in range(1,13):
    print(page)
    time.sleep(0.3)
    url="https://bid.twincn.com/c.aspx?sn=15373&page="+str(page) #改變sn=的代碼可以爬取不同公司的標案紀錄
    nreq=req.get(url,headers=header)
    soup=BeautifulSoup(nreq.text,"html.parser")
    row=soup.find_all(class_="row")
    for item in row[1:]:
        k=item.select("div.col-sm-auto")
        for n,i in enumerate(k):
            if n == 1:
                times=i.text
            elif n == 3:
                title=i.text
            elif n == 5:
                money=i.text
            elif n == 7:
                autrname=i.text

        data={"公告日期":times,"標案名稱":title,"決標金額":money,"機關名稱":autrname,"得標廠商":"康軒文教"}
        df=pd.DataFrame(data,index=[0])
        alldf=pd.concat([alldf,df],ignore_index=True)

alldf.index+=1


alldf.to_excel("康軒.xlsx",encoding="utf-8")