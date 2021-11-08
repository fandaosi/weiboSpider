from scrapy import cmdline
from weiboSpider.utils.redisUtil import RedisUtil
import time, schedule, multiprocessing


def job():
    RedisUtil().add_hotsearch_url()


def m_schedule():
    schedule.every().hour.at(":00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    args = "scrapy runspider spiders/hotsearch.py".split()

    p_1 = multiprocessing.Process(target=cmdline.execute, args=(args,))
    p_2 = multiprocessing.Process(target=m_schedule, args=())

    p_1.start()
    p_2.start()
