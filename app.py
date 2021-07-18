import requests
from bs4 import BeautifulSoup
import json
import os
import pandas as pd
import time
import random
from fake_useragent import UserAgent as ua

columns=['名稱', '內容', '推','發文時間','店家名稱','作者給分','平均分數','評分人數']
data=[]
none_page=0
mis_pag=[]
#st=[]
thrt=0

keywords = ['台北美食']
for keyword in keywords:
    print(f'---------{keyword}---------')
    
    for i in range(20):
        r=i+1
        url='https://www.pixnet.net/mainpage/api/tags/%E5%8F%B0%E5%8C%97%E7%BE%8E%E9%A3%9F/feeds?page={}&per_page=10&filter=comments&sort=latest&refer=https%3A%2F%2Fwww.pixnet.net%2Fblog%2Farticles%2Fcategory%2F26'.format(r)
        ua1=ua().random
        params={'page':r,'per_page':'10','filter':'comments','sort':'latest','refer':'https://www.pixnet.net/blog/articles/category/26'}
        headers = {'User-Agent':"".format(ua1)}
        ss=requests.session()
        try:
            res =ss.get(url=url , headers=headers , params=params)
        except IndexError as e:
            break
        js=json.loads(res.text)
        if len(js['data']['feeds']) !=0:
            
            
            for n in range(0,10):
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
        else:
            none_page+=1
            mis_pag.append(js['data']['page'])
        
        rtt=random.randint(1,5)
        time.sleep(rtt)
        print("page{} break {} s".format(r,rtt))
        
        thrt=thrt+rtt
        
        
print("none_page:{}".format(none_page))
print('total_break_time: {}s'.format(thrt))
print('total_page: {}'.format(r))
#print("each_break_time:{}".format(st))
print("missing_page:{}".format(mis_pag))
df =pd.DataFrame(data=data,columns=columns)
df          
     
        
