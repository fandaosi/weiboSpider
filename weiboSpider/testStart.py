"""
测试用文件
"""
import urllib.parse

from scrapy import cmdline
# args = "scrapy runspider spiders/hotsearch.py".split()
# cmdline.execute(args)

args = "scrapy runspider spiders/blog.py".split()
cmdline.execute(args)

# args = "scrapy crawl test".split()
# cmdline.execute(args)
