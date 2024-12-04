import pygame
from pygame.locals import *
from window import Window
from plot import Plot

class Game:
    def __init__(self):
        self.window = Window(1980, 1240)
        pygame.init()

        self.screen = pygame.display.set_mode(self.window.get_dimensions())

        self.clock = pygame.time.Clock()

        self.running = True

        self.plot_width = self.window.get_dimensions()[0] / 1.25
        self.plot_height = self.window.get_dimensions()[1] /  1.5


        self.plot_position_x = self.plot_width * 0.1
        self.plot_position_y = self.plot_height * 0.1
    
        self.plot = Plot(self.plot_position_x, self.plot_position_y, self.plot_width, self.plot_height)

        self.plot.test_grid()

    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
            self.screen.fill("black")

            self.plot.draw(self.screen)

            pygame.display.flip()

            self.__keyboard_event_listener()

            self.clock.tick(60)

    def __keyboard_event_listener(self):
        keys = pygame.key.get_pressed()

        if keys[K_ESCAPE] or keys[K_q]:
            self.running = False

    def quit(self):
        pygame.quit()    

def main():
    game = Game()

    game.loop()
     
    game.quit()
    

if __name__ == "__main__":
    main()
