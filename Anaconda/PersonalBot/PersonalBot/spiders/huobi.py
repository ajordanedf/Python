# -*- coding: utf-8 -*-
import scrapy


class HuobiSpider(scrapy.Spider):
    name = 'huobi'
    allowed_domains = ['www.huobi.com']
    start_urls = ['http://https://www.huobi.com//']

    def parse(self, response):
        pass
