# _*_coding:utf-8_*_
from pprint import pprint
from time import sleep

import xlrd

from common.log import Log
from common.readConfig import Config
from common.utils import current_path


class Case(object):

	def __init__(self):
		self.log = Log().log()
		cfg = Config().testcase()
		path = cfg["path"]
		self.path = current_path(path)
		file = self.path + "测试用例.xlsx"
		self.log.debug("测试用例文件路径: %s", file)
		self.excel = xlrd.open_workbook(file, "rb")
		self.case_title = cfg["cast_title"].strip(",").split(',')

	def import_list(self):
		"""

		:return:
		"""
		self.table = self.excel.sheet_by_name("接口功能")
		self.log.debug("sheet name: %s", self.table.name)
		self.rows = self.table.nrows
		self.cols = self.table.ncols
		self.log.debug("%s 有 %d 行, %d 列" % (self.table.name, self.table.nrows, self.table.ncols))
		sleep(1)
		cases = []

		for row in range(self.rows):
			s = self.table.cell(row, 0).ctype

			if s == 2:
				case = {}
				for col in range(self.cols):
					case[self.case_title[col]] = self.table.cell(row, col).value
				print("-"*80)
				pprint(case)
				cases.append(case)
		self.log.debug(cases)


if __name__ == "__main__":
	Case().import_list()
