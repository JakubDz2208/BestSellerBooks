import scrapy
from ..items import BooksItem

class EbaySpider(scrapy.Spider):
    name = 'ebay'
    start_urls = [
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=best+seller+books&_sacat=0'
    ]

    def parse(self, response):
        items = BooksItem()

        product_name = response.css('.s-item__title').css('::text').extract()
        product_secondary = response.css('.s-item__subtitle').css('::text').extract()
        product_price = response.css('.s-item__price').css('::text').extract()

        items['product_name'] = product_name
        items['product_author'] = product_secondary
        items['product_price'] = product_price

        for i in items:
            yield items