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


class BlogItem(scrapy.Item):
    mblogid = scrapy.Field()  # id
    text_raw = scrapy.Field()  # 内容
    user_id = scrapy.Field()  # 用户id
    created_at = scrapy.Field()  # 发布时间
    captured_at = scrapy.Field()  # 捕获时间
    comments_count = scrapy.Field()  # 评论数
    reposts_count = scrapy.Field()  # 转发数
    screen_name = scrapy.Field()  # 用户名
    attitudes_count = scrapy.Field()  # 点赞数
    keyword = scrapy.Field()  # 关键词
