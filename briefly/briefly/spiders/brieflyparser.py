import scrapy
from briefly.items import BrieflyItem

class BrieflyparserSpider(scrapy.Spider):
    name = "brieflyparser"
    allowed_domains = ["briefly.ru"]
    start_urls = ["https://briefly.ru"]

    # def parse(self, response):
    #     # summary = response.xpath('span.microsummary_content::text').get()
    #     for item in response.xpath('//article[@class="summary_box"]'):
    #         yield {
    #             'title': item.css('span.main::text').getall(),
    #             'summary': item.css('span.microsummary__content::text').getall(),
    #             'text': (''.join((item.css('p::text')).getall())).replace('\n','')
    #         }
    #         # print("Смотри сюда")
    #         # print(item)

    
    def parse(self, response):
            base = response.css('.culture-cards-grid')
            links = base.css('a::attr(href)').getall()
            for link in links:
                yield scrapy.Request(link, callback=self.parse_by_alphabet)
                
    def parse_by_alphabet()
    # def parse_page(self, response):
    #     try:
    #         for item in response.xpath('//article[@class="summary_box"]'):
    #             yield {
    #                 'title': item.css('span.main::text').getall(),
    #                 'summary': item.css('span.microsummary__content::text').getall(),
    #                 'text': (''.join((item.css('p::text')).getall())).replace('\n','')
    #             }
    #     except:
    #          pass