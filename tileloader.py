from settings import *
from pytmx.util_pygame import load_pygame

class Tiles(pygame.sprite.Sprite):
    def __init__(self):

        self.tmx_data = load_pygame('Assets/tmx/basic.tmx')
        self.sprite_group = pygame.sprite.Group()

    def load_layers(self):

        #Loads tile layers
        for layer in self.tmx_data.visible_layers:
            # if layer.name in ('Platforms','Small Trees','Big Trees', 'Rocks'): #Use when you only want to show a selected range of layers
            if hasattr(layer,'data'): #Use to collect every layer
                for x,y,surf in layer.tiles():
                    pos = (x * 16, y * 16) #16 os the tile size
                    LoadTile(pos = pos, surface = surf, groups = self.sprite_group)
                # print(layer)

                
    def draw(self, display):
        #print(self.tmx_data.layernames)
        self.load_layers()
        self.sprite_group.draw(display)


class LoadTile(pygame.sprite.Sprite):
        def __init__(self, pos, surface, groups):
            super().__init__(groups)
            self.image = surface
            self.rect = self.image.get_rect(topleft = pos)

