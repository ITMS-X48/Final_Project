import csv
import os
import re
import json
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from twisted.internet.error import DNSLookupError

class spider_one(scrapy.Spider):
    name = 'spider_one'
    scraped_ips = []
    CLOSESPIDER_ITEMCOUNT = 5
    meta = {
        'dont_redirect': true,
        "handle_httpstatus_list": [301, 302, 400, 401, 402, 403, 404, 410]
    }

    def start_requests(self):
        csv_file_path = os.path.abspath('python/my_spiders/datasets/benign_list_big_final.csv')
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                try:
                    url = row[0]
                    yield scrapy.Request(url=url, callback=self.parse)
                except UnicodeDecodeError:
                    continue
    def parse(self, response):
## This try handles DNS lookup errors
## Hardcoded stop to check only so many ips
        if len(self.scraped_ips) >= self.meta[CLOSESPIDER_ITEMCOUNT]:
            self.crawler.engine.close_spider(self, 'item_count_reached')
        try:
## Checks for no response from site
            if not response.body:
                self.logger.warning('Empty response: %s', response.url)

            content_type = response.headers.get(b'Content-Type', b'').decode('utf-8').lower()
## Makes sure it's a JSON response we're dealing with here
            if 'application/json' in content_type:
## If the http response is OK
                if response.status == 200:
## Try unless there's an issue with the JSON
                    try:
                        data = json.loads(response.body)
## Makes sure that the JSON responds with an origin key that is a proper ipv4 address
                        if 'origin' in data and re.match(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', data['origin']):
                            ip_address = data['origin']
                            self.logger.info('IP Address: %s', ip_address)
                            self.scraped_ips.append(ip_address)
                    except json.JSONDecodeError as e:
                        self.logger.error('Error decoding JSON: %s', str(e))
                elif response.status in self.http_bad_status_list:
                    self.logger.warning(f"Ignoring Bad HTTP Error: {response.status}")
            else:
                self.logger.warning('Response is not JSON: %s', response.url)
        except DNSLookupError as e:
            self.logger.error(f"DNS lookup failed: {response.url}: {str(e)}")

## these are for stopping the spider and making sure they output the correct ips
    def stop_spider(self):
        self.logger.info('Stopping spider...')
        self.close_spider('Terminated')

    def close_spider(self, reason):
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