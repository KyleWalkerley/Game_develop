import pygame, sys

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

wood_bg = pygame.image.load('Images/Wood_BG.png')
land_bg = pygame.image.load('Images/Land_BG.png')
water_bg = pygame.image.load('Images/Water_BG.png')
cloud1_bg = pygame.image.load('Images/Cloud1.png')
cloud2_bg = pygame.image.load('Images/Cloud2.png')
crosshair = pygame.image.load('Images/crosshair.png')
duck_surface = pygame.image.load('Images/duck.png')

land_position_y = 560
land_speed = 1

water_position_y = 600
water_speed = 1.5 

duck_list = []
for duck in range(20):
	duck_position_x = random.randrange(50,1200)
	duck_position_y = random.randrange(120,600)
	duck_rect = duck_surface.get_rect(center = (duck_position_x, duck_position_y))
	duck_list.append(duck_rect)


while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEMOTION:
			crosshair_rect = crosshair.get_rect(center = event.pos)


	screen.blit(wood_bg,(0,0))
	land_position_y -= land_speed

	if land_position_y <=500 or land_position_y >= 600:
		land_speed *= -1

	screen.blit(land_bg,(0,land_position_y))

	water_position_y -=water_speed
	if water_position_y <=585 or water_position_y >= 660:
		water_speed *= -1

	screen.blit(water_bg,(0,water_position_y))

	for duck_rect in duck_list:
		screen.blit(duck_surface,duck_rect)

	screen.blit(crosshair,crosshair_rect)

	screen.blit(cloud1_bg,(1000,10))
	screen.blit(cloud2_bg,(180,0))
	screen.blit(cloud1_bg,(850,55))
	screen.blit(cloud2_bg,(550,25))
	pygame.display.update()
	clock.tick(120)