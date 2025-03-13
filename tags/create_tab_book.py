# coding=utf-8

import pickle
import urllib.request
import urllib.parse
import re
import time
import threading
import socket
import os
import json

socket.setdefaulttimeout(120)

error_file_list = []

content_search = re.compile(r'<!--content-->(.*?)<!--/content-->', re.S).search

class Conn(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
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
                result = link.read().decode('utf-8')
            return result
        except Exception as e:  # 处理超时、url不正确异常
            if times < 20:
                print("conn error: %s" % e)
                print(r'重新连接')
                return self.request(url, data, times + 1)
            else:
                print(r'重试超过20次,退出')
                error_file_list.append(url)

def createContent(lists, file_name):
    articles = []
    for l in lists:
        articles.append('<h2>%s</h2>' % ' '.join(l['tags']))
        for item in l['articles']:
            c = Conn()
            page = c.request(item['link'])
            content = content_search(page).group(1)
            article = "<h3>%s</h3><div>%s</div>" % (
                item["title"].encode('utf-8').decode('gbk', 'ignore'),
                content.encode('utf-8').decode('gbk', 'ignore')
            )
            articles.append(article)
    book_content = r'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"><html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh"><head><meta http-equiv="Content-Type" content="text/html;charset=UTF-8"><title> %s </title></head><body> %s </body></html>' % (
        file_name, ''.join(articles)
    )
    with open("%s.html" % file_name, 'w', encoding='utf-8') as f:
        f.write(book_content)

if __name__ == '__main__':
    start = time.time()
    print(start)
    print(u'开始下载')
    lists = pickle.load(open("tags_news.p", "r"))
    createContent(lists, u'央广观察_tag20240112版')
    end = time.time()
    print(u'全部下载完毕,共用时%s' % (end - start))