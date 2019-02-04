import cv2
import numpy
import sys
import signal
import os

os.system("setterm -cursor off")
rows, columns = os.popen('stty size', 'r').read().split()

def create_ascii_map():
    char_array = list(".:o08#")
    new_array = []

    for ch in char_array:
        for i in range(50):
            new_array.append(ch)

    return new_array

def convert_to_ascii(image, grey_image):
    map_array = create_ascii_map()
    new_ascii_array = []
    last_ascii_array = []
    width = int(image.shape[1])
    height = int(image.shape[0])
    
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=height, cols=width))
    sys.stdout.write("\033[H\033[J")

    for i in range(height):
        for j in range(width):
            color = "\033[38;2;" + str(image[i, j][2]) + ";" + str(image[i, j][1]) + ";" + str(image[i, j][0]) + "m"
            new_ascii_array.append(color+map_array[grey_image[i, j]])

        new_ascii_array.append("\n")

    for i in range(len(new_ascii_array)-1):
        last_ascii_array.append(new_ascii_array[i])

    return last_ascii_array

def handle_exit(signum, frame):
    os.system("setterm -cursor on")
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=rows, cols=columns))
    sys.stdout.write("\033[H\033[J")
    sys.exit(0)

vc = cv2.VideoCapture(0)

if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False

while rval:
    signal.signal(signal.SIGINT, handle_exit)

    frame_grey = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    scale_percent = 8
    width = int(frame_grey.shape[1] * scale_percent / 50)
    height = int(frame_grey.shape[0] * scale_percent / 100)
    dim = (width, height)
    
    frame_resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
    frame_grey_resized = cv2.resize(frame_grey, dim, interpolation=cv2.INTER_AREA)

    ascii_image = convert_to_ascii(cv2.flip(frame_resized, 1), cv2.flip(frame_grey_resized, 1))

    print(''.join(ascii_image))

    if cv2.waitKey(16) & 0xFF == ord('q'):
        break

    rval, frame = vc.read()

vc.release()
cv2.destroyAllWindows()
os.system("setterm -cursor on")
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=rows, cols=columns))
sys.stdout.write("\033[H\033[J")
sys.exit(0)
