import turtle as t

sc=t.Screen()
spositions = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.snake_build()

    def snake_build(self):
        
        for i in spositions:
            self.add_segment(i)
           

    def snake_move(self):
        for  seg_num in range(len(self.segments)-1, 0, -1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(15)
        
    def add_segment(self,position):
        t2 = t.Turtle(shape="square")
        t2.penup()
        t2.color("red")
        t2.goto(position)
        self.segments.append(t2)

    def extend(self):
        self.add_segment(self.segments[-1].position())
        
    def up(self):
        if self.segments[0].heading() == 180:
            self.segments[0].right(90)
        elif self.segments[0].heading() == 0 :
            self.segments[0].left(90)
    def down(self):
        if self.segments[0].heading() == 180:
            self.segments[0].left(90)
        elif self.segments[0].heading() == 0:
            self.segments[0].right(90)
    def left(self):
        if self.segments[0].heading() == 90:
            self.segments[0].left(90)
        elif self.segments[0].heading() == 270:
            self.segments[0].right(90)
    def right(self):
        if self.segments[0].heading() == 270:
            self.segments[0].left(90)
        elif self.segments[0].heading() == 90:
            self.segments[0].right(90)        








