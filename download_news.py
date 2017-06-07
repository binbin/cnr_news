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

socket.setdefaulttimeout(120)



# list_pattern=re.compile(r'{\'title\':\'.*?\'<!--VIDEOSTR-->\'}', re.S)
# content_search=re.compile(r'<div class="body" id="content_body">(.*?)</div>', re.S).search
# file_name_search=re.compile(r'\d{4}/\d{2}/\d{2}').search

# list_pattern=re.compile(r'<li><span class="left ml20">(.*?)</a>\n</span><span class="left ml20">2014-06-(?:19|20)', re.S)
list_pattern=re.compile(r'<li><span class="left ml20">(.*?)</a>', re.S)
list_get_title_search=re.compile(r'target="_blank">(.*)', re.S).search
list_get_link_search=re.compile(r'<a href="(.*?)" target="_blank">', re.S).search
content_search=re.compile(r'<!--content-->(.*?)<!--/content-->', re.S).search

# rc = re.compile(r'\\x(\w\w)')
# def chg(mo): return chr(string.atoi(mo.group(1),16))


class Conn(object):  
    def __init__(self):  
            self.headers = {  
                                        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
                                    }       
    def request(self, url, data={},times=0):  
           try:
                   postdata = urllib.urlencode(data)        
                   req = urllib2.Request(
                                                       url=url,
                                                       data=postdata,
                                                       headers=self.headers  
                                                       )  
                   req.get_method = lambda: 'GET'
                   link = urllib2.urlopen(req)  
                   result = link.read()  
                   link.close()  
                   return  result  
           except  Exception, e:         #处理超时、url不正确异常
                 if times <20:
                          print "conn error:%s"%e
                          print r'重新连接'
                          self.request(url, data,times+1)
                 else:
                          print r'重试超过20次,退出'
                          error_file_list.append(url)

def get_list(urls):
  c=Conn()
  result=[]
  for url in urls:
      list_page=c.request(url)
      # print list_page
      l=re.findall(list_pattern,list_page)
      # print l
      for i in l:
        # print urllib.unquote(i.replace("\\x","%"))
        # print i
        result.append({
              'link':list_get_link_search(i).group(1),
              'title':list_get_title_search(i).group(1)
          })
    # print '#'*100
  return result  
  # for i in l:
  #   result.append(eval(i))
  # return result[:count]


def createContent(lists,file_name):
  articles=[]
  for item in lists:
      c=Conn()
      page=c.request(item['link'])
      content=content_search(page).group(1)
      article="<h2>%s</h2><div>%s</div>"%(item["title"],content)
      # print item["title"].decode('gbk','ignore').encode('utf-8')
      articles.append(article)
  # b=file_name_search(list[0]["link_add"]).group(0).replace('/','')
  # e=file_name_search(list[-1]["link_add"]).group(0).replace('/','')
  # a=''.join(articles)
  # print a
  book_content=r'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"><html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh"><head><meta http-equiv="Content-Type" content="text/html;charset=UTF-8"><title> %s </title></head><body> %s </body></html>'%(file_name,''.join(articles).decode('gbk','ignore').encode('utf-8'))
  # f=open("%s-%s.html"%(b,e),'w')
  f=open("%s.html"%file_name,'w')
  f.write(book_content)
  f.close()
if __name__ == '__main__':
  start=time.time()
  print start
  print u'开始下载'
  urllist=['http://news.cnr.cn/comment/latest/']
  # for i in range(1,15):
  #   urllist.append('http://news.cnr.cn/comment/latest/index_%s.html'%i)
  print urllist
  lists=get_list(urllist)
  createContent(lists,u'央广观察_6.20')
  end=time.time()
  print u'全部下载完毕,共用时%s'%(end-start)
  #文章总数
  # count=200
  # #每本书中文章数
  # articlesOfBook=50

  # start=time.time()
  # lists=get_list('http://cctv.cntv.cn/lm/xinwenyijiayi/video/index.shtml',count)
  # books_nums= count/articlesOfBook
  # if count%articlesOfBook != 0:
  #     books_nums+=1
  # threads=[]
  # for i in range(0,books_nums):
  #     threads.append(threading.Thread(target=createContent,args=(lists[i*articlesOfBook:i*articlesOfBook+articlesOfBook],)))
  # for i in threads:
  #     i.start()
  # while reduce(lambda x,y:x or y,[ i.isAlive() for i in threads]):
  #     time.sleep(1)
  #     # print time.time()
  # end=time.time()
  # print end,start,end-start
  # print r'全部下载完毕,共用时%s'%(end-start)
  # print len(lists),books_nums