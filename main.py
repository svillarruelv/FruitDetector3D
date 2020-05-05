import sys, pygame
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *

#Archivo para carjar objetos
from obj_loader import *

pygame.init()
viewport = (1280,720)
hx = viewport[0]/2
hy = viewport[1]/2
srf = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)

glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0))
glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
glEnable(GL_LIGHT0)
glEnable(GL_LIGHTING)
glEnable(GL_COLOR_MATERIAL)
glEnable(GL_DEPTH_TEST)
#Sombreado suavecito
glShadeModel(GL_SMOOTH)    

#Cargamos el objeto despues de inicializar pygame
#obj = OBJ("food/cereza/10174_Cherry_v01_l3.obj", swapyz=True)
#obj = OBJ("food/durazno/12203_Fruit_v1_L3.obj", swapyz=True)
#obj = OBJ("food/fresa/Strawberry-L3.obj", swapyz=True)
#obj = OBJ("food/lechuga/10187_LettuceBibb_v1-L2.obj", swapyz=True)
obj = OBJ("food/limon/10187_Lime.obj", swapyz=True)
#obj = OBJ("food/mango/10190_Mango-L3.obj", swapyz=True)
#obj = OBJ("food/manzana/10162_Apple_v01_l3.obj", swapyz=True)
#obj = OBJ("food/maracuya/12206_Fruit_v1_L3.obj", swapyz=True)
#obj = OBJ("food/naranja/12204_Fruit_v1_L3.obj", swapyz=True)
#obj = OBJ("food/palta/10163_Avocado_v2_L3.obj", swapyz=True)
#obj = OBJ("food/pera/10197_Pear.obj", swapyz=True)
#obj = OBJ("food/pinha/10200_Pineapple_v1-L2.obj", swapyz=True)
#obj = OBJ("food/sandia/10211_Watermelon_v1-L3.obj", swapyz=True)
obj.generate()

clock = pygame.time.Clock()

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
width, height = viewport
gluPerspective(90.0, width/float(height), 1, 300.0)
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_MODELVIEW)

rx, ry = (0,0)
tx, ty = (0,0)
zpos = 5
rotate = move = False
while 1:
    clock.tick(30)
    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit()
        elif e.type == KEYDOWN and e.key == K_ESCAPE:
            sys.exit()
        elif e.type == MOUSEBUTTONDOWN:
            if e.button == 4: zpos = max(1, zpos-1)
            elif e.button == 5: zpos += 1
            elif e.button == 1: rotate = True
            elif e.button == 3: move = True
        elif e.type == MOUSEBUTTONUP:
            if e.button == 1: rotate = False
            elif e.button == 3: move = False
        elif e.type == MOUSEMOTION:
            i, j = e.rel
            if rotate:
                rx += i
                ry += j
            if move:
                tx += i
                ty -= j

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(1.,1.,1.,1)
    glLoadIdentity()

    # Renderizamos el objeto
    glTranslate(tx/20., ty/20., - zpos)
    glRotate(ry, 1, 0, 0)
    glRotate(rx, 0, 1, 0)
    obj.render()

    pygame.display.flip()
