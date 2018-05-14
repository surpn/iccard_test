# _*_coding:utf-8_*_
import unittest

from ddt import ddt, data, unpack, file_data

from common.annotation import try_except
from common.baseTest import BaseTest
from common.utils import current_path


@ddt
class TestDDT(BaseTest):

	def setUp(self):
		super().setUp()
		self.resource = "/ICCardCheckIn"
		self.method = "post"
		self.s.set(url=self.test_url, resource=self.resource, method=self.method)
		global file
		print(1)
	file = r"F:\mycode\iccard_test\test_case_data\data.yml"



	data1 = [{"cardNo": 1001}, u'{"expectResult":"0","expectSysMessage":"插卡成功！"}']
	data2 = [{"cardNo": 1000}, u'{"expectResult":"1","expectSysMessage":"卡号不存在！"}']
	# @data(data1, data2)
	@data(data1, data2)
	@unpack
	def est_DdtData(self,json, result):
		r = self.s.request(json=json)
		self.log.info(r.text)
		self.assertEqual(result, r.text, "123")

	@file_data(file)
	def test_DdtDataFile(self,data, result):
		print(file)
		r = self.s.request(json=data)
		self.log.info(r.text)
		self.assertEqual(result, r.text, "123")


if __name__ == "__main__":
	# suite = unittest.TestLoader().loadTestsFromTestCase(test_ddt)
	# unittest.TextTestRunner(verbosity=2).run(suite)
	unittest.main()
