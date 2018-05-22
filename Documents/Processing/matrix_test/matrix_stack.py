# Matrix Stack Library

# you should modify the routines below to complete the assignment

mStack = []

def gtInitialize():
    for i in range(len(mStack)):
        mStack.pop()
    mStack.append(
              [[1,0,0,0],
              [0,1,0,0],
              [0,0,1,0],
              [0,0,0,1]]
              )
    
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

def gtTranslate(x, y, z):
    T = [[1,0,0,x],
         [0,1,0,y],
         [0,0,1,z],
         [0,0,0,1]]
    newM = gtMult(mStack[-1],T)
    mStack.append(newM)

def gtScale(x, y, z):
    S = [[x,0,0,0],
         [0,y,0,0],
         [0,0,z,0],
         [0,0,0,1]]
    newM = gtMult(mStack[-1],S)
    mStack.append(newM)

#rotate around X means x is unchanged
def gtRotateX(angle):
    theta = radians(angle)
    Rx = [[1,0,0,0],
          [0,cos(theta),-sin(theta),0],
          [0,sin(theta),cos(theta),0],
          [0,0,0,1]]
    newM = gtMult(mStack[-1],Rx)
    mStack.append(newM)

def gtRotateY(angle):
    theta = radians(angle)
    Ry = [[cos(theta),0,sin(theta),0],
          [0,1,0,0],
          [-sin(theta),0,cos(theta),0],
          [0,0,0,1]]
    newM = gtMult(mStack[-1],Ry)
    mStack.append(newM)

def gtRotateZ(angle):
    theta = radians(angle)
    Rz = [[cos(theta),-sin(theta),0,0],
          [sin(theta),cos(theta),0,0],
          [0,0,1,0],
          [0,0,0,1]]
    newM = gtMult(mStack[-1],Rz)
    mStack.append(newM)

def gtGetMatrix():
    return mStack[-1]

def print_ctm():
    for stack in mStack[-1]:
        print(stack)
    print("\n")

def print_m():
    print(mStack)