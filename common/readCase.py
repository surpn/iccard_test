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
		# sleep(1)

		cases = []
		case = {}
		casetitle = {}
		x = 0
		while x < self.rows:
			s = self.table.cell(x, 0).ctype
			# 1字符,2数字
			if s == 1 and self.table.cell(x, 0).value == "用例编号":
				# self.log.debug(casetitle)
				cases.append({"title": casetitle, "case": 1})

			# 读取测试用例题头
			if s == 10 and self.table.cell(x, 0).value != "用例编号":
				i = 0
				r = self.table.row_slice(x)
				while i < len(r):
					try:
						if r[i].value != "":
							casetitle[r[i].value] = r[i+1].value
							i += 2
						else:
							break
					except IndexError:
						break

			# 读取测试用例
			if s == 2:
				for c in range(self.cols):
					case[self.case_title[c]] = self.table.cell(x, c).value
			# self.log.debug(case)
			x += 1
			sleep(0.1)
		self.log.debug(cases)


if __name__ == "__main__":
	Case().import_list()
