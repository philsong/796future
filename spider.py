import threading
from lib2 import interest as i
i = i.interest()

class interest(threading.Thread):

	def run(self):
		data = i.start()
		btc = data[0]; ltc = data[1]

		with open('/root/796/data/interest', 'a+') as f:
			f.write(str(btc)+' '+str(ltc)+'\n')

thread1 = interest()
thread1.start()