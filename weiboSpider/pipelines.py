from weiboSpider.utils.mysqlUtil import MysqlUtil
from weiboSpider.utils.redisUtil import RedisUtil
from weiboSpider.utils.dataProcessUtil import DataProcessUtil


class HotSearchPipeline:
    def process_item(self, item, spider):
        if spider.name == 'hotsearch':
            # 将热榜数据存储至数据库
            mysql = MysqlUtil()
            redis = RedisUtil()
            data_process = DataProcessUtil()
            mysql.save_hot_search(item)
            bloglist_url = data_process.get_page_url(item["word"])
            redis.add_page_url(bloglist_url)
        return item


class PagePipeline:
    def process_item(self, item, spider):
        if spider.name == 'page':
            redis = RedisUtil()
            url = DataProcessUtil().get_bloglist_url(item['url'])
            redis.add_bloglist_url(url)
            print("dddddddddddddddddddddddd")
        return item
