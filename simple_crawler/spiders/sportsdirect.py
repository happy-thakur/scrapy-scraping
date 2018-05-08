# -*- coding: utf-8 -*-
import scrapy
from ..items import ProductItem


class SportsdirectSpider(scrapy.Spider):
    name = 'sportsdirect'
    allowed_domains = ['srmehranclub.com']
    start_urls = ['https://srmehranclub.com/category/premium-wordpress-plugin/page/1/?product_count=500',
                  'https://srmehranclub.com/category/premium-wordpress-plugin/page/2/?product_count=500',
                  'https://srmehranclub.com/category/premium-wordpress-plugin/page/3/?product_count=500',
                  'https://srmehranclub.com/category/premium-wordpress-plugin/page/4/?product_count=500'
                  ]


    def parse(self, response):
        containers = response.css('li.product-grid-view')
        for one in containers:
            img = one.css('.featured-image img[data-lazy-src]').xpath('@data-lazy-src').extract_first()
            link = one.css('.product-title a').xpath('@href').extract_first()
            title = one.css('.product-title a::text').extract_first()
            realPrice = one.css('.price del .woocommerce-Price-amount::text').extract_first()
            price = one.css('.price ins .woocommerce-Price-amount::text').extract_first()
            # print (img, link, title, realPrice, price)
    #
            item = ProductItem()
            item['img'] = img
            item['link'] = link
            item['title'] = title
            item['realPrice'] = realPrice
            item['price'] = price

            # yield item
            # item['url'] = response.urljoin(productUrl)
            r = scrapy.Request(url=link, callback=self.parseProduct)
            r.meta['item'] = item
            yield r
    #     nextPageLinkSelector = response.css('.NextLink::attr("href")')
    #     if nextPageLinkSelector:
    #         nextPageLink = nextPageLinkSelector[0].extract()
    #         yield scrapy.Request(url=response.urljoin(nextPageLink))
    #

# main div
# div.product

# image
# product.css('div.woocommerce-product-gallery__image img::attr("data-large_image")').extract()

# categories
# product.css('div.product_meta span.posted_in a::text').extract(

# tags
# product.css('div.product_meta span.tagged_as a::text').extract()

# short desc
# product.css('div.woocommerce-product-details__short-description p::text').extract()

# extra text
# product.css('div.custom_added_text ul li::text').extract()

# for footer
# footer = product.css('div.wc-tabs-wrapper div.woocommerce-Tabs-panel')

# productDetail
# footer[0].css('p::text').extract()

# demoLink
# footer[1].css('p::text').extract()

# description
# footer[4].css('p::text').extract()



    def parseProduct(self, response):
        item = response.meta['item']
        product = response.css('div.product')

        bigImg = product.css('div.woocommerce-product-gallery__image img::attr("data-large_image")').extract()
        categories = product.css('div.product_meta span.posted_in a::text').extract()
        tags = product.css('div.product_meta span.tagged_as a::text').extract()
        shortDesc = product.css('div.woocommerce-product-details__short-description p::text').extract_first()
        extraText = product.css('div.custom_added_text ul li::text').extract()

        footer = product.css('div.wc-tabs-wrapper div.woocommerce-Tabs-panel')
        if(footer[0]):
            productDetail = footer[0].css('p::text').extract_first()
        if(footer[1]):
            demoLink = footer[2].css('div.tab-editor-container').extract_first()
        if(footer[len(footer)-1]):
            description = footer[len(footer)-1].css('div.post-content').extract_first()

        item['image_urls'] = bigImg
        item['categories'] = categories
        item['tags'] = tags
        item['shortDesc'] = shortDesc
        item['extraText'] = extraText
        item['productDetail'] = productDetail
        item['demoLink'] = demoLink
        item['description'] = description
        yield item
