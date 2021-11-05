# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HotSearchItem(scrapy.Item):
    mid = scrapy.Field()  # id
    word = scrapy.Field()  # 内容
    category = scrapy.Field()  # 分类
    num = scrapy.Field()  # 热度
    onboard_time = scrapy.Field()  # 上榜时间
    hot_rank = scrapy.Field()  # 排名
    captured_at = scrapy.Field()  # 捕获时间


class PageItem(scrapy.Item):
    url = scrapy.Field()
