# _*_coding:utf-8_*_
from pprint import pprint

import requests


class BeautifulHttp(object):
	"""返回页面元素提取器"""
	def __init__(self, response):
		pprint(response.text.encode(encoding='utf-8'))



if __name__ == "__main__":
	r = requests.get("http://www.baidu.com")
	BeautifulHttp(r)
