# _*_coding:utf-8_*_
import requests


class Http(object):

	def __init__(self, url):
		self.s = requests.session()
		self.url = url

	def get(self, method, **kwargs):
		self.s.get(url=self.url+method, **kwargs)

	def post(self, method="/", head=None, data=None, json=None, **kwargs):
		if head is not None:
			self.s.headers.update(head)
		response = \
			self.s.post(url=self.url+method, data=data, json=json, **kwargs)
		return response

	def close(self):
		self.s.close()


if __name__ == "__main__":
	h = Http(url="http://localhost:9090/iccard")

	h.post("/InitSystem")

	url = "http://localhost:9090/iccard/ICCardCheckIn"
	json = {"cardNo": "1001"}
	r = h.post("/ICCardCheckIn", json=json)

	print(r.text)
