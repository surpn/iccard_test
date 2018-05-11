# _*_coding:utf-8_*_


class CustomException(Exception):
	pass


class UnsupportedMethodException(CustomException):

	def __init__(self):
		super().__init__()

	def __str__(self):
		return "The Mehod is Unsupported"


if __name__ == "__main__":
	try:
		raise UnsupportedMethodException()
	except UnsupportedMethodException as e:
		print(e)
