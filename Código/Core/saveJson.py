# -*- coding: utf-8 -*-

import turtle

class GoToCommand:
    def __init__(self, x, y, width=1, color="black"):
        self.x = x
        self.y = y
        self.width = width
        self.color = color

    def draw(self, turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.goto(self.x, self.y)

    def __str__(self):
        return '{"Command": "GoTo", "x":"' + str(self.x) + '", "y":"' + \
             str(self.y) + '", "width":"' + str(self.width) + '", "color": "' + str(self.color) + '"}'

class CircleCommand:
    def __init__(self, radius, width=1, color="black"):
        self.radius = radius
        self.width = width
        self.color = color

    def draw(self, turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.circle(self.radius)

    def __str__(self):
        return '{"Command": "Circle", "radius": "' + str(self.radius) + '", "width":"' + str(self.width) + '", "color":"' + str(self.color) + '"}'


class BeginFillCommand:
    def __init__(self, color):
        self.color = color

    def draw(self, turtle):
        turtle.fillcolor(self.color)
        turtle.begin_fill()

    def __str__(self):
        return '{"Command":"BeginFill", "color":"' + str(self.color) +  '"}'

class EndFillCommand:
    def __init__(self):
        pass
    
    def draw (self, turtle):
        turtle.end_fill()

    def __str__(self):
        return '{"Command":"EndFill"}' 

class PenUpCommand:
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.penup()

    def __str__(self):
        return '{"Command":"PenUp"}'

class PenDownCommand:
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.pendown()

    def __str__(self):
        return '{"Command":"PenDown"}'

class PyList:
    def __init__(self):
        self.gcList = []

    def append(self, item):
        self.gcList = self.gcList + [item]

    def removeLast(self):
        self.gcList = self.gcList[:-1]

    def __iter__(self):
        for c in self.gcList:
            yield c

    def __len__(self):
        return len(self.gcList)