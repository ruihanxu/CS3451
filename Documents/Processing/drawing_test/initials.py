# In the routine below, you should draw your initials in perspective
#Ruihan Xu

from matlib import *
from drawlib import *

def persp_initials():
    gtInitialize()
    gtTranslate(-70,60,0)
    gtRotateZ(5)
    gtRotateX(25)
    gtRotateY(20)
    gtPerspective(60,0,0)
    name()
    
def name():
    gtBeginShape()
    
    # R
    gtVertex(10,-10,100)
    gtVertex(25,-10,100)
    
    gtVertex(10,-10,100)
    gtVertex(10,-50,100)
    
    gtVertex(25,-10,100)
    gtVertex(25,-25,100)
    
    gtVertex(10,-25,100)
    gtVertex(25,-25,100)
    
    gtVertex(10,-25,100)
    gtVertex(25,-50,100)
    
    #X
    gtVertex(30,-10,100)
    gtVertex(50,-50,100)
    
    gtVertex(50,-10,100)
    gtVertex(30,-50,100)
    
    gtEndShape()