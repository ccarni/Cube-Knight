
import pygame
import random
import platformer.helper
import platformer.collisions
import platformer.helper
#drawing stuff make different file

def draw_dirt():
    surf = pygame.Surface((12, 12))
    surf.fill((99, 80, 61))
    pygame.draw.line(surf, (79, 50, 21), (0, 0), (12, 0))
    pygame.draw.line(surf, (79, 50, 21), (0, 6), (12, 6))
    pygame.draw.line(surf, (79, 50, 21), (0, 12), (12, 12))
    for i in range(surf.get_width()):
        for j in range(surf.get_width()):
            amount = [random.randint(-5, 5) for i in range(3)]
            platformer.helper.update_surrounding(surf, i, j, amount)
        return surf
    return surf

def draw_grass(dirt):
    surf = dirt.copy()
    grass_rect = pygame.Rect(0, 0, surf.get_width(), round(surf.get_width()*0.3))
    pygame.draw.rect(surf, (100, 100, 100), grass_rect)
    #for i in range(surf.get_width()):
        #for j in range(grass_rect.height):
            #mount = [random.randint(-10, 10) for i in range(3)]
            #platformer.helper.update_adjacent(surf, i, j, amount)
    return surf

def draw_cloud():
    surf = pygame.Surface((5, 5)).convert_alpha()
    surf.fill((255, 255, 255, 100)) # (red, green, blue, alpha)
    for i in range(surf.get_width()):
        for j in range(surf.get_width()):
            amount = [random.randint(-10, 10) for i in range(3)]
            platformer.helper.update_surrounding(surf, i, j, amount)
    return surf

def draw_tree(width, height):
    surf = pygame.Surface((width, height)).convert_alpha()
    surf.fill((0, 0, 0, 0))
    pygame.draw.rect(surf, (150, 150, 150), [0,0,surf.get_width(), surf.get_height()])
    return surf


def draw_spring():
    surf = pygame.Surface((20, 10)).convert_alpha()
    surf.fill((0, 0, 0, 0))
    r = round(surf.get_height() / 1.5)  # Round the corners of the spring
    pygame.draw.rect(surf, (18, 202, 219), surf.get_rect(), border_radius=r)
    # pygame.draw.circle(surf, (11, 31, 180), (10, 5), 2)
    pygame.draw.rect(surf, (50, 50, 50), surf.get_rect(), border_radius=r, width=1)
    return surf


def draw_moon():
    moon = pygame.Surface((100, 100)).convert_alpha()
    moon.fill((0, 0, 0, 0))
    pygame.draw.ellipse(moon, (200, 200, 200), moon.get_rect())
    for i in range(moon.get_width()):
        for j in range(moon.get_width()):
            amount = [random.randint(-10, 10)]*3 # This duplicates the number three times to ensure we don't get colors
            platformer.helper.update_surrounding(moon, i, j, amount)
    return moon

def draw_star(r):
    star = pygame.Surface((100, 100)).convert_alpha()
    star.fill((0, 0, 0, 0))
    pygame.draw.circle(star, (160, 160, 200), (50, 50), r)
    pygame.draw.circle(star, ([random.randint(0, 128) for i in range(3)]), (50, 50), r/2)
    pygame.draw.circle(star, (1, 1, 1), (50, 50), r/3)
    return star
    # what a function this one is
#"Mountains"


# You should make this cooler
def draw_player():
    surf = pygame.Surface((10, 10))
    surf.fill((50, 200, 50))
    return surf

def draw_teleporter():
    surf = pygame.Surface((10, 20)).convert_alpha()
    surf.fill((0,0,0,0))
    r = round(surf.get_height()/1.5) # Round the corners of the spring
    #inside
    pygame.draw.rect(surf, (0, 0, 255), surf.get_rect(), border_top_left_radius=r, border_top_right_radius=r)
    # outline
    pygame.draw.rect(surf, (0, 0, 0), surf.get_rect(), border_top_left_radius=r, border_top_right_radius=r, width=4)
    return surf

