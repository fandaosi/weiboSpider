from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func
from weiboSpider.settings import *
from weiboSpider.models import *


class MysqlUtil:

    def __init__(self):
        self.__engine = create_engine(
            'mysql+pymysql://{}:{}@{}:{}/{}'.format(MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT,
                                                    MYSQL_DATABASE))
        self.__db_session = sessionmaker(bind=self.__engine)
        self.__session = self.__db_session()

    def get_proxy(self):  # 获取代理
        return self.__session.query(Cookie).order_by(func.rand()).limit(1).one()

    def get_cookie(self):  # 获取cookie
        return self.__session.query(Cookie).order_by(func.rand()).limit(1).one()

    def save_hot_search(self, item):  # 存储热搜
        self.__session.add(
            HotSearch(item["mid"], item["word"], item["category"], item["num"], item["onboard_time"],
                      item["hot_rank"], item["captured_at"]))
        self.__session.commit()

    def save_mblog(self, item):  # 存储微博
        self.__session.add(
            Mblog(item["mid"], item["text_raw"], item["user_id"], item["created_at"], item["captured_at"],
                  item["comments_count"], item["reposts_count"], item["screen_name"], item["attitudes_count"],
                  item["keyword"]))
        self.__session.commit()

    def __exit__(self, type, value, trace):
        self.__session.close()
