
# from django.contrib import admin
# from django.urls import path
from django.conf.urls import url
from msgboardAPP.views import *#讀取msgboardAPP裡的views.py

urlpatterns = [

 
#************ msgboardapp *************** 
    url(r'^memberIndex/$', memberIndex),
    url(r'^$',memberIndex),#網址的寫法 memberIndex是msgboardAPP裡的views.py 的函式
    url(r'^createMessge/$', createMessge),
    url(r'^receivedMessge/$', receivedMessge),
    url(r'^listGroupMsg/$', listGroupMsg),
    url(r'^updateMsg/$', updateMsg),
    url(r'^updateMsg/(\d+)/$', updateMsg),
    url(r'^deleteMsg/(\d+)/$', deleteMsg),

]