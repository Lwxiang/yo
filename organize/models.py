# -*- coding: utf-8 -*-
from django.db import models
from share.models import Comment

class DateInfo(models.Model):
    did = models.CharField(u'编号', max_length=4)
    dtype = models.CharField(u'类型', max_length=6)
    title = models.CharField(u'主题', max_length=30)
    content = models.CharField(u'详细内容', max_length=500)
    username = models.CharField(u'发起的用户', max_length=30)
    time = models.DateTimeField(u'发起时间', auto_now_add=True)
    last = models.DateTimeField(u'最近回复日期', auto_now=True)
    num = models.CharField(u'加入人数', max_length=4)
    joins = models.CharField(u'加入的人们', max_length=1000)
    jumpurl = models.URLField(u'跳转地址', max_length=30)
    belongs = models.URLField(u'属于哪篇分享', blank=True)
    start = models.DateTimeField(u'开始时间')
    end = models.DateTimeField(u'结束时间')
    comment = models.ManyToManyField(Comment)


