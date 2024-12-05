import pygame
from .global_ui.base import Screen


class MainMenu(Screen):
    def __init__(self):
        super().__init__()
        pygame.font.init()
        self.title_font = pygame.font.Font(None, 74)
        self.title_text = self.title_font.render("Main Menu", True, (255, 255, 255))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return "gameplay"  # Indicate switching to the gameplay screen

    def render(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.title_text, (200, 150))