import pygame
from projectile import Projectile


class Player(pygame.sprite.Sprite):
    def __init__(self):
      super().__init__()
      self.health = 100
      self.max_health = 100
      self.attack = 10
      self.all_projectiles = pygame.sprite.Group()
      self.velocity = 1
      self.image = pygame.image.load('Tuto-Game/assets/player.png')
      self.rect = self.image.get_rect()
      self.rect.x = 400
      self.rect.y = 500
    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))
    def move_right(self):
      self.rect.x += self.velocity
    def move_left(self):
      self.rect.x -= self.velocity
    def attack(self):
        self.health -= self.attack
        if self.health <= 0:
            self.health = 0
            print("You died")
        else:
            print("You attacked")