# -*- coding: utf-8 -*-
from organize.models import DateInfo
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from yo.lib import make_url
from yo.settings import DOMAIN
from share.models import Comment
import datetime

titles = {'dinner':'约饭约饭', 'play':'约玩约玩', 'movie':'约电影约电影'}

def organize_list(request, _type='dinner'):
    if request.user.is_authenticated():
 	user = request.user
    dtype = _type
    datelist = DateInfo.objects.filter(dtype=dtype)
    tips = titles[dtype]
    return render_to_response('datelist.html', locals())

def join_date(request):  
    if request.user.is_authenticated():
 	user = request.user 
    else:
 	return HttpResponseRedirect('/index/?ERROR=LoginFirst')
    joined = False
    dateinfo = DateInfo.objects.get(did=request.POST['did'])
    join_list = dateinfo.joins.split(',')
    j = -1
    for i in join_list:
  	    if i == user.email:
		joined = True
                j += 1
		break
    if joined:
	del join_list[j]
        dateinfo.joins = ','.join(join_list)
        dateinfo.num = str(int(dateinfo.num) - 1)
        dateinfo.save()
    else:
	if dateinfo.joins:
            dateinfo.joins += (',' + user.email)
	else:
	    dateinfo.joins = user.email
        dateinfo.num = str(int(dateinfo.num) + 1)
        dateinfo.save()
    return HttpResponseRedirect(dateinfo.jumpurl)

def organize_page(request, _type='dinner', urlid='0001'):
    did = int(urlid)
    stype = _type
    try:
 	dateinfo = DateInfo.objects.get(did=did)
    except DateInfo.DoesNotExist:
	return HttpResponseRedirect('/index/')
    joined = False
    if request.user.is_authenticated():
 	user = request.user
        join_list = dateinfo.joins.split(',')
	for i in join_list:
  	    if i == user.email:
		joined = True
		break
    comment = dateinfo.comment.all()
    date_hot = DateInfo.objects.filter(dtype="dinner").order_by("-last")
    if len(date_hot)>=1:
	date_dinner = date_hot[0]
    date_hot = DateInfo.objects.filter(dtype="play").order_by("-last")
    if len(date_hot)>=1:
	date_play = date_hot[0]
    date_hot = DateInfo.objects.filter(dtype="movie").order_by("-last")
    if len(date_hot)>=1:
    	date_movie = date_hot[0]
    return render_to_response('datepage.html', locals())

def edit_organize(request):
    if request.user.is_authenticated():
 	user = request.user 
    else:
 	return HttpResponseRedirect('/index/?ERROR=LoginFirst')
    if request.method == 'GET':
    	if 'type' in request.GET:
    	    stype = request.GET['type']
        if 'id' in request.GET:
            sid = request.GET['id']
            belongs = DOMAIN + make_url('share', stype, sid)
    return render_to_response('editdate.html', locals())
    
def organize(request):
    if request.user.is_authenticated():
 	user = request.user 
    else:
 	return HttpResponseRedirect('/index/?ERROR=LoginFirst')
    #添加信息
    dateinfo = DateInfo()
    dateinfo.did = len(DateInfo.objects.all()) + 1
    dateinfo.dtype = request.POST['type']
    dateinfo.title = request.POST['title']
    dateinfo.content = request.POST['content']
    dateinfo.username = request.user.username
    dateinfo.num = 1
    dateinfo.joins = request.user.email
    dateinfo.jumpurl = make_url('date', dateinfo.dtype, dateinfo.did)
    dateinfo.start = datetime.datetime(int(request.POST['year1']), int(request.POST['month1']), int(request.POST['day1']), int(request.POST['hour1']), int(request.POST['minute1']), 0, 0)
    dateinfo.end = datetime.datetime(int(request.POST['year2']), int(request.POST['month2']), int(request.POST['day2']), int(request.POST['hour2']), int(request.POST['minute2']), 0, 0)
    if 'belongs' in request.POST:
	dateinfo.belongs = request.POST['belongs']
    dateinfo.save()
    #跳到新建的约？页面
    return HttpResponseRedirect(dateinfo.jumpurl)

def make_comment_date(request):
    if request.user.is_authenticated():
 	user = request.user 
    else:
 	return HttpResponseRedirect('/index/?ERROR=LoginFirst')
    comment = Comment()
    comment.username = user.username
    comment.text = request.POST['text']
    comment.save()
    dateinfo = DateInfo.objects.get(did = str(int(request.POST['did'])))
    dateinfo.comment.add(comment)
    dateinfo.save()
    return HttpResponseRedirect(dateinfo.jumpurl)
    
