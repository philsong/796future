import auth, urllib

class client():

	'''
		# See: https://796.com/wiki/api.html
	'''

	def __init__(self):
		self.auth = auth.auth()

	# # # # # # #
	def tickers(self, coin='btc'):
		path = '/ticker.html?type='
		if coin == 'btc':
			path += 'weekly'
		elif coin == 'ltc':
			path += 'ltc'
		else:
			return
		return self.auth.get(path)

	# # # # # # #
	def _user(self, path):
		return self.auth.request('/v1/user'+path+'?')

	def _futures(self, path, params='', coin='btc'):
		if params: params = urllib.urlencode(params)+'&'
		if coin == 'btc': data = '/v1/weeklyfutures'+path+'?'+params
		elif coin == 'ltc': data = '/v1/ltcfutures'+path+'?'+params
		else: return
		return self.auth.request(data)


	# # # # # # #
	def get_info(self):
		'''# get usr info'''
		return self._user('/get_info')
	def get_balance(self):
		'''# get usr balance'''
		return self._user('/get_balance')
	def delete_token(self):
		'''# delete token'''
		return self._user('/delete_token')


	# # # # # # #
	def btc_orders(self):
		'''# get your btc orders'''
		return self._futures('/orders')
	def btc_records(self):
		'''# get last 100 trade history'''
		return self._futures('/records')
	def btc_position(self):
		'''# get btc position'''
		return self._futures('/position')


	# # # # # # #
	def btc_open_buy(self, vol=0, price=0):
		'''# btc long position - open'''
		params = {'buy_num': float(vol), 'buy_price': float(price)}
		return self._futures('/open_buy', params)

	def btc_close_buy(self, vol=0, price=0):
		'''# btc long position - close'''
		params = {'amount': float(vol), 'price': float(price)}
		return self._futures('/close_buy', params)

	def btc_open_sell(self, vol=0, price=0):
		'''# btc short position - open'''
		params = {'sell_num': float(vol), 'sell_price': float(price)}
		return self._futures('/open_sell', params)

	def btc_close_sell(self, vol=0, price=0):
		'''# btc short position - close'''
		params = {'amount': float(vol), 'price': float(price)}
		return self._futures('/close_sell', params)


	# # # # # # #
	def btc_cancel(self, bs='', no=0):
		'''
			cancel an exact order
			# (buy) or (sell)
			# id of order
		'''
		params = {'bs': str(bs), 'no': str(no)}
		return self._futures('/cancel_order', params)

	def btc_cancel_all(self, bs='all'):
		'''
			cancel all orders
			# (buy) or (sell) or (all)
		'''
		params = {'bs': bs}
		return self._futures('/cancel_all', params)
