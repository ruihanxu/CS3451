def setup():
    size(500,500)
    
def rec_draw(bigR, xc, yc, flag):
    if bigR>1:
        flag+=1
        smallR = (bigR*2 - mouseY*(bigR*2/height)) * 0.7
        if smallR >= bigR*0.7: 
            smallR = bigR*0.7  
        num = 3
        for i in range (num):
            theta = 2 * PI * (i/float(num) + (mouseX/500.0)) - 0.5 * PI
            x = (bigR-smallR) * cos(theta) + xc
            y = (bigR-smallR) * sin(theta) + yc
            if flag%2 == 0:
                fill(255,240,(mouseX*255/width))
            else:
                fill(220,(mouseY*255/height),60)
            ellipse(x,y,smallR*2,smallR*2)
            #print(smallR)
            if flag<9:
                rec_draw(smallR, x, y,flag)
                    
def draw():
    bigR = 250
    xc = 250
    yc = 250
    flag = 0
    noStroke()
    background(255,255,255)
    fill(255,182,193)
    ellipse(xc, yc, bigR*2, bigR*2)
    rec_draw(bigR, xc, yc, flag)
    
    