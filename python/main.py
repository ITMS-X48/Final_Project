# from my_spiders import spider_one, spider_two, spider_three
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
# from webscrape import LogReader
from sockets_script import ip_puller

st = ip_puller()
st.run_pull()
print(st.ips)

# api_caller = 'https://api.ip2location.io/?key=A8EDA2B1A861BF908F3EC687E20C9CC7&ip='
# for row in st.ips:
#     scraper.scrape(api_caller + row)