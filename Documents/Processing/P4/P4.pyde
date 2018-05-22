# Project 4 base code (GPU shaders)

def setup():
    global catTexture, bumpTexture
    size(640, 640, P3D)
    noStroke()
    
    catTexture = loadImage("data/cat.png")
    bumpTexture = loadImage("data/bumps.jpg")
    
    loadShaders()

# load the vertex and fragment shaders (four of each)
def loadShaders():
    global shaders
    shaders = []
    names = ["bullseye", "cat", "fractal", "bumps"]
    for i in range(4):
        shader = loadShader("data/shader_" + names[i] + ".frag", "data/shader_" + names[i] + ".vert")
        shaders.append(shader)

# draw the whole scene
def draw():
    
    noLights()
    background(0, 0, 0)
    camera (0, 0, 400, 0, 0, 0, 0, 1, 0)

    pushMatrix()
    
    # rotate the scene based on the mouse position
    dirY = (mouseY / float(height) - 0.5) * 2
    dirX = (mouseX / float(width) - 0.5) * 2
    rotate(-dirY, 1, 0, 0)
    rotate(dirX * 3, 0, 1, 0)
    
    # draw the various shaded quadrilaterals
    ground_plane()
    fractal()
    horizontal_blur()
    bumps()
    bullseye()
    
    popMatrix()

# Draw Quad 0 (Bullseye)
def bullseye():
    fill(200, 30, 200)  # purple indicates a broken shader
    pushMatrix()
    translate(100, 0, 120)
    translate(0, 80, 0)
    scale(0.7, 0.7, 0.7)
    shader(shaders[0])
    beginShape()
    vertex(-100, -100, 0, 0, 0)
    vertex( 100, -100, 0, 1, 0)
    vertex( 100, 100,  0, 1, 1)
    vertex(-100, 100,  0, 0, 1)
    endShape()
    popMatrix()

# Draw Quad 1 (Blur)
def horizontal_blur():
    fill(200, 30, 200)  # purple indicates a broken shader
    pushMatrix()
    translate(-100, 0, 120)
    translate(0, 80, 0)
    scale(0.7, 0.7, 0.7)
    shader(shaders[1])
    textureMode(NORMAL)
    beginShape()
    texture(catTexture)
    vertex(-100, -100, 0, 0, 0)
    vertex( 100, -100, 0, 1, 0)
    vertex( 100, 100,  0, 1, 1)
    vertex(-100, 100,  0, 0, 1)
    endShape()
    popMatrix()

# Draw Quad 2 (Fractal)
def fractal():
    fill(200, 30, 200)  # purple indicates a broken shader
    pushMatrix()
    translate(100, 0, -120)
    translate(0, 80, 0)
    scale(0.7, 0.7, 0.7)
    textureMode(NORMAL)
    shader(shaders[2])
    beginShape()
    vertex(-100, -100, 0, 0, 0)
    vertex( 100, -100, 0, 1, 0)
    vertex( 100, 100,  0, 1, 1)
    vertex(-100, 100,  0, 0, 1)
    endShape()
    popMatrix()

# Draw Quad 3 (Bumps) -- You will need to modify this routine to chop up the quad into pieces
def bumps():
    fill(200, 30, 200)  # purple indicates a broken shader
    pushMatrix()
    translate(-100, 0, -120)
    translate(0, 80, 0)
    translate(0,0,40)
    scale(0.7, 0.7, 0.7)
    rotateZ(radians(180))
    shader(shaders[3])
    textureMode(NORMAL)
    
    c = 40
    b = 200.0/float(c)
    a = float(c)
    
    for i in range(c):
        for j in range(c):
            beginShape()
            texture(bumpTexture)
            # vertex(-100, -100, 0, 0, 0)
            # vertex( 100, -100, 0, 1, 0)
            # vertex( 100, 100,  0, 1, 1)
            # vertex(-100, 100,  0, 0, 1)
    
       
            vertex(100 - b*i, 100-b*j, 0, i/a, j/a)
            vertex(100 - b*(i+1), 100-b*j, 0, (i+1)/a, j/a)
            vertex(100- b*(i+1), 100 - b*(j+1), 0, (i+1)/a, (j+1)/a)
            vertex(100 - b*i, 100 - b*(j+1), 0, i/a, (j+1)/a)
            
            endShape()
    popMatrix()

# Draw the ground plane
def ground_plane():
    noStroke()
    fill(200, 200, 200)
    pushMatrix()
    translate(0, 150, 0)
    rotate(PI/2, 1, 0, 0)
    scale(2.0, 2.0, 2.0)
    resetShader()  # de-activate any shader that was previously in use
    beginShape()
    vertex(-100, -100, 0, 0, 0)
    vertex( 100, -100, 0, 1, 0)
    vertex( 100, 100, 0, 1, 1)
    vertex(-100, 100, 0, 0, 1)
    endShape()
    popMatrix()