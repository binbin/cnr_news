#coding=utf-8

import pickle
import re

import sys



reload(sys) 
sys.setdefaultencoding('utf8')  


lists = pickle.load(open("news.p", "r"))

tags={}

#过滤出公用tags
ars=[]
for i in lists:
    for j in lists:
        if i is not j:
            h=set(i['tags'])&set(j['tags'])
            if len(h)>=4:
                ars.append(set(h))
                # print ' '.join()
#去重   
flist=[]            
for i in range(len(ars)):
    for j in range(i+1,len(ars)): 
        h= ars[i]&ars[j]
        if len(h)>=2:
               flist.append(ars[i])

print len(ars)
for i in flist:
    if i in ars:
       ars.remove(i)
for i in range(len(ars)):
    ars[i]={'tags':ars[i],'articles':[]}

print len(ars)
# for item in lists:
#   l+=item['tags']
for item in lists:
    times=0;index=0
    for i in range(len(ars)):
        t=len(set(item['tags'])&set(ars[i]['tags']))
        if t>times:
            times=t
            index=i
    if times>=2:
        ars[index]['articles'].append(item)
for i in ars:
    taglist=[x['tags'] for x in i['articles']]
    i['tags'] = reduce(lambda x,y:set(x)&set(y),taglist)
    if len(i['tags']) < 2:
        i['tags'] = reduce(lambda x,y:set(x)&set(y),taglist[:2])
    if len(i['tags']) < 2:
        i['tags'] = taglist[0]
#过滤重复文章        
for i in ars:
    titles=[];articles_new=[]
    for a in i['articles']:
        if a['title'] not in titles:
            titles.append(a['title'])
            articles_new.append(a)
    i['articles']=articles_new

pickle.dump(ars, open("tags_news.p", "w"))
# for i in ars:
#     print ' '.join(i['tags'])
#     for j in i['articles']:
#         print '    %s'%j['title']
# print len(l)


# for tag in l:
#   if tags.has_key(tag):
#       tags[tag]+=1
#   else:
#       tags[tag]=1
# lists=[]
# for k in tags:
#     lists.append((k,tags[k]))

# print len(lists)
# lists.sort(key=lambda x:x[1])

# for i in lists:
#   print "%s:%s"%i
  
    




# s='dfasf'
# re.m
# a=[u'测试',aaa]


