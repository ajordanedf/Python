# -*- coding: utf-8 -*-
import scrapy


class BinanceSpider(scrapy.Spider):
    name = 'binance'
    allowed_domains = ['www.binance.com']
    start_urls = ['https://www.binance.com/es/markets']

    def parse(self, response):
        btcprecio= response.xpath("//a[@id='exchange-recommendation-BTC-USDT']//div[@class='sc-9mpve0-13 dmflyC']/text()[3]").get()
        btcvolumen= response.xpath("//div[1]/div/a[2]/div/div[1]/div[2]/span/span/text()").get()
        yield{
            "BINANCE":"BINANCE",
            "BTC-Precio": btcprecio,
            "BTC-Volumen" : btcvolumen,
        }
    
