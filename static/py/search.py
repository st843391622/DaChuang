#!/usr/bin/env python
# encoding: utf-8
from static.py import pdftext


# 关键词查找并返回结果字符串
def parse(str):
    name = '1204740858'
    # pdftext.gettext(name)
    fp = open('static/data/'+name+'.txt', 'rt')
    inner = fp.read()
    key = inner.find(str)
    text = inner[key-30:key+len(str)+30]
    return text