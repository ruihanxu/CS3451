# Ruihan Xu
# 
# This is the starter code for the CS 3451 Ray Tracing project.
#
# The most important part of this code is the interpreter, which will
# help you parse the scene description (.cli) files.

from oopObjects import *
objects = []
light = []
scene = Scene()

def setup():
    size(300, 300) 
    noStroke()
    colorMode(RGB, 1.0)  # Processing color values will be in [0, 1]  (not 255)
    background(0, 0, 0)

# read and interpret the appropriate scene description .cli file based on key press
def keyPressed():
    refresh()
    if key == '1':
        interpreter("i1.cli")
    elif key == '2':
        interpreter("i2.cli")
    elif key == '3':
        interpreter("i3.cli")
    elif key == '4':
        interpreter("i4.cli")
    elif key == '5':
        interpreter("i5.cli")
    elif key == '6':
        interpreter("i6.cli")
    elif key == '7':
        interpreter("i7.cli")
    elif key == '8':
        interpreter("i8.cli")
    elif key == '9':
        interpreter("i9.cli")
    elif key == '0':
        interpreter("i10.cli")

def interpreter(fname):
    global objects
    global light
    global secne
    surface = None
    obj = None
    
    fname = "data/" + fname
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()

    # parse each line in the file in turn
    for line in lines:
        words = line.split()  # split the line into individual tokens
        if len(words) == 0:   # skip empty lines
            continue
        if words[0] == 'sphere':
            x = float(words[1])
            y = float(words[2])
            z = float(words[3])
            radius = float(words[4])
            obj = Sphere(radius,x,y,z,surface)
            print("add sphere")
            objects.append(obj)
        elif words[0] == 'fov':
            scene.fov = float(words[1])
        elif words[0] == 'background':
            scene.bg = (float(words[1]),float(words[2]),float(words[3]))
        elif words[0] == 'light':
            r,b,g = float(words[1]),float(words[2]),float(words[3])
            x,y,z = float(words[4]),float(words[5]),float(words[6])
            l = Light(x,y,z,r,b,g)
            light.append(l)
            
        elif words[0] == 'surface':
            Car,Cag,Cab = float(words[1]),float(words[2]),float(words[3])
            Cdr,Cdg,Cdb = float(words[4]),float(words[5]),float(words[6])
            Csr,Csg,Csb = float(words[7]),float(words[8]),float(words[9])
            surface = Surface(Car,Cag,Cab,Cdr,Cdg,Cdb,Csr,Csg,Csb,float(words[10]),float(words[11]))
        
        elif words[0] == 'cylinder':
            radius = float(words[1])
            x = float(words[2])
            z = float(words[3])
            ymin = float(words[4])
            ymax = float(words[5])
            obj = Cylinder(radius,x,z,ymin,ymax,surface)
            print("add cylinder")
            objects.append(obj)
        
        elif words[0] == 'write':
            render_scene()    # render the scene
            save(words[1])    # write the image to a file
            pass

# render the ray tracing scene
def render_scene():
    global scene
    
    n = 100.0
    # map fov to viewplane
    top = math.tan(math.radians(scene.fov)/2) * n
    right = top/height * width

    for j in range(height):
        for i in range(width):
            # compute viewing ray
            u = -right + 2.0*right*(i + 0.5)/width
            v = -top + 2.0*top*(j + 0.5)/height
            ray = Ray((u, -v, -n), (0, 0, 0)) #flip v so that y axis points up
            
            hit = getHit(ray,maxt=100)
            
            r,g,b = finalColor(hit,0)
            pix_color = color(r,g,b)  # you should calculate the correct pixel color here
            set(i, j, pix_color)         # fill the pixel with the calculated color

