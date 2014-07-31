from lib2 import interest as i
i = i.interest()

data = i.data()
btc = data[0]; ltc = data[1]

with open('/root/796/data/interest', 'a+') as f:
	f.write(str(btc)+' '+str(ltc)+'\n')