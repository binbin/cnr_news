#coding=utf-8

import urllib2
import urllib
import re
import time
import threading
import socket
import os
import json


list_page=r'''</style>
						
							
							<div class="item url_http" style="clear: both;">
								<a href="https://www.cnr.cn/newscenter/comment/cnrp/20230327/t20230327_526197246.shtml" target="_blank">
									<span class="pic scale">
										 <img src="https://www.cnr.cn/newscenter/comment/cnrp/20230327/W020230327766395883073.jpg" width=160 height=120 border=0/>
									</span>
									<span class="text kuaixun">
										<strong>【央广网评】“以人为本”  警惕面子工程带偏“创城”</strong>
										<em>创建文明城市的核心要义在于提升市民的整体素质和城市的整体文明程度，文明城市就要以人为本，以人民为中心，创建文明城市的根本目的是提升人民的幸福感、获得感。如果违背了这一目的，而以争排名、争荣誉、搞面子工程为目的，就会出现种种偏差。</em>
									</span>
									<span class="publishTime">2023-03-27  21:17</span>
								</a>
							</div>
							
                        
							
							<div class="item url_http" style="clear: both;">
								<a href="https://www.cnr.cn/newscenter/comment/cnrp/20230327/t20230327_526197037.shtml" target="_blank">
									<span class="pic scale">
										 <img src="https://www.cnr.cn/newscenter/comment/cnrp/20230327/W020230327631815914753.jpg" width=160 height=120 border=0/>
									</span>
									<span class="text kuaixun">
										<strong>【央广网评】总决赛引全网关注  “村BA”为什么这么火？</strong>
										<em>“村BA”的出圈，让更多人看到了乡土间平凡人的精神世界。它既是人们茶余饭后自娱自乐的一项休闲活动，也是他们在平凡、忙碌的日常生活之中保有的一份热爱，追求的一种积极健康的生活方式，更是外出的游子对乡土的一份牵挂、对传统的一种继承。球赛背后的这些情感，正是“村BA”引发全网共鸣的原因所在。</em>
									</span>
									<span class="publishTime">2023-03-27  17:33</span>
								</a>
							</div>
							
                        
							
							<div class="ite'''

list_pattern=re.compile(r'<div class="item url_http" style="clear: both;">(.*?)</div>', re.S)
list_get_title_search=re.compile(r'<strong>(.*?)</strong>', re.S).search
list_get_link_search=re.compile(r'<a href="(.*?)"', re.S).search 


content_search=re.compile(r'(<div class="article-content">.*?</div>)', re.S).search


l=re.findall(list_pattern,list_page)
print 'list'
print l
for i in l:
    print urllib.unquote(i.replace("\\x","%"))
    print i
    print list_get_title_search(i).group(1)
    print list_get_link_search(i).group(1)
