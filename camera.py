import cv2
import numpy
import sys


def create_ascii_map():  # by adding additional color codings you can refine the qualtity
    map_array = []
    for i in range(50):  # black
        map_array.append('X')

    for i in range(50, 150):  # greyish
        map_array.append('.')

    for i in range(150, 255):  # white
        map_array.append(' ')
    return map_array


def convert_to_ascii(image):
    map_array = create_ascii_map()
    new_ascii_array = []
    width = int(image.shape[1])
    height = int(image.shape[0])

    for i in range(height):
        new_ascii_array.append([])
        sys.stdout.write("\n")
        for j in range(width):
            new_ascii_array[i].append(map_array[image[i, j]])
            sys.stdout.write(map_array[image[i, j]])
    return new_ascii_array #contains the image that gets printed too


# begin main
vc = cv2.VideoCapture(0)

if vc.isOpened():  # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

# loop transforms image, prints it and gets a new image
while rval:
    frame_grey = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)  # convert to gray image
    scale_percent = 15  # percent of original size
    width = int(frame_grey.shape[1] * scale_percent / 100)
    height = int(frame_grey.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(frame_grey, dim, interpolation=cv2.INTER_AREA)

    ascii_image = convert_to_ascii(resized)

    #print(ascii_image)
    # cv2.imshow("original", frame)
    cv2.imshow("gray", frame_grey)

    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break

    rval, frame = vc.read()

vc.release()
cv2.destroyAllWindows()
