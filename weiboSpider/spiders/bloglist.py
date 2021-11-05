from scrapy_redis.spiders import RedisSpider

class BloglistSpider(RedisSpider):
    name = 'bloglist'
    redis_key = 'bloglist:start_urls'

    def parse(self, response):
        pass
