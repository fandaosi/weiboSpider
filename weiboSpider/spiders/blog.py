from scrapy import Request
from scrapy_redis.spiders import RedisSpider

from weiboSpider.items import BlogItem
from weiboSpider.utils.dataProcessUtil import DataProcessUtil

import json


class BlogSpider(RedisSpider):
    name = 'blog'
    redis_key = 'blog:start_urls'

    def parse(self, response):
        url_list = response.xpath('//div[@class="content"]/p[1]/a[1]/@href').extract()
        data_process = DataProcessUtil()
        for url in url_list:
            url = data_process.get_blog_url(url)
            yield Request(url, callback=self.parse_blog,
                          meta={'keyword': data_process.get_keyword(response.request.url)},
                          dont_filter=False)

    def parse_blog(self, response):
        mblog = json.loads(response.text)
        data_process_util = DataProcessUtil()
        keyword = response.request.meta['keyword']
        try:
            item = BlogItem()
            item["mblogid"] = mblog.get("mblogid")
            item["text_raw"] = mblog.get("text_raw")
            item["user_id"] = mblog.get("user", {}).get("id")
            item["created_at"] = data_process_util.get_created_at(mblog.get("created_at"))
            item["captured_at"] = data_process_util.get_captured_at()
            item["comments_count"] = mblog.get("comments_count")
            item["reposts_count"] = mblog.get("reposts_count")
            item["screen_name"] = mblog.get("user", {}).get("screen_name")
            item["attitudes_count"] = mblog.get("attitudes_count")
            item["keyword"] = keyword
            yield item
        except KeyError:
            pass
