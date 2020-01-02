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
            link= country.xpath(".//@href").get()

            yield response.follow(url=link, callback= self.parse_country)
        
    def parse_country(self, response):
        rows= response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]")

        for row in rows:
            year= row.xpath(".//tr/td[1]/text()").get()
            population= row.xpath(".//tr/td[2]/strong/text()").get()
            yield{
                "Año": year,
                "Poblacion": population
            }


