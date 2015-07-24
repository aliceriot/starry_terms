import curtsies
from curtsies import FullscreenWindow, FSArray

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
        numstars = (self.screen.height * self.screen.width) / 10
        for i in range(numstars):
            self.makestar()

    def makestar(self):
        while True:
            row = random.choice(range(self.screen.height))
            column = random.choice(range(self.screen.width))
            if (row, column) in used:
                pass
            else:
                self.array[row, column] = '*'
                self.screen.render_to_terminal(self.array)

# actually do the thing!
field = Starfield()
field.populate()
field.listen()
