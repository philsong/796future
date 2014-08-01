import re, urllib2, threading
from bs4 import BeautifulSoup as bs

class elite(threading.Thread):

	def run(self):
		
		try:
			response = urllib2.urlopen('https://796.com')
			html = response.read()
			soup = bs(html).find('div', id='focus1')
		except:
			print '(futures) cannot connect 796.'
			return 0,0,0,0

		ratio = re.findall('>(\d+.*)%<', str(soup))
		if len(ratio) != 8:
			return 0,0,0,0
		rBTC = [float(i) for i in ratio[:4]]
		rLTC = [float(i) for i in ratio[4:]]

		rlbtc = rBTC[0] * rBTC[1] / 10000
		rsbtc = rBTC[2] * rBTC[3] / 10000
		rlltc = rLTC[0] * rLTC[1] / 10000
		rsltc = rLTC[2] * rLTC[3] / 10000

		return rlbtc, rsbtc, rlltc, rsltc