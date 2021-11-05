import time
from scrapy import signals
from weiboSpider.utils.mysqlUtil import MysqlUtil
from weiboSpider.utils.dataProcessUtil import DataProcessUtil


class WeiboSpiderMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        return None

    def process_spider_output(self, response, result, spider):
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        pass

    def process_start_requests(self, start_requests, spider):
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class WeiboDownloaderMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):  # 设置cookie
        mysql = MysqlUtil()
        while True:
            cookies = mysql.get_cookie()
            if cookies:
                break
            time.sleep(5)

        cookies = DataProcessUtil().format_cookie(cookies.cookie)  # 获取cookie后格式化
        now_time = int(time.time())
        cookies['SSOLoginState'] = str(now_time)
        cookies['ALF'] = str(now_time + 365 * 24 * 60 * 60 - 1)
        request.cookies = cookies
        request.dont_filter = True

        return None

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
