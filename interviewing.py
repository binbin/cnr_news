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

list_pattern=re.compile(r'<a(.*?)style="font-size:14px;color:#07519A;">', re.S)
list_get_title_search=re.compile(r"title='(.*?)'", re.S).search
list_get_link_search=re.compile(r'href="(.*?)"', re.S).search
content_search=re.compile(r'id=sina_keyword_ad_area2>(.*?)<DIV class="articalList', re.S).search
content_search2=re.compile(r'id=sina_keyword_ad_area2>(.*?)</DIV>', re.S).search
content_search3=re.compile(r'id="read_tpc">(.*?)</td>', re.S).search

content_replace=re.compile(r">.*?陈建军.*?<", re.S)
content_replace_a=re.compile(r'<a.*?</a>',re.S)


# list_pattern=re.compile(r'<li><span class="left ml20">(.*?)</a>\n</span>', re.S)
# list_get_title_search=re.compile(r'target="_blank">(.*)', re.S).search
# list_get_link_search=re.compile(r'<a href="(.*?)" target="_blank">', re.S).search 
# content_search=re.compile(r'<!--content-->(.*?)<!--/content-->', re.S).search
# content_search=re.compile(r'(<div class=TRS_Editor>.*?纵横点评.*?</div>)', re.S).search

error_file_list=[]

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
              'link':'http://www.cjjms.net/%s'%list_get_link_search(i).group(1),
              'title':list_get_title_search(i).group(1)
          })
    # print '#'*100
  # print len(result)
  return result

def createContent(lists,file_name):
  articles=[]
  for item in lists:
      c=Conn()
      try:
          page=c.request(item['link']).decode('gbk','ignore').encode('utf-8')
          # print page
          # print page.decode('gbk','ignore').encode('utf-8')
          matche=content_search(page)
          if not matche:
            matche=content_search2(page)
          if not matche:
            matche=content_search3(page)
          if not matche:
            print 'not matche'
            print item['link']
            continue
          content=matche.group(1).decode('utf-8').encode('gbk')

          content=content_replace.sub('><',content)
          content=content_replace_a.sub('',content)

          article="<h3>%s</h3>%s"%(item["title"],content)
          articles.append(article)
      except Exception as e:
          print e

      
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
  urllist=[]
  for i in range(1,2):
     urllist.append('http://www.cjjms.net/list.php?fid=56&page=%s'%i)
  print urllist
  lists=get_list(urllist)
  createContent(lists,u'面试题2')
  end=time.time()
  print u'全部下载完毕,共用时%s'%(end-start)

# s=''' <!--content--><p>　　<font color="#993300"><strong>“我听过买房送家具、送汽车、送厨具……送老婆还是头一回听说。”</strong></font></p>
# <p>　　央广网北京6月29日消息 据中国之声《新闻纵横》报道，买房送老婆？您没听错！这是四川德阳一开发商打出的楼市灯箱广告。偌大的灯箱上赫然就写着五个大字：买房送老婆，旁边就是一位性感的美女图像。可是当惊讶的记者向开发商询问时，开发商却解释说：广告词的真正意思是：买房子送给自己的老婆。回过头再看，还真是，灯箱广告上，几个大字下面的确写着：爱老婆，就送她一个更舒适的家。只是这几个字小的真是可以忽视了。</p>
# <p>　　<strong>纵横点评：</strong>拿无聊当有趣，拿低俗当创新。自以为博得了眼球，却不知失了格调，侮辱了消费者，更污浊了眼睛。这样的房子，可能什么都能送，唯一送不了的就是家的温馨；这样的开发商，可能什么都不缺，唯一缺的，是智商。</p><!--/content-->'''


# content_search=re.compile(r'(<p>　　<strong>纵横点评：</strong>.*</p>)', re.S).search

# matche = content_search(s)
# if matche:
#     print matche.group(0)
# else:
#     print 'go on'