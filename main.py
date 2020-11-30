import os
from datetime import datetime
from util import *

if __name__ == '__main__':
	# pa = os.environ["P_A"]
	t = datetime.now().strftime("%H:%M")
	pb = os.environ["PWD"]
	send2server_jiang(pb, t)