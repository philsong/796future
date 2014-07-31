import re, urllib2
from bs4 import BeautifulSoup as bs

class interest():

	def __init__(self):

		pass

	def data(self):
		
		try:
			response = urllib2.urlopen('https://796.com')
			html = response.read()
			soup = bs(html).findAll('div', {'class':'arrowNum'})
		except:
			print 'cannot connect 796.'
			return 0,0

		btc_int = float(re.findall('(\d+\.\d+)', str(soup[0]))[0])
		ltc_int = float(re.findall('(\d+\.\d+)', str(soup[1]))[0])

		return btc_int, ltc_int