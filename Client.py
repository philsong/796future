import auth, urllib

class client():

	'''
		# See: https://796.com/wiki/api.html
	'''

	def __init__(self):
		self.auth = auth.auth()

	def _user(self, path):
		return self.auth.request('/v1/user'+path+'?')

	def _futures(self, path, params='', coin='btc'):

		if params:
			params = urllib.urlencode(params)+'&'

		if coin == 'btc':
			data = '/v1/weeklyfutures'+path+'?'+params
		elif coin == 'ltc':
			data = '/v1/ltcfutures'+path+'?'+params
		else:
			return
		return self.auth.request(data)

	'''
		# get usr info.
		# get usr balance.
		# delete token.
	'''
	def get_info(self):
		return self._user('/get_info')
	def get_balance(self):
		return self._user('/get_balance')
	def delete_token(self):
		return self._user('/delete_token')

	'''
		# get your btc orders
		# get last 100 trade history
		# get btc position
	'''
	def btc_orders(self):
		return self._futures('/orders')
	def btc_records(self):
		return self._futures('/records')
	def btc_position(self):
		return self._futures('/position')

	'''
		# btc long  - open
		# btc long  - close
		# btc short - open
		# btc short - close
	'''
	def btc_open_buy(self, vol=0, price=0):
		params = {'buy_num': float(vol), 'buy_price': float(price)}
		return self._futures('/open_buy', params)

	def btc_close_buy(self, vol=0, price=0):
		params = {'amount': float(vol), 'price': float(price)}
		return self._futures('/close_buy', params)

	def btc_open_sell(self, vol=0, price=0):
		params = {'sell_num': float(vol), 'sell_price': float(price)}
		return self._futures('/open_sell', params)

	def btc_close_sell(self, vol=0, price=0):
		params = {'amount': float(vol), 'price': float(price)}
		return self._futures('/close_sell', params)

	'''
		# cancel an exact order
		# cancel all orders
	'''
	def btc_cancel(self, bs='', no=0):
		'''
			# (buy) or (sell)
			# id of order
		'''
		params = {'bs': str(bs), 'no': str(no)}
		return self._futures('/cancel_order', params)

	def btc_cancel_all(self, bs='all'):
		'''
			# (buy) or (sell) or (all)
		'''
		params = {'bs': bs}
		return self._futures('/cancel_all', params)
