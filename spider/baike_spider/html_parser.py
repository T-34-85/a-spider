# coding=utf-8
import re
import urlparse

from bs4 import BeautifulSoup

#解析器，传入一个url和一个下载好的页面数据，解析出新的url列表和数据并返回
class HtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls=self._get_new_urls(page_url,soup)                              #检索这个页面的url链接
        new_data=self._get_new_data(page_url,soup)                              #
        return new_urls,new_data

    def _get_new_urls(self, page_url, soup):
        new_urls=set()                                                          #新的集合
        links=soup.find_all('a',href=re.compile(r"/item"))          #用正则表达式匹配找到的链接
        for link in links:
            new_url=link['href']
            new_full_url=urlparse.urljoin(page_url,new_url)           #拼接成一个完整的url
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):                          #获取当前url链接网页的我们需要的内容
         res_data={}
         res_data['url']=page_url

        # < dd class ="lemmaWgt-lemmaTitle-title" >< h1 > Python < / h1 >

         title_node=soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find('h1')
         res_data['title']=title_node.get_text()

         summary_node=soup.find('div',class_="lemma-summary")
         res_data['summary']=summary_node.get_text()
         return res_data

    
