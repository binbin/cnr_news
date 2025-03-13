# coding=utf-8

import urllib.request
import urllib.parse
import re
import time
import threading
import socket
import os
from datetime import datetime


list_pattern = re.compile(r'<div class="item url_http" style="clear: both;">(.*?)</div>', re.S)
list_get_link_search = re.compile(r'<a href="(.*?)"', re.S).search
list_get_title_search = re.compile(r'<strong>(.*?)</strong>', re.S).search
list_get_sub_title_search = re.compile(r'<em>(.*?)</em>', re.S).search
content_search=re.compile(r'(<div class="article-content">.*?</div>)', re.S).search

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
                result = link.read().decode('gbk', 'ignore').encode('utf-8')
            return result
        except Exception as e:  # 处理超时、url不正确异常
            if times < 20:
                print("conn error:%s" % e)
                print("重新连接")
                return self.request(url, data, times+1)
            else:
                print("重试超过20次,退出")
                error_file_list.append(url)

def get_list(urls):
    c = Conn()
    result = []
    for url in urls:
        list_page = c.request(url)
        if list_page is None:  # 添加错误检查
            continue
        list_page_str = list_page.decode('utf-8', 'ignore')
        l = re.findall(list_pattern, list_page_str)
        for i in l:
            try:
                result.append({
                    'link': list_get_link_search(i).group(1),
                    'title': list_get_title_search(i).group(1),
                    'sub_title': list_get_sub_title_search(i).group(1)
                })
            except (AttributeError, TypeError) as e:
                print(f"解析列表项时出错: {e}")
                continue
    return result

def createContent(lists, file_name):
    articles = []
    for item in lists:
        c = Conn()
        try:
            page = c.request(item['link'])
            if page is None:  # 添加错误检查
                continue
            page_str = page.decode('utf-8', 'ignore')  # 改用utf-8解码
            matche = content_search(page_str)  # 在字符串上使用正则
            if matche:
                print(f'下载中: {item["title"]}')
                content = matche.group(1)
                article = f"<div><h3>{item['title']}</h3><h4>{item['sub_title']}</h4>{content}</div>"
                articles.append(article)
            else:
                print('未找到内容')
        except Exception as e:
            print(f"处理文章时出错: {e}")
            continue

    book_content = f'''<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
    <title>{file_name}</title>
</head>
<body>
    {''.join(articles)}
</body>
</html>'''

    with open(f"{file_name}.html", 'w', encoding='utf-8') as f:
        f.write(book_content)

if __name__ == '__main__':
    start = time.time()
    print(start)
    print(u'开始下载')
    urllist = ['http://news.cnr.cn/comment/cnrp/']
    for i in range(1, 50):
        urllist.append('http://news.cnr.cn/comment/cnrp/index_%s.html' % i)
    lists = get_list(urllist)
    createContent(lists, u'央广网评%s' % datetime.now().strftime('%Y-%m-%d'))
    end = time.time()
    print(u'全部下载完毕,共用时%s' % (end-start))