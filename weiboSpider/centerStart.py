from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

import time, schedule


def job():
    settings = get_project_settings()
    crawler = CrawlerProcess(settings)
    crawler.crawl('hotsearch')
    crawler.start()


if __name__ == '__main__':
    job()
    schedule.every().hour.at(":00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
