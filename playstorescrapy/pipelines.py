# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class PlaystorescrapyPipeline(object):
    def process_item(self, item, spider):
        return item

# class testSpider(InitSpider):
#     name = 'test'
#     custom_settings = {
#         'ITEM_PIPELINES': {
#             'app.MyPipeline': 400
#         }
#     }