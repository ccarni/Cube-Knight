import pygame
import random
import sys
import platformer.helper
import platformer.landscape as landscape
import platformer.collisions as collisions
import platformer.background as background

def draw_player():
    surf = pygame.Surface((95, 95))
    pygame.draw.rect(surf, (246, 247, 139), (0,0,surf.get_width(), surf.get_height()))
    pygame.draw.circle(surf, (0, 0, 0), (surf.get_width(), surf.get_height() / 3),5 + surf.get_width() / 2)
    pygame.draw.circle(surf,(200,200,200), (surf.get_width(), surf.get_height()/3) ,surf.get_width()/2 )
    pygame.draw.rect(surf, (246, 247, 139), (0, 0, surf.get_width(), surf.get_height()/3))
    pygame.draw.rect(surf, (246, 247, 139), (0, 2 * surf.get_height() / 3, surf.get_width(), surf.get_height() / 3))
    pygame.draw.rect(surf, (50, 50, 50), (8 * surf.get_width() / 12,surf.get_height() / 3, surf.get_width()/30, surf.get_height() / 3))
    pygame.draw.rect(surf, (50, 50, 50), (7 * surf.get_width() / 12, surf.get_height() / 3, surf.get_width() / 30, surf.get_height() / 3))
    pygame.draw.rect(surf, (50, 50, 50), (9 * surf.get_width() / 12, surf.get_height() / 3, surf.get_width() / 30, surf.get_height() / 3))
    pygame.draw.rect(surf, (50, 50, 50), (10 * surf.get_width() / 12, surf.get_height() / 3, surf.get_width() / 30, surf.get_height() / 3))
    pygame.draw.rect(surf, (50, 50, 50), (11 * surf.get_width() / 12, surf.get_height() / 3, surf.get_width() / 30, surf.get_height() / 3))
    pygame.draw.line(surf,(246, 247, 139),(10*surf.get_width()/30,10*surf.get_height()/30),(20*surf.get_width()/24,surf.get_height()),10)
    pygame.draw.rect(surf, (0, 0, 0), (surf.get_width() / 2, surf.get_height() / 3, surf.get_width() / 2, 10))
    pygame.draw.rect(surf, (0, 0, 0),(29 * surf.get_width() / 48, 2 * surf.get_height() / 3, surf.get_width() / 2, 5))
    pygame.draw.rect(surf,(0,0,0), (0,0,surf.get_width(),5))
    pygame.draw.rect(surf, (0, 0, 0), (0, 0, 5, surf.get_height()))
    pygame.draw.rect(surf, (0, 0, 0), (0, surf.get_height()-5, surf.get_width(), 5))
    pygame.draw.rect(surf, (0, 0, 0), (surf.get_width() - 5,0 ,5 , surf.get_height()))
    surf = pygame.transform.scale(surf, (10, 10))
    return surf

foreground_blocks = pygame.sprite.Group()
background_blocks = pygame.sprite.Group()



objs = []
# Make the clouds
# for i in range(20):
#     x = random.randint(0, level_size[0]//tilesize)
#     y = random.randint(0, level_size[1]//tilesize//2)
#     c = background.Background(cloud, x*tilesize, y*tilesize)
#     c.depth = random.uniform(0.5, 1)
#     objs.append(c)

