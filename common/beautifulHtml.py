# _*_coding:utf-8_*_
from pprint import pprint
from bs4 import BeautifulSoup

import requests


class BeautifulHttp(object):
	"""返回页面元素提取器"""
	def __init__(self, response):
		response.encoding='utf-8'
		html = response.text
		soup=BeautifulSoup(html, 'html.parser')
		print(soup)




if __name__ == "__main__":
	r = requests.get("http://www.baidu.com")
	BeautifulHttp(r)