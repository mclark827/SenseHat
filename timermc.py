from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

G = [0, 255, 0]
R = [255, 0, 0]
W = [255, 255, 255]

for i in range(5, 3, -1):
    sense.show_letter( str(i), G)
    sleep(1)
for i in range(3, -1, -1):
    sense.show_letter( str(i), R)
    sleep(1)
for i in range(5):
    sense.show_letter( str(0), R)
    sleep(.5)
    sense.clear(W)
    sleep(.5)
    