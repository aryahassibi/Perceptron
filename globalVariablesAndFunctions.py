# This file is for creating functions and initializing variables that are used in multiple files

from random import uniform

# width and height of the Pygame window
width = 600
height = 600

# slope of the line
m = uniform(-1, 1)

# y-intercept of the line
b = uniform(-1, 1)


def mapx(var, minimum, maximum, a, b):
    # The mapx function takes a var in range of (minimum, maximum) and maps it to  range of (a, b)
    # This function is used to map coordinate of points(between (-1, 1) to screen width and height

    mapped_var = (var - minimum) / (maximum - minimum) * (b - a) + a
    return mapped_var


def line_equation(x, map_it=False):
    # The line equation function takes x and returns the slope-intercept based on m and b
    # if map_it was True then it the line function maps the slope-intercept of the line to the height of window
    y = m * x + b
    if map_it:
        mapped_y = int(mapx(y, -1, 1, height, 0))
        return mapped_y
    return y
