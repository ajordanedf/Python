# -*- coding: utf-8 -*-
import scrapy


class OkexSpider(scrapy.Spider):
    name = 'okex'
    allowed_domains = ['https://www.okex.com/']
    start_urls = ['http://https://www.okex.com//']

    def parse(self, response):
        pass
