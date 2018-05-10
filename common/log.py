import logging
import os
import threading

from common.readConfig import Config
from common.utils import timestamp, current_path


class Logging(object):
	"""
	日志输出配置
	"""
	# logging 配置文件
	__config = Config().logging()
	__output_format = __config["output_format"]
	__dir = __config["dir"]
	__log_path = current_path(__dir)
	__handler = __config["handler"]
	__console = __config["console"]
	__handler_name = __config["handler_level"]
	__console_name = __config["console_level"]
	_nameToLevel = {
		'CRITICAL': logging.CRITICAL,
		'FATAL': logging.FATAL,
		'ERROR': logging.ERROR,
		'WARN': logging.WARNING,
		'WARNING': logging.WARNING,
		'INFO': logging.INFO,
		'DEBUG': logging.DEBUG,
		'NOTSET': logging.NOTSET,
	}
	__handler_level = _nameToLevel[__handler_name]
	__console_level = _nameToLevel[__console_name]
	__logger = None

	def __init__(self):
		# 创建日志文件夹
		if not os.path.exists(self.__log_path):
			os.mkdir(self.__log_path)

		# 初始化
		self.__logger = logging.getLogger(__name__)
		self.__logger.setLevel(logging.DEBUG)

		# 设置log文件输出 级别.路径.格式化
		if self.__handler == "1":
			# 创建,路径
			handler = logging.FileHandler(
				filename=self.__log_path + timestamp() + "--"
				+ self.__handler_name + ".log", encoding='utf-8')
			# 级别
			handler.setLevel(self.__handler_level)
			# 格式化
			formatter = logging.Formatter(self.__output_format)
			handler.setFormatter(formatter)
			# 添加
			self.__logger.addHandler(handler)

		# 设置控制台日志 级别格式化
		if self.__console == "1":
			# 创建
			console = logging.StreamHandler()
			# 级别
			console.setLevel(self.__console_level)
			# 添加
			self.__logger.addHandler(console)

	def debug(self, msg, *args, **kwargs):
		"""debug级别日志"""
		self.__logger.debug(msg, *args, **kwargs)

	def info(self, msg, *args, **kwargs):
		"""info级别日志"""
		self.__logger.info(msg, *args, **kwargs)

	def warning(self, msg, *args, **kwargs):
		"""warning级别日志"""
		self.__logger.warning(msg, *args, **kwargs)

	def error(self, msg, *args, **kwargs):
		"""error级别日志"""
		self.__logger.error(msg, *args, **kwargs)

	def get_logger(self):
		"""
		get logger
		:return:
		"""
		return self.__logger


class Log(object):
	"""单例"""
	__log = None
	__mutex = threading.Lock()

	def __init__(self):
		if Log.__log is None:
			# print("log")
			Log.__mutex.acquire()
			Log.__log = Logging()
			Log.__mutex.release()

	@staticmethod
	def log():
		return Log.__log


if __name__ == '__main__':
	log = Log().log()
	log.debug("debug")
	log.info("info")
	log.warning("warning")
	log.error("error")
	log.get_logger().warn("123")
	# print(log.get_logger())
