import scrapy


class BrieflyparserSpider(scrapy.Spider):
    name = "brieflyparser"
    allowed_domains = ["briefly.ru"]
    start_urls = ["https://briefly.ru/bulgakov/sobachie_serdtse/"]

    def parse(self, response):
        pars_dict = {}
        for item in response.xpath('//article').extract():
            print("Смотри сюда")
            print(item)
        # response.xpath("//*[contains(@class, 'author-cards-grid')]/text()").getall()
