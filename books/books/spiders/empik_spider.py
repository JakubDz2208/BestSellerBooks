import scrapy
from ..items import BooksItem

class EmpikSpider(scrapy.Spider):
    name = 'empik'
    books = 31
    start_urls = [
        'https://www.empik.com/bestsellery/ksiazki'
        ]

    def parse(self, response):
        items = BooksItem()

        product_name = response.css('.ta-product-title').css('::text').extract()
        product_author = response.css('.smartAuthor').css('::text').extract()
        product_price = response.css('.ta-price-tile').css('::text').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price



        yield items
