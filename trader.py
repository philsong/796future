from lib import Client
client = Client.client()

from lib2 import elite
e = elite.elite()
res = e.follow()

btc = res[0]-res[1]
ltc = res[2]-res[3]

if client.btc_orders():
	client.btc_cancel_all()

def interest(coin='btc'):
	
	import re
	from lib2 import interest as i
	i = i.interest()

	with open('/root/796/data/interest', 'r') as f:
		lines = f.readlines()[-3:]

	if coin == 'btc':
		interest = [float(re.findall('(.+) ', line)) for line in lines]
		last = i.data()[0]
	elif coin == 'ltc':
		interest = [float(re.findall(' (.+)', line)) for line in lines]
		last = i.data()[1]
	return sum(interest)/3/last

###------------------------------------------------###
#                         BTC                        #
###------------------------------------------------###

def btc_position():

	try:
		return client.btc_position()
	except:
		print 'wrong when getting btc position'
		raise Exception

def btc_balance():

	try:
		return btc*float(client.get_balance()['futures_wallet']['btc'])
	except:
		print 'wrong when getting balance'
		raise Exception

if btc >= 0.03:

	bal = btc_balance()
	pos = btc_position()
	try: pos = float(pos['buy']['bzj'])
	except: pos = 0.0
	vol = round(bal-pos, 2)*interest()*4
	if vol>0:
		price = float(client.tickers()['ticker']['buy'])
		client.btc_open_buy(vol, price)

elif abs(btc) <= 0.01:

	pos = btc_position()

	if not pos: raise Exception

	if pos['sell']:
		vol = float(pos['sell']['total'])
		price = float(client.tickers()['ticker']['sell'])
		client.btc_close_sell(vol, price)

	if pos['buy']:
		vol = float(pos['buy']['total'])
		price = float(client.tickers()['ticker']['buy'])
		client.btc_close_buy(vol, price)

elif btc <= -0.03:

	bal = btc_balance()
	pos = btc_position()
		
	try: pos = float(pos['sell']['bzj'])
	except: pos = 0.0

	vol = round(bal-pos, 2)*interest()*4
	if vol:
		price = float(client.tickers()['ticker']['sell'])
		client.btc_open_sell(vol, price)


###------------------------------------------------###
#                         LTC                        #
###------------------------------------------------###

def ltc_position():

	try:
		return client.ltc_position()
	except:
		print 'wrong when getting ltc position'
		raise Exception

def ltc_balance():

	try:
		return ltc*float(client.get_balance()['futures_wallet']['ltc'])
	except:
		print 'wrong when getting balance'
		raise Exception

if ltc >= 0.03:

	bal = ltc_balance()
	pos = ltc_position()
	try: pos = float(pos['buy']['bzj'])
	except: pos = 0.0
	vol = round(bal-pos, 2)*interest('ltc')*4
	if vol:
		price = float(client.tickers('ltc')['ticker']['buy'])
		client.ltc_open_buy(vol, price)

elif abs(ltc) <= 0.01:

	pos = ltc_position()

	try:
		vol = float(pos['sell']['total'])
		if vol:
			price = float(client.tickers('ltc')['ticker']['sell'])
			client.ltc_close_sell(vol, price)
	except:
		pass

	try:
		vol = float(pos['buy']['total'])
		if vol:
			price = float(client.tickers('ltc')['ticker']['buy'])
			client.ltc_close_buy(vol, price)
	except:
		pass

elif ltc <= -0.03:

	bal = ltc_balance()
	pos = ltc_position()
		
	try: pos = float(pos['sell']['bzj'])
	except: pos = 0.0

	vol = round(bal-pos, 2)*interest('ltc')*4
	if vol>0:
		price = float(client.tickers('ltc')['ticker']['sell'])
		client.ltc_open_sell(vol, price)