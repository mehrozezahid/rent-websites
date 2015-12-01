# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PlaceItem(scrapy.Item):
    item_source = scrapy.Field()
    referrer = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
