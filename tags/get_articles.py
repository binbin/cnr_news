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
import jieba
import jieba.analyse

import pickle

socket.setdefaulttimeout(240)

list_pattern = re.compile(r'<li><span class="left ml20">(.*?)</a>', re.S)
list_get_title_search = re.compile(r'target="_blank">(.*)', re.S).search
list_get_link_search = re.compile(r'<a href="(.*?)" target="_blank">', re.S).search
content_search = re.compile(r'<!--content-->(.*?)<!--/content-->', re.S).search

re_h = re.compile('</?\w+[^>]*>').sub  # HTML标签
re_comment = re.compile('<!--[^>]*-->').sub  # HTML注释

error_file_list = []


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
                print("conn error:%s" % e)
                print(r'重新连接')
                return self.request(url, data, times + 1)
            else:
                print(r'重试超过20次,退出')
                error_file_list.append(url)
                return None


def get_list(urls):
    c = Conn()
    result = []
    for url in urls:
        list_page = c.request(url)
        if list_page is None:
            continue
        l = re.findall(list_pattern, list_page)
        for i in l:
            title = list_get_title_search(i).group(1)
            link = list_get_link_search(i).group(1)

            if link[:36] == r'http://www.cnr.cn/newscenter/comment':
                print('i:%s' % i)
                print('title:%s' % title)
                print('link:%s' % link)
                tags = get_tags(link, title)
                if tags is None:
                    continue
                result.append({
                    'link': link,
                    'title': title,
                    'tags': tags
                })
            else:
                print(link[:36])
    return result


def get_tags(link, title):
    print(link)
    c = Conn()
    page = c.request(link)

    if page is None:
        return None
    try:
        content = content_search(page).group(1)
        content = re_h(' ', content)
        content = re_comment(' ', content)
        tags = jieba.analyse.extract_tags(content, topK=10)
        print(title)
        print(tags)
        return tags
    except Exception as e:
        return None


if __name__ == '__main__':
    start = time.time()
    print(start)
    print(u'开始下载')
    urllist = ['http://news.cnr.cn/comment/latest/']
    for i in range(1, 15):
        urllist.append('http://news.cnr.cn/comment/latest/index_%s.html' % i)
    lists = get_list(urllist)
    pickle.dump(lists, open("news.p", "wb"))  # 使用二进制模式写入
    end = time.time()
    print(u'全部下载完毕,共用时%s' % (end - start))