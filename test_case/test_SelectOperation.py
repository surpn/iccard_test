# _*_coding:utf-8_*_
import unittest

from common.baseTest import BaseTest


class SelectOperation(BaseTest):

	def setUp(self):
		super().setUp()
		method = "/ICCardCheckIn"
		self.url = self.test_url + method
		self.log.info(self.url)

	def test_SelectOperation01(self):
		pass


if __name__ == "__main__":
	unittest.main()
