# Kyle Segrist
# Chapter 6 cpx lab-1
# Light pattern

from adafruit_circuitplayground import cp
import time
import random

OFF = (0, 0, 0)
TIME = .5   # Time in seconds

PATTERN = [0, 5, 1, 6, 2, 7, 3, 8, 4, 9]


# generate a random color using RGB spectrum
def pixel_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)

def main():
    while True:
        for pixel in PATTERN:
            cp.pixels[pixel] = pixel_color()
            time.sleep(TIME)
            cp.pixels[pixel] = OFF
            time.sleep(TIME)


main()# Write your code here :-)
