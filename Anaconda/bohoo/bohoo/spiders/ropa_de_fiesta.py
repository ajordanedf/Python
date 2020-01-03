# -*- coding: utf-8 -*-
import scrapy


class RopaDeFiestaSpider(scrapy.Spider):
    name = 'ropa_de_fiesta'
    allowed_domains = ['es.boohoo.com']
    start_urls = ['https://es.boohoo.com/mujer/estilos/ropa-de-fiesta/']


    #xpath expresion --> //div[@class="search-result-content js-search-result-content"]//div

    def parse(self, response):
        for product in response.xpath("//div[@class='search-result-content js-search-result-content']//div"):
            yield{
                "Titulo" : product.xpath(".//div[1 and @class='product-tile-badge bottom-right']/span/text()").get(),
                "Url" : product.xpath(".//div[@class='product-image load-bg']/a/@href").get(),
                "Precio con descuento" : product.xpath(".//span[@class='product-sales-price']/text()").get(),
                "Precio sin descuento" : product.xpath(".//span[@class='product-standard-price']/text()").get()
            }

        siguiente_pagina= response.xpath("//li[@class='pagination-item pagination-item-next']/a/@href").get()

        if siguiente_pagina:
            print("________________________si______________________")
            yield scrapy.Request(url= siguiente_pagina, callback= self.parse)
