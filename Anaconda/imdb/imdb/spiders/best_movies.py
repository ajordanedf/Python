# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3[@class='lister-item-header']//a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='nav']/div[@class='desc']"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield{
            "title" : response.xpath("//div[@class='title_wrapper']/h1[1]/text()").get(),
            "Año" : response.xpath("//span[@id='titleYear']/a/text()").get(),
            "Duracion" : response.xpath('normalize-space(//div[@class="subtext"]/time/text())').get(),
            "genero" : response.xpath("//div[@class='subtext']/a[1]/text()").get(),
            "rating" : response.xpath("//strong/span[@itemprop]/text()").get(),
            "Url-pelicula" : response.url
        }
