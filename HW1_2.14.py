import math #import the math module
x1,y1,x2,y2,x3,y3 = 1.5,-3.4,4.6,5,9.5,-3.4 #define the value of all of the points of the triangle
print(x1,y1,x2,y2,x3,y3) #print the values to make sure they are correct
s = ((x1*y2)+(x2*y3)+(x3*y1)-(y1*x2)-(y2*x3)-(y3*x1))/2 #perform the evaluation of s
print(s) # print s
