import redis, threading
from weiboSpider.settings import *
from weiboSpider.utils.dataProcessUtil import DataProcessUtil


class RedisUtil:

    def __init__(self):
        self.__pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True,
                                           password=REDIS_PARAMS['password'], health_check_interval=10,
                                           socket_timeout=10, socket_keepalive=True,
                                           socket_connect_timeout=10, retry_on_timeout=True)
        self.__r = redis.Redis(connection_pool=self.__pool)

    def add_page_url(self, url):  # 添加微博页面列表第一页的地址
        self.__r.lpush('page:start_urls', url)

    def add_bloglist_url(self, url):  # 添加微博页面列表的地址
        self.__r.lpush('bloglist:start_urls', url)
