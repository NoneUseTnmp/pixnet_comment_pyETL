import requests
from bs4 import BeautifulSoup
import json
import os
import pandas as pd
import time
import random

columns=['名稱', '內容', '推','發文時間','店家名稱','作者給分','平均分數','評分人數']
data=[]

keywords = ['台北美食']
for keyword in keywords:
    print(f'---------{keyword}職位---------')
    
    for i in range(2):
        r=i+1
        url='https://www.pixnet.net/mainpage/api/tags/%E5%8F%B0%E5%8C%97%E7%BE%8E%E9%A3%9F/feeds?page={}&per_page=10&filter=comments&sort=latest&refer=https%3A%2F%2Fwww.pixnet.net%2Fblog%2Farticles%2Fcategory%2F26'.format(r)
        
        params={'page':r,'per_page':'10','filter':'comments','sort':'latest','refer':'https://www.pixnet.net/blog/articles/category/26'}
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
        ss=requests.session()
        try:
            res =ss.get(url=url , headers=headers , params=params)
        except IndexError as e:
            break
        js=json.loads(res.text)
        for n in range(0,9):
            name=js['data']['feeds'][n]['display_name']
            con=js['data']['feeds'][n]['description']
            push=js['data']['feeds'][n]['total_push']
            t = time.localtime(int(js['data']['feeds'][n]['created_at']))
            a=time.asctime(t)
            poi=js['data']['feeds'][n]['poi']
            if len(poi)!=0:
                sn=js['data']['feeds'][n]['poi']['name']
                memcerr=js['data']['feeds'][n]['poi']['member_rating']
                avgr=js['data']['feeds'][n]['poi']['rating']['avg']
                countr=js['data']['feeds'][n]['poi']['rating']['count']
            else:
                sn=None
                memcerr= None
                avgr=None
                countr=None
       
                
      
            
            rdata=[name,con,push,a,sn,memcerr,avgr,countr]
            data.append(rdata)
        
        time.sleep(random.randint(1,10))
        
df =pd.DataFrame(data=data,columns=columns)
df          
     
        
