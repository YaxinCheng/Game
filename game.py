import pygame
from Platform import platform
from Player import player

class game:
	def __init__(self, screenSize, fullScreen = False, backgroundColour = (249, 250, 255)):
		pygame.init()
		self._bgColour = backgroundColour
		self.screenSize = screenSize
		self.screen = pygame.display.set_mode(screenSize, fullScreen)
		self.screen.fill(self._bgColour)
		self.playerList = None
		self._generatePlatform()
		self._generateSticks()

	def _generatePlatform(self):
		self.platformList = pygame.sprite.Group()
		plats = platform.generatePlatforms()
		for plat in plats:
			self.platformList.add(plat)

	def _generateSticks(self):
		self.stickList = pygame.sprite.Group()
		sticks = platform.generateSticks()
		for stick in sticks:
			self.stickList.add(stick)

	def addPlayer(self):
		self.Player = player(platforms = self.platformList, sticks = self.stickList)
		initialLocation = (700, 500)
		self.Player.rect.x, self.Player.rect.y = initialLocation
		if self.playerList is None:
			self.playerList = pygame.sprite.Group()
		self.playerList.add(self.Player)

	def _update(self):
		self.screen.fill(self._bgColour)
		self.platformList.update()
		self.platformList.draw(self.screen)
		self.playerList.update()
		self.playerList.draw(self.screen)
		self.stickList.update()
		self.stickList.draw(self.screen)
		pygame.display.flip()

	def start(self):
		clock = pygame.time.Clock()
		self.gaming = True
		while self.gaming:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.gaming = False
					break
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.gaming = False
						break
					if event.key == pygame.K_LEFT:
						self.Player.go_left()
					if event.key == pygame.K_RIGHT:
						self.Player.go_right()
					if event.key == pygame.K_UP:
						self.Player.jump()
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT and self.Player.xSpeed < 0:
						self.Player.stop()
					if event.key == pygame.K_RIGHT and self.Player.xSpeed > 0:
						self.Player.stop()
			clock.tick(60)
			self._update()
		pygame.quit()