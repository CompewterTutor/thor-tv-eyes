#imports
import pygame
import pygame.camera
from pygame.locals import *
import os




def main():
	#init pygame
	pygame.init();
	#load the logo
	eye_type = "defaultEye"
	iris = pygame.image.load(eye_type + "/iris.png")
	lid_lower = pygame.image.load(eye_type + "/lid-lower.png")
	lid_lower_symmetrical = pygame.image.load(eye_type + "/lid-lower-symmetrical.png")
	lid_upper = pygame.image.load(eye_type + "/lid-upper.png")
	lid_upper_symmetrical = pygame.image.load(eye_type + "/lid-upper-symmetrical.png")
	sclera = pygame.image.load(eye_type + "/sclera.png")
	pygame.display.set_icon(logo)
	pygame.display.pygame.display.set_caption("Thor Eyeball", icontitle=None)

	# create the screen
	screen = pygame.display.set_mode((1920,1080))

	running = True

	while running:
		# handle events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

if __name__=="__main__":
	main()

