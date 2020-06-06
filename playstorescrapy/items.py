# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PlaystorescrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class PackagescrapyItem(scrapy.Item):
    package_name = scrapy.Field()
    ranking = scrapy.Field()
    playstore_ranking_country = scrapy.Field()
    app_url = scrapy.Field()