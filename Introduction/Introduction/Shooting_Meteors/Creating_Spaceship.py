import pygame, sys

class SpaceShip(pygame.sprite.Sprite):
	def __init__(self,path,x_pos,y_pos,speed):
		super().__init__()
		self.image = pygame.image.load(path)
		self.rect = self.image.get_rect(center = (x_pos,y_pos))

	def update(self):
		self.rect.center = pygame.mouse.get_pos()
		self.screen_constrain()

	def screen_constrain(self):
		if self.rect.right >= 1280:
			self.rect.right = 1280

		if self.rect.left <=0:
			self.rect.left = 0


pygame.init() #initiating pygame
screen = pygame.display.set_mode((1280,720)) #Creating the display surface
clock = pygame.time.Clock() #creating clock objective

spaceship = SpaceShip('spaceship.png',640,500,10)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: #closing the game
			pygame.quit()
			sys.exit()


	screen.fill((42,45,51))
	spaceship_group.draw(screen)
	spaceship_group.update()
	pygame.display.update() #Draws a frame
	clock.tick(120) # controls the framerate