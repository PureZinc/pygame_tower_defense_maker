import pygame
from pygame.locals import *
import sys
from config.config import *
from sprites import *
from app import *

# Initialize Pygame
pygame.init()

# Game setup
def main():
    chosen_map = all_maps['base']

    # Enemy spawn event
    ENEMY_SPAWN = pygame.USEREVENT + 1
    pygame.time.set_timer(ENEMY_SPAWN, 2000)

    running = True
    while running:
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == ENEMY_SPAWN:
                new_enemy = Enemy()
                new_enemy.set_path(chosen_map.paths[0])
                enemies.add(new_enemy)
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                new_tower = Tower(*mouse_pos)
                towers.add(new_tower)

        # Update
        towers.update()
        enemies.update()
        bullets.update()

        for tower in towers:
            tower.attack(enemies, bullets)

        # Draw
        chosen_map.draw()
        towers.draw(screen)
        enemies.draw(screen)
        bullets.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

# Run the game
if __name__ == "__main__":
    main()
