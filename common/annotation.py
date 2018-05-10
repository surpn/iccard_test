# _*_coding:utf-8_*_
from common.log import Log


def try_except(func):
	"""自定义cry_exception异常捕获修饰器"""

	def log_func(*arg, **kwargs):
		try:
			return func(*arg, **kwargs)
		except Exception as e:
			# 编写测试错误信息报告
			Log().log().info(
				"error file:{0}{1}\n"
				"error model:{2}\n"
				"error def:{3}\n"
				"error message:{4}\n"
				.format(
					str(func.__code__).split('"')[1],
					str(func.__code__).split('"')[2][0:-1],
					func.__module__,
					func.__name__,
					e.__str__()
				)
			)
		finally:
			pass

	return log_func


if __name__ == "__main__":
	pass
