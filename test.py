#coding=utf-8

import urllib2
import urllib
import re
import time
import threading
import socket
import os
import json

import sys  
reload(sys)  
sys.setdefaultencoding('utf8')  


s="""<li><a href='/pinglun/n/2015/0301/c78779-26614969.html' target=_blank>人民日报评论员：从严治党锻造坚强领导核心</a> [<i>03月01日 08:27</i>]</li>
<li><a href='/pinglun/n/2015/0228/c78779-26614244.html' target=_blank>人民日报评论员：从严治党锻造坚强领导核心</a> [<i>02月28日 21:03</i>]</li>
<li><a href='/pinglun/n/2015/0228/c241140-26610110.html' target=_blank>人民日报评论员：依靠学习 走向未来</a> [<i>02月28日 08:20</i>]</li>
<li><a href='/pinglun/n/2015/0228/c78779-26609377.html' target=_blank>人民日报评论员：法治让国家治理迈向新境界</a> [<i>02月28日 07:15</i>]</li>
<li><a href='/pinglun/n/2015/0227/c78779-26608485.html' target=_blank>人民日报评论员：法治让国家治理迈向新境界</a> [<i>02月27日 20:08</i>]</li>
<li><a href='/pinglun/n/2015/0227/c78779-26603301.html' target=_blank>人民日报评论员：改革让中国道路越走越宽广</a> [<i>02月27日 07:12</i>]</li>
<li><a href='/pinglun/n/2015/0226/c78779-26602206.html' target=_blank>人民日报评论员：改革让中国道路越走越宽广</a> [<i>02月26日 20:32</i>]</li>
<li><a href='/pinglun/n/2015/0226/c78779-26597187.html' target=_blank>人民日报评论员：让全面小康激荡中国梦</a> [<i>02月26日 07:14</i>]</li>
<li><a href='/pinglun/n/2015/0225/c78779-26595970.html' target=_blank>人民日报评论员：让全面小康激荡中国梦</a> [<i>02月25日 20:01</i>]</li>
      </ul>"""
list_pattern=re.compile(r'<li>(.*?)<i>', re.S)
list_get_title_search=re.compile(r'target="?_blank"?>(.*)<', re.S).search
list_get_link_search=re.compile(r'<a href=\'(.*?)\' target="?_blank"?>', re.S).search

l=re.findall(list_pattern,s)
# for i in l:
# 	print i
# print list_get_title_search(s)

s1="""<a href='/pinglun/n/2015/0301/c78779-26614969.html' target=_blank>人民日报评论员：从严治党锻造坚强领导核心</a> ["""
print list_get_link_search(s1).group(1)
print list_get_title_search(s1).group(1)