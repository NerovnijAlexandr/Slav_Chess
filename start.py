import pygame

from objs import *

CELL_SIZE = 64
CELL_IN_ROW = 9
LEVEL = [
    (0, 0, 0, 3, 3, 3, 0, 0, 0),
    (0, 0, 0, 0, 3, 0, 0, 0, 0),
    (0, 0, 0, 0, 2, 0, 0, 0, 0),
    (3, 0, 0, 0, 2, 0, 0, 0, 3),
    (3, 3, 2, 2, 1, 2, 2, 3, 3),
    (3, 0, 0, 0, 2, 0, 0, 0, 3),
    (0, 0, 0, 0, 2, 0, 0, 0, 0),
    (0, 0, 0, 0, 3, 0, 0, 0, 0),
    (0, 0, 0, 3, 3, 3, 0, 0, 0)
]

KING = (128, 128, 255)
DEFENDERS = (0 ,0, 255)
ATACKS = (255, 128, 0)

class Game:
    def __init__(self):
        self.__level = LEVEL
        self.__size = [CELL_IN_ROW * CELL_SIZE for i in range(2)]
        self.__cell_size = CELL_SIZE

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption('Славянские шахматы v1.0.0.0')


        self.screen = pygame.display.set_mode(self.__size, pygame.DOUBLEBUF, 32)
        self.clock = pygame.time.Clock()
        self.__frame_rate = 60

    def draw(self):
        for numrow, row in enumerate(self.__level, start=1):
            for numcell, cell in enumerate(row, start=1):
                color = None
                if cell == 1:
                    color = KING
                elif cell == 2:
                    color = DEFENDERS
                elif cell == 3:
                    color = ATACKS
                if color != None:
                    pygame.draw.circle(self.screen,
                                       color,
                                       (numrow * self.__cell_size - self.__cell_size//2, numcell * self.__cell_size-self.__cell_size//2),
                                       self.__cell_size // 2)




    def run(self):
        while True:
            self.clock.tick(self.__frame_rate)
            self.screen.fill((0, 0, 0))

            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            pygame.display.update()


def main():
    g1 = Game()
    g1.run()

if __name__ == '__main__':
    main()
