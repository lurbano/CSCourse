import board
import neopixel
import time

nPix = 20
pixels = neopixel.NeoPixel(board.GP0, nPix)

class uLEDs:
    def __init__(self, nPix=20):
        self.nPix = nPix

    def lightUp(self, n = nPix, color=(10,0,0), dt=0.1):
        for i in range(n):
            pixels[i] = color
            time.sleep(dt)

    def lightDown(self, n=nPix, color=(10,0,0), dt=0.1):
        for i in range(n):
            pixels[-i] = color
            time.sleep(dt)

    def lightUpRed(self, n = nPix, dt=0.1):
        for i in range(n):
            pixels[i] = (10,0,0)
            time.sleep(dt)

    def upDown(self):
        self.lightUp()
        self.lightDown()