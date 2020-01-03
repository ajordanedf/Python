# -*- coding: utf-8 -*-
import scrapy


class BitfinextSpider(scrapy.Spider):
    name = 'bitfinext'
    allowed_domains = ['www.bitfinex.com']
    start_urls = ['https://www.bitfinex.com']

    def parse(self, response):
        #btcprecio= response.xpath("//a[@id='exchange-recommendation-BTC-USDT']//div[@class='sc-9mpve0-13 dmflyC']/text()[3]").get()
        btcvolumen= response.xpath("//div[3]//section[2]/div/div[1]/div[1]/text()").get()
        yield{
            "BITFINEXT":"BITFINEXT",
            "BTC-Precio": "Todo",
            "BTC-Volumen" : btcvolumen
        }