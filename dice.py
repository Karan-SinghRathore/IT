from tkinter import *
import random as rd

from turtle import RawTurtle, TurtleScreen

top = Tk()
top.geometry("200x250+50+50")
top.config(bg="black")
top.minsize(200, 250)
top.maxsize(200, 250)

def roll():
    canvas = Canvas(top, width=185, height=180)
    canvas.place(x=5, y=5)
    
    screen = TurtleScreen(canvas)
    screen.bgcolor("red")

    a1 = RawTurtle(screen)
    a1.color("white")
    a1.speed(0)
    a1.shapesize(1)
    a1.up()
    lis = [1, 2, 3, 4, 5, 6]
    output = rd.choice(lis)
    if output == 1:
        a1.shapesize(2)
        a1.shape("circle")
    if output == 2:
        a1.shapesize(2)
        a1.shape("circle")
        a1.bk(30)
        a2 = RawTurtle.clone(a1)
        a2.fd(70)
    if output == 3:
        a1.shapesize(2)
        a1.shape("circle")
        a1.bk(30)
        a1.left(90)
        a1.fd(40)
        a2 = RawTurtle.clone(a1)
        a2.right(90)
        a2.fd(70)
        a3 = RawTurtle.clone(a1)
        a3.bk(50)
        a3.right(90)
        a3.fd(35)

    if output == 4:
        a1.shapesize(2)
        a1.shape("circle")
        a1.bk(30)
        a2 = RawTurtle.clone(a1)
        a2.fd(70)
        
        a4 = RawTurtle.clone(a1)
        a4.shapesize(2)
        a4.shape("circle")
        a3 = RawTurtle.clone(a1)
        a3.fd(70)
        a4.left(90)
        a3.left(90)
        a4.fd(40)
        a3.fd(40)
        a1.right(90)
        a2.right(90)
        a1.fd(40)
        a2.fd(40)
    
    if output == 5:
        a1.shape("circle")
        a2 = RawTurtle.clone(a1)
        a3 = RawTurtle.clone(a1)
        a4 = RawTurtle.clone(a1)
        a5 = RawTurtle.clone(a1)
        a1.goto(-50, 50)
        a2.goto(50, 50)
        a3.goto(-50, -50)
        a4.goto(50, -50)
    
    if output == 6:
        a1.shape("circle")
        a2 = RawTurtle.clone(a1)
        a3 = RawTurtle.clone(a1)
        a4 = RawTurtle.clone(a1)
        a5 = RawTurtle.clone(a1)
        a6 = RawTurtle.clone(a1)
       
        a1.goto(-50, 50)
        a2.goto(50, 50)
        a3.goto(-50, -50)
        a4.goto(50, -50)
        a5.goto(-50, 0)
        a6.goto(50, 0)


Button(top, text="ROLL", command=lambda : roll(), width=22, height=2, bd=5, bg="lightcyan", fg="black", font=("times of roman",10),
            activebackground="skyblue",activeforeground="white", relief= GROOVE).place(x=4, y=200)

mainloop()