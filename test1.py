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

page="""

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<title>2015年5月26-29日广东省面试题 - 公务员面试题 - 陈建军面试工作室                                                   Powered By 陈建军面试工作室</title>
<link rel="stylesheet" type="text/css" href="http://www.cjjms.net/images/redzf/style.css">
<link rel="stylesheet" type="text/css" href="http://www.cjjms.net/images/redzf/css.css">
<meta http-equiv="Content-Type" content="text/html; charset=gb2312">
<meta name="keywords" content="">
<meta name="description" content="2015年5月26日广东省面试题(监狱系统)1、现在流行微博微信网络阅读，有人认为这可以更好增加知识面，及时了解时事动态，请问你怎么看？2、由于台风把乡村稻草房吹毁，现在上级政府要求给民众建房，并要求年底之前完工，请问落实此项工作的重点是什么？3、外来务工人..">
</head>
<SCRIPT LANGUAGE="JavaScript">
//屏蔽可忽略的js脚本错误
function killErr(){
	return true;
}
window.onerror=killErr;
</SCRIPT>

<SCRIPT LANGUAGE="JavaScript" src="http://www.cjjms.net/images/default/inc.js"></SCRIPT>
<SCRIPT LANGUAGE="JavaScript" src="http://www.cjjms.net/images/default/default.js"></SCRIPT>
<SCRIPT LANGUAGE="JavaScript" src="http://www.cjjms.net/images/default/swfobject.js"></SCRIPT>
<!--****************下拉菜单开始****************-->

<!--****************下拉菜单结束****************-->
<body>
<div class="warp">
<div class="header">
<div class="login ov">
<div class="logdl fl"><script language="JavaScript" src="http://www.cjjms.net/do/hack.php?hack=login&job=js&styletype=0"></script></div>
<div class="time fr">
<script language="JavaScript"> 
<!---
today=new Date();
var hours = today.getHours();
var minutes = today.getMinutes();
var seconds = today.getSeconds();
var timeValue = "<FONT COLOR='#ffffff'>" + ((hours >12) ? hours -12 :hours); timeValue += ((minutes < 10) ? "<BLINK><FONT COLOR='#ffffff'>:</FONT></BLINK>0" : "<BLINK><FONT COLOR='#ffffff'>:</FONT></BLINK>") + minutes+"</FONT></FONT>";
timeValue += (hours >= 12) ? " 下午 " : " 上午 ";
function initArray(){
this.length=initArray.arguments.length
for(var i=0;i<this.length;i++)
this[i+1]=initArray.arguments[i]  }
var d=new initArray("<font color='#ffffff'>星期日","<font color='#ffffff'>星期一","<font color='#ffffff'>星期二","<font color='#ffffff'>星期三","<font color='#ffffff'>星期四","<font color='#ffffff'>星期五","<font color='#ffffff'>星期六"); document.write("<font color='#ffffff'>",today.getYear(),"<font color='#ffffff'>年","<font color='#ffffff'>",today.getMonth()+1,"<font color='#ffffff'>月","<font color='#ffffff'>",today.getDate(),"<font color='#ffffff'>日 </FONT>",d[today.getDay()+1]," ",timeValue);  //-->
</script>
        <a class=top onClick="this.style.behavior='url(#default#homepage)';this.setHomePage('http://www.cjjms.net');" href="#">设为首页</a> <a class=top href="javascript:window.external.AddFavorite('http://www.cjjms.net','陈建军面试工作室')">加入收藏</a> 
</div>
</div>
<div class="htop ov">
<div class="logo fl"><img src="http://www.cjjms.net/images/redzf/logo.gif" /></div>
<div class="htopa fr"><a href='http://www.cjjms.net/bencandy.php?fid=53&id=5494' target=_blank><img src='http://www.cjjms.net/upload_files/label/1_20150529110550_nmee0.gif'  width='468'  height='60' border='0' /></a></div>
</div>
<div class="nav">
 
<font style="font-size:14px;line-height:180%;"> 
 <a href="" target="" style="color:;" ></a>    </font>        
<span><a href="http://www.cjjms.net/" target="" style="color:;" >首页</a></span>
<font style="font-size:14px;line-height:180%;"> 
 <a href="" target="" style="color:;" ></a>    </font>
        
<font style="font-size:14px;line-height:180%;"> 
 <a href="" target="" style="color:;" ></a>    </font>        
<span><a href="http://www.cjjms.net/list.php?fid=43" target="_blank" style="color:;" >招考信息</a></span>
<font style="font-size:14px;line-height:180%;"> 
 <a href="" target="" style="color:;" ></a>    </font>
        
<font style="font-size:14px;line-height:180%;"> 
 <a href="" target="" style="color:;" ></a>    </font>        
<span><a href="http://www.cjjms.net/list.php?fid=53" target="_blank" style="color:;" >培训信息</a></span>
<font style="font-size:14px;line-height:180%;"> 
 <a href="" target="" style="color:;" ></a>    </font>
        
<font style="font-size:14px;line-height:180%;"> 
 <a href="" target="" style="color:;" ></a>    </font>        
<span><a href="http://www.cjjms.net/list.php?fid=63" target="_blank" style="color:;" >面试辅导</a></span>
<font style="font-size:14px;line-height:180%;"> 
 <a href="" target="" style="color:;" ></a>    </font>
        
<font style="font-size:14px;line-height:180%;"> 
 <a href="" target="" style="color:;" ></a>    </font>        
<span><a href="http://www.cjjms.net/bbs" target="_blank" style="color:;" >交流论坛</a></span>
<font style="font-size:14px;line-height:180%;"> 
 <a href="" target="" style="color:;" ></a>    </font>
        
<font style="font-size:14px;line-height:180%;"> 
 <a href="" target="" style="color:;" ></a>    </font>        
<span><a href="http://www.cjjms.net/list.php?fid=62" target="_blank" style="color:;" >综合信息</a></span>
<font style="font-size:14px;line-height:180%;"> 
 <a href="" target="" style="color:;" ></a>    </font>
        
<font style="font-size:14px;line-height:180%;"> 
 <a href="" target="" style="color:;" ></a>    </font>        
<span><a href="http://www.cjjms.net/list.php?fid=67" target="_blank" style="color:;" >笔试辅导</a></span>
<font style="font-size:14px;line-height:180%;"> 
 <a href="" target="" style="color:;" ></a>    </font>
        
<font style="font-size:14px;line-height:180%;"> 
 <a href="" target="" style="color:;" ></a>    </font>        
<span><a href="http://www.cjjms.net/list.php?fid=69" target="_blank" style="color:;" >公选、遴选领导试题</a></span>
<font style="font-size:14px;line-height:180%;"> 
 <a href="" target="" style="color:;" ></a>    </font>
        
<font style="font-size:14px;line-height:180%;"> 
 <a href="" target="" style="color:;" ></a>    </font>        
<span><a href="http://www.cjjms.net/list.php?fid=59" target="_blank" style="color:;" >银行信用社面试题</a></span>
<font style="font-size:14px;line-height:180%;"> 
 <a href="" target="" style="color:;" ></a>    </font>
        
</div>
</div>

<div class="nav_guide">
 当前位置：<a href="http://www.cjjms.net/">陈建军面试工作室</a>  -&gt; <a  href='list.php?fid=55' class='guide_menu'>面试真题</a> -&gt; <a  href='list.php?fid=56' class='guide_menu'>公务员面试题</a> 
    </div>

<SCRIPT LANGUAGE="JavaScript">
<!--//目的是为了做风格方便
document.write('<div style="clear:both;"></div><div>');
//-->
</SCRIPT>


<!--
--> 
<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr> 
    <td style="padding-top:4px;"><SCRIPT LANGUAGE='JavaScript' src='http://www.cjjms.net/do/a_d_s.php?job=js&ad_id=show_topad'></SCRIPT></td>
  </tr>
</table>
<div class="MainTable MainDivTable">
  <div class="Main"> 
      <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center" class="dragTable" id="view_article">
        <tr> 
          <td class="head"> 
            <h3 class="L"></h3>
            <span class="TAG"><a editurl='http://www.cjjms.net/do/job.php?job=bencandy&fid=56&id=5545&act=do'>TOP</a></span> 
            <h3 class="R"></h3>
          </td>
        </tr>
        <tr> 
          <td class="middle"> 
            <div class="main_title">2015年5月26-29日广东省面试题</div>
            <div class="fit_title"></div>
            <div class="top_about"><a editurl='http://www.cjjms.net/do/job.php?job=bencandy&fid=56&id=5545&act=do'>2015-05-29 21:50:19</a>
                             来源:<a href="" target="_blank"></a> 
              作者: 【<a 
            href="javascript:doZoom(18)">大</a> <a 
            href="javascript:doZoom(14)">中</a> <a 
            href="javascript:doZoom(12)">小</a>】 浏览:<font id="hits">54</font>次 
              评论:<font id="commnetsnum">0</font>条 </div>
            <table class="content" width="100%" cellspacing="0" cellpadding="0" style='TABLE-LAYOUT: fixed;WORD-WRAP: break-word' align="center">
              <tr> 
                <td align="left" class="content_word" id="read_tpc"><font id="zoom" face="宋体"><span id="post1">
                  <div style="float:left;"></div>
                  <DIV class="articalContent   newfont_family" id=sina_keyword_ad_area2><FONT style="FONT-SIZE: 16px">2015年5月26日广东省面试题(监狱系统)<BR>1、现在流行微博微信网络阅读，有人认为这可以更好增加知识面，及时了解时事动态，请问你怎么看？<BR>2、由于台风把乡村稻草房吹毁，现在上级政府要求给民众建房，并要求年底之前完工，请问落实此项工作的重点是什么？<BR>3、外来务工人员的子女上学问题备受关注，政府为了出台相关政策需要前期展开调研，请问如何保障调研数据更加有效？<BR>4、某地乡村的旅游资源丰富，为此政府要求大力发展乡村旅游项目，但很多村民因为担心发展旅游人流量增加给他们生活带来压力，扰乱秩序，而不同意，请问你怎么做好沟通说服工作？
<P><FONT style="FONT-SIZE: 16px"><STRONG><FONT style="FONT-SIZE: 16px"><STRONG></STRONG></FONT>2015年5月27日广东省公务员面试题</STRONG></FONT></P>
<P><FONT style="FONT-SIZE: 16px">上午面试题<BR>1、关于学区房价高，教育资源分配不公怎么看。<BR>2、关于残疾人就业，县政府工作重点是什么?<BR>3、关于老年人事业发展状况调查?<BR>4、其他部门对我部门进行满意度调查，怎么沟通?</P>
<DIV><FONT style="FONT-SIZE: 16px"><FONT style="FONT-SIZE: 16px"></FONT>2015年5月29日广东省公务员面试题(地税部门)</FONT></DIV>
<DIV><FONT style="FONT-SIZE: 16px">1、为了节约水资源，有人倡导大幅度提高水价，你怎么看？<BR>2、由于教育资源的不公平，某地决定学校老师轮岗，在贯彻这一政策中，你认为有哪些重点？<BR>3、城市交通拥堵，为了了解交通拥堵的情况，你需要获得哪些方面的资料？从哪些渠道获得？<BR>4、目前，中小微企业有许多税收优惠政策，但你所在的地区仍有许多中小微企业表示优惠幅度不够，而且办事手续复杂，你作为税务部门，怎么和企业沟通？</FONT></DIV></FONT>
<P>&nbsp;</P></FONT></DIV>
<DIV class="articalList borderc">
<DIV class=listBg>
<DIV class=listTit><FONT style="FONT-SIZE: 15px">我的更多文章：</FONT></DIV>
<DIV class=chooseOk>
<UL>
<LI><LABEL><A href="http://blog.sina.com.cn/s/blog_4d4a50cc0102vp10.html" target=_blank><FONT style="FONT-SIZE: 15px" color=#800080>守擂成功谈面经</FONT></A></LABEL><SPAN><FONT style="FONT-SIZE: 15px">(2015-05-25 21:31:38)</FONT></SPAN></LI>
<LI><LABEL><A href="http://blog.sina.com.cn/s/blog_4d4a50cc0102vp0z.html" target=_blank><FONT style="FONT-SIZE: 15px" color=#800080>2015年5月25日广东省公务员面试题</FONT></A></LABEL><SPAN><FONT style="FONT-SIZE: 15px">(2015-05-25 21:25:14)</FONT></SPAN></LI>
<LI><LABEL><A href="http://blog.sina.com.cn/s/blog_4d4a50cc0102voys.html" target=_blank><FONT style="FONT-SIZE: 15px" color=#800080>2015年5月24日广东省公务员面试题(省直)</FONT></A><FONT style="FONT-SIZE: 15px" color=#800080><IMG class="SG_icon SG_icon18" title=此博文包含图片 height=15 src="http://simg.sinajs.cn/blog7style/images/common/sg_trans.gif" width=15 align=absMiddle></FONT></LABEL><SPAN><FONT style="FONT-SIZE: 15px">(2015-05-24 19:19:00)</FONT></SPAN></LI>
<LI><LABEL><A href="http://blog.sina.com.cn/s/blog_4d4a50cc0102vowp.html" target=_blank><FONT style="FONT-SIZE: 15px" color=#800080>成“公”应有法&nbsp;功夫必须下</FONT></A></LABEL><SPAN><FONT style="FONT-SIZE: 15px">(2015-05-23 13:26:52)</FONT></SPAN></LI>
<LI><LABEL><A href="http://blog.sina.com.cn/s/blog_4d4a50cc0102vowo.html" target=_blank><FONT style="FONT-SIZE: 15px" color=#800080>由七进三--功夫不负有心人</FONT></A></LABEL><SPAN><FONT style="FONT-SIZE: 15px">(2015-05-23 13:24:55)</FONT></SPAN></LI>
<LI><LABEL><A href="http://blog.sina.com.cn/s/blog_4d4a50cc0102vown.html" target=_blank><FONT style="FONT-SIZE: 15px" color=#800080>六人小组全通过&nbsp;总结面经供借鉴</FONT></A></LABEL><SPAN><FONT style="FONT-SIZE: 15px">(2015-05-23 13:22:37)</FONT></SPAN></LI>
<LI><LABEL><A href="http://blog.sina.com.cn/s/blog_4d4a50cc0102vowm.html" target=_blank><FONT style="FONT-SIZE: 15px" color=#800080>两次逆袭谈面经(15深考、广东省考）</FONT></A></LABEL><SPAN><FONT style="FONT-SIZE: 15px">(2015-05-23 13:18:47)</FONT></SPAN></LI>
<LI><LABEL><A href="http://blog.sina.com.cn/s/blog_4d4a50cc0102vowl.html" target=_blank><FONT style="FONT-SIZE: 15px" color=#800080>2015年5月23日广东省公务员面试题(省直)</FONT></A><FONT style="FONT-SIZE: 15px" color=#800080><IMG class="SG_icon SG_icon18" title=此博文包含图片 height=15 src="http://simg.sinajs.cn/blog7style/images/common/sg_trans.gif" width=15 align=absMiddle></FONT></LABEL><SPAN><FONT style="FONT-SIZE: 15px">(2015-05-23 13:07:09)</FONT></SPAN></LI>
<LI><LABEL><A href="http://blog.sina.com.cn/s/blog_4d4a50cc0102vouy.html" target=_blank><FONT style="FONT-SIZE: 15px" color=#800080>全场第一&nbsp;菜鸟逆袭&nbsp;感谢恩师</FONT></A><FONT style="FONT-SIZE: 15px" color=#800080><IMG class="SG_icon SG_icon18" title=此博文包含图片 height=15 src="http://simg.sinajs.cn/blog7style/images/common/sg_trans.gif" width=15 align=absMiddle></FONT></LABEL><SPAN><FONT style="FONT-SIZE: 15px">(2015-05-22 12:30:48)</FONT></SPAN></LI>
<LI><LABEL><A href="http://blog.sina.com.cn/s/blog_4d4a50cc0102vorv.html" target=_blank><FONT style="FONT-SIZE: 15px" color=#800080>坚持就是胜利，努力就能成功</FONT></A></LABEL><SPAN><FONT style="FONT-SIZE: 15px">(2015-05-21 10:38:51) </FONT></SPAN></LI></UL></DIV></DIV></DIV></span></font></td>
              </tr>
            </table>
            <!--//投票-->
            <table width="98%" border="0" cellspacing="0" cellpadding="0" style='TABLE-LAYOUT: fixed;WORD-WRAP: break-word;' align="center">
              <tr> 
                <td colspan="2" align="center">
                  
				  
				  
                    
                  
				  
				  
                  
                    <table border="0" cellspacing="25" cellpadding="15">
                    <tr> 
                      <td class="article_heart" align="left">您喜欢这篇文章就分享它吧 <br>
                      <div class="bdsharebuttonbox"><a class="bds_more" href="#" data-cmd="more"></a><a title="分享到QQ空间" class="bds_qzone" href="#" data-cmd="qzone"></a><a title="分享到新浪微博" class="bds_tsina" href="#" data-cmd="tsina"></a><a title="分享到腾讯微博" class="bds_tqq" href="#" data-cmd="tqq"></a><a title="分享到人人网" class="bds_renren" href="#" data-cmd="renren"></a><a title="分享到微信" class="bds_weixin" href="#" data-cmd="weixin"></a></div>
<script>window._bd_share_config={"common":{"bdSnsKey":{},"bdText":"","bdMini":"2","bdMiniList":false,"bdPic":"","bdStyle":"0","bdSize":"24"},"share":{},"image":{"viewList":["qzone","tsina","tqq","renren","weixin"],"viewText":"分享到：","viewSize":"24"},"selectShare":{"bdContainerClass":null,"bdSelectMiniList":["qzone","tsina","tqq","renren","weixin"]}};with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion='+~(-new Date()/36e5)];</script>
                      
                        <SCRIPT LANGUAGE="JavaScript">
<!--
document.write('<div id="article_heart"></div>');
document.write('<div style="display:none;"><iframe name="iframe_article_heart" id="iframe_article_heart" src="http://www.cjjms.net/do/job.php?job=heart&id=5545" width=0 height=0></iframe></div>');
document.write('<SCRIPT LANGUAGE="JavaScript" src="http://www.cjjms.net/images/default/cookie.js"><\/SCRIPT>');
function vote_heart(vt){
	if(getCookie('heart__'+'5545')){
		alert('^_^,你不是表过态了嘛?');
		return ;
	}
	setCookie('heart__'+'5545',1);
	window.open("http://www.cjjms.net/do/job.php?job=heart&id=5545&type=vote&Vtitle="+vt,"iframe_article_heart");
}
//-->
</SCRIPT>
                      </td>
                    </tr> </table>
                    
                 
                  <table width="99%" border="0" cellspacing="0" cellpadding="0" align="center" class="tag_username">
                    <tr> 
                      <td width="71%" align="left" class="Tags">Tags：</td>
                      <td align="right" width="29%">责任编辑：<a href="http://www.cjjms.net/member/homepage.php?uid=31" target="_blank">陈建军</a></td>
                    </tr>
                  </table>
                </td>
              </tr>
              <tr> 
                <td colspan="2" align="center" class="page" height="25"></td>
              </tr>
              <tr align="right"> 
                <td colspan="2" height="25"  > 
                  <SCRIPT LANGUAGE="JavaScript" src="http://www.cjjms.net/images/default/bencandy.js"></SCRIPT>
                  【<a 
            href="javascript:doZoom(18)">大</a> <a 
            href="javascript:doZoom(14)">中</a> <a 
            href="javascript:doZoom(12)">小</a>】【<a 
            href="javascript:doPrint()">打印</a>】 
                  <input type=hidden value=1 name="h1" id="h1">
                  【<a href="javascript:ft(1)" id="Maiweb1">繁体</a>】【<a href="http://www.cjjms.net/member/post.php?job=postnew&fid=56" target=_blank>投稿</a>】【<a href="http://www.cjjms.net/do/job.php?job=collect&fid=56&id=5545">收藏</a>】 
                  【<a href="http://www.cjjms.net/do/job.php?job=recommend&fid=56&id=5545" target=_blank>推荐</a>】【<a href="http://www.cjjms.net/do/job.php?job=report&fid=56&id=5545" target=_blank>举报</a>】【<a href="http://www.cjjms.net/do/comment.php?fid=56&id=5545" target=_blank>评论</a>】 
                  【<a 
            href="javascript:window.close()">关闭</a>】 【<a 
            href="javascript:window.close()"></a><a 
            href="#">返回顶部</a>】</td>               </tr
              ><tr class="nextpage"> 
                <td width="50%" align="left"><a href="bencandy.php?fid=56&id=5549" onclick="">上一篇</a>：<a href="bencandy.php?fid=56&id=5549" onclick="" title="2015年5月30日河北省直公务员考试面试题">2015年5月30日河北省直公务员考试..</a></td>
                <td width="50%" align="right" height="25"><a href="bencandy.php?fid=56&id=5543" onclick="">下一篇</a>：<a href="bencandy.php?fid=56&id=5543" onclick="" title="2015年5月25日广东省公务员面试题">2015年5月25日广东省公务员面试题</a></td>
              </tr>
            </table>
          </td>
        </tr>
        <tr> 
          <td class="foot"> 
            <h3 class="L"></h3>
            <h3 class="R"></h3>
          </td>
        </tr>
      </table>
      <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center" class="dragTable" id="view_article_bbs">
        
      </table>
      <!--
--> 
<table width="100%" border="0" cellspacing="0" cellpadding="0" class="dragTable" id="commentTable">
  <tr> 
    <td class="head"> 
      <h3 class="L"></h3>
      <span class="TAG">评论</span> 
      <h3 class="R"></h3>
    </td>
  </tr>
  <tr> 
    <td class="middle"> 
<SCRIPT LANGUAGE="JavaScript">
<!--
document.write('<span id="comment_show"><img alt="内容加载中,请稍候..." src="http://www.cjjms.net/images/default/ico_loading3.gif"></span>');
document.write('<div style="display:none;"><iframe src="http://www.cjjms.net/do/comment_ajax.php?fid=56&aid=5545&iframeID=comment_show" width=0 height=0 name="comment_show"></iframe></div>');
//-->
</SCRIPT>
      <table width="100%" border="0" cellspacing="0" cellpadding="0">
	  <form name="form_comment" id="form_comment" method="post" target="comment_show" action="http://www.cjjms.net/do/comment_ajax.php?fid=56&aid=5545&iframeID=comment_show">
        
		<tr style="display:" id="comment_username_tr"> 
          <td width="16%"><span class="L">帐　　号:</span></td>
            <td width="84%"><span class="R"> 
              <input type="text" name="username" id="comment_username" size="12">
              密码:
              <input type="password" name="password" id="comment_password" size="12">
              (<a href="http://www.cjjms.net/do/reg.php" target="_blank"><u>新用户注册</u></a>)</span></td>
        </tr>
        
        <tr style="display:none;" id="comment_yzimg_tr"> 
          <td width="16%"><span class="L">验 证 码:</span></td>
          <td width="84%"> 
              <input id="yzImgNum" type="text" name="yzimg" size="8">
            <img border="0" id="yz_Img" name="imageField" src="http://www.cjjms.net/do/yzimg.php"> 
          </td>
        </tr>
 
        <tr> 
          <td width="16%"><span class="L">表　　情:</span></td>
          <td width="84%"> 
            <style type="text/css">
<!--
.selected {filter:Alpha(opacity=100);border:1px solid #FF9900}
.unselected {filter:Alpha(opacity=50);border:1px solid #EDF8DD}
-->
</style>
<SCRIPT LANGUAGE="JavaScript">
 <!--
 var prevIcon;
function icon(num){
num.className="selected";
if(typeof(prevIcon)!="undefined"){
prevIcon.className="unselected";
}else{
document.all.firstface.className="unselected";
}
if(num.className=="unselected"){
num.className="selected";
}
prevIcon=num;
document.getElementById("commentface").value=num.childNodes(0).id ;
}
 //-->
 </SCRIPT>
            <table border=0 cellspacing=0 cellpadding=0>
              <tr> 
                <td class="selected" onClick="icon(this)" id="firstface" style="cursor:hand"><img src="http://www.cjjms.net/images/default/faceicon/1.gif" width="20" height="20" id="1"></td>
                
                <td class="unselected" onClick="icon(this)" style="cursor:hand"><img src="http://www.cjjms.net/images/default/faceicon/2.gif" width="20" height="20" id="2"></td>
                
                <td class="unselected" onClick="icon(this)" style="cursor:hand"><img src="http://www.cjjms.net/images/default/faceicon/3.gif" width="20" height="20" id="3"></td>
                
                <td class="unselected" onClick="icon(this)" style="cursor:hand"><img src="http://www.cjjms.net/images/default/faceicon/4.gif" width="20" height="20" id="4"></td>
                
                <td class="unselected" onClick="icon(this)" style="cursor:hand"><img src="http://www.cjjms.net/images/default/faceicon/5.gif" width="20" height="20" id="5"></td>
                
                <td class="unselected" onClick="icon(this)" style="cursor:hand"><img src="http://www.cjjms.net/images/default/faceicon/6.gif" width="20" height="20" id="6"></td>
                
                <td class="unselected" onClick="icon(this)" style="cursor:hand"><img src="http://www.cjjms.net/images/default/faceicon/7.gif" width="20" height="20" id="7"></td>
                
                <td class="unselected" onClick="icon(this)" style="cursor:hand"><img src="http://www.cjjms.net/images/default/faceicon/8.gif" width="20" height="20" id="8"></td>
                
                <td class="unselected" onClick="icon(this)" style="cursor:hand"><img src="http://www.cjjms.net/images/default/faceicon/9.gif" width="20" height="20" id="9"></td>
                
                <td class="unselected" onClick="icon(this)" style="cursor:hand"><img src="http://www.cjjms.net/images/default/faceicon/10.gif" width="20" height="20" id="10"></td>
                
                <td class="unselected" onClick="icon(this)" style="cursor:hand"><img src="http://www.cjjms.net/images/default/faceicon/11.gif" width="20" height="20" id="11"></td>
                
                <td class="unselected" onClick="icon(this)" style="cursor:hand"><img src="http://www.cjjms.net/images/default/faceicon/12.gif" width="20" height="20" id="12"></td>
                
                <td class="unselected" onClick="icon(this)" style="cursor:hand"><img src="http://www.cjjms.net/images/default/faceicon/13.gif" width="20" height="20" id="13"></td>
                
                <td class="unselected" onClick="icon(this)" style="cursor:hand"><img src="http://www.cjjms.net/images/default/faceicon/14.gif" width="20" height="20" id="14"></td>
                
                <td align="center" valign="top"> 
                  <input name="commentface" type="hidden" value="1">
                </td>
              </tr>
            </table>
          </td>
        </tr>
        <tr> 
          <td width="16%"><span class="L">内　　容:</span></td>
          <td width="84%"><span class="R"> 
              <textarea name="content" cols="50" rows="5" id="comment_content" onKeyDown="quickpost(event)"></textarea>
            </span></td>
        </tr>
        <tr> 
          <td width="16%"> 
<script language="JavaScript">
<!--
cnt = 0;
function quickpost(event){
	if((event.ctrlKey && event.keyCode == 13)||(event.altKey && event.keyCode == 83)){
		cnt++;
		if (cnt==1){
			post_comment();
		}else{
			alert('内容正在提交...');
		}
	}	
}
function post_comment(){
	if(document.getElementById("comment_yzimg_tr").style.display==''){
		if(document.getElementById("yzImgNum").value==''){
			alert('验证码不能为空!');
			return false;
		}
	}
	if(document.getElementById("comment_content").value==''){
		alert('内容不能为空!');
		return false;
	}
	document.getElementById("form_comment").submit();
	document.getElementById("comment_content").value='';
	if(document.getElementById("yzImgNum")!=null){
		document.getElementById("yzImgNum").value='';
		document.getElementById("yz_Img").src="http://www.cjjms.net/do/yzimg.php?"+Math.random();;
	}
	limitTime=parseInt('5');
	limitComment();
	
}
//-->
</script>
          </td>
            <td width="84%"><span class="R"> 
              <input type="button" id="comment_submit" onclick="post_comment()" name="Submit" value="提交" class="button">
              <input type="hidden" name="action" value="post">
              </span></td>
        </tr></form>
      </table>

    </td>
  </tr>
  <tr> 
    <td class="foot"> 
      <h3 class="L"></h3>
      <h3 class="R"></h3>
    </td>
  </tr>
</table>


    </div>
    <div class="Side"> 
      <table width="100%" border="0" cellspacing="0" cellpadding="0" class="dragTable" id="sonSortName">
        <tr> 
          <td class="head" height="19"> 
            <h3 class="L"></h3>
            <span class="TAG">相关栏目</span> 
            <h3 class="R"></h3>
          </td>
        </tr>
        <tr> 
          <td class="middle" align="left"> 
            <table width="98%" border="0"    cellspacing="5" cellpadding="5" align="center" style="margin:4px 0 4px 0;">
<!--
-->
<tr>

    <td><div style="margin:3px;background:#eee;border:1px solid #ccc;line-height:25px;text-align:center;"><a style="font-size:14px;" href="list.php?fid=68">综合面试题</a></div></td>
  
    <td><div style="margin:3px;background:#eee;border:1px solid #ccc;line-height:25px;text-align:center;"><a style="font-size:14px;" href="list.php?fid=60">警察面试真题</a></div></td>
  
  </tr>

<tr>

    <td><div style="margin:3px;background:#eee;border:1px solid #ccc;line-height:25px;text-align:center;"><a style="font-size:14px;" href="list.php?fid=56">公务员面试题</a></div></td>
  
    <td><div style="margin:3px;background:#eee;border:1px solid #ccc;line-height:25px;text-align:center;"><a style="font-size:14px;" href="list.php?fid=59">银行信用社面试题</a></div></td>
  
  </tr>

<tr>

    <td><div style="margin:3px;background:#eee;border:1px solid #ccc;line-height:25px;text-align:center;"><a style="font-size:14px;" href="list.php?fid=61">教师面试真题</a></div></td>
  
    <td><div style="margin:3px;background:#eee;border:1px solid #ccc;line-height:25px;text-align:center;"><a style="font-size:14px;" href="list.php?fid=57">事业单位面试真题</a></div></td>
  
  </tr>

<tr>

    <td><div style="margin:3px;background:#eee;border:1px solid #ccc;line-height:25px;text-align:center;"><a style="font-size:14px;" href="list.php?fid=69">公选遴选真题</a></div></td>
  
    <td><div style="margin:3px;background:#eee;border:1px solid #ccc;line-height:25px;text-align:center;"><a style="font-size:14px;" href="list.php?fid=70">村官选调生面试题</a></div></td>
  
  </tr>

<tr>

    <td><div style="margin:3px;background:#eee;border:1px solid #ccc;line-height:25px;text-align:center;"><a style="font-size:14px;" href="list.php?fid=77">烟草系统面试真题</a></div></td>
  
  </tr>

</table> </td>
        </tr>
        <tr> 
          <td class="foot"> 
            <h3 class="L"></h3>
            <h3 class="R"></h3>
          </td>
        </tr>
      </table>
      <table width="100%" border="0" cellspacing="0" cellpadding="0" >
        <tr> 
          <td style="padding-top:6px;" align="right"><SCRIPT LANGUAGE='JavaScript' src='http://www.cjjms.net/do/a_d_s.php?job=js&ad_id=show_right_top_picad'></SCRIPT></td>
        </tr>
      </table>
      <table width="100%" border="0" cellspacing="0" cellpadding="0" class="dragTable">
        <tr> 
          <td class="head"> 
            <h3 class="L"></h3>
            <span class="TAG">最新文章</span> 
            <h3 class="R"></h3>
          </td>
        </tr>
        <tr> 
          <td class="middle" align="left"> 
<SCRIPT LANGUAGE="JavaScript">
<!--
document.write('<span id="article_Newtopic"><img alt="内容加载中,请稍候..." src="http://www.cjjms.net/images/default/ico_loading3.gif"></span>');
document.write('<div style="display:none;"><iframe src="http://www.cjjms.net/do/jsarticle.php?fid=56&type=new&rows=5&leng=36&iframeID=article_Newtopic" width=0 height=0></iframe></div>');
//-->
</SCRIPT>
          </td>
        </tr>
        <tr> 
          <td class="foot"> 
            <h3 class="L"></h3>
            <h3 class="R"></h3>
          </td>
        </tr>
      </table>
      <table id="ListShowPic" width="100%" border="0" cellspacing="0" cellpadding="0" class="dragTable">
        <tr> 
          <td class="head"> 
            <h3 class="L"></h3>
            <span class="TAG">图片主题</span> 
            <h3 class="R"></h3>
          </td>
        </tr>
        <tr> 
          <td class="middle" align="left"> 
<SCRIPT LANGUAGE="JavaScript">
<!--
document.write('<span id="article_Pictopic"><img alt="内容加载中,请稍候..." src="http://www.cjjms.net/images/default/ico_loading3.gif"></span>');
document.write('<div style="display:none;"><iframe src="http://www.cjjms.net/do/jsarticle.php?fid=56&type=pic&rows=4&leng=22&iframeID=article_Pictopic" width=0 height=0></iframe></div>');
//-->
</SCRIPT>
          </td>
        </tr>
        <tr> 
          <td class="foot"> 
            <h3 class="L"></h3>
            <h3 class="R"></h3>
          </td>
        </tr>
      </table>
      <table width="100%" border="0" cellspacing="0" cellpadding="0" class="dragTable">
        <tr> 
          <td class="head"> 
            <h3 class="L"></h3>
            <span class="TAG">热门文章</span> 
            <h3 class="R"></h3>
          </td>
        </tr>
        <tr> 
          <td class="middle" align="left"> 
<SCRIPT LANGUAGE="JavaScript">
<!--
document.write('<span id="article_Hottopic"><img alt="内容加载中,请稍候..." src="http://www.cjjms.net/images/default/ico_loading3.gif"></span>');
document.write('<div style="display:none;"><iframe src="http://www.cjjms.net/do/jsarticle.php?fid=56&type=hot&rows=5&leng=36&iframeID=article_Hottopic" width=0 height=0></iframe></div>');
//-->
</SCRIPT>
          </td>
        </tr>
        <tr> 
          <td class="foot"> 
            <h3 class="L"></h3>
            <h3 class="R"></h3>
          </td>
        </tr>
      </table>
      <table width="100%" border="0" cellspacing="0" cellpadding="0" class="dragTable">
        <tr> 
          <td class="head"> 
            <h3 class="L"></h3>
            <span class="TAG">推荐文章</span> 
            <h3 class="R"></h3>
          </td>
        </tr>
        <tr> 
          <td class="middle" align="left"> 
<SCRIPT LANGUAGE="JavaScript">
<!--
document.write('<span id="article_Comtopic"><img alt="内容加载中,请稍候..." src="http://www.cjjms.net/images/default/ico_loading3.gif"></span>');
document.write('<div style="display:none;"><iframe src="http://www.cjjms.net/do/jsarticle.php?fid=56&type=com&rows=5&leng=36&iframeID=article_Comtopic" width=0 height=0></iframe></div>');
//-->
</SCRIPT>
          </td>
        </tr>
        <tr> 
          <td class="foot"> 
            <h3 class="L"></h3>
            <h3 class="R"></h3>
          </td>
        </tr>
      </table>
      <table width="100%" border="0" cellspacing="0" cellpadding="0" class="dragTable">
        <tr> 
          <td class="head"> 
            <h3 class="L"></h3>
            <span class="TAG">相关文章</span> 
            <h3 class="R"></h3>
          </td>
        </tr>
        <tr> 
          <td class="middle" align="left"> 
<SCRIPT LANGUAGE="JavaScript">
<!--
document.write('<span id="article_Liketopic"><img alt="内容加载中,请稍候..." src="http://www.cjjms.net/images/default/ico_loading3.gif"></span>');
document.write('<div style="display:none;"><iframe src="http://www.cjjms.net/do/jsarticle.php?fid=56&type=like&id=5545&rows=5&leng=36&iframeID=article_Liketopic" width=0 height=0></iframe></div>');
//-->
</SCRIPT>
          </td>
        </tr>
        <tr> 
          <td class="foot"> 
            <h3 class="L"></h3>
            <h3 class="R"></h3>
          </td>
        </tr>
      </table>
      <table width="100%" border="0" cellspacing="0" cellpadding="0" class="dragTable">
        <tr> 
          <td class="head"> 
            <h3 class="L"></h3>
            <span class="TAG">广告位</span> 
            <h3 class="R"></h3>
          </td>
        </tr>
        <tr> 
          <td class="middle" valign="top" align="left"> <SCRIPT LANGUAGE='JavaScript' src='http://www.cjjms.net/do/a_d_s.php?job=js&ad_id=article_show'></SCRIPT> 
          </td>
        </tr>
        <tr> 
          <td class="foot"> 
            <h3 class="L"></h3>
            <h3 class="R"></h3>
          </td>
        </tr>
      </table>
	  </div>
    </div>



<!--
-->
<!--- 营销模块改动部分  -->
<script language="javascript" type="text/javascript">document.write("<marquee height='2' width='2' scrollamount='5000' scrolldelay='5000'>");</script>友情链接：
<a href="http://www.cjjms.net/" target="_blank"><strong>陈建军</strong></a>&nbsp;
<a href="http://www.cjjms.net/" target="_blank"><strong>公务员面试</strong></a>&nbsp;
<script language="javascript" type="text/javascript">document.write("</marquee>");</script> 
<div id="bottom"></div>
<!--- 营销模块改动部分  -->
<div style="clear:both;"></div>
<div class="footer ad">
本站资料均由陈建军面试团队原创或整理转载请注明出处<script type="text/javascript">
var _bdhmProtocol = (("https:" == document.location.protocol) ? " https://" : " http://");
document.write(unescape("%3Cscript src='" + _bdhmProtocol + "hm.baidu.com/h.js%3Fde73ac18c63f587925f96a22f331edbe' type='text/javascript'%3E%3C/script%3E"));
</script>
<br>
      Copyright@http://www.cjjms.net all rights reserved <a href="http://www.miibeian.gov.cn" target="_blank">蜀ICP备06023138号</a> 
      <br>
      版权所有
      <a href="http://cjjms.net" target="_blank">陈建军面试工作室</a> 
      Code &copy; 2008-2016 <a href="http://cjjms.net/admin" target="_blank">管理入口</a><br><center><a href="http://webscan.360.cn/index/checkwebsite/url/www.cjjms.net"><img border="0" src="http://img.webscan.360.cn/status/pai/hash/5401ad0612d58dc297b2e9586d0fd916"/></a></center></br>
</div>
</div>
<SCRIPT LANGUAGE="JavaScript">
<!--//目的是为了做风格方便
document.write('</div>');
//-->
</SCRIPT>
<SCRIPT LANGUAGE="JavaScript">
<!--
clickEdit.init();
//-->
</SCRIPT><SCRIPT LANGUAGE="JavaScript" src="http://www.cjjms.net/do/count.php?fid=1"></SCRIPT>
<!--营销模块改动部分-->
<!--CNZZ站点统计-->
<div style="display:none"><script src='http://pw.cnzz.com/c.php?id=80373593' language='JavaScript' charset='gb2312'></script></div>
<!--CNZZ站点统计-->
</body>
</html>

<SCRIPT LANGUAGE='JavaScript' src='http://www.cjjms.net/do/job.php?job=updatehits&aid=5545'></SCRIPT>
"""

content_search=re.compile(r'sina_keyword_ad_area2>(.*?)<DIV class="articalList', re.S).search
matche=content_search(page)
print matche.group(1)#.decode('utf-8').encode('gbk')