import pygame
import platformer.platformer_runner

pygame.init()

Fonto = pygame.font.SysFont('None',30)
esurf = pygame.Surface((450,450))
psurf = pygame.Surface((300,300))
screen = pygame.display.set_mode((200, 400))
display = pygame.display.set_mode(flags=pygame.FULLSCREEN)
height = screen.get_height()
width = screen.get_width()

platformer = platformer.platformer_runner.Runner()
platformer.run()





