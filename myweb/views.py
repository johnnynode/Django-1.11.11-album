from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator

from myweb.models import Pic,Stu

from PIL import Image

import time,os

def index(request):
    #print("bbbbbbbbbbbbbbbbbbb")
    '''
    myob = Stu.objects.get(id=3)
    print(myob.name)
    myob.age = 22
    myob.save()
    '''
    #res = Stu.objects.raw('select name,age,classid from stu')
    #print(res[0])
    #return HttpResponse("aaaaaaaaaaaa:"+request.GET.get("m",""))
    return render(request,"myweb/index.html")

# 在线相册视图
def indexpic(request):
    # 执行数据查询，并放置到模板中
    list = Pic.objects.all()

    #list = Pic.objects.filter(id__lt=7)
    context = {"piclist":list}
    #return HttpResponse("ok")
    return render(request,"myweb/pic/index.html",context)

# 在线相册视图
def indexpic2(request,pIndex):
    # 执行数据查询，并放置到模板中
    list1 = Pic.objects.all()
    #创建分页对象
    p = Paginator(list1, 2)
    if pIndex == '':
        pIndex = '1'
    pIndex = int(pIndex)
    list2 = p.page(pIndex) #获取当前页信息
    plist = p.page_range #获取页列表信息

    #list = Pic.objects.filter(id__lt=7)
    context = {"piclist":list2,"plist":plist,"pIndex":pIndex}
    #return HttpResponse("ok")
    return render(request,"myweb/pic/index2.html",context)

def addpic(request):
    return render(request,"myweb/pic/add.html")

def insertpic(request):
    try:
        #print(request.FILES)
        upfile = request.FILES.get('mypic',None)
        print(upfile)
        #return HttpResponse("ok")
        if not upfile:
            return HttpResponse("没有上传的文件")
        #随机生成一个文件名
        filename = str(time.time())+"."+upfile.name.split('.').pop()
        ob = open("./static/pics/"+filename,"wb+")
        #ob.write(upfile.read()) # 一次性读写（适合小文件）
        for chunk in upfile.chunks(): # 分块写入文件  
            ob.write(chunk) 
        ob.close()

        # 执行图片缩放
        im = Image.open("./static/pics/"+filename)
        # 缩放到375*375:
        im.thumbnail((75, 75))
        # 把缩放后的图像用jpeg格式保存:
        im.save("./static/pics/s_"+filename,None)
        
        #添加图片水印
        # im = Image.open("./static/pics/"+filename)
        # logoim = Image.open("./static/pics/logo.png")
        # bw, bh = im.size
        # lw, lh = logoim.size
        # im.paste(logoim, (bw-lw, bh-lh))
        # im.save("./static/pics/"+filename,None) 

        #执行信息的添加
        ob = Pic()
        #ob.picinsert(request,filename)
        ob.name = request.POST['name']
        #ob.age = 20 #request.POST['age']
        ob.picname = filename
        # ob.addtime= time.time()
        ob.save()
        context = {'info':'添加成功！'}
    except Exception as err:
        context = {'info':err}
    return render(request,"myweb/pic/info.html",context)


def delpic(request,uid):
    try:
        ob = Pic.objects.get(id=uid)
        #执行图片删除
        os.remove("./static/pics/"+ob.picname)
        os.remove("./static/pics/s_"+ob.picname)
         
        #执行数据删除
        ob.delete()
        
        #重定向到浏览页
        return redirect(reverse('pic'))
        context = {'info':'删除成功！'}
    except:
        context = {'info':'删除失败！'}
    return render(request,"myweb/pic/info.html",context)


def editpic(request,uid):
    try:
        ob = Pic.objects.get(id=uid)
        context = {'pic':ob}
        #print(request.GET['name'])
        return render(request,"myweb/pic/edit.html",context)
    except:
        context = {'info':'没有找到要修改的信息！'}
        return render(request,"myweb/pic/info.html",context)

def updatepic(request):
    try:
        #获取原图片名
        oldpicname = request.POST['oldpicname']
        #判断是否有文件上传
        myfile = request.FILES.get("mypic",None)
        if not myfile:
            filename = oldpicname
        else:
            #执行上传处理
            filename = str(time.time())+"."+myfile.name.split('.').pop()
            destination = open("./static/pics/"+filename,"wb+")
            for chunk in myfile.chunks():      # 分块写入文件  
                destination.write(chunk)  
            destination.close()
            # 执行图片缩放
            im = Image.open("./static/pics/"+filename)
            # 缩放到375*375:
            im.thumbnail((75, 75))
            # 把缩放后的图像用jpeg格式保存:
            im.save("./static/pics/s_"+filename,None)

        ob = Pic.objects.get(id= request.POST['id'])
        ob.name = request.POST['name']
        #ob.age = request.POST.get('age',20)#request.POST['age']
        ob.picname = filename
        ob.save()
        context = {'info':'修改成功！'}
        # 判断删除老图片
        if myfile:
            os.remove("./static/pics/"+oldpicname)
            os.remove("./static/pics/s_"+oldpicname)
    except:
        context = {'info':'修改失败！'}
        #判断删除刚刚上传的图片
        if myfile:
            os.remove("./static/pics/"+picname)
            os.remove("./static/pics/s_"+picname)
    return render(request,"myweb/pic/info.html",context)