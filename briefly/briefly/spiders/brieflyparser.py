import scrapy

class BrieflyparserSpider(scrapy.Spider):
    name = "brieflyparser"
    allowed_domains = ["briefly.ru"]
    start_urls = ["https://briefly.ru"]


    def parse(self, response):
        yield scrapy.Request(url='https://briefly.ru/authors', callback=self.start_parse)


    def start_parse(self, response):
            next_page_url = response.urljoin('..')
            base = response.css('div.letter')
            links = base.css('a::attr(href)').getall()
            for link in links:
                yield scrapy.Request("https://briefly.ru" + link, callback=self.parse_by_author)
            

    def parse_by_author(self, response):
        try:
            if response.css('.works_index'):
                works = response.css('section.works_index')
                links = works.css('a.title::attr(href)').getall()
                for link in links:
                    yield scrapy.Request("https://briefly.ru" + link, callback=self.parse_page)
            
            elif response.css('.w-featured'):
                best = response.css('.w-featured')
                links = best.css('a::attr(href)').getall()
                for link in links:
                    yield scrapy.Request("https://briefly.ru" + link, callback=self.parse_page)
        except:
            pass


    def parse_page(self, response):
        try:
            for item in response.xpath('//article[@class="summary_box"]'):
                yield {
                    'title': item.css('span.main::text').getall(),
                    'author': response.xpath('//div[@class="breadcrumb__name"]/text()').get(),
                    'summary': item.css('span.microsummary__content::text').getall(),
                    'text': (''.join((item.css('p::text')).getall())).replace('\n','')
                }
        except:
             pass