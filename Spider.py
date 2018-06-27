import requests, re

class Spider(object):
	def __init__(self):
		self.search_url = 'http://www.boohee.com/food/search?keyword='
		self.query_url = 'http://www.boohee.com/shiwu/'
		self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
        }
		self.encoding = 'utf-8'

	def get_id(self, name):
		try:
			r = requests.get(self.search_url + name, headers = self.headers)
			r.raise_for_status()
			if self.encoding == None:
				r.encoding = r.apparent_encoding
			else:
				r.encoding = self.encoding
			res = re.findall(r'<div id="main">(.*?)</li>', r.text, re.S)
			if len(res) > 0:
				res = re.findall(r'/shiwu/(.*?)\'', res[0], re.S)
				if len(res) > 0:
					return res[0]
		except Exception as e:
			return None

	def get_query(self, id):
		return_data = {}
		try:
			r = requests.get(self.query_url + id, headers = self.headers)
			r.raise_for_status()
			if self.encoding == None:
				r.encoding = r.apparent_encoding
			else:
				r.encoding = self.encoding
			res = re.findall(r'<b>评价：</b>(.*?)</p>', r.text, re.S)
			if len(res) > 0:
				return_data['comment'] = res[0].strip()
			res = re.findall(r'热量\(大卡\)</span><span class="dd"><span class="stress red1">(.*?)</span>', r.text, re.S)
			if len(res) > 0:
				return_data['heat'] = res[0].strip()
			res = re.findall(r'碳水化合物\(克\)</span><span class="dd">(.*?)</span>', r.text, re.S)
			if len(res) > 0:
				return_data['carbo'] = res[0].strip()
			res = re.findall(r'脂肪\(克\)</span><span class="dd">(.*?)</span>', r.text, re.S)
			if len(res) > 0:
				return_data['fat'] = res[0].strip()
			res = re.findall(r'蛋白质\(克\)</span><span class="dd">(.*?)</span>', r.text, re.S)
			if len(res) > 0:
				return_data['protein'] = res[0].strip()
			res = re.findall(r'纤维素\(克\)</span><span class="dd">(.*?)</span>', r.text, re.S)
			if len(res) > 0:
				return_data['fibrinous'] = res[0].strip()
			return return_data
		except Exception as e:
			return None

	def get_data(self, name):
		r = self.get_id(name)
		if r :
			r = self.get_query(r)
			return r
		else:
			return None

