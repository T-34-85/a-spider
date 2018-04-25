# coding=utf-8
import urllib2

class HtmlDownloader(object):

    def download(self,url):                        #接受一个url并把这个链接的html文件下载下来
        if url is None:
            return None

        response=urllib2.urlopen(url)               #获取http的响应报文

        if response.getcode()!=200:                 #响应报文code字段200表示成功获取
            return None

        return response.read()                     #返回响应报文内容，也就是html文档的内容

