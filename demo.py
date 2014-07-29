from lib import Client
client = Client.client()

# get user info
client.get_info()

# get user balance
client.get_balance()

# delete token
client.delete_token()

# get btc orders
client.btc_orders()

# get btc records
client.btc_records()

# get btc position
client.btc_position()

'''
# buy open 0.01 btc
client.btc_open_buy(vol=0.01, price=550.0)

# buy close 0.01 btc
client.btc_close_buy(vol=0.01, price=650.0)

# cancel an order
client.cancel(bs='buy', no=00000)

# cancel all orders
client.cancel_all(bs='all')
'''