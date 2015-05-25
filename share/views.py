# -*- coding: utf-8 -*-
from share.models import *
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from yo.lib import make_url
from yo.settings import BASE_DIR
from organize.models import DateInfo

def Login(request):
    user = auth.authenticate(username = request.POST['username'], password = request.POST['password']) 
    callback = request.POST['callback']
    if user == None:   
	return HttpResponseRedirect(callback + '?ERROR=WrongPwd')
    auth.login(request,user)
    return HttpResponseRedirect(callback)

def Logout(request):
    auth.logout(request)
    return HttpResponseRedirect(request.POST['callback'])

def register_page(request):
    if (request.method == 'GET') and ('ERROR' in request.GET):
        if request.GET['ERROR'] == 'AlreadyExist':
            Error_AlreadyExist = True
        if request.GET['ERROR'] == 'NoMatch':
            Error_NoMatch = True
    return render_to_response('register.html',locals())

def register(request):
    try:  
        user = User.objects.get(username = request.POST['username'])  
    except User.DoesNotExist:  
        user = None
    if not (user == None):
	return HttpResponseRedirect('/register/?ERROR=AlreadyExist')
    if not (request.POST['password1'] == request.POST['password2']):
        return HttpResponseRedirect('/register/?ERROR=NoMatch')
    user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'], email=str(len(User.objects.all())+1))
    user.save()
    return HttpResponseRedirect('/index/?SUCCESS=RegisterDone')

def index(request):
    sharelist = ShareInfo.objects.all()
    datelist = DateInfo.objects.all()
    if datelist:
	lastdate = datelist[len(datelist)-1]
    if request.user.is_authenticated():
 	user = request.user
    if (request.method == 'GET') and ('ERROR' in request.GET):
        if request.GET['ERROR'] == 'LoginFirst':
            Error_LoginFirst = True
        if request.GET['ERROR'] == 'NoMatch':
            Error_NoMatch = True
    return render_to_response('index.html', locals())

def share_list(request, _type='dinner'):
    if request.user.is_authenticated():
 	user = request.user 
    sharelist = ShareInfo.objects.filter(stype=_type)
    stype = _type
    date_hot = DateInfo.objects.filter(dtype="dinner").order_by("-last")
    if len(date_hot)>=1:
	date_dinner = date_hot[0]
    date_hot = DateInfo.objects.filter(dtype="play").order_by("-last")
    if len(date_hot)>=1:
	date_play = date_hot[0]
    date_hot = DateInfo.objects.filter(dtype="movie").order_by("-last")
    if len(date_hot)>=1:
    	date_movie = date_hot[0]
    return render_to_response('sharelist.html', locals())

def edit_share(request):
    if request.user.is_authenticated():
 	user = request.user 
    else:
 	return HttpResponseRedirect('/index/?ERROR=LoginFirst')

    return render_to_response('editshare.html',locals())

def share(request):
    if request.user.is_authenticated():
 	user = request.user 
    else:
 	return HttpResponseRedirect('/index/?ERROR=LoginFirst')
    #添加信息
    shareinfo = ShareInfo()
    shareinfo.title = request.POST['title']
    shareinfo.sid = len(ShareInfo.objects.all()) + 1
    shareinfo.image = '/static/img/shareimg' + str(shareinfo.sid) + '.jpg'
    image_obj = request.FILES.get('image')	
    file_obj = open(BASE_DIR + shareinfo.image, 'wb+')
    file_obj.write(image_obj.read())
    file_obj.close()
    shareinfo.stype = request.POST['type']
    shareinfo.author = user.username
    shareinfo.content = request.POST['content']
    shareinfo.jumpurl = make_url('share', shareinfo.stype, shareinfo.sid)
    shareinfo.save()
    #跳到新建的分享页面
    return HttpResponseRedirect(shareinfo.jumpurl)

def share_page(request, _type='dinner', urlid='0001'):
    if request.user.is_authenticated():
 	user = request.user
    sid = int(urlid)
    try:
 	shareinfo = ShareInfo.objects.get(sid=sid)
    except ShareInfo.DoesNotExist:
	return HttpResponseRedirect('/index/')
    comment = shareinfo.comment.all()
    date_hot = DateInfo.objects.filter(dtype="dinner").order_by("-last")
    if len(date_hot)>=1:
	date_dinner = date_hot[0]
    date_hot = DateInfo.objects.filter(dtype="play").order_by("-last")
    if len(date_hot)>=1:
	date_play = date_hot[0]
    date_hot = DateInfo.objects.filter(dtype="movie").order_by("-last")
    if len(date_hot)>=1:
    	date_movie = date_hot[0]
    return render_to_response('sharepage.html',locals())

def make_comment_share(request):
    if request.user.is_authenticated():
 	user = request.user 
    else:
 	return HttpResponseRedirect('/index/?ERROR=LoginFirst')
    comment = Comment()
    comment.username = user.username
    comment.text = request.POST['text'].replace('\n','</br>').replace(' ','&npsb;')
    comment.save()
    shareinfo = ShareInfo.objects.get(sid = str(int(request.POST['sid'])))
    shareinfo.comment.add(comment)
    shareinfo.save()
    return HttpResponseRedirect(shareinfo.jumpurl)
    
    
