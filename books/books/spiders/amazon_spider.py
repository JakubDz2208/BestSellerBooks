import scrapy
from ..items import BooksItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 2
    start_urls = [
        'https://www.amazon.com/s?k=best+sellers+2021&i=stripbooks-intl-ship&crid=69V7E2YTDA5X&sprefix=best+sel%2Cstripbooks-intl-ship%2C269&ref=nb_sb_ss_ts-doa-p_1_8'
    ]

    def parse(self, response):
        items = BooksItem()

        product_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base+ .a-size-base').css('::text').extract()
        product_price = response.css('.a-spacing-top-small .a-price-whole').css('::text').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price

        yield items

        next_page = 'https://www.amazon.com/s?k=best+sellers+2021&i=stripbooks-intl-ship&page=' + str(AmazonSpider.page_number) + '&crid=69V7E2YTDA5X&qid=1629299967&sprefix=best+sel%2Cstripbooks-intl-ship%2C269&ref=sr_pg_2'
        if AmazonSpider.page_number <= 5:
            AmazonSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)