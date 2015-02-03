# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PcelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    image = scrapy.Field()
    rating = scrapy.Field()
    brand = scrapy.Field()
    sku = scrapy.Field()
    description = scrapy.Field()
    new_price = scrapy.Field()
    old_price = scrapy.Field()
