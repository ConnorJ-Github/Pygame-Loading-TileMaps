from settings import *
from tileloader import Tiles

class World:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.background_image = pygame.image.load('Assets/Background/Background.png')
        self.background_image = pygame.transform.scale(self.background_image,(HEIGHT,WIDTH))
        self.tile_map = Tiles()


    def run(self, fps):
        # self.display_surface.fill('grey')
        self.display_surface.blit(self.background_image,(0,0))
        self.tile_map.draw(self.display_surface)
