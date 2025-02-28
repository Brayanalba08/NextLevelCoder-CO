from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.components.obstacles.cactus import Cactus
import pygame

class ObstacleManager:
    
    def __init__(self):
        self.obstacles = []
        
    def update(self, game):
        if len(self.obstacles) == 0:
            new_obstacle = Cactus(SMALL_CACTUS)
            self.obstacles.append(new_obstacle)
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.shield:
                    self.obstacles.remove(obstacle)
                else:
                    pygame.time.delay(500)
                    game.playing = False
                    break;  

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
