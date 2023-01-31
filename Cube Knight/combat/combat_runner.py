import pygame
import sys
import button
from combat import enemy, player, coward, Bob, favourguy, smartypants, enemy_turn
import object
import random

class Runner:
    def __init__(self, e_type):
        self.Fonto = pygame.font.SysFont('None', 30)
        self.esurf = pygame.Surface((450, 450))


        def randenemy():
            R = random.randint(1, 4)
            if R == 1:
                print('1')
                return 'smartypants'
            elif R == 2:
                print('2')
                return 'Favourguy'
            elif R == 3:
                print('3')
                return 'coward'
            elif R == 4:
                print('4')
                return 'Bob'


        self.e_type = randenemy()

        if self.e_type == 'smartypants':
            smartypants.draw_Smartypants(self.esurf)
        elif self.e_type == 'Favourguy':
            favourguy.draw_Favourguy(self.esurf)
        elif self.e_type == 'coward':
            coward.draw_Coward(self.esurf)
        elif self.e_type == 'Bob':
            Bob.draw_Bob(self.esurf)


        self.psurf = pygame.Surface((300, 300))
        player.draw_player(self.psurf)
        self.screen = pygame.display.set_mode((200, 400))
        self.display = pygame.display.set_mode(flags=pygame.FULLSCREEN)
        height = self.screen.get_height()
        width = self.screen.get_width()

        self.window = object.Object('band-aid fix', pygame.Rect(width * 0.05, height * 0.05, width * .9, height * 0.7),
                                    (255, 255, 255))

        button1 = button.Button('Fast attack', pygame.Rect(width * 0.166, height * 0.9, width * 0.2, height * 0.1))
        button1.on_click = lambda: 1
        button2 = button.Button('Strong attack', pygame.Rect(width * 0.432, height * 0.9, width * 0.2, height * 0.1))
        button2.on_click = lambda: 2
        button3 = button.Button('Block', pygame.Rect(width * 0.698, height * 0.9, width * 0.15, height * 0.1))
        button3.on_click = lambda: 3
        self.buttons = [button1, button2,button3]

        self.player = player.Player(phealth=50, pdamage=10)
        self.enemy = enemy.Enemy(ehealth=50, edamage=10)


    def run(self):
        combat = True
        turn = True
        lastppick = 0
        ppick = None
        epick = None

        buttons = self.buttons
        button1 = self.buttons[0]
        button2 = self.buttons[1]
        button3 = self.buttons[2]


        while True:
            # INPUT
            mouse_loc = pygame.mouse.get_pos()
            active_button = None
            for button in buttons:
                if button.rect.collidepoint(mouse_loc):
                    active_button = button

            if pygame.mouse.get_pressed()[0] and not pressed:
                if active_button is not None:
                    ppick = active_button.on_click()
                    turn = False
                    pressed = True
            elif not pygame.mouse.get_pressed()[0]:
                pressed = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            # UPDATE
            if turn:
                # Waiting on player
                pass
            else:
                # Handle the move
                lastppick = ppick
                ai = enemy_turn.enemyTurn(epick, ppick, self.enemy, self.player)
                if self.e_type == 'smartypants':
                    epick = smartypants.Smartypants(lastppick, epick)
                elif self.e_type == 'Favourguy':
                    epick = favourguy.Favourguy(lastppick, epick)
                elif self.e_type == 'coward':
                    epick = coward.Coward(lastppick, epick)
                elif self.e_type == 'Bob':
                    epick = Bob.Bob(lastppick, epick)
                elif self.e_type == 'mrdude':
                    epick = 2
                ai.enemy_play(self.display, self.Fonto)
                if self.player.phealth <= 0:
                    return True
                if self.enemy.ehealth <= 0:
                    return False
                turn = True

            # DRAW
            button1.draw(self.screen)
            button2.draw(self.screen)
            button3.draw(self.screen)
            self.window.draw(self.screen)

            ehptext_surface = self.Fonto.render('enemy HP = ' + str(self.player.phealth), False, (0, 0, 0))
            phptext_surface = self.Fonto.render('Player HP = ' + str(self.enemy.ehealth), False, (0, 0, 0))
            self.screen.blit(phptext_surface, (100, 100))
            self.screen.blit(ehptext_surface, (1000, 100))
            self.screen.blit(self.esurf, (768, 150))
            self.screen.blit(self.psurf, (213, 300))

            s = pygame.transform.scale(self.screen, self.display.get_size())
            self.display.blit(s, (0, 0))
            pygame.display.update()