from scrapy_redis.spiders import RedisSpider

from weiboSpider.items import PageItem


class PageSpider(RedisSpider):
    name = 'page'
    redis_key = 'page:start_urls'

    def parse(self, response):
        url_list = response.xpath('//div[@class="m-page"]/div/span/ul/li/a/@href').extract()
        for url in url_list:
            item = PageItem()
            item['url'] = url
            yield item
