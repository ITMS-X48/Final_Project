from my_spiders.spider_one import spider_one
from my_spiders.spider_two import spider_two
from my_spiders.spider_three import spider_three
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from webscrape import LogReader

## Implement GUI here

if __name__ == "__main__":
    spider_one.run_spider_one()
    log_reader = LogReader(spider_one)
    log_reader.run_spider()
    logged_data = log_reader.log_messages
    print(logged_data)

