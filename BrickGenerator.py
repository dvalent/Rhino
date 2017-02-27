import rhinoscriptsyntax as rs
import random
widths = [1490, 742.5, 230.5]
heights = [295, 175, 115, 55]
lastW = []
lastH = []
bricks =[]

def row(x,y,counter = 0):
    print 'new height is {}'.format(y)
    selH = heights[random.randint(0,len(heights)-1)]
    lastH.append(selH)
    print 'selected height is {}'.format(lastH[-1])
    for i in range(70):
        o = [x,y,0]
        plane = rs.PlaneFromNormal(o,[0,0,1])
        selW = widths[random.randint(0,len(widths)-1)]
        lastW.append(selW)
        rect = rs.AddRectangle(plane,selW,selH)
        bricks.append(rect)
        x += lastW[-1]+5

    counter += 1
    newx = 0
    newy = sum(lastH)+ 5*len(lastH)
    print 'new y is {}'.format(newy)
    if counter <= 50:
        print 'continue, less than'
        row(newx,newy,counter)

row(0,0,0)

a = bricks
