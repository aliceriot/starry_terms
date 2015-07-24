import curtsies
import random
from curtsies import FullscreenWindow, FSArray, Input
from curtsies.fmtfuncs import *
from time import sleep

class Starfield():
    def __init__(self):
        self.screen = FullscreenWindow()
        self.array = FSArray(self.screen.height, self.screen.width)
        self.used = []

    def listen(self):
        with Input() as input_generator:
            for c in input_generator:
                if c == '<ESC>':
                    break
                elif c == '<SPACE>':
                    self.populate()

    def populate(self):
        numstars = int((self.screen.height * self.screen.width) / 10)
        for i in range(numstars):
            self.makestar()
            sleep(1)

    def color(self):
        return random.choice([cyan, blue, dark, green, magenta, gray, red,yellow])

    def makestar(self):
        while True:
            row = random.choice(range(self.screen.height))
            column = random.choice(range(self.screen.width))
            if (row, column) in self.used:
                pass
            else:
                color = self.color()
                self.array[row, column] = [color('*')]
                self.screen.render_to_terminal(self.array)
                self.used += [(row, column)]
                break

# actually do the thing!
field = Starfield()
field.populate()
field.listen()
