import pygame
from vector import Vector2D

class Plot:
    def __init__(self, plot_position: Vector2D,
                 plot_dimensions: Vector2D):
        
        self.plot_position = plot_position
        self.plot_dimensions = plot_dimsnions

        self.__init_grid()

    def __init__(self, x: float, y: float, width: float, height: float):
        plot_position = Vector2D(x, y)
        plot_dimensions = Vector2D(width, height)

        self.plot_position = plot_position
        self.plot_dimensions = plot_dimensions
        self.rect = pygame.Rect(self.plot_position.get_dimensions(),
                                self.plot_dimensions.get_dimensions())

        self.__init_grid()

    def __init_grid(self):
        self.x_arr = list()
        self.y_arr = list()
        
        max_width = self.plot_dimensions.get_dimensions()[0]
        max_height = self.plot_dimensions.get_dimensions()[1]
        
        gridcell_width = max_width / 30
        gridcell_height = max_height / 20

        curr_width = 0
        curr_height = 0
        
        while curr_width <= max_width:
            curr_width += gridcell_width
            self.x_arr.append(curr_width)

        while curr_height <= max_height:
           curr_height += gridcell_height
           self.y_arr.append(curr_height)

    def test_grid(self):
        for x in self.x_arr:
            print(x)

        for y in self.y_arr:
            print(y)

    def __draw_grid(self, surface):
        max_width = self.plot_dimensions.get_dimensions()[0]
        max_height = self.plot_dimensions.get_dimensions()[1]
        for x in self.x_arr:
            pygame.draw.aaline(surface, (0, 0, 0),
                               (x,
                                self
                                .plot_position
                                .get_dimensions()[0]),
                                
                                (x, max_height))

        for y in self.y_arr:
            pygame.draw.aaline(surface, (0, 0, 0),
                               (self
                                .plot_position
                                .get_dimensions()[1],
                                y), (max_width, y))

        
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect)
        self.__draw_grid(surface)
