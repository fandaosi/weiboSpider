import json
from scrapy import Request
from scrapy_redis.spiders import RedisSpider
from weiboSpider.utils.dataProcessUtil import DataProcessUtil
from weiboSpider.items import HotSearchItem, PageItem


class HotsearchSpider(RedisSpider):
    name = 'hotsearch'
    redis_key = 'hotsearch:start_urls'

    def parse(self, response):
        response = json.loads(response.text)
        data_process = DataProcessUtil()
        captured_at = data_process.get_captured_at()
        for hot_search in response["data"]["realtime"]:
            try:
                item = HotSearchItem()
                item["mid"] = hot_search["mid"]
                item["word"] = hot_search["word"]
                item["category"] = hot_search["category"]
                item["num"] = hot_search["num"]
                item["onboard_time"] = data_process.get_onboard_time(hot_search["onboard_time"])
                item["hot_rank"] = hot_search["rank"]
                item["captured_at"] = captured_at
                yield item
                yield Request(data_process.get_page_url(item['word']), callback=self.prase_page, dont_filter=True)
            except KeyError:
                continue

    def prase_page(self, response):
        url_list = response.xpath('//div[@class="m-page"]/div/span/ul/li/a/@href').extract()
        for url in url_list:
            item = PageItem()
            item['url'] = url
            yield item

