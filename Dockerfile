FROM python:3.8-slim-buster
WORKDIR /weiboSpider
COPY . .

ENV PATH=$PATH:/weiboSpider
ENV PYTHONPATH /weiboSpider
RUN pip install -r requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
ENV type ${type}
CMD cd weiboSpider && python3 ${type}Start.py