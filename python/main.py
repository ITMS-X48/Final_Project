from my_spiders import spider_one
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def run_spider_one():
    process = CrawlerProcess(get_project_settings())
    process.crawl(spider_one)