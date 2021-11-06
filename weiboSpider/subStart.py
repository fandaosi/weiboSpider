from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

if __name__ == '__main__':
    settings = get_project_settings()
    crawler = CrawlerProcess(settings)
    crawler.crawl('blog')
    crawler.start()
