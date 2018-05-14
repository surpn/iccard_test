# _*_coding:utf-8_*_
from pprint import pprint

import xlrd
import xlsxwriter

from common.log import Log
from common.readConfig import Config
from common.utils import current_path


class Case(object):
	"""
	xlsx文件测试用例读取
	"""
	def __init__(self):
		self.log = Log().log()
		# 初始化配置文件,
		cfg = Config().testcase()
		path = cfg["path"]
		self.path = current_path(path)
		file = self.path + "测试用例.xlsx"
		self.log.debug("测试用例文件路径: %s", file)
		try:
			self.excel = xlrd.open_workbook(file, "rb")
		except FileNotFoundError as f:
			self.log.error(f)
		self.case_title = cfg["cast_title"].strip(",").split(',')

	def import_list(self):
		"""
		读取用例信息
		:return:测试用例列表
		"""
		self.table = self.excel.sheet_by_name("接口功能")
		self.log.debug("sheet name: %s", self.table.name)
		self.rows = self.table.nrows
		self.cols = self.table.ncols
		self.log.debug(
			"%s 有 %d 行, %d 列"
			% (self.table.name, self.table.nrows, self.table.ncols))
		"""
		[{"casetitle":{},"case":{}},
		{"casetitle":{},	"case":{}}]
		"""
		suits = []
		cases = []
		suit = {}
		casetitle = {}
		case = {}
		x = 0
		while x < self.rows:
			x += 1
			s = self.table.cell(x-1, 0).ctype
			# 1字符,2数字
			# 读取测试用例题头
			if s == 1 and self.table.cell(x-1, 0).value != "用例编号":
				i = 0
				r = self.table.row_slice(x-1)
				while i < len(r):
					try:
						if r[i].value != "":
							casetitle[r[i].value] = r[i+1].value
							i += 2
						else:
							break
					except IndexError:
						break

			# 用例头
			if s == 1 and self.table.cell(x-1, 0).value == "用例编号":
				# casetitle集合
				# self.log.debug(casetitle)

				suit["casetitle"] = casetitle
				casetitle = {}
				self.log.debug("用例编号")
				continue

			# 读取测试用例
			if s == 2:
				case = {}
				for c in range(self.cols):
					case[self.case_title[c]] = self.table.cell(x-1, c).value
				cases.append(case)

			if s == 1 and self.table.cell(x-1, 0).value == "编制人":
				if case != {}:
					# 测试用例
					# self.log.debug(cases)
					suit["cases"] = cases
					cases = []
					self.log.debug("-"*100)
					# self.log.debug(suit["casetitle"])
					# self.log.debug(suit["cases"])
					self.log.debug(suit)
					self.log.debug("-"*100)
					suits.append(suit)
					suit = {}
					self.log.debug("编制人")

			if x == self.rows:
				suit["cases"] = cases
				cases = []
				self.log.debug(suit["casetitle"])
				self.log.debug(suit["cases"])
				suits.append(suit)
				self.log.debug(x)
				cases = []
				suit = {}
				casetitle = {}
				case = {}
			# sleep(0.001)
		return suits


if __name__ == "__main__":
	suits = Case().import_list()
	x = 0
	y = 0
	title = ["用例编号","步骤名称","输入","预期输出","实际输出","是否通过","备注"]

	xlsx = xlsxwriter.Workbook(current_path("test_case_data") + "case.xlsx")
	sheet = xlsx.add_worksheet("case")
	while y<len(title):
		sheet.write(0, y, title[y])
		y += 1


	for suit in suits:
		# pprint(suit["casetitle"])


		for case in suit["cases"]:
			x += 1
			sheet.write(x, 0, case["用例编号"])
			sheet.write(x, 1, case["步骤名称"])
			sheet.write(x, 2, case["输入"])
			sheet.write(x, 3, case["预期输出"])
			sheet.write(x, 4, case["实际输出"])
			sheet.write(x, 5, case["是否通过"])
			sheet.write(x, 6, case["备注"])
		x += 1
			# pprint()


	xlsx.close()