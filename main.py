import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()

	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	
	asteroids = pygame.sprite.Group()
	updateable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	shoot = pygame.sprite.Group()
	Player.containers = (updateable, drawable)
	Asteroid.containers = (asteroids, updateable, drawable)
	AsteroidField.containers = (updateable,)
	Shot.containers = (shoot, updateable, drawable)

	player = Player(x, y)
	asteroid_field = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		updateable.update(dt)
		for asteroid in asteroids:
			if asteroid.collide(player):
				print("Game over!")
				sys.exit()
			for bullet in shoot:
				if asteroid.collide(bullet):
					asteroid.split()
					break
		screen.fill((0,0,0))
		for d in drawable:
			d.draw(screen)
		pygame.display.flip()

		dt = clock.tick(60) / 1000 # limit FPS to 60 and get delta time from ms to seconds

if __name__ == "__main__":
	main()
