<hr style=" border:solid; width:100px; height:1px;" color=#000000 size=1">


# 前言

用于爬取微博的爬虫。内含两个爬虫，一个用于爬取热搜榜（热搜爬虫），另一个用于爬取对应热搜的微博内容（搜索爬虫）。
**本爬虫用到了Mysql、Redis，请提前安装好。**

<hr style=" border:solid; width:100px; height:1px;" color=#000000 size=1">

# 一、准备工作

## 1.下载源码

可以通过

```bash
git clone https://github.com/fandaosi/WeiboSpiders
```

或直接下载获取源码

## 2.修改配置文件

进入 WeiboSpiders_center/settings.py，将对应的IP地址、端口号、用户名、密码修改为你自己的。

```python
# mysql
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USERNAME = 'root'
MYSQL_PASSWORD = 'admin'
MYSQL_DATABASE = 'weibo'

# mongdb
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = 'admin'
MONGO_PASSWORD = 'admin'
MONGO_DATABASE = 'weibo'

# redis
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PARAMS = {
    'password': 'admin',
}
```

## 3.创建数据库

在Mysql中运行script.sql创建数据库

## 4.添加cookie

在Mysql的weibo_new库中的cookie表的cookie字段添加cookie，cookie获取方法与[这个项目](https://github.com/dataabc/weiboSpider/blob/master/docs/cookie.md)相同。
其他字段暂时不影响结果。
<hr style=" border:solid; width:100px; height:1px;" color=#000000 size=1">

# 二、开始爬取

该操作实际是运行热搜爬虫控制器、一个热搜爬虫与一个搜索爬虫

## 1.使用Docker运行（推荐）

创建镜像

```bash
 docker build -t weibospider .
```

 运行容器

```bash
docker run --name weibospiders_center -e type="center"  weibospider
```


## 2.直接在编辑器中运行

```bash
直接运行 WeiboSpiders_center/centerStart.py
```


# 提示

本项目是分布式爬虫，还可以通过再运行一个搜索爬虫加速爬取过程。
可通过

```bash
docker run --name weibospiders_sub -e type="sub"  weibospider
```

或

```bash
直接运行 WeiboSpiders_center/subStart.py
```

运行搜索爬虫
<hr style=" border:solid; width:100px; height:1px;" color=#000000 size=1">

# 三、查看结果

热搜榜存储于Mysql的hotsearch表中，获取的微博则存于mblog表中。
hotsearch的表信息如下表所示。

| 字段名   |   mid   |   word   |   category   |   num   |   onboard_time   |   hot_rank   |   captured_at   |
| -------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 实际意义 |   热搜id   |   热搜内容   |   热搜分类   |   热度   |   上榜时间   |   排名   |   热搜捕获时间   |

mblog的表信息如下表所示。

| 字段名   |   mblogid   |   text_raw   |   user_id   |   created_at   |   captured_at   |   comments_count   |   reposts_count   |   screen_name   |   attitudes_count   |keyword|
| -------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |---- |
| 实际意义 |   微博id   |   微博内容   |   用户id   |   微博发送时间   |   微博捕获时间   |   评论数   |   转发数   |   用户名   |   点赞数   |  捕获时关联的热搜  |