# _*_coding:utf-8_*_
import os
import configparser

from common.utils import current_path


class Config(object):
	"""
	获取配置 ini 文件
	read(filename)：读取ini文件中的内容
	sections()：得到所有section，返回列表形式
	[('key', 'value')]
	options(section)：得到给定section的所有option
	items(section):得到指定section的所有key-value
	get(section,option)：得到section中的option值，返回str类型
	get(section,option)：得到section中的option值，返回int类型
	"""

	def __init__(self):
		# 本地文件夹路径
		self.dir_path = current_path("config")
		if not os.path.exists(self.dir_path):
			os.mkdir(self.dir_path)

	def get_ini(self, ini_filename):
		file_path = self.dir_path + ini_filename
		cf = configparser.ConfigParser(interpolation=None)
		cf.read(file_path, encoding='UTF-8')
		return cf

	def item(self, ini_filename, item):
		items = self.get_ini(ini_filename).items(item)
		cfg = {}
		for item in items:
			cfg[item[0]] = item[1]
		return cfg

	def mysqldb(self):
		cfg = self.item("db.ini", "mysqlconf")
		return cfg

	def url(self):
		cfg = self.item("url.ini", "urls")
		return cfg

	def email(self):
		cfg = self.item("email.ini", "email")
		return cfg

	def logging(self):
		cfg = self.item("logging.ini", "logging")
		return cfg

	def testcase(self):
		cfg = self.item("testcase.ini", "testcase")
		return cfg


if __name__ == "__main__":
	config = Config().mysqldb()
	print(config)
	config = Config().url()
	print(config)
	config = Config().email()
	print(config)
	config = Config().logging()
	print(config)
