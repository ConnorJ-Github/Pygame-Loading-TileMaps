from settings import *
from world import World

class Game:
    def __init__(self):
        pygame.init()
        self.WIN = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Collision Demo")

        self.clock = pygame.time.Clock()

        self.world_screen = World()

        self.tmx_data = load_pygame('Assets/tmx/basic.tmx')
        


    def run(self):
        while True:
            fps = self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT()


            self.world_screen.run(fps)
            print(self.tmx_data)



            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()