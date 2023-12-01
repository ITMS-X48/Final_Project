from my_spiders import spider_one, spider_two, spider_three
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def run_spider_one():
    process = CrawlerProcess(get_project_settings())
    process.crawl(spider_one)
    process.start()

def run_spider_two():
    process = CrawlerProcess(get_project_settings())
    process.crawl(spider_two)
    process.start()

def run_spider_three():
    process = CrawlerProcess(get_project_settings())
    process.crawl(spider_three)
    process.start()

## Implement GUI here