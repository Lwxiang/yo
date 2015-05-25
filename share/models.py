# -*- coding: utf-8 -*-
from django.db import models
from yo.settings import DEFAULT_TITLE_IMAGE

class Comment(models.Model):
    username = models.CharField(u'评论的用户', max_length=30)
    text = models.CharField(u'评论内容', max_length=500)
    time = models.DateTimeField(u'评论时间', auto_now_add=True)	

class ShareInfo(models.Model):
    title = models.CharField(u'标题', max_length=30)
    image = models.URLField(u'题图', default=DEFAULT_TITLE_IMAGE)
    sid = models.CharField(u'分享编号', max_length=4)
    stype = models.CharField(u'分享类型', max_length=6)
    author = models.CharField(u'作者', max_length=10)
    content = models.CharField(u'内容', max_length=1000)
    time = models.DateTimeField(u'发表日期', auto_now_add=True)
    last = models.DateTimeField(u'最近回复日期', auto_now=True)	
    jumpurl = models.URLField(u'跳转地址', max_length=30)
    comment = models.ManyToManyField(Comment)
    
