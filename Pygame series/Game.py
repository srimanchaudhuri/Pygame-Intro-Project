import pygame
from sys import exit
from random import randint

def display_score():
	current_time = int(pygame.time.get_ticks()/1000) - start_time
	score_surface = test_font.render(f'{current_time}', False, (64,64,64))
	score_rect = score_surface.get_rect(center = (400,50))
	screen.blit(score_surface,score_rect)

def obstacle_movement(obstacle_list):
	if obstacle_list:
		for obstacle_rect in obstacle_list:
			obstacle_rect.x -= 5

			if(obstacle_rect.bottom == 300):
				screen.blit(snail_surface,obstacle_rect)
			else :
				screen.blit(fly_surface,obstacle_rect)

		obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

		return obstacle_list
	else: return []

def collisions(player,obstacles):
	if obstacles:
		for obstacle_rect in obstacles:
			if player.colliderect(obstacle_rect): return False
	return True

def player_animation():
	global player_surface, player_index

	if player_rect.bottom < 300:
		#jump
		player_surface = player_jump
	else:
		#walk
		player_index += 0.1
		if player_index >= len(player_walk): player_index = 0
		player_surface = player_walk[int(player_index)]
	#play walking animation
	#display jump



pygame.init() #To set everything. Initialises Pygame
screen = pygame.display.set_mode((800,400)) #screen variable is used to create a screen window param are width and height. This creates the window for just 1 frame which we have to make run forever by a while true loop
							  #width | hieght

pygame.display.set_caption('Runner')
clock = pygame.time.Clock() #adds a clock

bg_music = pygame.mixer.Sound('audio/music.mp3')
bg_music.set_volume(0.3)

jump_sound = pygame.mixer.Sound('audio/jump.mp3')
jump_sound.set_volume(0.3)

test_font = pygame.font.Font('font/Pixeltype.ttf', 50) # arguments -> font type and font size.

title_surface = test_font.render('Happy Sixth', False, (231, 120, 120))
title_rect = title_surface.get_rect(center = (400,50))

start_surface = test_font.render('Start Game', False, (231, 120, 120))
start_rect = start_surface.get_rect(center = (400,100))

#test_surface = pygame.Surface((100,200)) # needs width and hieght as params width->x , hieght->y
#test_surface.fill('Red') # color 

sky_surface = pygame.image.load('graphics/Sky.png').convert() # this is to import an image as a surface argument -> path
ground_surface = pygame.image.load('graphics/ground.png').convert() 

#Intro Screen
player_stand = pygame.image.load('graphics/player/Shraddha_Stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2) #(surfae, rotation, scale)
player_stand_rect = player_stand.get_rect(center = (400,200))

# text_surface = test_font.render('My Game', False, (64,64,64)).convert_alpha() # (text, Aniti Aliasing -> smoothing the edges of text, color) #convert alpha converts the png to a game file
# text_rect = text_surface.get_rect(center = (400,50))

game_active = False # Checks if game over or not

start_time = 0

#Obstacles
snail_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_1, snail_2]
snail_index = 0
snail_surface = snail_frames[snail_index]

fly_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
fly_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
fly_frames = [fly_1,fly_2]
fly_index = 0
fly_surface = fly_frames[fly_index]

obstacle_rect_list = []

bg_music.play(loops = -1)


# snail_x_pos = 600

# Timer
obstacle_timer = pygame.USEREVENT + 1; # To add a new USEREVENT -> we need +1 to denote its our own userevent not conflicting a python already existing userevent
pygame.time.set_timer(obstacle_timer,1500)

snail_animate_timer = pygame.USEREVENT + 2;
pygame.time.set_timer(snail_animate_timer, 500)

fly_animate_timer = pygame.USEREVENT + 3;
pygame.time.set_timer(fly_animate_timer, 200)

