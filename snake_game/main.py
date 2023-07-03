import turtle as t
import random as r
from snake import Snake
import time
from food import Food
from scoreb import Score

sc=t.Screen()
sc.setup(600,600)
sc.bgcolor("green")
sc.title("Snake Game !")
sc.tracer(0)

sn=Snake()
fd=Food()
scor=Score()
game_is_on = 1 
sc.listen()
sc.onkey(sn.up,"Up")
sc.onkey(sn.down,"Down")
sc.onkey(sn.left,"Left")
sc.onkey(sn.right,"Right")
while game_is_on:
        sc.update() 
        time.sleep(0.1) 
        sn.snake_move()
        if sn.segments[0].distance(fd) < 15:
                fd.ref()
                scor.scorin()
                sn.extend()
        if sn.segments[0].xcor() > 280 or sn.segments[0].xcor() < -280 or sn.segments[0].ycor() > 280 or sn.segments[0].ycor() < -280 :
                game_is_on=0
                scor.gameover()
        for i in range(1,len(sn.segments)):
                if sn.segments[0].distance(sn.segments[i]) < 10 :
                        game_is_on=0
                        scor.gameover()        

        
                
        
sc.exitonclick()