# -*- coding: utf-8 -*-
import scrapy


class BitfinextSpider(scrapy.Spider):
    name = 'bitfinext'
    allowed_domains = ['https://www.bitfinex.com/']
    start_urls = ['http://https://www.bitfinex.com//']

    def parse(self, response):
        pass
