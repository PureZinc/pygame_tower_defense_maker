import pygame
from utils.file_handler import default_image
from config.config import GREEN, BLUE


class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y, weapon: 'Projectile'=None, image_url=None):
        super().__init__()
        self.image = default_image(image_url, default_size=(30, 30), default_color=GREEN)
        self.rect = self.image.get_rect(center=(x, y))
        self.range = 150
        self.cooldown = 1000  # Fire rate in milliseconds
        self.last_shot = pygame.time.get_ticks()

    def attack(self, enemies, bullets_group):
        now = pygame.time.get_ticks()
        pass


class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, target, image_url=None):
        super().__init__()
        self.image = default_image(image_url, default_size=(10, 10), default_color=BLUE)
        self.rect = self.image.get_rect(center=(x, y))
        self.target = target
        self.speed = 5

    def update(self):
        if self.target.alive():
            movement = pygame.math.Vector2(self.target.rect.centerx - self.rect.x, self.target.rect.centery - self.rect.y)
            if movement.length() > self.speed:
                movement = movement.normalize() * self.speed
            self.rect.x += movement.x
            self.rect.y += movement.y
            if self.rect.colliderect(self.target.rect):
                self.target.kill()
                self.kill()
        else:
            self.kill()