# find the 1st hit point of all objects in the objects[]
def getHit(ray,maxt=100):
    global objects
    t = None
    
    for i in range(len(objects)):
        if objects[i].type == "sphere":
            distance = get_discriminant(ray.d,ray.origin,objects[i].center,objects[i].radius)
            if distance >= 0:
                t1,t2 = getTs(ray.d,ray.origin,objects[i].center,distance)
               
                 # get rid of rounding error
                t1 = 0 if t1 < 0.0001 or t1 > maxt else t1
                t2 = 0 if t2 < 0.0001 or t2 > maxt else t2

                currT = t1 + t2 if t1 * t2 == 0 else min(t1, t2)
            
                if currT>0 and (t==None or t>currT):
                    t = currT
                    hittedobj = objects[i]
                    pt = myVsum(ray.origin, myConsMult(t,ray.d))
                    
        elif objects[i].type == "cylinder":
            obj = objects[i]
            origin = ray.origin
            d = ray.d
            
            t1 = getCbodyT(ray,obj,maxt)
            t2 = getCupT(ray,obj,maxt)
            t3 = getCbottomT(ray,obj,maxt)
            # the postive min
            if any([t1,t2,t3]):
                mint = min(x for x in [t1,t2,t3] if x is not None and x > 0)
                t = mint
                hittedobj = obj
                pt = myVsum(ray.origin, myConsMult(t,ray.d))
    
    if t == None:
        return None
    return Hit(hittedobj,pt,hittedobj.getNormal(pt),ray)

def getCbodyT(ray,obj,maxt):
    origin = ray.origin
    d = ray.d
    
    flag = None
    a = d[0]*d[0] + d[2]*d[2]
    b = 2*(origin[0]-obj.posMin[0])*d[0] + 2*(origin[2]-obj.posMin[2])*d[2]
    c = (origin[0]-obj.posMin[0])**2 + (origin[2]-obj.posMin[2])**2 - obj.radius**2
            
    b24ac = b*b - 4*a*c
    if (b24ac<0):
        return None;
    t0 = (-b + math.sqrt(b24ac))/(2*a)
    t1 = (-b - math.sqrt(b24ac))/(2*a)
            
    # make sure Ts are in the range of scene
    if t1<0.0001 or t1>maxt:
        t1 = 0
    if t0<0.0001 or t0>maxt:
        t0 = 0
        
    t = min(t1,t0)
    if t < 0 and max(t1,t0)>0:
        t = max(t1,t0)
    if t >= 0:
        y = origin[1]+t*d[1] 
        if y > obj.posMin[1] and y < obj.posMax[1]:
            return t
            
    # y is the height
    # y0 = origin[1]+t0*d[1]
    # y1 = origin[1]+t1*d[1]

    # if y1 > obj.posMin[1] and y1 < obj.posMax[1]:
    #     if t0 > 0 and t1 > 0:
    #         flag = min(t0,t1)
    #     else:
    #         flag = None
        
    # return flag

def getCbottomT(ray,obj,maxt):
    x = obj.posMin[0]
    ymin = obj.posMin[1]
    z = obj.posMin[2]
     
    if ray.d[1] != 0:
        t = (ymin - ray.origin[1])/(ray.d[1])
        if t < 0.0001 or t > 100.0:
            t = 0
        #t = t*0.9999
        px = ray.origin[0]+ t*(ray.d[0])
        pz = ray.origin[2]+ t*(ray.d[2])
         
        v = math.sqrt((px-x)**2+ymin*ymin+(pz-z)**2)
        if v <= obj.radius+0.115 and t >0.0001 and t < maxt:
            return t
    return None

def getCupT(ray,obj,maxt):
    x = obj.posMax[0]
    ymin = obj.posMax[1]
    z = obj.posMax[2]
     
    if ray.d[1]-ray.origin[1] != 0:
        t = (ymin - ray.origin[1])/(ray.d[1])
        if t < 0.0001 or t > 100.0:
            t = 0
        #t = t*0.99999
        px = ray.origin[0]+ t*(ray.d[0])
        pz = ray.origin[2]+ t*(ray.d[2])
        
        v = math.sqrt((px-x)**2+ymin**2+(pz-z)**2)
        if v <= obj.radius+0.118 and t > 0.0001 and t < maxt:
            return t
    return None
     

