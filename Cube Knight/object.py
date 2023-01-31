import pygame


class Object:
    def __init__(self, text, rect,color=(0,0,0)):
        self.rect = rect
        font = pygame.font.Font(None, 1)
        text = font.render(text, True, (color))
        surf = pygame.Surface(text.get_size())
        surf.fill((color))

        surf.blit(text, (0, 0))
        self.surf = pygame.transform.smoothscale(surf, rect.size)
        pygame.draw.rect(self.surf, (255, 255, 255), self.surf.get_rect(), width=1)

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
