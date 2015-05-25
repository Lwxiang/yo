# -*- coding: utf-8 -*-
import string

def make_url(action, jumptype, jumpid):
    jumpid = string.zfill(jumpid,4)
    jumpurl = '/%s/%s/%s/' % (action, jumptype, jumpid)
    return jumpurl
