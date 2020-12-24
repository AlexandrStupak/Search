from Myproj.items import MyprojItem
# python 3
import scrapy
from urllib.parse import urljoin

class PycoderSpider(scrapy.Spider):
    name = 'pycoder'
    start_urls = ['https://hobbygames.ru/nastolnie?page=1']
    visited_urls = []

    def parse(self, response):
        if response.url not in self.visited_urls:
            self.visited_urls.append(response.url)
            SET_SELECTOR='a.name::attr(href)'
            for post_link in response.css(SET_SELECTOR).extract():
                url = urljoin(response.url, post_link)
                yield response.follow(url, callback=self.parse_dop)
            NEXT_PAGE = 'a.next::attr(href)'
            next_page = response.css(NEXT_PAGE).extract()
            next_page_url = urljoin(response.url, next_page[len(next_page) - 1])
            yield response.follow(next_page_url, callback=self.parse)

    def parse_dop(self, response):
        item = MyprojItem()
        title = response.css('h1::text').extract_first()
        body = response.xpath(
                '//div[@class="desc-text"]//p/text()').extract()
        url = response.url
        price = response.xpath(
                '//div[@class="price"]/text()').extract_first()
        dop = price.split()
        dop = ''.join(dop)
        item['title'] = title
        item['body'] = body
        item['url'] = url
        item['price'] = dop[0:len(dop)-1]#отрежем последний элемент Р
        yield item