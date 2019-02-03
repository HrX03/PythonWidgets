import time
import datetime
import sys
import curses
from pyfiglet import Figlet

f = Figlet(font='big')

now = datetime.datetime.now()

hours = now.hour
minutes = now.minute
seconds = now.second

def updateClock():
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

while(True):
	now = datetime.datetime.now()

	hours = now.hour
	minutes = now.minute
	seconds = now.second
		
	updateClock()
	time.sleep(0.990)
