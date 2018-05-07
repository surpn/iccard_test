import unittest

import requests

from common.log import Log
from common.readConfig import Config


class BaseTest(unittest.TestCase):
	"""
	测试基类
	"""
	def setUp(self):
		self.log = Log().log()
		self.log.info('-'*25 + u"test setUp" + '-'*25)
		cfg = Config().url()
		self.test_url = cfg["test"]

		self.s = requests.session()

		r = self.s.post("http://localhost:9090/iccard/InitSystem")

		self.log.info(r.text)

	def tearDown(self):
		self.s.close()
		self.log.info('-'*25 + u"test tearDown" + '-'*25)
