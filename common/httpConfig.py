# _*_coding:utf-8_*_
import threading

import requests

from common.customException import UnsupportedMethodException
from common.log import Log
from common.readConfig import Config


class HttpClient(object):
	"""http session"""

	METHOD = ['GET', 'POST', 'PUT', 'DELETE']

	def __init__(self, url, resource=None, method="get"):
		"""
		初始化 session 参数
		:param url:
		:param resource:
		:param method: 访问方式
		"""
		self.set(url=url, resource=resource, method=method)
		self.session = requests.session()
		self.log.info("url:{0}, method:'{1}', session:{2}"
		              .format(self.url, self.method, str(self.session)[-11:-1]))

	def request(
			self, params=None, data=None, headers=None,
			cookies=None, files=None, auth=None, timeout=None,
			allow_redirects=True, proxies=None, hooks=None, stream=None,
			verify=None, cert=None, json=None):

		resp = self.session.request(
			method=self.method, url=self.url, params=params, data=data,
			headers=headers, cookies=cookies, files=files, auth=auth,
			timeout=timeout, allow_redirects=allow_redirects, proxies=proxies,
			hooks=hooks, stream=stream, verify=verify, cert=cert, json=json)
		return resp

	def set(self, url=None, resource=None, method=None):
		"""修改请求基本配置"""
		self.log = Log().log()
		if method is not None:
			try:
				self.method = method.upper()
			except UnsupportedMethodException as e:
				self.log.error(e)

		if resource is not None:
			self.url = url + resource

	def close(self):
		"""关闭连接"""
		self.session.close()
		self.log.info("session关闭")

	# class Session():
	#
	# 	def __init__(self):
	# 		session = requests.session()
	# 		return session
	#
	#
	# 	def __get_session():
	# 		__session = None
	# 		__mutex = threading.Lock()
	#
	# 		if not __session:
	#

if __name__ == "__main__":
	cf = Config().url()
	print(cf)
	test_url = cf["test"]
	s = HttpClient(test_url, "/InitSystem", "post")
	print(s.request().text)
