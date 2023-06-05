import pygame
from sys import exit

pygame.init() #To set everything. Initialises Pygame
screen = pygame.display.set_mode((800,400)) #screen variable is used to create a screen window param are width and height. This creates the window for just 1 frame which we have to make run forever by a while true loop
							  #width | hieght

pygame.display.set_caption('Runner')
clock = pygame.time.Clock() #adds a clock


test_font = pygame.font.Font('font/Pixeltype.ttf', 50) # arguments -> font type and font size.

#test_surface = pygame.Surface((100,200)) # needs width and hieght as params width->x , hieght->y
#test_surface.fill('Red') # color 

sky_surface = pygame.image.load('graphics/Sky.png') #this is to import an image as a surface argument -> path
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render('My Game', False, 'Black') # (text, Aniti Aliasing -> smoothing the edges of text, color)

while True:
	for event in pygame.event.get(): #loops through all the event caught by pygame eg. keyboard event
		if event.type == pygame.QUIT: #Checks if the event is of clicking the close window button at top left corner
			pygame.quit() # opposite of pygame init - closes the pygame window (uninitialises) therefore after this we should no have any code. We should exit the while loop
			exit() #This is to close the while loop

	screen.blit(sky_surface,(0,0)) # blit-> block image transfer -> place one surface on another -> two arguments -> (surface,position) #Origin is at top left corner.
	screen.blit(ground_surface,(0,300))
	screen.blit(text_surface,(300,50))
	# draw all elements
	# update everything
	pygame.display.update()
	# An i/p must be dedicated to exit while loop
	# we would like to maintain a constan frame rate for our games -> 60 fps. 
	# Need to create a ceil and floor : ceil:easy to tell computer to pause between frames & floor : really hard to get a computer to run faster we need to change the frames to ensure it runs well
	clock.tick(60) # tells the while true loop that the while true loop should not run more then 60 times/second -> one while loop every ~ 17 msec. # SETS A MAXIMUM FRAME RATE
	