def finalColor(hit,depth):
    global scene
    global light

    if hit == None:
        return scene.bg[0], scene.bg[1], scene.bg[2]

    phong, Krefl = hit.obj.surface.P, hit.obj.surface.Krefl
    v = myNormalize(myVdiff(hit.ray.origin, hit.pt))[0]

    a_color = (0, 0, 0)
    d_color = (0, 0, 0)
    s_color = (0, 0, 0)

    for l in light:
        L, maxt = myNormalize(myVdiff(l.origin, hit.pt))
        H = myNormalize(myVsum(v, L))[0]

        a_color = myVsum(a_color, l.c)

        newN = myConsMult(0.0001, hit.N)
        shadow_hit = getHit(Ray(L, myVsum(hit.pt,newN)), maxt)

        if (shadow_hit == None):
            cL = math.fabs(myDotProduct(hit.N, L))
            d_color = myVsum(d_color, myConsMult(cL, l.c))
            
            cH = math.fabs(myDotProduct(hit.N, H))**phong
            s_color = myVsum(s_color, myConsMult(cH, l.c))

    kd = hit.obj.surface.getCd()
    ka = hit.obj.surface.getCa()
    ks = hit.obj.surface.getCs()

    r = myDotProduct((ka[0], kd[0], ks[0]), (a_color[0], d_color[0], s_color[0]))
    g = myDotProduct((ka[1], kd[1], ks[1]), (a_color[1], d_color[1], s_color[1]))
    b = myDotProduct((ka[2], kd[2], ks[2]), (a_color[2], d_color[2], s_color[2]))
    res = (r, g, b)

    if Krefl > 0 and depth < 100:
        r_ray_d = myVdiff(hit.ray.d, myConsMult(2*myDotProduct(hit.ray.d, hit.N), hit.N))
        r_ray = Ray(r_ray_d, hit.pt)
        r_color = myConsMult(Krefl, finalColor(getHit(r_ray), depth+1))
        res = myVsum(res, r_color)

    return res
    # global scene
    # global light
    
    # if hit == None:
    #     return scene.bg[0],scene.bg[1],scene.bg[2]
    
    # phong, Krefl = hit.obj.surface.P, hit.obj.surface.Krefl
    # v = myNormalize(myVdiff(hit.ray.origin,hit.pt))[0]
    
    # Cd = (0,0,0)
    # Ca = (0,0,0)
    # Cs = (0,0,0)
    
    # for l in light:
    #     # diffuse = Cr*Cl*max(0,N dot L)
    #     # get every component ready except Cr
    #     L, maxt = myNormalize(myVdiff(l.origin, hit.pt))
    #     H = myNormalize(myVsum(v,L))[0]
        
    #     Ca = myVsum(Ca,l.c)
        
    #     newN = myConsMult(0.001, hit.N)
    #     shadowPoint = getHit(Ray(L, myVsum(hit.pt,newN)),maxt)
        
    #     if shadowPoint == None:
    #         Cd_constant = math.fabs(myDotProduct(hit.N,L))
    #         # update (Cl*max(0,N dot L))
    #         Cd = myVsum(Cd, myConsMult(Cd_constant,l.c))
            
    #         Cs_constant = math.fabs(myDotProduct(hit.N,L))**phong
    #         Cs = myVsum(Cs, myConsMult(Cs_constant,l.c))
    
    # kd = hit.obj.surface.getCd()
    # ka = hit.obj.surface.getCa()
    # ks = hit.obj.surface.getCs()

    # r = myDotProduct((ka[0], kd[0], ks[0]), (Ca[0], Cd[0], Cs[0]))
    # g = myDotProduct((ka[1], kd[1], ks[1]), (Ca[1], Cd[1], Cs[1]))
    # b = myDotProduct((ka[2], kd[2], ks[2]), (Ca[2], Cd[2], Cs[2]))
    # res = (r,g,b)
    
    # #recursively get the reflection color
    # if Krefl>0 and depth<100:
    #     reflDirection = myVdiff(hit.ray.d, myConsMult(2*myDotProduct(hit.ray.d,hit.N),hit.N))
    #     reflRay = Ray(reflDirection, hit.pt)
    #     reflColor = myConsMult(Krefl, finalColor(getHit(reflRay),depth+1))
    #     res = myVsum(res,reflColor)
    
    # return res

def refresh():
    global objects
    global light
    global scene
    objects = []
    light = []
    scene = Scene()
    
# should remain empty for this assignment
def draw():
    pass