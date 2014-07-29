import httplib, hashlib, hmac, json, requests
from time import time
from base64 import b64encode
from urllib import urlencode


def ksort(d):
     return [(k,d[k]) for k in sorted(d.keys())]

class auth():

	def __init__(self):

		self.apiKey = "APIKEY"
		self.secretKey = "SECRETKEY"
		self.appid = 000000

	def __access_token(self):

		timestamp = int(time())
		url = "796.com"
		conn = httplib.HTTPSConnection(url, 443)

		secretKey = self.secretKey
		APIKEY = self.apiKey
		APPID = self.appid

		params = {'appid':APPID,
		          'apikey':APIKEY,
		          'secretkey':secretKey,
		          'timestamp':timestamp}

		data = urlencode(ksort(params))
		sig = b64encode(hmac.new(secretKey, data, hashlib.sha1).hexdigest())

		token_url = "/oauth/token?" + urlencode(ksort(params)) + "&sig=%s"%sig
		conn.request("GET", token_url)

		r1 = conn.getresponse()
		print r1.status, r1.reason

		while True:
			if r1.status == 200:
				resp = json.loads(r1.read())
				print 'token:', resp['msg']
				if resp['errno'] == '0':
					token = resp['data']['access_token']
					return token
				else:
					print 'error with your verification info'
					break
			else:
				s = raw_input(">>Exception (restart) or (quit):\n")
				if s == "restart":
					print "restart"
					conn.request("GET", token_url)
				elif s == "quit":
					print "close"
					conn.close()
					break
				else:
					print "break"

		return

	def request(self, path=''):

		token = self.__access_token()
		try:
			res = requests.get('https://796.com'+path+'access_token=%s' % token)
			res = json.loads(res.text)
			print 'request:', res['msg']
			if res['errno'] == '0':
				return res['data']
		except:
			print 'error with request'
			print res
			return
