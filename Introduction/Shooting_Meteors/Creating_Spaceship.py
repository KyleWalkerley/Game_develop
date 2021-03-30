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

class Meteor(pygame.sprite.Sprite):
	def __init__(self,path,x_pos,y_pos,x_speed,y_speed):
		super().__init__()
		self.image = pygame.image.load("Meteor2.png")
		self.rect = self.image.get_rect(center = (x_pos,y_pos))
		self.x_speed = x_speed
		self.y_speed = y_speed

	def update(self):
		self.rect.centerx += self.x_speed
		self.rect.centery += self.y_speed

pygame.init() #initiating pygame
screen = pygame.display.set_mode((1280,720)) #Creating the display surface
clock = pygame.time.Clock() #creating clock objective

spaceship = SpaceShip('spaceship.png',640,500,10)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

meteor_group = pygame.sprite.Group()

METEOR_EVENT = pygame.USEREVENT
pygame.time.set_timer(METEOR_EVENT,250)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: #closing the game
			pygame.quit()
			sys.exit()
		if event.type == METEOR_EVENT:


	screen.fill((42,45,51))
	spaceship_group.draw(screen)
	meteor_group.draw(screen)
	spaceship_group.update()
	meteor_group.update()
	pygame.display.update() #Draws a frame
	clock.tick(120) # controls the framerate