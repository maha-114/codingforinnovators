# Drawing a Polygon in turtle-Python  
  
from turtle import *   
import turtle as turt  
  
tr = turt.Turtle()  
  
# Total No. of sides of the polygon to be drawn  
side = int(input("The number of sides the Polygon should have is : "))  
  
# Total Length of each side of the polygon to be drawn  
lngth = int(input("The length of each side the Polygon should have is : "))  
  
for j in range(side):  
  tr.forward(lngth)  
  tr.right(360/side)  
