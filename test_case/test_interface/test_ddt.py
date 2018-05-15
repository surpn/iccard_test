# _*_coding:utf-8_*_
import unittest

from ddt import ddt, data, unpack, file_data, process_file_data

from common.annotation import try_except
from common.baseTest import BaseTest
from common.utils import current_path


@ddt
class TestDDT(BaseTest):
	file1 = r"F:\mycode\iccard_test\test_case_data\data.yml"

	def setUp(self):
		super().setUp()
		self.resource = "/ICCardCheckIn"
		self.method = "post"
		self.s.set(url=self.test_url, resource=self.resource, method=self.method)

		print("setup")

	data1 = [{"cardNo": 1001}, r'{"expectResult":"0","expectSysMessage":"插卡成功！"}']
	data2 = [{"cardNo": 1000}, r'{"expectResult":"1","expectSysMessage":"卡号不存在！"}']

	# @data(data1, data2)
	@data(data1, data2)
	def est_DdtData(self, json, result):
		r = self.s.request(json=json)
		self.log.info(r.text)
		self.assertEqual(result, r.text, "123")

	# print(file1)
	@file_data(file1)
	def test_DdtDataFile1(self, data, result):
		print("test_DdtData")
		"""		test_data : {data}, test_result : {result}"""
		r = self.s.request(json=data)
		self.log.info(r.text)
		self.assertEqual(result, r.text, "123")

	file2 = r"F:\mycode\iccard_test\test_case_data\data.json"

	@file_data(file2)
	def est_DdtDataFile2(self, a):
		"""Missing args with value {0}"""
		print(a)


if __name__ == "__main__":
	# suite = unittest.TestLoader().loadTestsFromTestCase(test_ddt)
	# unittest.TextTestRunner(verbosity=2).run(suite)
	unittest.main()
