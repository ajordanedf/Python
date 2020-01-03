# -*- coding: utf-8 -*-
import scrapy


class OkexSpider(scrapy.Spider):
    name = 'okex'
    allowed_domains = ['www.okex.com']
    start_urls = ['https://www.okex.com']

    def parse(self, response):
        # btcprecio= response.xpath("//a[@id='exchange-recommendation-BTC-USDT']//div[@class='sc-9mpve0-13 dmflyC']/text()[3]").get()
        # btcvolumen= response.xpath("//div[3]//section[2]/div/div[1]/div[1]/text()").get()
        # yield{
        #     "BITFINEXT":"BITFINEXT",
        #     "BTC-Precio": "Todo",
        #     "BTC-Volumen" : btcvolumen
        # }