player_walk_1 = pygame.image.load('graphics/player/Shraddha_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('graphics/player/Shraddha_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('graphics/player/Shraddha_jump.png').convert_alpha()

player_surface = player_walk[player_index] # picks first image
player_rect = player_surface.get_rect(midbottom = (80,300)) # get_rect takes a surface and draw a rectangle around it topleft = (x,y)
player_gravity = 0



while True:
	for event in pygame.event.get(): #loops through all the event caught by pygame eg. keyboard event
		if event.type == pygame.QUIT: #Checks if the event is of clicking the close window button at top left corner
			pygame.quit() # opposite of pygame init - closes the pygame window (uninitialises) therefore after this we should no have any code. We should exit the while loop
			exit() #This is to close the while loop
		if event.type == pygame.MOUSEBUTTONDOWN and game_active:
			if player_rect.collidepoint(event.pos): player_gravity = -20
		if event.type == pygame.MOUSEBUTTONDOWN and not game_active:
			if start_rect.collidepoint(event.pos): 
				game_active = 1
		if event.type == pygame.KEYDOWN:
			if game_active:
				if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
					jump_sound.play()
					player_gravity = -20
			else:
				if event.key == pygame.K_SPACE:
					game_active = True

		if game_active :
			if event.type == obstacle_timer:
				if randint(0,2):
					obstacle_rect_list.append(snail_surface.get_rect(midbottom = (randint(900,1100),300))) #Makes the snail append to the list
				else:
					obstacle_rect_list.append(fly_surface.get_rect(midbottom = (randint(900,1100),210))) #Makes the snail append to the list	
			if event.type == snail_animate_timer:
				if snail_index == 0 : snail_index = 1
				else : snail_index = 0
				snail_surface = snail_frames[snail_index]
			if event.type == fly_animate_timer:
				if fly_index == 1 : fly_index = 0
				else : fly_index = 1
				fly_surface = fly_frames[fly_index]


	if game_active: #Game playing
		screen.blit(sky_surface,(0,0)) # blit-> block image transfer -> place one surface on another -> two arguments -> (surface,position) #Origin is at top left corner.
		screen.blit(ground_surface,(0,300))
		# pygame.draw.rect(screen,'#c0e8ec',text_rect)
		# pygame.draw.rect(screen,'#c0e8ec',text_rect,10) #used to draw a shape in pygame window
		display_score()

		
		# pygame.draw.line(screen,'Gold',(0,0),pygame.mouse.get_pos(),10) #to draw line (screen, color, starting coordinate, ending coordinate, width)
		# pygame.draw.ellipse(screen,'Brown',pygame.Rect(50,200,100,100)) #Rect(left,top,width,hieght)
		# screen.blit(text_surface,text_rect)

		# if snail_x_pos <= -100:
		# 	snail_x_pos = 800 # Loop the snail

    	# snail_x_pos += -3 #To move the snail

		# snail_rect.right += -4

		# if snail_rect.right < -1 :
		# 	snail_rect.left = 800
		# screen.blit(snail_surface,snail_rect)


		#player_rect.left += 4

		#if player_rect.left > 800:
			#player_rect.right = 0

		player_gravity += 1
		player_rect.y += player_gravity
		if player_rect.bottom >= 300 : 
			#Creating ground
			player_rect.bottom = 300

		player_animation()
		screen.blit(player_surface,player_rect)

		#if player_rect.colliderect(snail_rect): #checks if two rectangles are colliding

		# keys = pygame.key.get_pressed()
		# if keys[pygame.K_SPACE] : print('JUMP')

		# Obstacle movement
		obstacle_rect_list =  obstacle_movement(obstacle_rect_list)

		game_active = collisions(player_rect,obstacle_rect_list)

	else: #Game over
		screen.fill((250,188,188))
		screen.blit(player_stand,player_stand_rect)
		obstacle_rect_list.clear()
		player_rect.midbottom = (80,300)
		player_gravity = 0

		start_time = int(pygame.time.get_ticks()/1000)
		screen.blit(title_surface,title_rect)
		screen.blit(start_surface,start_rect)



	mouse_pos = pygame.mouse.get_pos(); #get mouse position (x,y)
	pygame.mouse.get_pressed() #get bollean vector of 3 for checking 3 button presses of mouse
	# draw all elements
	# update everything
	pygame.display.update()
	# An i/p must be dedicated to exit while loop
	# we would like to maintain a constan frame rate for our games -> 60 fps. 
	# Need to create a ceil and floor : ceil:easy to tell computer to pause between frames & floor : really hard to get a computer to run faster we need to change the frames to ensure it runs well
	clock.tick(60) # tells the while true loop that the while true loop should not run more then 60 times/second -> one while loop every ~ 17 msec. # SETS A MAXIMUM FRAME RATE
	
