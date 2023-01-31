import random
import pygame


def Bob(lastppick,epick):
    if lastppick == 1:
        epick = 1
    elif lastppick == 3:
        epick = 3
    else:
        epick = random.randint(1,3)
    return epick

def draw_Bob(screen):
    pygame.draw.ellipse(screen, (192, 148, 90),
                        pygame.Rect(screen.get_width() * 0.2, screen.get_height() * 0.3, screen.get_width() * 0.6,
                                    screen.get_height() * 0.4))
    enemy_surf = pygame.Surface(screen.get_size())
    for i in range(200):
        x = random.randint(screen.get_width() * 0.2, screen.get_width() * 0.8)
        y = random.randint(screen.get_height() * 0.3, screen.get_height() * 0.7)
        pygame.draw.circle(screen, (255, 255, 255), (x, y), 2)
    pygame.draw.ellipse(screen, (255, 255, 255),
                        pygame.Rect(screen.get_width() * 0.4, screen.get_height() * 0.45, screen.get_width() * 0.2,
                                    screen.get_height() * 0.1))
    for i in range(200):
        x = random.randint(screen.get_width() * 0.2, screen.get_width() * 0.8)
        y = random.randint(screen.get_height() * 0.3, screen.get_height() * 0.7)
        pygame.draw.circle(screen, (20, 20, 20), (x, y), 2)
    pygame.draw.ellipse(screen, (255, 255, 255),
                        pygame.Rect(screen.get_width() * 0.4, screen.get_height() * 0.45, screen.get_width() * 0.2,
                                    screen.get_height() * 0.1))
    for i in range(200):
        x = random.randint(screen.get_width() * 0.2, screen.get_width() * 0.8)
        y = random.randint(screen.get_height() * 0.3, screen.get_height() * 0.7)
        pygame.draw.circle(screen, (112, 68, 10), (x, y), 2)
    pygame.draw.ellipse(screen, (255, 255, 255),
                        pygame.Rect(screen.get_width() * 0.4, screen.get_height() * 0.45, screen.get_width() * 0.2,
                                    screen.get_height() * 0.1))
    enemy_surf2 = pygame.Surface(screen.get_size())
    enemy_surf2.fill((255, 255, 255))
    pygame.draw.ellipse(enemy_surf2, (0, 255, 0),
                        pygame.Rect(screen.get_width() * 0.2, screen.get_height() * 0.3, screen.get_width() * 0.6,
                                    screen.get_height() * 0.4))
    enemy_surf2.set_colorkey((0, 255, 0))
    screen.blit(enemy_surf2, (0, 0))
    enemy_surf.set_colorkey((0, 0, 0))