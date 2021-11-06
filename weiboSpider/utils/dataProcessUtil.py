import time, urllib.parse, datetime
from urllib.parse import urlparse


class DataProcessUtil:

    def format_cookie(self, cookies):  # 把cookie转换成字典
        try:
            cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
            return cookies
        except IndexError:
            return ''

    def get_created_at(self, created_at):  # 把日期转换成时间戳
        if created_at is None:
            return None
        return time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(created_at, '%a %b %d %H:%M:%S %z %Y'))

    def get_keyword(self, url):  # 从url中获取关键词
        query = urllib.parse.urlparse(url).query
        params = urllib.parse.parse_qs(query)
        keyword = params['q'][0]
        return keyword

    def get_captured_at(self):  # 获取爬取时的时间
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_onboard_time(self, onboard_time):  # 获取上热搜的时间
        return time.strftime("%Y--%m--%d %H:%M:%S", time.localtime(onboard_time))

    def get_page_url(self, word):  # 获取搜索链接
        return 'https://s.weibo.com/realtime?q={}&tw=realtime&Refer=weibo_realtime'.format(
            urllib.parse.quote("#{}#".format(word)))

    def get_bloglist_url(self, url):  # 获取微博列表链接
        return "https://s.weibo.com{}".format(url)

    def get_blog_url(self, blog_url):  # 获取微博链接
        mblogid = urlparse(blog_url).path.split("/")[-1]
        return "https://weibo.com/ajax/statuses/show?id={}".format(mblogid)
