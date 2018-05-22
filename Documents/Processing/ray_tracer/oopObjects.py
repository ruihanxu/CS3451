# Ruihan Xu

import math

class Scene:
    def __init__(self):
        self.fov = 0
        self.bg = (0,0,0)
class Light:
    def __init__(self,x,y,z,r,g,b):
        self.c = (r,g,b)
        self.origin = (x,y,z)
class Surface:
    def __init__(self,Car,Cag,Cab,Cdr,Cdg,Cdb,Csr,Csg,Csb,P,Krefl):
        self.Car = Car  # partb
        self.Cag = Cag
        self.Cab = Cab
        
        self.Cdr = Cdr
        self.Cdg = Cdg
        self.Cdb = Cdb

        self.Csr = Csr # partb
        self.Csg = Csg
        self.Csb = Csb

        self.P = P
        self.Krefl = Krefl
    def getCa(self):
        return (self.Car,self.Cag,self.Cab)
    def getCd(self):
        return (self.Cdr,self.Cdg,self.Cdb)
    def getCs(self):
        return (self.Csr,self.Csg,self.Csb)
    
class Sphere:
    def __init__(self,radius,x,y,z,surface):
        self.center = (x,y,z)
        self.radius = radius
        self.surface = surface
        self.type = "sphere"
    def getNormal(self,pt):
        return myNormalize(myVdiff(pt,self.center))[0]
        
class Cylinder: # part2
    def __init__(self,radius,x,z,ymin,ymax,surface):
        self.radius = radius
        self.posMin = (x,ymin,z)
        self.posMax = (x,ymax,z)
        self.surface = surface
        self.type = "cylinder"
    def getNormal(self,pt):
        x = self.posMin[0]
        z = self.posMin[2]
        y = pt[1]
        if y <= self.posMin[1]:
            return (0,-1,0)
        elif y >= self.posMax[1]:
            return (0,1,0)
        else:
            return myNormalize((pt[0]-x,0,pt[2]-z))[0]        
class Ray:
    def __init__(self,d,origin):
        self.d = d
        self.origin = origin
        
# things needed:
# 1. light param <-- global
# 2. shape <--N
# 3. material param <--obj's surface tuple
# 4. eyeray <--ray
# 5. overall the color is the color of one point, so need hitted pt
class Hit:
    def __init__(self,obj,pt,N,ray):
        self.obj = obj
        self.N = N
        self.pt = pt
        self.ray = ray
        
# math
def myNormalize(v):
    myLen = math.sqrt(myDotProduct(v,v))
    myVec = (v[0]/myLen,v[1]/myLen,v[2]/myLen)
    return myVec,myLen
def myConsMult(c, v):
    return (c*v[0], c*v[1], c*v[2])
def myVsum(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2])
def myVdiff(v1, v2):
    return (v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2])
def myDotProduct(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]
def getTs(d, e, c, dis):
    v = myVdiff(e, c)
    c1 = myDotProduct(d, v)
    c2 = myDotProduct(d, d)
    return (-c1+math.sqrt(dis))/c2, (-c1-math.sqrt(dis))/c2
def get_discriminant(d, e, c, R):
    v = myVdiff(e, c)
    c1 = myDotProduct(d, v)
    c2 = myDotProduct(d, d) * (myDotProduct(v, v) - R*R)
    return c1*c1 - c2
    