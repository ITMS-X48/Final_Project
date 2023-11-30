import scrapy
import csv

class spider_one(scrapy.spider):
    name = 'uno'
    def start_requests(self):
        with open(python/datasets/benign_list_big_final.csv, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                url = row[0]
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
            title = response.css('title::text').get()
            meta = response.css('meta[name="description"]::attr(content)').get()
            item = YourItem(parent_url=response.url)
            item['child_urls'] = response.css('a::attr(href)').extract()
