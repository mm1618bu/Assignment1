import math
x1,y1,x2,y2,x3,y3 = 1.5,-3.4,4.6,5,9.5,-3.4
print(x1,y1,x2,y2,x3,y3)
side1 = y1-x1
side2 = y2-x2
side3 = y3-x3
print(side1, side2, side3)

s = (side1+side2+side3)/2
area = s*(s-side1)*(s-side2)*(s-side3)
print(s)
print(area)
