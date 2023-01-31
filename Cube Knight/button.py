import pygame


class Button:
    def __init__(self, text, rect):
        self.rect = rect
        font = pygame.font.Font(None, 100)
        text = font.render(text, True, (255, 255, 255))
        surf = pygame.Surface(text.get_size())
        surf.fill((25, 25, 50))

        surf.blit(text, (0, 0))
        self.surf = pygame.transform.smoothscale(surf, rect.size)
        pygame.draw.rect(self.surf, (255, 255, 255), self.surf.get_rect(), width=1)

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
