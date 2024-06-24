# Python program to draw star 
# using Turtle Programming 
import turtle 
star = turtle.Turtle() 

star.right(75) 
star.forward(100) 

for i in range(5): 
	star.right(60) 
	star.forward(100) 
	
turtle.done() 
