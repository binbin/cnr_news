# coding=utf-8

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

# from html_minifier.minify import Minifier
# minifier = Minifier()

# list_pattern=re.compile(r'div class="text"(.*?)</a>', re.S)
# list_get_title_search=re.compile(r'target=_blank>(.*)', re.S).search
# list_get_link_search=re.compile(r'<a href="(.*?)" target=_blank>', re.S).search

list_pattern = re.compile(
    r'<div class="item url_http" style="clear: both;">(.*?)</div>', re.S)
list_get_title_search = re.compile(r'<strong>(.*?)</strong>', re.S).search
list_get_link_search = re.compile(r'<a href="(.*?)"', re.S).search
list_get_sub_title_search = re.compile(r'<em>(.*?)</em>', re.S).search


# content_search=re.compile(r'<!--content-->(.*?)<!--/content-->', re.S).search
# content_search=re.compile(r'(<div class=TRS_Editor>.*?纵横点评.*?</div>)', re.S).search
content_search = re.compile(
    r'(<div class="article-content">.*?</div>)', re.S).search

error_file_list = []

error_file_list = []


class Conn(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
        }

    def request(self, url, data={}, times=0):
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
            return result
        except Exception, e:  # 处理超时、url不正确异常
            if times < 20:
                print "conn error:%s" % e
                print r'重新连接'
                self.request(url, data, times+1)
            else:
                print r'重试超过20次,退出'
                error_file_list.append(url)


def get_list(urls):
    c = Conn()
    result = []
    for url in urls:
        # print url
        list_page = c.request(url)
        # print list_page
        l = re.findall(list_pattern, list_page)
        for i in l:
            result.append({
                'link': list_get_link_search(i).group(1),
                'title': list_get_title_search(i).group(1),
                'sub_title': list_get_sub_title_search(i).group(1)
            })
    # print len(result)
    return result


def createContent(lists, file_name):
    articles = []
    for item in lists:
        c = Conn()
        try:
            page = c.request(item['link']).decode(
                'gbk', 'ignore').encode('utf-8')
            matche = content_search(page)
            if matche:
                print '下载中,请稍后...'
                content = matche.group(1).decode('utf-8').encode('gbk')
                # print content.decode('utf-8').encode('gbk')
                article = "<div><h3>%s</h3><h4>%s</h4>%s</div>" % (item["title"], item["sub_title"], content.replace(
                    '<p style="text-align:center"><img src="https://mediabluk.cnr.cn/img/cnr/CNRCDP/2023/0327/74087a70cafa7167990984081848542410.jpg?auth=d616466058cc72f1c1d6157d45723ad1" style=";max-width:100%;height:auto;" /></p>', ''))
                # articles.insert(0, article)
                articles.append(article)
            else:
                print 'not matche'
        except Exception as e:
            print e

    book_content = r'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"><html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh"><head><meta http-equiv="Content-Type" content="text/html;charset=UTF-8"><title> %s </title></head><body> %s </body></html>' % (
        file_name, ''.join(articles).decode('gbk', 'ignore').encode('utf-8'))
    f = open("%s.html" % file_name, 'w')
    f.write(book_content)
    f.close()


if __name__ == '__main__':
    start = time.time()
    print start
    print u'开始下载'
    urllist = ['http://news.cnr.cn/comment/cnrp/']
    # for i in range(1,15):
    for i in range(1, 50):
        urllist.append('http://news.cnr.cn/comment/cnrp/index_%s.html' % i)
    # print urllist
    lists = get_list(urllist)
    createContent(lists, u'央广网评20230328')
    end = time.time()
    print u'全部下载完毕,共用时%s' % (end-start)

# s=''' <!--content--><p>　　<font color="#993300"><strong>“我听过买房送家具、送汽车、送厨具……送老婆还是头一回听说。”</strong></font></p>
# <p>　　央广网北京6月29日消息 据中国之声《新闻纵横》报道，买房送老婆？您没听错！这是四川德阳一开发商打出的楼市灯箱广告。偌大的灯箱上赫然就写着五个大字：买房送老婆，旁边就是一位性感的美女图像。可是当惊讶的记者向开发商询问时，开发商却解释说：广告词的真正意思是：买房子送给自己的老婆。回过头再看，还真是，灯箱广告上，几个大字下面的确写着：爱老婆，就送她一个更舒适的家。只是这几个字小的真是可以忽视了。</p>
# <p>　　<strong>纵横点评：</strong>拿无聊当有趣，拿低俗当创新。自以为博得了眼球，却不知失了格调，侮辱了消费者，更污浊了眼睛。这样的房子，可能什么都能送，唯一送不了的就是家的温馨；这样的开发商，可能什么都不缺，唯一缺的，是智商。</p><!--/content-->'''
