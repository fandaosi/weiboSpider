import scrapy,json
from weiboSpider.utils.dataProcessUtil import DataProcessUtil
from weiboSpider.items import HotSearchItem


class HotsearchSpider(scrapy.Spider):
    name = 'hotsearch'
    allowed_domains = ['weibo.com']
    start_urls = ['https://weibo.com/ajax/side/hotSearch']

    def parse(self, response):
        response = json.loads(response.text)
        captured_at = DataProcessUtil().get_captured_at()
        for hot_search in response["data"]["realtime"]:
            try:
                item = HotSearchItem()
                item["mid"] = hot_search["mid"]
                item["word"] = hot_search["word"]
                item["category"] = hot_search["category"]
                item["num"] = hot_search["num"]
                item["onboard_time"] = DataProcessUtil().get_onboard_time(hot_search["onboard_time"])
                item["hot_rank"] = hot_search["rank"]
                item["captured_at"] = captured_at
                yield item
            except KeyError:
                continue
