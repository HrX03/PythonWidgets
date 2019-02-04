import psutil
import signal
import math
import time
import sys
import os

cpu_percent = psutil.cpu_percent(interval=1)
ram_percent = dict(psutil.virtual_memory()._asdict())['percent']

os.system("setterm -cursor off")
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=6, cols=58))
rows, columns = os.popen('stty size', 'r').read().split()

def cpu_bar():
    cpu_loading_bar_array = []
    cpu_loading_bar_array.append("(")

    cpu_bars = math.floor(int(cpu_percent)/2)

    for obj in range(cpu_bars):
        cpu_loading_bar_array.append('=')

    for obj in range(50-cpu_bars):
        cpu_loading_bar_array.append(' ')

    cpu_loading_bar_array.append(")")

    return cpu_loading_bar_array

def ram_bar():
    ram_loading_bar_array = []
    ram_loading_bar_array.append("(")

    ram_bars = math.floor(int(ram_percent)/2)

    for obj in range(ram_bars):
        ram_loading_bar_array.append('=')

    for obj in range(50-ram_bars):
        ram_loading_bar_array.append(' ')

    ram_loading_bar_array.append(")")

    return ram_loading_bar_array

def handle_exit(signum, frame):
    os.system("setterm -cursor on")
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=rows, cols=columns))
    sys.stdout.write("\033[H\033[J")
    sys.exit(0)

def space_num(param):
    spaces = []
    float_to_int = len(str(int(param)))

    for obj in range(3 - float_to_int):
        spaces.append(" ")

    return ''.join(spaces)

while True:
    cpu_percent = psutil.cpu_percent(interval=1)
    ram_percent = dict(psutil.virtual_memory()._asdict())['percent']

    cpu_string = "CPU Usage:\n" + str(cpu_percent) + "%" + space_num(cpu_percent) + ''.join(cpu_bar()) + "\n\n"
    ram_string = "RAM Usage:\n" + str(ram_percent) + "%" + space_num(ram_percent) + ''.join(ram_bar())
    
    sys.stdout.write("\033[H\033[J")
    
    signal.signal(signal.SIGINT, handle_exit)
    print(cpu_string + ram_string)
