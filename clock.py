import time
import datetime
import sys
import signal
import os
from pyfiglet import Figlet

f = Figlet(font='big')

now = datetime.datetime.now()

hours = now.hour
minutes = now.minute
seconds = now.second

os.system("setterm -cursor off")
rows, columns = os.popen('stty size', 'r').read().split()

def update_clock():
	if(len(str(hours)) == 1):
		altH = "0" + str(hours)
	else:
		altH = str(hours)
	
	if(len(str(minutes)) == 1):
		altM = "0" + str(minutes)
	else:
		altM = str(minutes)
	
	if(len(str(seconds)) == 1):
		altS = "0" + str(seconds)
	else:
		altS = str(seconds)
	
	clock_input = f.renderText(altH+':'+altM+':'+altS)
	row_array = clock_input.split('\n')
	length_array = []
	output = []

	for obj in row_array:
		length_array.append(len(obj))
	
	for i in range(6):
		output.append(row_array[i])

	console_length = max(length_array)
	
	sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=7, cols=console_length))
	sys.stdout.write("\033[H\033[J")
	
	print('\n'.join(output))

def handle_exit(signum, frame):
    os.system("setterm -cursor on")
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=rows, cols=columns))
    sys.stdout.write("\033[H\033[J")
    sys.exit(0)

while(True):
	now = datetime.datetime.now()

	hours = now.hour
	minutes = now.minute
	seconds = now.second
	
	signal.signal(signal.SIGINT, handle_exit)

	update_clock()
	time.sleep(0.990)
