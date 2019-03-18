# Will need to install PyOpenGL for these libraries to work.
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

name = 'Python Test Sphere generation'

def main():
	# Setting up window to output on.
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(800, 800)
	glutInitWindowPosition(350, 200)
	glutCreateWindow(name)

	#GL Shader for coloring background and output.
	glClearColor(0.2, 0., 0.2, 1.)
	glShadeModel(GL_SMOOTH)
	
  # Lighting Model
	glEnable(GL_CULL_FACE)
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_LIGHTING)
	lightZeroPosition = [10., 4., 10., 1.]
	lightZeroColor = [1.0, 1.0, 1.0, 1.0]
	glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
	glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
	glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
	glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
	glEnable(GL_LIGHT0)
	
	#Function to display Spheres.
	glutDisplayFunc(displayscene)
    
	# Camera definition
	glMatrixMode(GL_PROJECTION)
	gluPerspective(40., 1., 1., 40.) #angle, aspect ratio, near clip, far clip.
	glMatrixMode(GL_MODELVIEW)
	gluLookAt(0, 0, 10,# camera position
			  0, 0, 0, # where camera points
			  0, 1, 0) # which direction is up
	glPushMatrix()
	
	# Loop for GLUT
	glutMainLoop()
    
	return


# Creating three spheres to look like the water molecule (H2O).
def displayscene():
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glPushMatrix()

  # One Oxygengen Sphere
	colorGray = [1.0, 1.0, 1.0, 1.0]
	glMaterialfv(GL_FRONT, GL_DIFFUSE, colorGray)
	#glTranslatef(0, 0, 0) No need to translate since we start at the center
	glutSolidSphere(2, 100, 20)

	
	# 2 Red Hydrogen Spheres
	colorRed = [1.0, 0.0, 0.0, 1.0]
	glMaterialfv(GL_FRONT, GL_DIFFUSE, colorRed)
	glTranslatef(-2, 2, 0) #left and up 2 units
	glutSolidSphere(0.85, 100, 20)
	
	glMaterialfv(GL_FRONT, GL_DIFFUSE, colorRed)
	glTranslatef(4, 0, 0) #right 4 units
	glutSolidSphere(0.85, 100, 20)
	

	glPopMatrix()
	glutSwapBuffers()
	return

if __name__ == '__main__':
	main()
