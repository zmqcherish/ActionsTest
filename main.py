import os
from datetime import datetime
from util import *

if __name__ == '__main__':
	t = datetime.now().strftime("%H:%M")
	pb = os.environ["PWD"]
	#todo
	send2server_jiang(pb, t)