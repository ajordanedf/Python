# -*- coding: utf-8 -*-
import scrapy
import logging

class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['http://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries= response.xpath("//td/a")
        for country in countries: 
            name= country.xpath(".//text()").get()
            link= country.xpath(".//@href").get()

            yield response.follow(url=link, callback= self.parse_country, meta= {"nombre_pais": name})
    
    #Segunda página web
    def parse_country(self, response):
        rows= response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]")
        nombre= response.request.meta["nombre_pais"]
        for row in rows:
            year= row.xpath(".//tr/td[1]/text()").get()
            population= row.xpath(".//tr/td[2]/strong/text()").get()
            yield{
                "Nombre del pais": nombre,
                "Año": year,
                "Poblacion": population
            }


