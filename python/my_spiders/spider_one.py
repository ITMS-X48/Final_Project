import csv
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import scrapy
import json
import os
import re

class spider_one(scrapy.Spider):
## First Read through our dataset and select the url's
    name = 'spider_one'
    scraped_ips = []
    settings = {
        'CLOSESPIDER_ITEMCOUNT': 50,
    }

    def start_requests(self):
        csv_file_path = os.path.abspath('python/my_spiders/datasets/benign_list_big_final.csv')
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                url = row[0]
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if not response.body:
            self.logger.warning('Empty response: %s', response.url)
            return

        # Check if the response is JSON
        content_type = response.headers.get(b'Content-Type', b'').decode('utf-8').lower()
        if b'application/json' in content_type:
            if response.status == 200:
                try:
                    data = json.loads(response.body)
                    if 'origin' in data and re.match(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', data['origin']):
                        ip_address = data['origin']
                        self.logger.info('IP Address: %s', ip_address)
                        self.scraped_ips.append(ip_address)
                        if len(self.scraped_ips) >= self.settings.get('CLOSESPIDER_ITEMCOUNT'):
                            self.crawler.engine.close_spider(self, 'item_count_reached')
                except json.JSONDecodeError as e:
                    self.logger.error('Error decoding JSON: %s', str(e))
        else:
            self.logger.warning('Response is not JSON: %s', response.url)

    def stop_spider(self):
        self.logger.info('stopping spider...')
        self.closeSpider('Terminated')
    
    def closeSpider(self, spider, reason):
        self.logger.info('Spider closed: %s', reason)
        self.process_ips()
    
    def process_ips(self): 
        self.logger.info('Scraped IPs:%s', self.scraped_ips)
        for x in self.scraped_ips:
            print(x)
    
def run_spider_one():
    process = CrawlerProcess(get_project_settings())
    process.crawl(spider_one)
    process.start()