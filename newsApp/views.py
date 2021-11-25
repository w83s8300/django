from django.shortcuts import render #資料混和網頁送出
from django.http import HttpResponse, request #直接將訊息傳回
from django.shortcuts import redirect #導入其它功能網址
from bs4 import BeautifulSoup
import requests
import pymysql
import datetime

def newsSearch (request):
    if request.method=="GET":
        return render(request,"newsApp/newsSearch.htm")
    else:
        keyword=request.POST.get('keyword')
        udn=request.POST.get('udn')
        kimo=request.POST.get('kimo')
        bbc=request.POST.get('bbc')
        if udn =='on':
            url="https://udn.com/search/word/2/{}".format(keyword)
            page=requests.get(url).text
            soup=BeautifulSoup(page,'lxml')
            title=soup.select("div.story-list__text h2 a")
            newsData=[]
            titles=[]
            links=[]
            for i in title:
                newsData.append({"titles":i.text,"links":i.get('href')})
            return render(request,"newsApp/newsList.htm",{"newsData":newsData})
        if kimo =='on':
            return HttpResponse("kimo")
        if bbc =='on':
            return HttpResponse("bbc")
        
