# !!!!!READ ME!!!!!!
# The music is really important! 
# To import the Minim library, go sketchpad->library->add library
# and search for minim
# thank you~ hope you like it

import math
add_library("minim")

time = 0   # use time to move objects from one frame to the next

def setup():
    size (800, 800, P3D)
    perspective (60 * PI / 180, 1, 0.1, 1000)  # 60 degree field of view
    global bg
    bg = loadImage("bgimg.jpg")
    
    minim = Minim(this)
    sf=minim.loadFile("Papillon.mp3")
    sf.play()
    
    # heart shape
    global s
    s = loadShape("Heart.obj")
    
def draw():
    global time
    
    time += 0.01
    # position the virtual camera
    if time > 4.2 and time < 7.2:
        camera (-100, 0, 100, 0, 0, 0, 0,  1, 0)
    elif time > 7.2 and time < 9.2:
        camera (100,-50,100,0,0,0,0,1,0)
    elif time > 9.2 and time < 11.2:
        camera (100, 0, 100, 0, 0, 0, 0,  1, 0)
    elif time > 14 and time < 15:
        camera (0,0,80,-10,0,0,0,1,0)
    else:
        camera (0, 0, 100, 0, 0, 0, 0,  1, 0)

    background (bg)  # clear screen and set background to white
    
    # create a light source
    ambientLight(50, 50, 50);
    directionalLight(200*time*0.5, 102, 126, -1, 0, 0);
    directionalLight(200*time*0.5, 102, 0, 1, 0, 0);
    lightSpecular(255, 255, 255)
    directionalLight (100, 100, 100, -0.3, 0.5, -1)
    
    # background objects
    if time > 1.4:
        pushMatrix()
        specular(0,0,0)
        shininess(30.0)
        fl()
        popMatrix()
    
        pushMatrix()
        specular(time*10,250-time,time)
        shininess(5.0)
        translate(-50,-50,-10)
        scale(.9,.9,.9)
        rotateY(time)
        light(250,0,0)
        popMatrix()
        
        pushMatrix()
        specular(time,time*10,250-time)
        shininess(5.0)
        translate(-30,-30,-10)
        scale(.5,.5,.5)
        rotateY(time)
        light(125,125,125)
        popMatrix()
        
        pushMatrix()
        specular(200,250-time*10,100)
        shininess(5.0)
        translate(30,-40,0)
        scale(.9,.9,.9)
        rotateY(time)
        light(100,0,245)
        popMatrix()
        
        pushMatrix()
        specular(time*50,100,100-time*10)
        shininess(5.0)
        translate(15,-15,20)
        scale(.5,.5,.5)
        rotateY(time)
        light(125,125,125)
        popMatrix()
        
        pushMatrix()
        specular(255,0,0)
        shininess(10.0)
        translate(50,-45,10)
        scale(1,1,1)
        rotateY(time)
        light(100,100,250)
        popMatrix()
    
    noStroke()
    specular (255,255,255)
    shininess (20.0)
    
    # 1.scanline to find the kitty, time<1.3
    if time*600< height:
        pushMatrix()
        stroke(226, 204, 0)
        line(-width/2,time*100-50,width,time*100-50)
        popMatrix()
    
    # 2.zoom in the camera to found the kitty, time<2.3
    if time*600>=height and (time-1.3)*5<5:
        translate(0,10,10)
        scale(0.1,0.1,0.1)    
        scale(5*(time-1.3),5*(time-1.3),5*(time-1.3))
        kitty(time,0)
    
    # 3. hold to prepare and say hi
    if time > 2.3 and time <4.2:
        translate(0,10,10)
        scale(.5,.5,.5)
        kitty(time,0)
        
    # 4. rotate
    if time >=4.2 and time <9.2:
        if time>4.4 and time<5:
            rotateY(radians((4.5-4.2)/0.5*36))
        elif time>5.4 and time<6:
            rotateY(radians((5.5-4.2)/0.5*36))
        elif time>6.4 and time<7:
            rotateY(radians((6.5-4.2)/0.5*36))
        elif time>7.4 and time<8:
            rotateY(radians((7.5-4.2)/0.5*36))
        elif time>8.4 and time<9:
            rotateY(radians((8.5-4.2)/0.5*36))
        else: 
            rotateY(radians((time-4.2)/0.5*36))
        translate(0,10,10)
        scale(.5,.5,.5)
        kitty(time,0)    
    
    # 5. raise hand and jump
    if time > 9.2 and time < 11.2:
        camera (100, 0, 100, 0, 0, 0, 0,  1, 0)
        translate(10,10,10)
        translate(20*(time-9.2),0,0)
        scale(.5,.5,.5)
        kitty(time,0)
    if time >= 11.2 and time < 15:
        translate(10,10,10)
        translate(20*(11.2-9.2)-20*(time-11.2),0,0)
        scale(.5,.5,.5)
        kitty(time,0)  
    
    # another cat
    if time >=15 and time <17:
        pushMatrix()
        translate(40-10*(time-15),10,10)
        scale(.5,.5,.5)
        kitty(time,1)
        popMatrix()
        
        pushMatrix()
        translate(10,10,10)
        translate(-10*(15-11.2),0,0)
        scale(.5,.5,.5)
        kitty(time,0)
        popMatrix()
    
    # blue one turn around
    if time > 17 and time  <= 18:
        pushMatrix()
        translate(40-10*(17-15),10,10)
        scale(.5,.5,.5)
        rotateY(radians(-90)*(time-17))
        kitty(time,1)
        popMatrix()
        
        pushMatrix()
        translate(10,10,10)
        translate(-10*(15-11.2),0,0)
        scale(.5,.5,.5)
        kitty(time,0)
        popMatrix()
    
    # pink turn around
    if time > 18 and time <19:
        pushMatrix()
        translate(40-10*(17-15),10,10)
        scale(.5,.5,.5)
        rotateY(radians(-90))
        kitty(time,1)
        popMatrix()
        
        pushMatrix()
        translate(10,10,10)
        translate(-10*(15-11.2),0,0)
        scale(.5,.5,.5)
        rotateY(radians(90)*(time-18))
        kitty(time,0)
        popMatrix()
        
    # eye to heart
    if time>19 and time < 20:
        pushMatrix()
        translate(40-10*(17-15),10,10)
        scale(.5,.5,.5)
        rotateY(radians(-90))
        kitty(time,1)
        popMatrix()
        
        pushMatrix()
        translate(10,10,10)
        translate(-10*(15-11.2),0,0)
        scale(.5,.5,.5)
        rotateY(radians(90))
        kitty(time,0)
        popMatrix()
        
    # last dance
    if time>20 and time < 30:
        pushMatrix()
        translate(32-10*(17-15),10,10)
        scale(.5,.5,.5)
        kitty(time,1)
        popMatrix()
        
        pushMatrix()
        translate(10,10,10)
        translate(-7*(15-11.2),0,0)
        scale(.5,.5,.5)
        kitty(time,0)
        popMatrix()
        
        
