
#finding type of triangle with the given coordinates

from math import sqrt

x1 = float(raw_input('x1:'))
y1 = float(raw_input('y1:'))
x2 = float(raw_input('x2:'))
y2 = float(raw_input('y2:'))
x3 = float(raw_input('x3:'))
y3 = float(raw_input('y3:'))

side1 = sqrt((x1-x2)**2 + (y1-y2)**2)
side2 = sqrt((x2-x3)**2 + (y2-y3)**2)
side3 = sqrt((x3-x1)**2 + (y3-y1)**2)

tri = [side1, side2, side3]

tri.sort()

if tri[0]< tri[1]+tri[2]:
    if tri[0] == tri[2]:
        print 'its an equilateral triangle'
    elif tri[0] == tri[1] or tri[1] == tri[2]:
        print 'its an isosceles triangle'
    else:
        print 'its a scelen traingle'
else:
    print 'its not a triangle'
