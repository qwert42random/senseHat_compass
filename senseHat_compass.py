from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

R = [255, 0, 0]  # Red
Y = [255, 255, 0] # Yellow
G = [0, 255, 0] # Green
B = [0, 0, 255] # Blue
W = [255, 255, 255]  # White
O = [0, 0, 0]   # Off

pointer = 0
colourList = [R, G, B, W]

# Map from linear number section of edge.
def mapEdge(position):
     
    position = position % 28

    if (position < 8):
        return position 
    elif (8 <= position < 15):
        return ((position - 6) * 8) - 1
    elif (15 <= position < 22):
        return 63 - (position - 15) - 1
    elif (22 <= position < 28):
        return (position * (-8)) + 224

def mapValue(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

while True:

    for event in sense.stick.get_events():

        if (event.action == "pressed" and event.direction == "left"):
            pointer += 1
        elif (event.action == "pressed" and event.direction == "right"):
            pointer -= 1
        pointer = pointer % 28

    direction = sense.get_compass()
    screen = []
    indicator_pos = mapEdge(mapValue(direction, 0, 360, 0, 28))
    pointer_pos = mapEdge(pointer)

    for i in range(64):
        if (indicator_pos == pointer_pos == i):
            screen.append(Y)
        elif (indicator_pos == i):
            screen.append(W)
        elif (pointer_pos == i):
            screen.append(B)
        else:
            screen.append(O)

    sense.set_pixels(screen)

