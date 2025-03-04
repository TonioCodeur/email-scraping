import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 2.5
        self.image = pygame.image.load('Tuto-Game/assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + player.rect.width - 50
        self.rect.y = player.rect.y + (player.rect.height / 2) -10
        self.player = player
        self.origin_image = self.image.copy()
        self.angle = 0
    def rotate(self):
        self.angle += 2
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
    def remove(self):
      self.kill()
    def launch(self):
        self.rect.x += self.velocity
        if self.rect.x > 1080:
            self.remove()
        self.rotate()  # Fait tourner le sprite lentement
    def update(self):
        self.rect.y -= 1
        if self.rect.y < -100:
            self.kill()