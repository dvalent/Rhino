import rhinoscriptsyntax as rs
import random as r

r.seed(seed)

class Walker:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        
    def point(self):
        shape = rs.AddPoint(self.x,self.y,self.z)
        return shape
        
    def step(self):
        
        stepX = r.uniform(-1,1)
        stepY = r.uniform(-1,1)
        stepZ = r.uniform(-1,1)
        
        self.x += stepX
        self.y += stepY
        self.z += stepZ

            
            
w = Walker()

pList = []

for t in range(time):
    w.step()
    pList.append(w.point())

a = pList
print pList