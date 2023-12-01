import csv
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import scrapy
import json
import os
import re

class spider_one(scrapy.Spider):
## These are the established variables for naming and ip holding/output as well as a max number of ips
    name = 'spider_one'
    scraped_ips = []
    settings = {
        'CLOSESPIDER_ITEMCOUNT': 50,
    }
## This is going to read through the csv file and then fill an order for each url element contained within the file
    def start_requests(self):
        csv_file_path = os.path.abspath('python/my_spiders/datasets/benign_list_big_final.csv')
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                url = row[0]
                yield scrapy.Request(url=url, callback=self.parse)


## Parsing function
    def parse(self, response):
## This checks to see if the site is responding or not
        if not response.body:
            self.logger.warning('Empty response: %s', response.url)
            return

# This checks if the response is JSON
        content_type = response.headers.get(b'Content-Type', b'').decode('utf-8').lower()
        if b'application/json' in content_type:
## Checks if the site is blocking the scraper or if the scraper does not have access to the site for whatever reason
            if response.status == 200:
                try:
                    data = json.loads(response.body)
## Checks to see if the JSON response has key = origin and if the value corresponding to the origin is a valid ipv4  address
                    if 'origin' in data and re.match(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', data['origin']):
                        ip_address = data['origin']
                        self.logger.info('IP Address: %s', ip_address)
                        self.scraped_ips.append(ip_address)
## Hardcoded limit
                        if len(self.scraped_ips) >= self.settings.get('CLOSESPIDER_ITEMCOUNT'):
                            self.crawler.engine.close_spider(self, 'item_count_reached')
                except json.JSONDecodeError as e:
                    self.logger.error('Error decoding JSON: %s', str(e))
        else:
            self.logger.warning('Response is not JSON: %s', response.url)

##process to stop a spider suddenly
    def stop_spider(self):
        self.logger.info('stopping spider...')
        self.closeSpider('Terminated')
## part of the process of correctly closing the spider out
    def closeSpider(self, spider, reason):
        self.logger.info('Spider closed: %s', reason)
        self.process_ips()
## processes the ips so that they can be made use of
    def process_ips(self): 
        self.logger.info('Scraped IPs:%s', self.scraped_ips)
        for x in self.scraped_ips:
            print(x)
    
def run_spider_one():
    process = CrawlerProcess(get_project_settings())
    process.crawl(spider_one)
    process.start()