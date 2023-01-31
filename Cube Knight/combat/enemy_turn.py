import pygame

class enemyTurn():
	def __init__(self, epick, ppick, enemy, player):
		self.epick = epick
		self.ppick = ppick
		self.enemy = enemy
		self.player = player

	def enemy_play(self, screen, Fonto):
		if self.epick == 3 and self.ppick == 2:
			epicktext_surface = Fonto.render('Enemy Blocked:You win', False, (0, 0, 0))
			screen.blit(epicktext_surface, (500, 100))
			pygame.display.update()
			pygame.time.wait(1000)
			self.player.Ponhit(self.enemy.edamage)


		if self.epick == 3 and self.ppick == 3:
			epicktext_surface = Fonto.render('Enemy Blocked:You tie', False, (0, 0, 0))
			screen.blit(epicktext_surface, (500, 100))
			pygame.display.update()
			pygame.time.wait(1000)

		if self.epick == 2 and self.ppick == 1:
			epicktext_surface = Fonto.render('Enemy Attacked Strongly:You win', False, (0, 0, 0))
			screen.blit(epicktext_surface, (500, 100))
			pygame.display.update()
			pygame.time.wait(1000)
			self.player.Ponhit(self.enemy.edamage)

		if self.epick == 2 and self.ppick == 3:
			epicktext_surface = Fonto.render('Enemy Attacked Strongly:You lose', False, (0, 0, 0))
			screen.blit(epicktext_surface, (500, 100))
			pygame.display.update()
			pygame.time.wait(1000)
			self.enemy.Eonhit(self.player.pdamage)

		if self.epick == 2 and self.ppick == 2:
			epicktext_surface = Fonto.render('Enemy Attacked Strongly:You tie', False, (0, 0, 0))
			screen.blit(epicktext_surface, (500, 100))
			pygame.display.update()
			pygame.time.wait(1000)

		if self.epick == 1 and self.ppick == 2:
			epicktext_surface = Fonto.render('Enemy Attacked Quickly:You lose', False, (0, 0, 0))
			screen.blit(epicktext_surface, (500, 100))
			pygame.display.update()
			pygame.time.wait(1000)
			self.enemy.Eonhit(self.player.pdamage)

		if self.epick == 1 and self.ppick == 3:
			epicktext_surface = Fonto.render('Enemy Attacked Quickly:You win', False, (0, 0, 0))
			screen.blit(epicktext_surface, (500, 100))
			pygame.display.update()
			pygame.time.wait(1000)
			self.player.Ponhit(self.enemy.edamage)

		if self.epick == 1 and self.ppick == 1:
			epicktext_surface = Fonto.render('Enemy Attacked Quickly:You tie', False, (0, 0, 0))
			screen.blit(epicktext_surface, (500, 100))
			pygame.display.update()
			pygame.time.wait(1000)

		if self.epick == 3 and self.ppick == 1:
			epicktext_surface = Fonto.render('Enemy Blocked:You lose', False, (0, 0, 0))
			screen.blit(epicktext_surface, (500, 100))
			pygame.display.update()
			pygame.time.wait(1000)
			self.enemy.Eonhit(self.player.pdamage)