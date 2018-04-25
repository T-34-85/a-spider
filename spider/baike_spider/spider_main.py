# coding=utf-8
import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlManager()                              #spider类的每一个元素都是一个类
        self.downloader=html_downloader.HtmlDownloader()                #包括urls,downloader,parser,outputer类
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()

    def craw(self,root_url):                                            #启动爬虫
        count=1                                                         #记录当前爬取得是哪一个url
        self.urls.add_new_url(root_url)                                 #导入初始url
        while self.urls.has_new_url():                                 #循环检验有没有新的url
           try:
            new_url=self.urls.get_new_url()                             #取出待处理url集合中的第一个url
            print 'craw %d : %s ' % (count,new_url)
            html_cont=self.downloader.download(new_url)                 #下载新的url页面的html
            new_urls,new_data=self.parser.parse(new_url,html_cont)      #解析当前html文件并更新url
            self.urls.add_new_urls(new_urls)                            #获取新的url，为下一次while检测准备
            self.outputer.collect_data(new_data)                        #把当前页面数据放入页面收集器存储

            if count==1000:                                             #1000个页面时跳出
                break
            count=count+1
           except:
               print 'craw failed'
        self.outputer.output_html()                                     #输出搜集好的数据


if __name__=="__main__":
    root_url="https://baike.baidu.com/item/Python/407313"
    obj_spider=SpiderMain()                                             #爬虫入口
    obj_spider.craw(root_url)                                           #启动爬虫