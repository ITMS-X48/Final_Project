import scrapy

class spider_one(scrapy.spider):
    name = 'uno'
    start_url = [
        ''
    ]

    def parse(self, response):
        title = response.css(title).extract()
        yield('title_text': title)
