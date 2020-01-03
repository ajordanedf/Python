# -*- coding: utf-8 -*-
import scrapy


class BinanceSpider(scrapy.Spider):
    name = 'binance'
    allowed_domains = ['https://www.binance.com/']
    start_urls = ['http://https://www.binance.com//']

    def parse(self, response):
        pass
