from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import itertools

#Atividade
#Construir uma Piramide quadrangular encima do Cubo.

#Global
window = 0
windowTitle = "Atividade X"
rtri = 0.0 # Rotation angle for the triangle.
rquad = 0.0 # Rotation angle for the quadrilateral.
ESCAPE = '\033'
size = 2

###Objetos (Geometrias)

#Cuboso
cubeVertices = ((1,1,1),(1,1,-1),(1,-1,-1),(1,-1,1),(-1,1,1),(-1,-1,-1),(-1,-1,1),(-1,1,-1))
cubeEdges = ((0,1),(0,3),(0,4),(1,2),(1,7),(2,5),(2,3),(3,6),(4,6),(4,7),(5,6),(5,7))
cubeQuads = ((0,3,6,4),(2,5,6,3),(1,2,5,7),(1,0,4,7),(7,4,6,5),(2,3,0,1))

#Piramidosa
piramidVertices = (
	(-0.5 *size,-0.5*size,-0.5*size),
	(0.5*size,-0.5*size,-0.5*size),
	(0.5*size,-0.5*size,0.5*size),
	(-0.5*size,-0.5*size,0.5*size),
	(0.0*size,0.5*size,0.0*size))
piramidEdges = ((0,1),(0,3),(2,1),(2,3),(4,0),(4,1),(4,2),(4,3))
piramidTriangs = ((0,1,2,3),(0,1,4),(0,3,4),(2,1,4),(2,3,4))

color = (1,0.5,1,1)
color2 = (1,0.2,1,1)

def wirePiramid():
	glBegin(GL_LINES)
	for edge in piramidEdges:
		glColor4fv(color)
		for vertex in edge:
			glVertex3f(piramidVertices[vertex][0],piramidVertices[vertex][1],piramidVertices[vertex][2])
	glEnd()

def solidPiramid():
	glBegin(GL_TRIANGLES)
	for piramidTriang in piramidTriangs:
		glColor4fv(color)
		for piramidVertex in piramidTriang:
			glVertex3f(piramidVertices[piramidVertex][0],piramidVertices[piramidVertex][1],piramidVertices[piramidVertex][2])
	glEnd()

def wireCube():
	glBegin(GL_LINES)
	for cubeEdge in cubeEdges:
		#glColor3f()
		for cubeVertex in cubeEdge:
			glVertex3fv(cubeVertices[cubeVertex])
	glEnd()

def solidCube():
	glBegin(GL_QUADS)
	for cubeQuad in cubeQuads:
		glColor4fv(color2)
		for cubeVertex in cubeQuad:
			glVertex3fv(cubeVertices[cubeVertex])
	glEnd()

# A general OpenGL initialization function.  Sets all of the initial parameters.
def InitGL(Width, Height):                	# We call this right after our OpenGL window is created.
	glClearColor(0.0, 0.0, 0.0, 0.0)    	# This Will Clear The Background Color To Black
	glClearDepth(1.0)                    	# Enables Clearing Of The Depth Buffer
	glDepthFunc(GL_LESS)                	# The Type Of Depth Test To Do
	glEnable(GL_DEPTH_TEST)               	# Enables Depth Testing
	glShadeModel(GL_SMOOTH)               	# Enables Smooth Color Shading

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()                    	# Reset The Projection Matrix
											# Calculate The Aspect Ratio Of The Window
	gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

	glMatrixMode(GL_MODELVIEW)

# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
	if Height == 0:                        # Prevent A Divide By Zero If The Window Is Too Small
		Height = 1

	glViewport(0, 0, Width, Height)        # Reset The Current Viewport And Perspective Transformation
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
	glMatrixMode(GL_MODELVIEW)

# The main drawing function.
def DrawGLScene():
	global rtri, rquad
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear The Screen And The Depth Buffer
   
	glLoadIdentity()                    				# Reset The View
	glTranslatef(0,1,-7.0)                			# Move Left And Into The Screen
	glRotatef(rtri,0,1,0)                				# Rotate The Pyramid On It's Y Axis
	solidPiramid()
	
	glLoadIdentity()
	glTranslatef(0,-1,-7)        						# Move Right And Into The Screen
	glRotatef(rquad,0,1,0)        						# Rotate The Cube On X, Y & Z
	solidCube()

	rtri  = rtri + 0.4                 				# Increase The Rotation Variable For The Triangle
	rquad = rquad + 0.4                				# Decrease The Rotation Variable For The Quad


	#  since this is double buffered, swap the buffers to display what just got drawn.
	glutSwapBuffers()

# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)
def keyPressed(*args):
	# If escape is pressed, kill everything.
	if args[0] == ESCAPE:
		sys.exit()

def main():
	
	global window
	
	display = (640, 480)

	glutInit(sys.argv)
	#Select type of Display mode:
	# Double buffer
	# RGBA color
	# Alpha components supported
	# Depth buffer
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

	# get a 640 x 480 window
	glutInitWindowSize(display[0],display[1])
	
	# the window starts at the upper left corner of the screen
	glutInitWindowPosition(0, 0)

	window = glutCreateWindow(windowTitle)

	glutDisplayFunc(DrawGLScene)

	# When we are doing nothing, redraw the scene.
	glutIdleFunc(DrawGLScene)

	# glutFullScreen()

	# Register the function called when our window is resized.
	glutReshapeFunc(ReSizeGLScene)

	# Register the function called when the keyboard is pressed.
	glutKeyboardFunc(keyPressed)

	# Initialize our window.
	InitGL(display[0],display[1])

	# Start Event Processing Engine
	glutMainLoop()

if __name__ == "__main__":
	print("Hit ESC key to quit.")
	main()