# # Make the mountains (which look more like trees)
def make_mountains(self, level_size, objs):
    for i in range(50):
        x = random.randint(0, level_size[0])
        y = random.randint(100, 2 * level_size[1] // 3)
        w = random.randint(50, 500)
        mountain = platformer.helper.draw_mountain(w, level_size[1] - y)
        m = background.Background(mountain, x, y)
        m.depth = random.uniform(0.25, 0.5)
        temp_surf = pygame.Surface(mountain.get_size()).convert_alpha()
        temp_surf.fill((0, 0, 0, 255 * m.depth))
        m.image.blit(temp_surf, (0, 0))
        m.image.set_colorkey((0, 0, 0))
        objs.append(m)

# draw the moon
# moon = landscape.draw_moon()
# m = background.Background(moon, 200, 10)
# m.depth = 0.1 # This depth controls the parallax - smaller is slower
# objs.append(m)

# # Draw the stars
def make_stars(self, level_size, objs):
    for i in range(500):
        star = platformer.helper.draw_star(random.randint(1, 20))
        star.set_alpha(random.randint(0, 255))
        x = random.randint(-1 * level_size[0], level_size[0])
        y = random.randint(-1 * level_size[1], level_size[1])
        s = background.Background(star, x, y)
        s.depth = random.uniform(0, 0.01)
        objs.append(s)

    return star, x, y, s, objs

objs.sort(key=lambda x: x.depth)

def build_world(block_grid, tilesize):
    dirt = landscape.draw_dirt()
    grass = landscape.draw_grass(dirt)
    cloud = landscape.draw_cloud()
    spring = landscape.draw_spring()
    teleporter = landscape.draw_teleporter()
    spike = landscape.draw_spike()
    checkpoint = landscape.draw_checkpoint()
    breakable = landscape.draw_breakable()
    bouncer = landscape.draw_bouncer()
    combat = landscape.draw_combat()
    # Make all the tiles the right size
    cloud = pygame.transform.scale(cloud, (tilesize, tilesize))
    dirt = pygame.transform.scale(dirt, (tilesize, tilesize))
    grass = pygame.transform.scale(grass, (tilesize, tilesize))
    spring = pygame.transform.scale(spring, (tilesize, tilesize / 2))
    teleporter = pygame.transform.scale(teleporter, (tilesize, tilesize / 2))
    # spike = pygame.transform.scale(spike, (tilesize, tilesize/2))
    checkpoint = pygame.transform.scale(checkpoint, (tilesize, tilesize / 2))
    breakable = pygame.transform.scale(breakable, (tilesize, tilesize))
    bouncer = pygame.transform.scale(bouncer, (tilesize, tilesize / 2))
    combat = combat = pygame.transform.scale(combat, (tilesize, tilesize))
    # new code may break
    spike_up = pygame.transform.scale(landscape.draw_spike(0), (tilesize, tilesize))
    spike_down = pygame.transform.scale(landscape.draw_spike(180), (tilesize, tilesize))
    spike_left = pygame.transform.scale(landscape.draw_spike(90), (tilesize, tilesize))
    spike_right = pygame.transform.scale(landscape.draw_spike(270), (tilesize, tilesize))
    water = pygame.transform.scale(landscape.draw_water(), (tilesize, tilesize))

    blocks = pygame.sprite.Group()
    reset_blocks = []
    for row in range(len(block_grid)):
        for col in range(len(block_grid[row])):
            if block_grid[row][col] == 'd':
                d = collisions.Block(dirt, col*tilesize, row*tilesize)
                blocks.add(d)
            if block_grid[row][col] == 'g':
                g = collisions.Block(grass, col*tilesize, row*tilesize)
                blocks.add(g)
            if block_grid[row][col] == 's':
                s = collisions.Spring(spring, col*tilesize, row*tilesize + tilesize/2)
                blocks.add(s)
            #water rework for water logged spikes
            if block_grid[row][col] == 'w': #or block_grid[row][col] == 'k' or block_grid[row][col] == 'b' or block_grid[row][col] == 'l' or block_grid[row][col] == 'r':or block_grid[row][col] == 'U' or block_grid[row][col] == 'B' or block_grid[row][col] == 'L' or block_grid[row][col] == 'R':
                w = collisions.Water(water, col * tilesize, row * tilesize)
                background_blocks.add(w)
                blocks.add(w)
            #combat block
            if block_grid[row][col] == 'V':
                V = collisions.Combat(combat, col*tilesize, row*tilesize, False)
                blocks.add(V)
            #teleporters
            #up
            if block_grid[row][col] == 'U':
                U = collisions.Teleporter(teleporter, col*tilesize, row*tilesize + tilesize/2, 0, -120)
                blocks.add(U)
            #down
            if block_grid[row][col] == 'D':
                D = collisions.Teleporter(teleporter, col*tilesize, row*tilesize + tilesize/2, 0, 120)
                blocks.add(D)
            #left
            if block_grid[row][col] == 'L':
                L = collisions.Teleporter(teleporter, col*tilesize, row*tilesize + tilesize/2, -120, 0)
                blocks.add(L)
            #right
            if block_grid[row][col] == 'R':
                R = collisions.Teleporter(teleporter, col*tilesize, row*tilesize + tilesize/2, 120, 0)
                blocks.add(R)
            # spike code
            #up
            if block_grid[row][col] == 'k':
                K = collisions.Spike(spike_up, col * tilesize, row * tilesize)
                foreground_blocks.add(K)
                blocks.add(K)
            #down
            if block_grid[row][col] == 'b':
                B = collisions.Spike(spike_down, col * tilesize, row * tilesize)
                foreground_blocks.add(B)
                blocks.add(B)
            #left
            if block_grid[row][col] == 'l':
                L = collisions.Spike(spike_left, col * tilesize, row * tilesize)
                foreground_blocks.add(L)
                blocks.add(L)
            #right
            if block_grid[row][col] == 'r':
                r = collisions.Spike(spike_right, col * tilesize, row * tilesize)
                foreground_blocks.add(r)
                blocks.add(r)
           #breakable blocks
            if block_grid[row][col] == 'u':
                u = collisions.Breakable(breakable, col*tilesize, row*tilesize, [blocks])
                blocks.add(u)
                reset_blocks.append(u)
            #bouncer right
            if block_grid[row][col] == 'p':
                p = collisions.Bouncer(bouncer, col*tilesize, row*tilesize + tilesize/2, 15)
                blocks.add(p)
            #bouncer left
            if block_grid[row][col] == 'q':
                q = collisions.Bouncer(bouncer, col*tilesize, row*tilesize + tilesize/2, -15)
                blocks.add(q)


    return blocks

class Runner:
    def __init__(self):
        self.tilesize = 20
        with open('platformer/level.txt', 'r') as level:
            block_grid = level.read()
            self.block_grid = block_grid.split('\n')
        self.blocks = build_world(self.block_grid, self.tilesize)

        self.level_size = (self.tilesize * len(block_grid[0]), self.tilesize * len(block_grid))

        self.display = pygame.display.set_mode(flags=pygame.FULLSCREEN)
        self.screen = pygame.Surface((300, 200))

        self.clock = pygame.time.Clock()
        self.fps = 30
        self.true_scroll = [0, 0]
        self.scroll = [0, 0]
        self.player = collisions.Player(draw_player(), 0, 0)

    def run(self):
        clock = self.clock
        fps = self.fps
        scroll = self.scroll
        true_scroll = self.true_scroll
        running = True
        screen = self.screen
        blocks = self.blocks
        display = self.display
        player = self.player
        level_size = self.level_size
        tilesize = self.tilesize
        block_grid = self.block_grid

        while running:
            clock.tick(fps)

            # DRAW
            screen.fill((60, 20, 90))
            for obj in objs:
                screen.blit(obj.image, obj.rect)
            blocks.draw(screen)
            screen.blit(player.image, (player.rect.x-scroll[0], player.rect.y-scroll[1]))
            s = pygame.transform.scale(screen, display.get_size())
            display.blit(s, (0, 0))
            pygame.display.update()

            # INPUT
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_SPACE and (player.on_ground or player.airtime <= 2):
                        player.v = -10
                        player.on_ground = False


            # UPDATE
            keys = pygame.key.get_pressed()
            player.horizontal_dir = None
            if keys[pygame.K_a]:
                player.rect.x -= 2
                player.horizontal_dir = 'left'
                if player.rect.x < 0:
                    player.rect.x = 0

            if keys[pygame.K_d]:
                player.rect.x += 2
                player.horizontal_dir = 'right'
                if player.rect.right-scroll[0] > screen.get_width():
                    player.rect.right = screen.get_width() + scroll[0]

            # Reset the player if they fall good for checkpoints
            if player.rect.y > level_size[1]:
                player.respawn()

            # The camera magic :)
            # Every object moves based on the scroll variable
            # The scroll variable updates based on how far from the player the center of the screen is
            true_scroll[0] += (player.rect.x - true_scroll[0] - screen.get_width() / 2) / 20
            true_scroll[1] += (player.rect.y - true_scroll[1] - screen.get_height() / 2) / 20

            # Casting to an integer when using the scroll improves the quality
            scroll[0] = int(true_scroll[0])
            scroll[1] = int(true_scroll[1])

            # Block scrolling on reaching level boundaries
            if scroll[0] < 0:
                scroll[0] = 0
            if scroll[0] + screen.get_width() > len(block_grid[0]) * tilesize:
                scroll[0] = len(block_grid[0]) * tilesize - screen.get_width()

            if scroll[1] < 0:
                scroll[1] = 0
            if scroll[1] + screen.get_height() > len(block_grid) * tilesize:
                scroll[1] = len(block_grid) * tilesize - screen.get_height()

            # Update block and background locations
            for obj in objs:
                obj.update(scroll)
            blocks.update(scroll)

            # Convert the player coordinates to world coordinates
            player.rect.x -= scroll[0]
            player.rect.y -= scroll[1]

            # Check horizontal collisions
            # Doing things this way avoids issues where the collision occurs on a corner of the block
            # so that there isn't confusion over whether to place the player above the block or to the side
            player.update_x(scroll)
            collides = pygame.sprite.spritecollide(player, blocks, dokill=False)
            for block in collides:
                block.collide_horizontal(player, scroll=scroll)

            # Update y position and check vertical collisions
            player.update_y(scroll)
            collides = pygame.sprite.spritecollide(player, blocks, dokill=False)
            for block in collides:
                block.collide_vertical(player, scroll=scroll)

            if not player.on_ground:
                player.airtime += 1
            # Convert the world coordinates back to player coordinates
            player.rect.x += scroll[0]
            player.rect.y += scroll[1]
