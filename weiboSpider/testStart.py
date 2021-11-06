"""
测试用文件
"""
import urllib.parse

from scrapy import cmdline
# args = "scrapy runspider spiders/hotsearch.py".split()
# cmdline.execute(args)

# args = "scrapy runspider spiders/blog.py".split()
# cmdline.execute(args)

# args = "scrapy crawl test".split()
# cmdline.execute(args)

# from datetime import datetime, timedelta
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
#
# import time
#
# args = "scrapy runspider spiders/hotsearch.py".split()
#
# if __name__ == '__main__':
#
#     settings = get_project_settings()
#     crawler = CrawlerProcess(settings)
#     crawler.crawl('hotsearch')
#     while True:
#         crawler.start()
#         now = datetime.now()  # 整点开启热榜爬虫
#         str_time = str(now - timedelta(hours=-1))[:13] + ':00:00'
#         target_time = datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')
#         delay = (target_time - datetime.now()).total_seconds()
#         time.sleep(delay)
#



