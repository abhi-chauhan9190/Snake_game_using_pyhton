from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color('yellow')
        self.speed(100)
        rx=random.randint(-280,280)
        ry=random.randint(-280,260)
        self.goto(rx,ry)
    def ref(self):
        rx=random.randint(-280,280)
        ry=random.randint(-280,280)
        self.goto(rx,ry)



