# coding=utf-8

class UrlManager(object):
    def __init__(self):
        self.new_urls=set()                                           #新url集合
        self.old_urls=set()                                          #已经处理过得url集合

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:    #当前url既不在待处理集合也不在已处理集合
            self.new_urls.add(url)                                     #说明是新的url需要加入到集合中

    def add_new_urls(self, urls):                                      #当处理一个html文件时可能扫描出多个url链接
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)                                      #把批量的url集合分解单个的url来加入到待处理集合

    def has_new_url(self):
        return len(self.new_urls)!=0                                  #待处理url集合是否为空

    def get_new_url(self):                                            #取出待处理集合的第一个url来处理
        new_url=self.new_urls.pop()
        self.old_urls.add(new_url)                                     #同时把这个url加入到已处理集合中
        return new_url

