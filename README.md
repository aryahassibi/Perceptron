# Perceptron
> In machine learning, the perceptron is an algorithm for supervised learning of binary classifiers. A binary classifier is a function which can decide whether or not an input, represented by a vector of numbers, belongs to some specific class. [Wikipedia](https://en.wikipedia.org/wiki/Perceptron)

This Perceptron is written in Python(3.7.6) and the problem has been visualized using the Pygame(1.9.6) library.
![PerceptronGIF](https://user-images.githubusercontent.com/31355913/86508503-cea86100-bdf5-11ea-87d7-b571734cb31c.gif)
## Visualization
1. Darwing a random line on the screen<br>
    > This line is invisible in the video

2. Putting random points on the screen 
    > the points above the line are shown with an empty circle ○ <br>
    > the points below the line are shown with a filled circle **•**

3. Showing the predicted line by perceptron <br>
    > the points that are classified correctly by the predicted line turn **green**<br>
    > the points that are not classified correctly turn **red**
    
4. The predicted line moves until it matches the desired line

> *note:* to see the visualization run **main.py**

### *HOW TO WORK WITH Perceptron.py:*
1. Import Class
    
        from Perceptron import *
    
2. Create an Object

        p = Perceptron()
        
    You can also change the numebr of input layer nodes by giving perceptron number_of_input_nodes:
    
        p = Perceptron(5)
        
3. Train perceptron

        p.train(inputs, target)
        
     For example, this time our inputs are coordinates of points and their bias : (x, y, 1)<br>
     and the target is the label of the point (whether it is above or below the line)
     
        inputs = [point.x, point.y, point.bias]
        target = point.label
     

4. get the slope-intercept of the predicted line

        p.predicted_line(x)
        
