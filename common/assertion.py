# _*_coding:utf-8_*_
import requests

from common.baseTest import BaseTest
from common.log import Log


# class Assertion_Error(BaseTest):
# 	"""自定义断言"""
#
# 	def __init__(self):
# 		self.log = Log().log()

def assertHTTPCode(response, status_code_list=None):
	"""断言:返回状态码"""
	if not status_code_list :
		status_code_list = [200, 201, 301, 302]
	if response.status_code not in status_code_list:
		raise AssertionError("响应错误码:{}".format(response.status_code))

def assertHTTPText(response, status_text):
	# 断言:返回文本值
	text = response.text
	if text != status_text:
		raise AssertionError(
			"返回内容不一致:\n"
		    "返回文本:\n"
			"{0}\n"
			"预期文本:\n{1}".format(text, status_text))





if __name__ == "__main__":
	r = requests.get("http://www.qq.com")
