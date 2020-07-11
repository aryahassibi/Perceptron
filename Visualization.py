from random import uniform
from pygame import draw
from globalVariablesAndFunctions import *


class Point():
    def __init__(self):
        # initializing the point with random x and y values and a constant bias of 1
        self.x = uniform(-1, 1)
        self.y = uniform(-1, 1)
        self.b = 1

        # if the point is above the line, it gets a label of 1
        # and if it is below the line it will get a label of -1
        if (self.y > line_equation(self.x)):
            self.label = 1
        else:
            self.label = -1

        # mapping x and y of the point to screen height and width
        self.mapped_x = int(mapx(self.x, -1, 1, 0, width))
        self.mapped_y = int(mapx(self.y, -1, 1, height, 0))

    def show(self, screen):
        # draws a circle for the given point
        # if the point is above the line, the circle will have black stroke ( label = 1 )
        # and if the point is below the line , the circle will be filled with black color ( label = -1 )

        if self.label == 1:
            draw.circle(screen, (0, 0, 0), (self.mapped_x, self.mapped_y), 8, 2)
        else:
            draw.circle(screen, (0, 0, 0), (self.mapped_x, self.mapped_y), 8)
