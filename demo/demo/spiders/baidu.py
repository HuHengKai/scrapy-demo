# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['https://icanhazip.com/']
    def parse(self, response):
        print("*" * 50)
        print(response.request.headers['User-Agent'])
        print(response.text)
        print("*"*50)

    #测试随机请求头
    # start_urls = ['http://httpbin.org/get']
    #
    # def parse(self, response):
    #     print("*" * 50)
    #     print(response.request.headers['User-Agent'])
    #     print("*"*50)
    #     pass
