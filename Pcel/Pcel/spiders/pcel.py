# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from Pcel.items import PcelItem

class PcelSpider(CrawlSpider):
    name = "pcel"
    allowed_domains = ["pcel.com"]
    start_urls = (
        'http://pcel.com/computadoras/laptops-notebooks',
    )
    rules = (
        Rule(
            LxmlLinkExtractor(
                restrict_xpaths='//div[@class="links"]/a'
            ),
            callback='parse_item',
            follow=True,
        ),
    )

    def parse_item(self, response):
        for product in response.xpath('//div[@class="product-list"]/table/tr[count(*)=4]'):
            image = ''.join(product.xpath('.//div[@class="image"]/a/img/@src').extract())
            rating = int(''.join(product.xpath('.//div[@class="rating"]/img/@src').re('\d+')))
            brand = ''.join(product.xpath('./td[2]/a/img/@alt').extract())
            sku = int(''.join(product.xpath('./td[2]/span[1]/text()').re('Sku: (\d+)')))
            description = ''.join(product.xpath('.//div[@class="name"]/a/text()').extract()).replace('\r', '').strip()
            if len(product.xpath('.//div[@class="price"]/div').extract()) == 2:
                new_price = ''.join(product.xpath('.//div[@class="price-new"]/text()').extract()).strip()
                old_price = ''.join(product.xpath('.//div[@class="price-old"]/text()').extract()).strip()
            else:
                new_price = ''.join(product.xpath('.//div[@class="price"]/text()').extract()).strip()
                old_price = new_price
            item = PcelItem()
            item['image'] = image
            item['rating'] = rating
            item['brand'] = brand
            item['sku'] = sku
            item['description'] = description 
            item['new_price'] = new_price
            item['old_price'] = old_price
            yield item
