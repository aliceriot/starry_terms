import curtsies
import random
from curtsies import FullscreenWindow, FSArray, Input
from curtsies.fmtfuncs import *
from time import sleep

class Starfield():
    def __init__(self):
        self.screen = FullscreenWindow()
        self.array = FSArray(self.screen.height, self.screen.width)

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
            num = random.choice(range(2))
            if num == 1:
                self.make_star()
            else:
                self.make_fancy_star()
            sleep(1)

    def color(self):
        return random.choice([cyan, blue, dark, green, magenta, gray, red,yellow])

    def random_row_and_column(self):
        dimensions = [self.screen.height, self.screen.width]
        return list(map(lambda x: random.choice(range(x)), dimensions))

    def place_with_random_color(self, row, column, character):
        color = self.color()
        if row < self.array.height and column < self.array.width:
            self.array[row, column] = [color('*')]
        self.screen.render_to_terminal(self.array)

    def make_fancy_star(self):
        row, column = self.random_row_and_column()
        self.place_with_random_color(row, column+1, '*')
        self.place_with_random_color(row+1, column, '*')
        self.place_with_random_color(row+1, column+1, ':')
        self.place_with_random_color(row+1, column+2, '*')
        self.place_with_random_color(row+2, column+1, '*')

    def make_star(self):
        row, column = self.random_row_and_column()
        self.place_with_random_color(row, column, '*')

# actually do the thing!
field = Starfield()
field.populate()
field.listen()
