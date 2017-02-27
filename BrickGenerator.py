import rhinoscriptsyntax as rs
import random
widths = [1490, 742.5, 230.5]
heights = [295, 175, 115, 55]

lastW = []
lastH = []

bricks =[]

#panelX = 70
#panelY = 50

def row(x,y,counter = 0):
    print 'new height is {}'.format(y)
    selH = heights[random.randint(0,len(heights)-1)]
    lastH.append(selH)
    print 'selected height is {}'.format(lastH[-1])
    for i in range(panelX):
        o = [x,y,0]
        plane = rs.PlaneFromNormal(o,[0,0,1])
        selW = widths[random.randint(0,len(widths)-1)]
        if len(lastW) > panelX and selW == lastW[-panelX]:
            selW = widths[random.randint(0,len(widths)-1)]
        else:
            lastW.append(selW)
            rect = rs.AddRectangle(plane,selW,selH)
            bricks.append(rect)
            x += lastW[-1]+5

    counter += 1
    newx = 0
    newy = sum(lastH)+ 5*len(lastH)
    print 'new y is {}'.format(newy)
    if counter <= panelY:
        print 'continue, count {}'.format(counter)
        row(newx,newy,counter)

row(0,0,0)

a = bricks
