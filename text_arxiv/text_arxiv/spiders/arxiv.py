# -*- coding: utf-8 -*-
import scrapy
from text_arxiv.items import TextArxivItem

class ArxivSpider(scrapy.Spider):
    name = 'arxiv'
    allowed_domains = ['http://arxiv.org']
    start_urls = ['http://arxiv.org/']

    def parse(self, response):
        response.
        for target_list in expression_list:
            item = TextArxivItem()

            item.title = 
            item.abstract = 
            item.comments = 
            pass


        pass
