import unittest


from common.httpConfig import Http
from common.log import Log
from common.readConfig import Config


class BaseTest(unittest.TestCase):
	"""
	测试基类
	"""
	def setUp(self):
		self.log = Log().log()
		# print(self.log)
		self.log.info('-'*25 + u"test setUp" + '-'*25)
		cfg = Config().url()
		self.test_url = cfg["test"]
		self.s = Http(self.test_url)

	def tearDown(self):
		self.s.close()
		self.log.info('-'*25 + u"test tearDown" + '-'*25)


if __name__ == "__main__":
	unittest.mian()