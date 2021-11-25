from django.shortcuts import render #資料混和網頁送出
from django.http import HttpResponse #直接將訊息傳回
from django.shortcuts import redirect #導入其它功能網址
import pymysql
import datetime

def memberIndex(request):
    return HttpResponse("首頁")#顯示文字

def updateMsg(request,id=""):
    if id=="":
        HttpResponse("")
    else:
        if request.method=="GET":
            db = pymysql.connect(host="127.0.0.1", user="user",passwd="user1234",database="mdu",charset='utf8')
            cursor = db.cursor() 
            sql=f"select *  from msgboard where id={id}"
            cursor.execute(sql)
            db.commit()
            data=cursor.fetchone()
            db.close()
            return render(request,'msgboardAPP/updataMsg.htm',{"data":data})
        elif request.method=="POST":
            #收資料
            title=request.POST['title'].strip()#讀取網頁title的資料
            content=request.POST['content'].strip()
            tag=request.POST['tag'].strip()
            author=request.POST['author'].strip()
            # 糾正資料
            db = pymysql.connect(host="127.0.0.1", user="user",passwd="user1234",database="mdu",charset='utf8')
            cursor = db.cursor() 
            sql='''update msgboard
                set title="{}", content="{}", tag="{}", author="{}" 
                where id={}'''.format(title,content,tag,author,id)

            cursor.execute(sql)
            db.commit()
            data=cursor.fetchone()
            db.close()


            return redirect('/listGroupMsg/')

def deleteMsg(request,id=""):
    db = pymysql.connect(host="127.0.0.1", user="user",passwd="user1234",database="mdu",charset='utf8')
    cursor = db.cursor() 
    sql=f"delete  from msgboard where id={id}"
    cursor.execute(sql)
    db.commit()
    data=cursor.fetchall()
    db.close()

    return HttpResponse("刪除成功，回到 <a href='/listGroupMsg/'>列表</a>")




def createMessge(request):
    return render(request,"msgboardapp/createMessge.htm")

def listGroupMsg(request):
    db = pymysql.connect(host="127.0.0.1", user="user",passwd="user1234",database="mdu",charset='utf8')
    cursor = db.cursor() 
    sql="select * from msgboard where seq=0"
    cursor.execute(sql)
    db.commit()
    data=cursor.fetchall()
    db.close()
    return render(request,'msgboardapp/listGroupMsg.htm',{'data':data})

    
def receivedMessge(request):
    if request.method == 'POST':
        #資料處理 
        #1. 收資料
        title=request.POST['title'] #讀取網頁title的資料
        if 'content' in request.POST:
            content=request.POST['content']
        else:
            content= 'None'
        tag=request.POST['tag']  
        title=request.POST['title']    
        author=request.POST['author']
        #2,資料計算或處理 3.資料庫存檔
        db = pymysql.connect(host="127.0.0.1", 
                        user="user",
                        passwd="user1234",
                        database="mdu")#連接資料庫
        cursor = db.cursor()#cursor是前置緩衝區
    # 決定mid的值
        sql="select mid from sys_parameter"
        cursor.execute(sql)
        db.commit()
        data=cursor.fetchone()
        if data == None:
            mid=1
            sql="insert into sys_parameter (mid) values (1)"
        else:
            mid=data[0]+1
            sql="update sys_parameter set mid={}".format(mid)
            
            
        cursor.execute(sql)
        db.commit()  
        postTime=datetime.datetime.now()
        postTime=str(postTime)[:19]
        sql="insert into msgboard (mid,seq,author,content,tag,time,title) values \
            ({},{},'{}','{}','{}','{}','{}')".format(mid,0,author,content,tag,postTime,title)
    
        cursor.execute(sql)
        db.commit()      
        return HttpResponse("已收到留言，請等待回覆 <p> <a href='/listGroupMsg/'>回留言</a>")

    #來自瀏覽器網址 request.method == 'GET':  
    else:
        return render(request,"msgboardapp/createMessge.htm")