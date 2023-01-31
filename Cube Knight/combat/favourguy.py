import random
import pygame
random = random.randint(1,3)

def Favourguy(lastppick,epick):
	# print (lastppick)
	# if lastppick == 0:
	# 	return 1
	#
	# else:
	# 	return lastppick

	if lastppick == random - 1 and random != 1:
		epick = random + 1
	elif lastppick == 2 and random == 3:
		epick = 1
	elif lastppick == 3 and random == 1:
		epick = 3
	else:
		epick = random
	return epick


def draw_Favourguy(screen):
	screen.fill((0, 0, 0))
	pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(screen.get_width() * 0.47, screen.get_height() * 0.31,
														  screen.get_width() * 0.06, screen.get_height() * 0.55),
					 border_radius=int(screen.get_width() / 30))
	pygame.draw.rect(screen, (120, 120, 120), pygame.Rect(screen.get_width() * 0.47, screen.get_height() * 0.31,
														  screen.get_width() * 0.06, screen.get_height() * 0.55),
					 border_radius=int(screen.get_width() / 30), width=3)
	pygame.draw.polygon(screen, (80, 80, 80), (
	(screen.get_width() * 0.48, screen.get_height() * 0.36), (screen.get_width() * 0.43, screen.get_height() * 0.31),
	(screen.get_width() * 0.43, screen.get_height() * 0.25), (screen.get_width() * 0.43, 0),
	(screen.get_width() * 0.47, screen.get_height() * 0.25), (screen.get_width() * 0.5, 0),
	(screen.get_width() * 0.53, screen.get_height() * 0.25), (screen.get_width() * 0.57, 0),
	(screen.get_width() * 0.57, screen.get_height() * 0.25), (screen.get_width() * 0.57, screen.get_height() * 0.31),
	(screen.get_width() * 0.52, screen.get_height() * 0.36)))
	screen.set_colorkey((0, 0, 0))