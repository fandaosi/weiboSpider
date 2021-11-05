from scrapy_redis.spiders import RedisSpider


class BlogSpider(RedisSpider):
    name = 'blog'
    allowed_domains = ['weibo.com']
    start_urls = ['http://weibo.com/']


    def parse(self, response):
        pass
