import scrapy
from bs4 import BeautifulSoup



class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    #   注释默认的parse函数
    #   def parse(self, response):
    #        pass


    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)
            # url 请求访问的网址
            # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    # 解析函数
    def parse(self, response):
        items = []
        soup = BeautifulSoup(response.text, 'html.parser')
        title_list = soup.find_all('div', attrs={'class': 'movie-hover-info'})
        print(title_list)
        for i in range(len(title_list)):
            # 在Python中应该这样写
            # for i in title_list:
            # 在items.py定义
            from week01.spiders.spiders.items import MaoyanItem
            item = MaoyanItem()
            item['name'] = title_list[i].find('span', attrs={'class': 'name'}).text

            for divs in title_list[i].find_all('div', attrs={'class': 'movie-hover-title'}):
                for spans in divs.find_all('span', attrs={'class': 'hover-tag'}):
                    if spans.text == '类型:':
                        spans.replace_with('')
                        item['type'] = divs.text.replace(' ', '').strip()
                    if spans.text == '上映时间:':
                        spans.replace_with('')
                        item['date'] = divs.text.replace(' ', '').strip()
                    items.append(item)
        print(items)
        return items
