# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PlaystorescrapyItem(scrapy.Item):

    app_package_name = scrapy.Field()
    app_image_url = scrapy.Field()
    app_name = scrapy.Field()
    genre = scrapy.Field()
    price = scrapy.Field()
    price_type = scrapy.Field()
    author = scrapy.Field()
    author_play_store_company_url = scrapy.Field()    
    rating_value = scrapy.Field()
    review_number = scrapy.Field()
    updated = scrapy.Field()
    app_size = scrapy.Field()
    downloads = scrapy.Field()
    current_version = scrapy.Field()
    compatibility = scrapy.Field()
    content_rating = scrapy.Field()
    in_app_products = scrapy.Field()
    developer_website = scrapy.Field()
    developer_email = scrapy.Field()
    developer_address = scrapy.Field()
    description = scrapy.Field()

class PackagescrapyItem(scrapy.Item):
    package_name = scrapy.Field()
    ranking = scrapy.Field()
    playstore_ranking_country = scrapy.Field()
    app_url = scrapy.Field()