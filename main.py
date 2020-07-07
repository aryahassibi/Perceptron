from Perceptron import *
from Visualization import *
import pygame
from globalVariablesAndFunctions import *

# initializing pygame
pygame.init()

# creating the screen
size = [width, height]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Perceptron")

# colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (100, 150, 255)
GREEN = (100, 255, 100)
RED = (255, 100, 100)

# create instance of the Perceptron class
p = Perceptron()

points = []
numberOfPoints = 0
trainingIndex = 0
done = False

while (not done):

    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # adding a new point to the screen
    points.append(Point())
    numberOfPoints += 1

    # showing every point on screen
    for pt in points:
        pt.show(screen)

    # training all the point at once ( one loop )
    for pt in points:
        inputs = [pt.x, pt.y, pt.b]
        target = pt.label

        # training each point
        p.train(inputs, target)

        # predicting label of the point
        prediction = p.predict(inputs)

        # showing a green dot for point that are being classified correctly
        # and a red dot for point that are not
        if prediction == target:
            pygame.draw.circle(screen, GREEN, (pt.mappedx, pt.mappedy), 2)
        else:
            pygame.draw.circle(screen, RED, (pt.mappedx, pt.mappedy), 2)

    # predicted_slope = -(p.weights[0] / p.weights[1])
    # predicted_y_intecept = -(p.weights[2] / p.weights[1])

    # drawing the desired line
    pygame.draw.line(screen, GRAY, (0, line_equation(-1, True)), (width, line_equation(1, True)), 1)

    # drawing the predicted line
    pygame.draw.line(screen, BLUE, (0, p.predicted_line(-1)), (width, p.predicted_line(1)), 5)
    pygame.display.flip()

pygame.quit()
