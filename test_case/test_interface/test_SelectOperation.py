# _*_coding:utf-8_*_
import unittest

from ddt import ddt, file_data

from common.baseTest import BaseTest
from common.utils import current_path


@ddt
class SelectOperation(BaseTest):

	file = current_path("test_case_data") + r"SelectOperation.yml"

	def setUp(self):
		super().setUp()
		# 前置条件
		self.s.set(self.test_url, "/ICCardCheckIn", "post")
		self.s.request(json={"cardNo":1001})

		self.resource = "/SelectOperation"
		self.method = "post"
		self.log.info(self.method)
		self.s.set(self.test_url, self.resource, self.method)

	@file_data(file)
	def test_SelectOperation(self, data, result):
		"""输入{data}"""
		r = self.s.request(json=data)
		self.log.info(r.text)
		self.assertEqual(result, r.text, "返回结果与预期不一致")


if __name__ == "__main__":
	unittest.main()
