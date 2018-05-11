import unittest


from common.httpConfig import HttpClient
from common.log import Log
from common.readConfig import Config


class BaseTest(unittest.TestCase):
	"""
	测试基类
	"""
	def setUp(self):
		# 记录日志
		self.log = Log().log()
		self.log.info('-'*25 + u"test start" + '-'*25)
		# 读取 url
		cfg = Config().url()
		self.test_url = cfg["test"]
		# 创建会话,并初始化
		self.s = HttpClient(
			url=self.test_url, resource="/InitSystem", method="post")
		self.s.request()

	def tearDown(self):
		# 关闭会话
		self.s.close()
		self.log.info('-'*25 + u"test end" + '-'*25)


if __name__ == "__main__":
	unittest.mian()