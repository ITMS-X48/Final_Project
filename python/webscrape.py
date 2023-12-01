from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
import scrapy

class LogReader:
    def __init__(self, spider):
        self.log_messages = []
        self.runner = CrawlerRunner()
        self.crawler = self.runner.create_crawler(spider)
        self.crawler.signals.connect(self.log_callback, signal=scrapy.signals.log)

    def log_callback(self, item, response, spider):
        self.log_messages.append(item)

    def run_spider(self):
        self.runner.crawl(self.crawler.spider)
        self.runner.join()
        self.runner.stop()

