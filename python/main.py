from my_spiders import spider_one, spider_two, spider_three
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from webscrape import LogReader

if __name__ == "__main__":
    log_reader = LogReader(spider_one)
    log_reader.run_spider()
    logged_data = log_reader.log_messages
    print(logged_data)