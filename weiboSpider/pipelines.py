from weiboSpider.utils.mysqlUtil import MysqlUtil
from weiboSpider.utils.redisUtil import RedisUtil
from weiboSpider.utils.dataProcessUtil import DataProcessUtil


class HotSearchPipeline:
    def process_item(self, item, spider):
        print(spider.name)
        if spider.name == 'hotsearch':
            mysql = MysqlUtil()
            redis = RedisUtil()
            data_process = DataProcessUtil()

            if type(item).__name__ == 'HotSearchItem':
                # 将热榜数据存储至数据库
                mysql.save_hot_search(item)

            if type(item).__name__ == 'PageItem':
                url = data_process.get_bloglist_url(item['url'])
                print("ddd")
                redis.add_blog_url(url)

        return item


class BlogPipeline:
    def process_item(self, item, spider):
        if spider.name == 'blog':
            mysql = MysqlUtil()
            mysql.save_mblog(item)

        return item
