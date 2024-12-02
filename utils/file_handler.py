import pygame
from pathlib import Path

base_path = Path(__file__).parent
assets_path = "assets/"


class ImageUrl(str):
    def __new__(cls, value):
        if not value.startswith("http") or value.startswith(assets_path):
            raise ValueError(f"ImageUrl must start with 'http' or {assets_path}")
        return super().__new__(cls, value)


def default_image(
        image_url: ImageUrl | None = None, 
        default_size: tuple[int, int] | None = None,
        default_color: tuple[int, int, int] | None = None
    ):
    if image_url:
        return pygame.image.load(base_path / image_url).convert_alpha()
    else:
        image = pygame.Surface(default_size)
        image.fill(default_color)
        return image
    