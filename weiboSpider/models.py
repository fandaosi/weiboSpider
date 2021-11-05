# coding: utf-8
from sqlalchemy import Column, DECIMAL, DateTime, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TEXT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Cookie(Base):
    __tablename__ = 'cookie'

    cid = Column(DECIMAL(10, 0), primary_key=True)
    username = Column(Text, nullable=False)
    password = Column(Text, nullable=False)
    cookie = Column(Text, nullable=False)
    set_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))


class HotSearch(Base):
    __tablename__ = 'hot_search'

    mid = Column(VARCHAR(20), primary_key=True, nullable=False)
    word = Column(TEXT, nullable=False)
    category = Column(TEXT, nullable=False)
    num = Column(INTEGER(11), nullable=False)
    onboard_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    hot_rank = Column(INTEGER(11), nullable=False)
    captured_at = Column(DateTime, primary_key=True, nullable=False, server_default=text("CURRENT_TIMESTAMP"))

    def __init__(self, mid, word, category, num, onboard_time, hot_rank, captured_at):
        self.mid = mid
        self.word = word
        self.category = category
        self.num = num
        self.onboard_time = onboard_time
        self.hot_rank = hot_rank
        self.captured_at = captured_at


class Mblog(Base):
    __tablename__ = 'mblog'

    mblogid = Column(VARCHAR(20), primary_key=True)
    text_raw = Column(TEXT, nullable=False)
    user_id = Column(BIGINT(20), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    captured_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    comments_count = Column(INTEGER(11), nullable=False)
    reposts_count = Column(INTEGER(11), nullable=False)
    screen_name = Column(VARCHAR(255), nullable=False)
    attitudes_count = Column(INTEGER(11), nullable=False)
    keyword = Column(TEXT, nullable=False)

    def __init__(self, mblogid, text_raw, user_id, created_at, captured_at, comments_count, reposts_count, screen_name,
                 attitudes_count, keyword):
        self.mblogid = mblogid
        self.text_raw = text_raw
        self.user_id = user_id
        self.created_at = created_at
        self.captured_at = captured_at
        self.comments_count = comments_count
        self.reposts_count = reposts_count
        self.screen_name = screen_name
        self.attitudes_count = attitudes_count
        self.keyword = keyword
