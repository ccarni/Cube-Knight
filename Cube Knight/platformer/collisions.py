import pygame
import combat.combat_runner


# Class for things that the player can collide with

class Block(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image.copy()
        self.rect = image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.depth = 1

    def update(self, scroll = (0, 0)):
        self.rect.x = round(self.x - scroll[0])
        self.rect.y = round(self.y - scroll[1])

    def collide_vertical(self, player, **kwargs,):
        # Collide on top
        if player.rect.bottom > self.rect.top and player.v > 0:
            player.rect.bottom = self.rect.top
            player.v = 0
            player.on_ground = True
            player.airtime = 0

        # Collide on bottom
        if player.rect.top < self.rect.bottom and player.v < 0:
            player.rect.top = self.rect.bottom
            player.v = 0

    def collide_horizontal(self, player, **kwargs):
        # Collide with left side
        if player.rect.right > self.rect.left and player.horizontal_dir == 'right':
            player.rect.right = self.rect.left
        # Collide with right side
        if player.rect.left < self.rect.right and player.horizontal_dir == 'left':
            player.rect.left = self.rect.right

# A sublcass of block as an example of how to create special objects
class Combat(Block):
    def __init__(self, image, x, y, combat):
        Block.__init__(self, image, x, y)
        self.combat = combat
    def collide_vertical(self, player, **kwargs):
        runner = combat.combat_runner.Runner('smartypants')
        player_win = runner.run()
        if player_win:
            self.kill()
            del self
        else:
            player.respawn()

    def collide_horizontal(self, player, **kwargs):
        self.collide_vertical(player) # These are the same

class Spring(Block):
    def __init__(self, image, x, y, strength=15):
        Block.__init__(self, image, x, y)
        self.strength = strength

    def collide_vertical(self, player, **kwargs):
        # Collide on bottom
        if player.rect.top < self.rect.bottom and player.v < 0:
            player.rect.top = self.rect.bottom
            player.v = 0

    def collide_horizontal(self, player, **kwargs):
        player.v = -self.strength
        player.rect.bottom = self.rect.top

class Teleporter(Block):
    def __init__(self, image, x, y, teleX, teleY):
        Block.__init__(self, image, x, y)
        self.teleX = teleX
        self.teleY = teleY

    def collide_vertical(self, player, **kwargs):
        player.rect.x += self.teleX
        player.rect.y += self.teleY

    def collide_horizontal(self, player, **kwargs):
        player.rect.x += self.teleX
        player.rect.y += self.teleY


# The player!
class Player(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image.copy()
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.depth = 1
        self.spawnx = 0
        self.spawny = 0
        self.v = 0
        self.xv = 0
        self.xa = 1
        self.a = 1 # Acceleration due to gravity
        self.on_ground = False
        self.horizontal_dir = None # This is useful for determining collisions
        self.airtime = 0
        self.reset_blocks = []

    # What would be update_x happens inline in the draw/update loop
    def update_y(self, scroll=(0, 0)):
        self.v += self.a
        self.rect.y += self.v

    def respawn(self, scroll=(0,0), **kwargs):
        self.rect.x = self.spawnx
        self.rect.y = self.spawny

        for thing in self.reset_blocks:
            thing.respawn()

    def update_x(self, scroll=(0, 0)):
        if self.xv > 0:
            self.xv -= self.xa
        if self.xv < 0:
            self.xv += self.xa
        self.rect.x += self.xv

# from blocks.block import Block


class Spike(Block):

    def __init__(self, image, x, y):
        Block.__init__(self, image, x, y)

    def collide_vertical(self, player, scroll=0):
        player.rect.x += scroll[0]
        player.rect.y += scroll[1]
        player.respawn()
        player.rect.x -= scroll[0]
        player.rect.y -= scroll[1]
        return False

    def collide_horizontal(self, player, scroll=(0,0)):
        player.rect.x += scroll[0]
        player.rect.y += scroll[1]
        player.respawn()
        player.rect.x -= scroll[0]
        player.rect.y -= scroll[1]
        return False


class Checkpoint(Block):
    def __init__(self, image, x, y):
        Block.__init__(self, image, x, y)

    def collide_vertical(self, player, scroll=(0,0), **kwargs):
        player.spawnx = self.x
        player.spawny = self.y

    def collide_horizontal(self, player, scroll=(0,0), **kwargs):
        player.spawnx = self.x
        player.spawny = self.y

class Breakable(Block):
    def __init__(self, image, x, y, groups):
        Block.__init__(self, image, x, y)
        self.time_till_destroyed = -1
        self.groups = groups

    def collide_vertical(self, player, **kwargs):
        Block.collide_vertical(self,player)
        if self.time_till_destroyed == -1:
            self.time_till_destroyed = 15

    def collide_horizontal(self, player, **kwargs):
        Block.collide_horizontal(self,player)
        if self.time_till_destroyed == -1:
            self.time_till_destroyed = 15

    def respawn(self):
        for group in self.groups:
            group.add(self)
        self.time_till_destroyed = -1

    def update(self, scroll):
        Block.update(self, scroll)
        if self.time_till_destroyed > 0:
            self.time_till_destroyed -= 1

        if self.time_till_destroyed == 0:
            self.kill()
            return

class Bouncer(Block):
    def __init__(self, image, x, y, bstrength):
        Block.__init__(self, image, x, y)
        self.bstrength = bstrength

    def collide_vertical(self, player, **kwargs):
        if player.rect.bottom == self.rect.bottom:
            player.xv = self.bstrength
            player.v = -5

    def collide_horizontal(self, player, **kwargs):
        player.xv = self.bstrength
        player.v = -5


class Water(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image.copy()
        self.rect = image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.depth = 1

    def update(self, scroll = (0, 0)):
        self.rect.x = round(self.x - scroll[0])
        self.rect.y = round(self.y - scroll[1])

    def collide_vertical(self, player, **kwargs):
        player.on_ground = True
        player.on_water = True
        return False


    def collide_horizontal(self, player, **kwargs):
        player.on_ground = True
        return False
#
# class Flag(pygame.sprite.Sprite):
#
#     def __init__(self, image, x, y):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = image.copy()
#         self.rect = image.get_rect()
#         self.x = x
#         self.y = y
#         self.rect.x = x
#         self.rect.y = y
#         self.depth = 1
#
#     def update(self, scroll = (0, 0)):
#         self.rect.x = round(self.x - scroll[0])
#         self.rect.y = round(self.y - scroll[1])
#
#     def collide_vertical(self, player, **kwargs):
#         return True
#
#
#     def collide_horizontal(self, player, **kwargs):
#         return True
#
#
#
# class Mud(Block):
#
#     def __init__(self, image, x, y):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = image.copy()
#         self.rect = image.get_rect()
#         self.x = x
#         self.y = y
#         self.rect.x = x
#         self.rect.y = y
#         self.depth = 1
#
#     def update(self, scroll = (0, 0)):
#         self.rect.x = round(self.x - scroll[0])
#         self.rect.y = round(self.y - scroll[1])
#
#     def collide_vertical(self, player, **kwargs):
#         # Collide on top
#         if player.rect.bottom > self.rect.top and player.v > 0:
#             player.rect.bottom = self.rect.top
#             player.v = 0
#             player.on_ground = True
#             player.on_mud = True
#
#         # Collide on bottom
#         if player.rect.top < self.rect.bottom and player.v < 0:
#             player.rect.top = self.rect.bottom
#             player.v = 0
#
#         return False
#
#     def collide_horizontal(self, player, **kwargs):
#         # Collide with left side
#         if player.rect.right > self.rect.left and player.horizontal_dir == 'right':
#             player.rect.right = self.rect.left
#         # Collide with right side
#         if player.rect.left < self.rect.right and player.horizontal_dir == 'left':
#             player.rect.left = self.rect.right
#
#         return False
#
#
# class Ladder(pygame.sprite.Sprite):
#
#     def __init__(self, image, x, y):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = image.copy()
#         self.rect = image.get_rect()
#         self.x = x
#         self.y = y
#         self.rect.x = x
#         self.rect.y = y
#         self.depth = 1
#
#     def update(self, scroll = (0, 0)):
#         self.rect.y = round(self.y - scroll[1])
#
#     def collide_vertical(self, player, **kwargs):
#         player.on_ground = True
#         player.on_ladder = True
#         return False
#
#
#     def collide_horizontal(self, player, **kwargs):
#         player.on_ground = True
#         return False
#
#
# class Ice(Block):
#
#     def __init__(self, image, x, y):
#         Block.__init__(self, image, x, y)
#
#     def collide_vertical(self, player, **kwargs):
#         # Collide on top
#         if player.rect.bottom > self.rect.top and player.v > 0:
#             player.rect.bottom = self.rect.top
#             player.v = 0
#             player.on_ice = True
#             player.on_ground = True
#
#
#         # Collide on bottom
#         if player.rect.top < self.rect.bottom and player.v < 0:
#             player.rect.top = self.rect.bottom
#             player.v = 0
#
#         return False
#
#     def collide_horizontal(self, player, **kwargs):
#         # Collide with left side
#         if player.rect.right > self.rect.left and player.horizontal_dir == 'right':
#             player.rect.right = self.rect.left
#         # Collide with right side
#         if player.rect.left < self.rect.right and player.horizontal_dir == 'left':
#             player.rect.left = self.rect.right
#
#         return False
