import random
import pygame

def Coward(lastppick,epick):
	if lastppick == 2:
		epick = 1
	else:
		epick = 3
	return epick

def draw_Coward(screen):
	screen.fill((0,0,0))
	for i in range(100):
		pygame.draw.lines(screen, (227, 208, 128), False, ((screen.get_width() / 2, screen.get_height() / 2), (
		random.randint(0, screen.get_width()), random.randint(0, screen.get_height())), (
														   random.randint(0, screen.get_width()),
														   random.randint(0, screen.get_height())), (
														   random.randint(0, screen.get_width()),
														   random.randint(0, screen.get_height()))), width=10)
	pygame.draw.circle(screen, (105, 47, 38), (screen.get_width() / 3, screen.get_height() / 3), 60)
	pygame.draw.circle(screen, (105, 47, 38), (screen.get_width() / 2, screen.get_height() / 2), 40)
	pygame.draw.circle(screen, (105, 47, 38), (2 * screen.get_width() / 3, 2 * screen.get_height() / 3), 50)
	pygame.draw.circle(screen, (105, 47, 38), (screen.get_width() / 4, screen.get_height() / 2), 40)
	pygame.draw.circle(screen, (105, 47, 38), (3 * screen.get_width() / 4, screen.get_height() / 4), 30)
	screen.set_colorkey((0,0,0))