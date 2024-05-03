from settings import *


class World:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

    def run(self, fps):
        self.display_surface.fill('grey')
