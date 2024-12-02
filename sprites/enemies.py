import pygame
from utils.file_handler import default_image
from config.config import RED


class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed=2, health=1, image_url=None):
        super().__init__()
        self.image = default_image(image_url, default_size=(30, 30), default_color=RED)
        self.speed = speed
        self.health = health
        self.path_index = 0

    def set_path(self, path: list[tuple[int, int]]):
        self.path = path
        self.rect = self.image.get_rect(center=path[0])

    def update(self):
        if hasattr(self, 'path') and self.path and self.path_index < len(self.path):
            target_position = self.path[self.path_index]
            movement = pygame.math.Vector2(target_position[0] - self.rect.x, target_position[1] - self.rect.y)

            # Move the enemy towards the target position
            if movement.length() > self.speed:
                movement = movement.normalize() * self.speed
            self.rect.x += movement.x
            self.rect.y += movement.y

            # Check if the enemy has reached the target point
            if self.rect.colliderect(pygame.Rect(target_position[0], target_position[1], 1, 1)):
                self.path_index += 1  # Move to the next point in the path

            # Remove the enemy when it has reached the end of the path
            if self.path_index >= len(self.path):
                self.kill()
