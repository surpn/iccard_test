# -*- coding:utf-8 -*-
import unittest

from ddt import ddt, file_data

from common.baseTest import BaseTest
from common.annotation import try_except
from common.assertion import assertHTTPCode, assertHTTPText
from common.utils import current_path


@ddt
class TestICCardCheckIn(BaseTest):
	"""校验IC卡的有效性"""
	file = current_path("test_case_data") + r"ICCardCheckIn.yml"

	def setUp(self):
		super().setUp()
		self.resource = "/ICCardCheckIn"
		self.method = "post"
		self.s.set(url=self.test_url, resource=self.resource, method=self.method)

	@file_data(file)
	def test_ICCardCheckIn(self,data, result):
		"""输入{data}"""
		r = self.s.request(json=data)
		self.log.info(r.text)
		self.assertEqual(result, r.text, "返回结果与预期不一致")


if __name__ == "__main__":
	unittest.main()
# suite = unittest.TestSuite()
# suite.addTest(TestICCardCheckIn('test_ICCardCheckIn01'))
# # 执行测试
# runner = unittest.TextTestRunner()
# runner.run(suite)
