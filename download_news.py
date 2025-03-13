#coding=utf-8

import urllib.request
import urllib.parse
import re
import time
import threading
import socket
import os
import json

import sys  

list_pattern = re.compile(r'<li><span class="left ml20">(.*?)</a>', re.S)
list_get_title_search = re.compile(r'target="_blank">(.*)', re.S).search
list_get_link_search = re.compile(r'<a href="(.*?)" target="_blank">', re.S).search
content_search = re.compile(r'<!--content-->(.*?)<!--/content-->', re.S).search

class Conn(object):  
    def __init__(self):  
            self.headers = {  
                                        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
                                    }       
    def request(self, url, data={}, times=0):
        try:
            postdata = urllib.parse.urlencode(data).encode('utf-8')
            req = urllib.request.Request(
                url=url,
                data=postdata,
                headers=self.headers
            )
            req.get_method = lambda: 'GET'
            with urllib.request.urlopen(req) as link:
                result = link.read()
                try:
                    decoded_result = result.decode('utf-8')
                except UnicodeDecodeError:
                    # Handle decoding error by using a different encoding
                    decoded_result = result.decode('gbk', 'ignore')
                return decoded_result
        except Exception as e:
            if times < 20:
                print("conn error: %s" % e)
                print("重新连接")
                return self.request(url, data, times + 1)
            else:
                print("重试超过20次,退出")
                error_file_list.append(url)

def get_list(urls):
    c = Conn()
    result = []
    for url in urls:
        list_page = c.request(url)
        l = re.findall(list_pattern, list_page)
        for i in l:
            result.append({
                'link': list_get_link_search(i).group(1),
                'title': list_get_title_search(i).group(1)
            })
    return result  

def createContent(lists, file_name):
    articles = []
    for item in lists:
        c = Conn()
        page = c.request(item['link'])
        content = content_search(page).group(1)
        article = "<h2>%s</h2><div>%s</div>" % (item["title"], content)
        articles.append(article)
    book_content = r'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"><html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh"><head><meta http-equiv="Content-Type" content="text/html;charset=UTF-8"><title> %s </title></head><body> %s </body></html>' % (file_name, ''.join(articles).encode('utf-8', 'replace').decode('utf-8'))
    with open("%s.html" % file_name, 'w', encoding='utf-8') as f:
        f.write(book_content)

if __name__ == '__main__':
    start = time.time()
    print(start)
    print(u'开始下载')
    urllist = ['http://news.cnr.cn/comment/latest/']
    print(urllist)
    lists = get_list(urllist)
    createContent(lists, u'央广观察_20240112')
    end = time.time()
    print(u'全部下载完毕,共用时%s' % (end - start))
