import random
import pygame

random1 = random.randint(1,3)
randomtext = random.randint(1000000,9999999)
def Smartypants(lastppick,epick):
	if lastppick == 3:
		epick = 2
	elif lastppick == 0:
		epick = random1
	else:
		epick = lastppick
	return epick

def draw_Smartypants(screen):
	screen.fill((0, 0, 0))
	pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(screen.get_width() * 0.15, screen.get_height() * 0.3,
														  screen.get_width() * 0.7, screen.get_height() * 0.4),
					 border_radius=int(screen.get_width() / 30))
	pygame.draw.rect(screen, (10, 10, 10), pygame.Rect(screen.get_width() * 0.2, screen.get_height() * 0.35,
													   screen.get_width() * 0.45, screen.get_height() * 0.3),
					 border_radius=int(screen.get_width() / 30))
	pygame.draw.rect(screen, (10, 10, 10), pygame.Rect(screen.get_width() * 0.67, screen.get_height() * 0.35,
													   screen.get_width() * 0.16, screen.get_height() * 0.06),
					 border_radius=int(screen.get_width() / 60))
	pygame.draw.circle(screen, (75, 75, 75), (screen.get_width() * 0.69, screen.get_height() * 0.45),
					   screen.get_width() * 0.02)
	pygame.draw.circle(screen, (75, 75, 75), (screen.get_width() * 0.75, screen.get_height() * 0.45),
					   screen.get_width() * 0.02)
	pygame.draw.circle(screen, (75, 75, 75), (screen.get_width() * 0.81, screen.get_height() * 0.45),
					   screen.get_width() * 0.02)
	pygame.draw.circle(screen, (75, 75, 75), (screen.get_width() * 0.69, screen.get_height() * 0.51),
					   screen.get_width() * 0.02)
	pygame.draw.circle(screen, (75, 75, 75), (screen.get_width() * 0.75, screen.get_height() * 0.51),
					   screen.get_width() * 0.02)
	pygame.draw.circle(screen, (75, 75, 75), (screen.get_width() * 0.81, screen.get_height() * 0.51),
					   screen.get_width() * 0.02)
	pygame.draw.circle(screen, (75, 75, 75), (screen.get_width() * 0.69, screen.get_height() * 0.57),
					   screen.get_width() * 0.02)
	pygame.draw.circle(screen, (75, 75, 75), (screen.get_width() * 0.75, screen.get_height() * 0.57),
					   screen.get_width() * 0.02)
	pygame.draw.circle(screen, (75, 75, 75), (screen.get_width() * 0.81, screen.get_height() * 0.57),
					   screen.get_width() * 0.02)
	pygame.draw.rect(screen, (75, 75, 75), pygame.Rect(screen.get_width() * 0.67, screen.get_height() * 0.62,
													   screen.get_width() * 0.16, screen.get_height() * 0.06),
					 border_radius=int(screen.get_width() / 60))
	font = pygame.font.Font(None, int(screen.get_width() / 20))
	text = font.render(str(randomtext), True, (0, 255, 0))
	screen.blit(text, (screen.get_width() * 0.68, screen.get_height() * 0.37))
	screen.set_colorkey((0, 0, 0))
