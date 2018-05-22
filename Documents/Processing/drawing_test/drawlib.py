# Drawing Routines, like OpenGL
#Ruihan Xu

from matlib import *

numVertex = 0
vStack = []
isOrtho = False
gLeft = -1
gRight = -1
gBottom = -1
gTop = -1
gFov = -1

# These projections do not affect the matrix stack and the current transformation
# matrix!
# FIRST apply T/S/R, THEN apply proj


def gtOrtho(left, right, bottom, top, near, far):
    global isOrtho
    global gLeft
    global gRight 
    global gBottom
    global gTop
    isOrtho = True
    gLeft = left
    gRight = right
    gBottom = bottom
    gTop = top
    

def gtPerspective(fov, near, far):
    global isOrtho
    global gFov
    isOrtho = False
    gFov = fov

def gtBeginShape():
    del vStack[0:]

def gtEndShape():
    global numVertex
    while numVertex > 0:
        v1 = vStack.pop()
        v2 = vStack.pop()
        x1 = (float)(v1[0])
        y1 = (float)(v1[1])
        z1 = (float)(v1[2])
        x2 = (float)(v2[0])
        y2 = (float)(v2[1])
        z2 = (float)(v2[2]) 
        print x1,y1,z1  
        if isOrtho == True:
            x1 = (x1-gLeft)*800/float(gRight-gLeft)
            y1 = (y1-gBottom)*800/float(gTop-gBottom)
            z1 = 0
            x2 = (x2-gLeft)*800/float(gRight-gLeft)
            y2 = (y2-gBottom)*800/float(gTop-gBottom)
            z2 = 0
        else:
            theta = radians(gFov)
            k = (float)(tan(theta/2.0))
            if k == 0:
                k = 1
            #if z1 == 0.0:
                #z1 = 1.0
            #if z2 == 0.0:
                #z2 = 1.0
            x1 = (((x1 / abs(z1))+k)*800)/(float)(2.0*k)
            y1 = (((y1 / abs(z1))+k)*800)/(float)(2.0*k)
            z1 = 0
            x2 = (((x2 / abs(z2))+k)*800)/(float)(2.0*k)
            y2 = (((y2 / abs(z2))+k)*800)/(float)(2.0*k)
            z2 = 0
        print x1,y1,x2,y2
        
        v1 = [x1, y1, z1, 1]
        v2 = [x2, y2, z2, 1]
        
        line(x1, 800-y1, x2, 800-y2)
        #print 800-y1
        
        numVertex = numVertex - 2
        print numVertex
        
#what does square() do exactly? does it push a new matrix on the stack? how the CTM affects the square()?
def gtVertex(x, y, z):
    #y = 800 - y
    myVertex = gtVecMult(mStack[-1],[x,y,z,1])
    vStack.append(myVertex)
    global numVertex 
    numVertex += 1