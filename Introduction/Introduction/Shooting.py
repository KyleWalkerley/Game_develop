import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

wood_bg = pygame.image.load('Images/Wood_BG.png')
water_bg = pygame.image.load('Images/Water_BG.png')
land_bg = pygame.image.load('Images/Land_BG.png')
cloud1_bg = pygame.image.load("Images/Cloud1.png")
cloud2_bg = pygame.image.load("Images/Cloud2.png")
crosshair = pygame.image.load('Images/crosshair.png')
duck_surface = pygame.image.load('Images/duck.png')


game_font = pygame.font.Font(None,60)
text_surface = game_font.render('YOU HAVE WON!',True,(225,225,225))
text_rect = text_surface.get_rect(center = (640,360))

land_position_y = 580
land_speed = 1

water_position_y = 620
water_speed = 1.5

duck_list = []
for duck in range(20):
	duck_position_x = random.randrange(50,1200)
	duck_position_y = random.randrange(120,600)
	duck_rect = duck_surface.get_rect(center = (duck_position_x,duck_position_y))
	duck_list.append(duck_rect)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEMOTION:
			crosshair_rect = crosshair.get_rect(center = event.pos)
		if event.type == pygame.MOUSEBUTTONDOWN:
			for index,duck_rect in enumerate(duck_list):
				if  duck_rect .collidepoint(event.pos): #crosshair_rect.colliderect(duck_rect):
					del duck_list[index]



	screen.blit(wood_bg,(0,0))

	for duck_rect in duck_list:
		screen.blit(duck_surface,duck_rect)

	if len(duck_list) <= 0 :
		screen.blit(text_surface,text_rect)

	land_position_y -= land_speed
	if land_position_y <= 520 or land_position_y >= 600:
		land_speed *= -1

	water_position_y += water_speed
	if water_position_y <= 600 or water_position_y >= 640:
		water_speed *= -1

	screen.blit(land_bg,(0,land_position_y))
	screen.blit(water_bg,(0,water_position_y))
	screen.blit(crosshair,crosshair_rect)
	screen.blit(cloud1_bg,(485,93))
	screen.blit(cloud2_bg,(750,41))
	screen.blit(cloud1_bg,(900,18))
	screen.blit(cloud2_bg,(225,72))
	screen.blit(cloud1_bg,(1100,72))
	screen.blit(cloud2_bg,(40,85))
	pygame.display.update()
	clock.tick(120)