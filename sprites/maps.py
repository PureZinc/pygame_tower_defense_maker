import pygame
from utils.file_handler import default_image
from config.config import SCREEN_DIMENSIONS, screen, BLACK, BACKGROUND
from .enemies import Enemy

class BattleMap(pygame.sprite.Sprite):
    def __init__(self, image_url=None, paths=None):
        super().__init__()
        self.image = default_image(image_url, default_size=SCREEN_DIMENSIONS, default_color=BACKGROUND)
        self.paths = paths
        self.num_paths = len(paths)
        self.enemies = pygame.sprite.Group()

    def update_enemies(self):
        self.enemies.update()

    def get_path_index_for_round(self, round):
        p = (round-1) % self.num_paths
        return p, self.paths[p][0]
    
    def spawn_enemy(self, enemy_sprite: Enemy, round=1):
        _, enemy_path = self.get_path_index_for_round(round)
        enemy_sprite.set_path(enemy_path)
        enemy_sprite.rect.topleft = enemy_path[0]
        self.enemies.add(enemy_sprite)
    
    def draw(self):
        screen.blit(self.image, (0, 0))
        self._draw_path()
        self.enemies.draw(screen)
    
    def _draw_path(self):
        for path in self.paths:
            for point in path:
                pygame.draw.circle(screen, BLACK, point, 5)
