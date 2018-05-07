# -*- coding:utf-8 -*-
import unittest

from common.baseTest import BaseTest


class TestICCardCheckIn(BaseTest):
	"""校验IC卡的有效性"""

	def setUp(self):
		super().setUp()
		method = "/ICCardCheckIn"
		self.url = self.test_url + method
		self.log.info(self.url)

	def test_ICCardCheckIn01(self):
		"""输入{"cardNo":1001}"""
		json = {
			"cardNo": 1001
		}
		r = self.s.post(url=self.url, json=json)
		self.log.info(r.text)
		self.assertEqual(u'{"expectResult":"0","expectSysMessage":"插卡成功！"}', r.text, "123")

	def test_ICCardCheckIn02(self):
		"""输入{"cardNo":1000}"""
		json = {
			"cardNo": 1000
		}
		r = self.s.post(url=self.url, json=json)
		self.log.info(r.text)
		self.assertEqual(u'{"expectResult":"1","expectSysMessage":"卡号不存在！"}', r.text, "123")

	def test_ICCardCheckIn03(self):
		"""输入{"cardNo":100*}"""
		json = {
			"cardNo": "100*"
		}
		r = self.s.post(url=self.url, json=json)
		self.log.info(r.text)
		self.assertEqual(u'{"expectResult":"1","expectSysMessage":"卡号不存在！"}', r.text, "123")

	def test_ICCardCheckIn04(self):
		"""输入{"cardNo":""}"""
		json = {
			"cardNo": ""
		}
		r = self.s.post(url=self.url, json=json)
		self.log.info(r.text)
		self.assertEqual(u'{"expectResult":"1","expectSysMessage":"卡号不存在！"}', r.text, "123")

	def test_ICCardCheckIn05(self):
		"""输入{"cardNo":""}"""
		json = {
			"cardNo": ""
		}
		r = self.s.post(url=self.url, json=json)
		self.log.info(r.text)
		self.assertEqual(u'{"expectResult":"1","expectSysMessage":"卡号不存在！"}', r.text, "123")


if __name__ == "__main__":
	unittest.main()
	# suite = unittest.TestSuite()
	# suite.addTest(TestICCardCheckIn('test_ICCardCheckIn01'))
	# # 执行测试
	# runner = unittest.TextTestRunner()
	# runner.run(suite)
