import pygame

from game import Game

pygame.init()
pygame.display.set_caption("My Game")
screen = pygame.display.set_mode((1080, 700))
background = pygame.image.load('Tuto-Game/assets/bg.jpg')
game = Game()
running = True
while running:
  screen.blit(background, (-100, -200))
  game.player.all_projectiles.draw(screen)
  screen.blit(game.player.image, game.player.rect)
  for projectile in game.player.all_projectiles.sprites():
      projectile.launch()
  if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
    game.player.move_right()
  if game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
    game.player.move_left()
  pygame.display.flip()
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
          pygame.quit()
      elif event.type == pygame.KEYDOWN:
          game.pressed[event.key] = True
          if event.key == pygame.K_SPACE:
              game.player.launch_projectile()
      elif event.type == pygame.KEYUP:
          game.pressed[event.key] = False
    