def light(r,g,b):
    fill(r,g,b)
    pushMatrix()
    sphereDetail(8)
    sphere(10)
    popMatrix()
    
def fl():
    fill(100,100,100)
    pushMatrix()
    translate(0,30,20)
    box(150,5,100)
    popMatrix()
    
def heart():
    fill(255,0,0)
    pushMatrix();
    scale(10,10,10)
    shape(s);
    popMatrix();
    
def kitty(time,gender):
    noStroke()
    # head
    fill (255,255,255)
    pushMatrix()
    translate(0,-10,0)
    scale(3, 2.5, 2.5)
    sphereDetail(60)
    sphere(10)
    popMatrix()
    
    #fill (0,0,0)
    for i in range (3):
        pushMatrix()
        if ((time >1.3 and time < 14) or (time>=15 and time <=17) or (time>20 and time<30)) and int(time*100)%20 == 0:
            rotateX(radians(-20))
        #rotateY (time)
        translate (-25, -5+5*i, 20)  # move up and down
        rotateZ(radians(10 - i*10))
        scale (1, .01, .01)
        sphereDetail(60)  # this controls how many polygons are used to make a sphere
        sphere(10)
        popMatrix()
        
    fill (0,0,0)
    for i in range (3):
        pushMatrix()
        if ((time >1.3 and time < 14) or (time>=15 and time <=17) or (time>20 and time<30)) and int(time*100)%20 == 0:
            rotateX(radians(-20))
        #rotateY (time)
        translate (25, -5+5*i, 20)  # move up and down
        rotateZ(radians(-10 + i*10))
        scale (1, .01, .01)
        sphereDetail(60)  # this controls how many polygons are used to make a sphere
        sphere(10)
        popMatrix()
        
    # black eye1
    if time > 19:
        fill(250,0,0)
    else:
        fill (0, 0, 0)
    pushMatrix()
    #rotateY (time)
    if ((time >1.3 and time < 14) or (time>=15 and time <=17) or (time>20 and time<30)) and int(time*100)%20 == 0:
        rotateX(radians(-20))
    translate(-8,-10,25)
    scale (0.5, 0.8, 0.5)
    if time >=14 and time <=14.3:
        scale(1,0.2,1)
    sphereDetail(60)
    sphere(10)
    popMatrix()
    
    # black eye2
    if time > 19:
        fill(250,0,0)
    else:
        fill (0, 0, 0)
    pushMatrix()
    if ((time >1.3 and time < 14) or (time>=15 and time <=17) or (time>20 and time<30)) and int(time*100)%20 == 0:
        rotateX(radians(-20))
    #rotateY (time)
    translate(8,-10,25)
    scale (0.5, 0.8, 0.5)
    sphereDetail(60)
    sphere(10)
    popMatrix()
    
    # nose
    fill (0, 0, 0)
    pushMatrix()
    if ((time >1.3 and time < 14) or (time>=15 and time <=17) or (time>20 and time<30)) and int(time*100)%20 == 0:
        rotateX(radians(-20))
    #rotateY (time)
    translate(0,0,25)
    scale (0.2, 0.1, 0.2)
    sphereDetail(60)
    sphere(10)
    popMatrix()
    
    # ear
    fill (255,255,255)
    pushMatrix()
    #rotateY (time)
    if ((time >1.3 and time < 14) or (time>=15 and time <=17) or (time>20 and time<30)) and int(time*100)%20 == 0:
        rotateX(radians(-20))
    translate (-15, -30, 10)
    rotateX(45)
    scale (10, 10, 10)
    cone()
    popMatrix()
    
    # ear2
    fill (255,255,255)
    pushMatrix()
    if ((time >1.3 and time < 14) or (time>=15 and time <=17) or (time>20 and time<30)) and int(time*100)%20 == 0:
        rotateX(radians(-20))
    #rotateY (time)
    translate (15, -30, 10)
    rotateX(45)
    scale (10, 10, 10)
    cone()
    popMatrix()

    # body
    if (gender == 0):
        fill (240,100,100)
    if (gender == 1):
        fill (100,100,250)
    pushMatrix()
    translate (0, 20, 0)
    rotateX(radians(90))
    scale (10, 10, 10)
    if time>4.5 and time<4.7:
        scale(1,1,1*(1-(time-4.5)*2))
    if time>5.5 and time<5.7:
        scale(1,1,1*(1-(time-5.5)*2))
    if time>6.5 and time<6.7:
        scale(1,1,1*(1-(time-6.5)*2))
    if time>7.5 and time<7.7:
        scale(1,1,1*(1-(time-7.5)*2))
    if time>8.5 and time<8.7:
        scale(1,1,1*(1-(time-8.5)*2))
    cylinder()
    popMatrix()
    
    #arm left
    fill (255,255,255)
    pushMatrix()
    #rotateY (time)
    translate (-15, 18, 0)  # move up and down
    rotateY(radians(40))
    global finalPos
    if time>2.5 and time<2.9:
        rotateZ(radians(20*(time*4-2.5*4)))
        finalPos = 20*(time*4-2.5*4)
    if time>=2.8 and time<3.3:
        rotateZ(radians(finalPos-20*(time*4-2.5*4)))
    if time>2.5 and time<2.9:
        rotateZ(radians(20*(time*4-2.5*4)))
        finalPos = 20*(time*4-2.5*4)
        
    if time>9.5 and time<10:
        rotateZ(radians(20*(time*4-2.5*4)))
        finalPos = 20*(time*4-2.5*4)
    if time>=10 and time<10.5:
        rotateZ(radians(finalPos-20*(time*4-2.5*4)))
    if time>10.1 and time<10.4:
        rotateZ(radians(20*(time*4-2.5*4)))
        finalPos = 20*(time*4-2.5*4)
    if time>=10.4 and time<10.8:
        rotateZ(radians(finalPos-20*(time*4-2.5*4)))
    if time>10.8 and time<11.2:
        rotateZ(radians(20*(time*4-2.5*4)))
        finalPos = 20*(time*4-2.5*4)
    if time>=11.2 and time<11.6:
        rotateZ(radians(finalPos-20*(time*4-2.5*4)))

    scale (1, .5, .5)
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(10)
    popMatrix()
    
    #arm right
    fill (255,255,255)
    pushMatrix()
    #rotateY (time)
    translate (15, 18, 0)  # move up and down
    rotateY(radians(140))
    global finalPos
    if time>=3.3 and time<3.75:
        rotateZ(radians(20*(time*4-3.3*4)))
        finalPos = 20*(time*4-3.3*4)*1.5
    if time>=3.7 and time<4.2:
        rotateZ(radians(finalPos-20*(time*4-3.3*4)))
        
    if time>9.5 and time<9.8:
        rotateZ(radians(20*(time*4-2.5*4)))
        finalPos = 20*(time*4-2.5*4)
    if time>=9.8 and time<10.1:
        rotateZ(radians(finalPos-20*(time*4-2.5*4)))
    if time>10.1 and time<10.4:
        rotateZ(radians(20*(time*4-2.5*4)))
        finalPos = 20*(time*4-2.5*4)
    if time>=10.4 and time<10.8:
        rotateZ(radians(finalPos-20*(time*4-2.5*4)))
    if time>10.8 and time<11.2:
        rotateZ(radians(20*(time*4-2.5*4)))
        finalPos = 20*(time*4-2.5*4)
    if time>=11.2 and time<11.6:
        rotateZ(radians(finalPos-20*(time*4-2.5*4)))
        
    scale (1, .5, .5)
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(10)
    popMatrix()
    

# cylinder with radius = 1, z range in [-1,1]
def cylinder(sides = 64):
    # first endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, -1)
    endShape(CLOSE)
    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, 1)
    endShape(CLOSE)
    # sides
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal (x1, y1, 0)
        vertex (x1, y1, 1)
        vertex (x1*2, y1*2, -1)
        normal (x2, y2, 0)
        vertex (x2*2, y2*2, -1)
        vertex (x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2

def cone(sides = 64):
    # first endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, -1)
    endShape(CLOSE)
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal (x1, y1, 0)
        vertex (0, 0, 1)
        vertex (x1, y1, -1)
        normal (x2, y2, 0)
        vertex (x2, y2, -1)
        vertex (0, 0, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2
        
def pyrimaid():
    beginShape()
    vertex(-100, -100, -100)
    vertex( 100, -100, -100)
    vertex(   0,    0,  100)

    vertex( 100, -100, -100)
    vertex( 100,  100, -100)
    vertex(   0,    0,  100)

    vertex( 100, 100, -100)
    vertex(-100, 100, -100)
    vertex(   0,   0,  100)

    vertex(-100,  100, -100)
    vertex(-100, -100, -100)
    vertex(   0,    0,  100)
    endShape()
    
    