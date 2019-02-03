import psutil
import math
import time
import sys

cpu_percent = psutil.cpu_percent(interval=1)
ram_percent = dict(psutil.virtual_memory()._asdict())['percent']

def cpuBar():
    cpu_loading_bar_array = []
    cpu_loading_bar_array.append("[")

    cpu_bars = math.floor(int(cpu_percent)/2)

    for obj in range(cpu_bars):
        cpu_loading_bar_array.append('=')

    for obj in range(50-cpu_bars):
        cpu_loading_bar_array.append('-')

    cpu_loading_bar_array.append("]")

    return cpu_loading_bar_array

def ramBar():
    ram_loading_bar_array = []
    ram_loading_bar_array.append("[")

    ram_bars = math.floor(int(ram_percent)/2)

    for obj in range(ram_bars):
        ram_loading_bar_array.append('=')

    for obj in range(50-ram_bars):
        ram_loading_bar_array.append('-')

    ram_loading_bar_array.append("]")

    return ram_loading_bar_array

def spaceNum(param):
    spaces = []
    float_to_int = len(str(int(param)))

    for obj in range(3 - float_to_int):
        spaces.append(" ")

    return ''.join(spaces)

while True:
    cpu_percent = psutil.cpu_percent(interval=1)
    ram_percent = dict(psutil.virtual_memory()._asdict())['percent']

    cpu_string = "CPU Usage:\n" + str(cpu_percent) + "%" + spaceNum(cpu_percent) + ''.join(cpuBar()) + "\n\n"
    ram_string = "RAM Usage:\n" + str(ram_percent) + "%" + spaceNum(ram_percent) + ''.join(ramBar())
    
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=6, cols=58))
    sys.stdout.write("\033[H\033[J")

    print(cpu_string + ram_string)
