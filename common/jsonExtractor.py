# _*_coding:utf-8_*_
import json
from pprint import pprint

import jmespath
import requests

from common.log import Log


class JMESPathExtractor(object):
	"""json格式数据提取器"""

	def extractor(self, query=None, body=None):
		"""
		:param query:
		:param body:
		:return:
		"""
		try:
			# 转译 json 格式至 python 格式
			return jmespath.search(query, data=json.loads(body))
		except Exception as e:
			Log().log().error(e)


if __name__ == "__main__":
	r = requests.post("http://surpn.iok.la:58080/iccard/InitSystem")
	data = r.text
	pprint(type(json.loads(data)))
	path = JMESPathExtractor().extractor("expectResult", data)
	pprint(path)