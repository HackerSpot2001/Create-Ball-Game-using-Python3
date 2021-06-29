from tkinter import *
from time import sleep
from random import randrange

root = Tk()
root.geometry("650x600+200+50")
root.title("Moving Boll")
can = Canvas(root,width=650,height=600)
can.pack(fill=BOTH)
# root.minsize(650,500)
class Ball:
    def __init__(self,color):
        self.ball = can.create_oval(15,15,75,75,fill=color)
        self.xspeed= randrange(1,10)
        self.yspeed= randrange(1,10)
        
        
    def moving_ball(self):
        can.move(self.ball,self.xspeed,self.yspeed)
        position = can.coords(self.ball)
        if position[3]>=600 or position[1]<=0:
           self.yspeed = -self.yspeed

        if position[2]>=650 or position[0]<=0:
            self.xspeed = -self.xspeed

ball_one = Ball("green")
ball_two = Ball("red")
ball_three = Ball("blue")
ball_four = Ball("black")
ball_five = Ball("grey")
ball_six = Ball("orange")
ball_seven = Ball("purple")
ball_eight = Ball("yellow")
while True:
    ball_one.moving_ball()
    ball_two.moving_ball()
    ball_three.moving_ball()
    ball_four.moving_ball()
    ball_five.moving_ball()
    ball_six.moving_ball()
    ball_seven.moving_ball()
    ball_eight.moving_ball()
    root.update()
    sleep(0.02)
root.mainloop()






