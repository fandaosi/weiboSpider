import redis
from weiboSpider.settings import *


class RedisUtil:

    def __init__(self):
        self.__pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True,
                                           password=REDIS_PARAMS['password'], health_check_interval=10,
                                           socket_timeout=10, socket_keepalive=True,
                                           socket_connect_timeout=10, retry_on_timeout=True)
        self.__r = redis.Redis(connection_pool=self.__pool)

    def add_blog_url(self, url):  # 添加微博页面列表的地址
        self.__r.lpush('blog:start_urls', url)