def draw_spike(rotate=0):
    surf = pygame.Surface((20, 10)).convert_alpha()
    surf.fill((0, 0, 0, 0))
    pygame.draw.polygon(surf, (200, 225, 250),
                        [(0, surf.get_height()), (surf.get_width() / 6, surf.get_height() * 0.25),
                         (surf.get_width() / 5, surf.get_height() * 0.66),
                         (surf.get_width() / 2.5, surf.get_height() / 10),
                         (surf.get_width() / 2, surf.get_height() / 2), (surf.get_width() / 1.5, 0),
                         (surf.get_width() / 1.25, surf.get_height() / 1.8),
                         (surf.get_width() / 1.1, surf.get_height() / 4), (surf.get_width(), surf.get_height())])
    pygame.draw.polygon(surf, (160, 146, 211),
                        [(0, surf.get_height()), (surf.get_width() / 6, surf.get_height() * 0.25),
                         (surf.get_width() / 5, surf.get_height() * 0.66),
                         (surf.get_width() / 2.5, surf.get_height() / 10),
                         (surf.get_width() / 2, surf.get_height() / 2), (surf.get_width() / 1.5, 0),
                         (surf.get_width() / 1.25, surf.get_height() / 1.8),
                         (surf.get_width() / 1.1, surf.get_height() / 4), (surf.get_width(), surf.get_height())],
                        width=1)
    surf = pygame.transform.rotate(surf, rotate)
    return surf

def draw_checkpoint():
    surf = pygame.Surface((20, 10)).convert_alpha()
    surf.fill((0,0,0,0))
    r = round(surf.get_height()/1.5)
    pygame.draw.rect(surf, (50, 200, 50), surf.get_rect(), border_top_left_radius=r, border_top_right_radius=r)
    pygame.draw.rect(surf, (25, 100, 25), surf.get_rect(), border_top_left_radius=r, border_top_right_radius=r, width=1)
    return surf

def draw_combat():
    surf = pygame.Surface((12, 12))
    surf.fill((235, 64, 52))
    return surf

def draw_breakable():
    surf = pygame.Surface((5,5)).convert_alpha()
    surf.fill((200,125,50,255))
    for i in range(surf.get_width()):
        for j in range(surf.get_width()):
            if random.randint(0, 100) < 50:
                amount = [random.randint(0,10),random.randint(0,10),random.randint(0,10)]
                platformer.helper.update_color(surf, (i, j), amount)
    return surf

def draw_bouncer():
    surf = pygame.Surface((20, 10)).convert_alpha()
    surf.fill((0, 0, 0, 0))
    r = round(surf.get_height() / 1.5)  # Round the corners of the spring
    pygame.draw.rect(surf, (250, 0, 250), surf.get_rect(), border_top_left_radius=r, border_top_right_radius=r)
    pygame.draw.rect(surf, (0, 0, 0), surf.get_rect(), border_top_left_radius=r, border_top_right_radius=r, width=1)
    return surf

# new code may cause problems

# def draw_ice():
#     surf = pygame.Surface((5, 5))
#     surf.fill((142, 215, 219))
#     for i in range(surf.get_width()):
#         for j in range(surf.get_width()):
#             amount = [random.randint(-3, 3) for i in range(3)]
#             platformer.helper.update_surrounding(surf, i, j, amount)
#     return surf

def draw_water():
    surf = pygame.Surface((20, 10))
    surf.fill((15, 94, 156))
    for i in range(surf.get_width()):
        for j in range(surf.get_height()):
            amount = [random.randint(-1, 1) for i in range(3)]
            platformer.helper.update_surrounding(surf, i, j, amount)
    return surf
#
# def draw_mud():
#     surf = pygame.Surface((5, 5))
#     surf.fill((47, 35, 21))
#     for i in range(surf.get_width()):
#         for j in range(surf.get_width()):
#             amount = [random.randint(-2, 2) for i in range(3)]
#             platformer.helper.update_surrounding(surf, i, j, amount)
#     return surf
#
# def draw_flag():
#     surf = pygame.Surface((45, 60)).convert_alpha()
#     surf.fill((0, 0, 0, 0))
#     pygame.draw.rect(surf, (210, 150, 30), pygame.Rect(5, 0, 40, 30))
#     pygame.draw.rect(surf, (120, 95, 90), pygame.Rect(5, 30, 3, 30))
#     pygame.draw.rect(surf, (255, 255, 255), pygame.Rect(17, 7, 16, 16))
#     pygame.draw.rect(surf, (255, 0, 0), pygame.Rect(19, 9, 12, 12))
#     return surf
#
# def draw_ladder():
#     surf = pygame.Surface((20, 20)).convert_alpha()
#     surf.fill((0, 0, 0, 0))
#     pygame.draw.rect(surf, (180, 180, 15), pygame.Rect(2, 0, 2, 20))
#     pygame.draw.rect(surf, (180, 180, 15), pygame.Rect(16, 0, 2, 20))
#     pygame.draw.rect(surf, (180, 180, 15), pygame.Rect(2, 9, 16, 2))
#     pygame.draw.rect(surf, (180, 180, 15), pygame.Rect(2, 19, 16, 2))
#     return surf