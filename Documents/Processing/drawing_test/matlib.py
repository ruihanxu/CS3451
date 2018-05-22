# Matrix Stack Library -- Use your code from Project 1A
#Ruihan Xu

mStack = []

def gtInitialize():
    matrix = [[1, 0, 0, 0], 
              [0, 1, 0, 0], 
              [0, 0, 1, 0], 
              [0, 0, 0, 1]]
    del mStack[0:len(mStack)]
    mStack.append(matrix)
    

def gtPushMatrix():
    newM = mStack[-1]
    mStack.append(newM)

def gtPopMatrix():
    if(len(mStack)==1):
        print("cannot pop the matrix stack")
    else:
        mStack.pop()

# helper to do multiplication    
def gtMult(CTM, trans):
    newM = [[0 for x in range(4)] for y in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                newM[i][j] += CTM[i][k]*trans[k][j]
    return newM

def gtVecMult(CTM, v):
    newM = [0, 0, 0, 0]
    for i in range(4):
        for k in range(4):
            newM[i] += CTM[i][k] * v[k]
    return newM

def gtTranslate(x, y, z):
    T = [[1,0,0,x],
         [0,1,0,y],
         [0,0,1,z],
         [0,0,0,1]]
    newM = gtMult(mStack[-1],T)
    mStack[-1] = newM

def gtScale(x, y, z):
    S = [[x,0,0,0],
         [0,y,0,0],
         [0,0,z,0],
         [0,0,0,1]]
    newM = gtMult(mStack[-1],S)
    mStack[-1] = newM

#rotate around X means x is unchanged
def gtRotateX(angle):
    theta = radians(angle)
    Rx = [[1,0,0,0],
          [0,cos(theta),-sin(theta),0],
          [0,sin(theta),cos(theta),0],
          [0,0,0,1]]
    newM = gtMult(mStack[-1],Rx)
    mStack[-1] = newM

def gtRotateY(angle):
    theta = radians(angle)
    Ry = [[cos(theta),0,sin(theta),0],
          [0,1,0,0],
          [-sin(theta),0,cos(theta),0],
          [0,0,0,1]]
    newM = gtMult(mStack[-1],Ry)
    mStack[-1] = newM

def gtRotateZ(angle):
    theta = radians(angle)
    Rz = [[cos(theta),-sin(theta),0,0],
          [sin(theta),cos(theta),0,0],
          [0,0,1,0],
          [0,0,0,1]]
    newM = gtMult(mStack[-1],Rz)
    mStack[-1] = newM