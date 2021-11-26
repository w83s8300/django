from django.shortcuts import render #資料混和網頁送出
from django.http import HttpResponse #直接將訊息傳回
from django.shortcuts import redirect #導入其它功能網址
import pymysql
import datetime


# Create your views here.
def memberIndex(request):
        return render(request,"front_pageApp/memberIndex.htm")