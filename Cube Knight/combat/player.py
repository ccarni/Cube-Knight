import pygame
maxphealth = 100
phealth = 100
pdamage = 100

class Player:
    def __init__(self, phealth, pdamage):
        self.phealth = phealth
        self.pdamage = pdamage

    def Ponhit(self,edamage):
        self.phealth -= edamage

def draw_player(screen):
    pygame.draw.rect(screen, (246, 247, 139), (0,0,screen.get_width(), screen.get_height()))
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width(), screen.get_height() / 3),5 + screen.get_width() / 2)
    pygame.draw.circle(screen,(200,200,200), (screen.get_width(), screen.get_height()/3) ,screen.get_width()/2 )
    pygame.draw.rect(screen, (246, 247, 139), (0, 0, screen.get_width(), screen.get_height()/3))
    pygame.draw.rect(screen, (246, 247, 139), (0, 2 * screen.get_height() / 3, screen.get_width(), screen.get_height() / 3))
    pygame.draw.rect(screen, (50, 50, 50), (8 * screen.get_width() / 12,screen.get_height() / 3, screen.get_width()/30, screen.get_height() / 3))
    pygame.draw.rect(screen, (50, 50, 50), (7 * screen.get_width() / 12, screen.get_height() / 3, screen.get_width() / 30, screen.get_height() / 3))
    pygame.draw.rect(screen, (50, 50, 50), (9 * screen.get_width() / 12, screen.get_height() / 3, screen.get_width() / 30, screen.get_height() / 3))
    pygame.draw.rect(screen, (50, 50, 50), (10 * screen.get_width() / 12, screen.get_height() / 3, screen.get_width() / 30, screen.get_height() / 3))
    pygame.draw.rect(screen, (50, 50, 50), (11 * screen.get_width() / 12, screen.get_height() / 3, screen.get_width() / 30, screen.get_height() / 3))
    pygame.draw.line(screen,(246, 247, 139),(10*screen.get_width()/30,10*screen.get_height()/30),(20*screen.get_width()/24,screen.get_height()),10)
    pygame.draw.rect(screen, (0, 0, 0), (screen.get_width() / 2, screen.get_height() / 3, screen.get_width() / 2, 5))
    pygame.draw.rect(screen, (0, 0, 0),(29 * screen.get_width() / 48, 2 * screen.get_height() / 3, screen.get_width() / 2, 5))
    pygame.draw.rect(screen,(0,0,0), (0,0,screen.get_width(),5))
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 5, screen.get_height()))
    pygame.draw.rect(screen, (0, 0, 0), (0, screen.get_height()-5, screen.get_width(), 5))
    pygame.draw.rect(screen, (0, 0, 0), (screen.get_width() - 5,0 ,5 , screen.get_height()))

