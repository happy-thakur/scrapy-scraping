# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    img = scrapy.Field()
    link = scrapy.Field()
    title = scrapy.Field()
    realPrice = scrapy.Field()
    price = scrapy.Field()
    image_urls = scrapy.Field()
    categories = scrapy.Field()
    tags = scrapy.Field()
    shortDesc = scrapy.Field()
    extraText = scrapy.Field()
    productDetail = scrapy.Field()
    demoLink = scrapy.Field()
    description = scrapy.Field()
    images = scrapy.Field()
