from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        
        self.hideturtle()
        self.update_board()
    def update_board(self):
        self.goto(-100,260)
        self.write(f"Score is : {self.score}" , "left" , font=('Arial', 24, 'normal'))

    def scorin(self):
        self.score+=1
        self.clear()
        self.update_board()
    def gameover(self):
        self.goto(-100,0)
        self.write("Game Over !!!" , "center" , font=('Arial', 25, 'normal'))

        

        