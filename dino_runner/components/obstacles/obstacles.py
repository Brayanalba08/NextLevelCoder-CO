from pygame.sprite import Sprite
from dino_runner.utils.constans import SCREEN_WIDTH

class Obstacle(Sprite):

    def __init__(self, image):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed):
        self.rect.x -= game_speed
        if self.rect.x < 0:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)