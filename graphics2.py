import turtle  
# Creating turtle  
t = turtle.Turtle()  
  
turtle.bgcolor("yellow")  
turtle.pensize(2)  
turtle.speed(0)  
  
while (True):  
    for i in range(3):  
        for colors in ["red", "magenta", "black"]:  
            turtle.color(colors)  
            turtle.circle(100)  
            turtle.left(10)  
  
  
turtle.hideturtle()  
turtle.mainloop()  
