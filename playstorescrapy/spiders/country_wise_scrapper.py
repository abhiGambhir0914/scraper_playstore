import scrapy
# import pandas as pd
import os
from ..items import PackagescrapyItem

path = '../output/India'
list_urls = ['file:///Users/abhigambhir/Desktop/Work/play_store_scrapy/playstorescrapy/output/India/' + f for f in os.listdir(path) if f.endswith('.html')]
print(list_urls)

class TrendDetailScrapper(scrapy.Spider):
    name = 'package_scrap'

    # allowed_domains = []
    start_urls = list_urls
    # start_urls = ['file:///Users/abhigambhir/Desktop/Work/play_store_scrapy/playstorescrapy/output/page_in_1.html']


    def parse(self, response):

        items = PackagescrapyItem()

        all_tr_elements = response.xpath('.//table[contains(@id,"rankings-table")]/tbody/*')

        # response.xpath('//td[contains(@class,"ranking-app-cell")]/a/@href').extract():

        for apps in response.xpath('.//table[contains(@id,"rankings-table")]/tbody/*'):

            package_name = apps.xpath('./td[contains(@class,"ranking-app-cell")]/a/@href').extract_first().split('/')[3]
            ranking = apps.xpath('./td[contains(@class, "ranking-rank")]/text()').extract_first()
            playstore_ranking_country = response.request.url.split('/')[-2]


            items['package_name'] = package_name
            items['ranking'] = ranking
            items['playstore_ranking_country'] = playstore_ranking_country

            # print(items)
            yield items
