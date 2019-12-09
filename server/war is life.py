import pygame
from pygame.locals import *
from random import randint as rand
from random import choice as rand1


class GameOfLife:
    def __init__(self, width=1080, height=720, cell_size=10, speed=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

        self.k = 0

        self.colors = ['white', 'gray', 'blue', 'red']
        self.n = len(self.colors)
        self.score = [{'converted': 0, 'result': 0} for i in range(self.n)]
        self.moves = 10
        self.counter = 0

        self.chosengame = 0

    def draw_war_map(self):
        pygame.draw.rect(self.screen, pygame.Color('red'), (260, 180, 120, 120), 3)
        pygame.draw.rect(self.screen, pygame.Color('red'), (0, 0, 200, 140), 3)
        pygame.draw.rect(self.screen, pygame.Color('red'), (440, 0, 640, 140), 3)
        pygame.draw.rect(self.screen, pygame.Color('red'), (0, 340, 200, 480), 3)
        pygame.draw.rect(self.screen, pygame.Color('red'), (440, 340, 640, 480), 3)

    def draw_grid(self):
        # http://www.pygame.org/docs/ref/draw.html#pygame.draw.line
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (0, y), (self.width, y))

    def evolve(self):
        temporary_matrix = [[0] * self.cell_width for i in range(self.cell_height)]
        for t in self.score:
            t['result'] = 0
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                colors_distribution = [0] * self.n
                for i1 in range(i - 1, i + 2):
                    for j1 in range(j - 1, j + 2):
                        if not (i1 == i and j1 == j):
                            colors_distribution[self.cell_list[i1 % self.cell_height][j1 % self.cell_width]] += 1
                if self.cell_list[i][j] == 0:
                    if colors_distribution[0] == 5:
                        max_color = max(colors_distribution[1:])
                        if max_color == 3:
                            col = colors_distribution.index(max_color)
                            temporary_matrix[i][j] = col
                            self.score[col]['result'] += 1
                        else:
                            temporary_matrix[i][j] = 1
                            self.score[1]['result'] += 1
                    else:
                        temporary_matrix[i][j] = 0
                        self.score[0]['result'] += 1
                else:
                    if colors_distribution[0] in [5, 6]:
                        max_color = max(colors_distribution[1:])
                        if max_color == 8 - colors_distribution[0]:
                            col = colors_distribution.index(max_color)
                        else:
                            col = 1
                        temporary_matrix[i][j] = col
                        self.score[col]['result'] += 1
                    else:
                        temporary_matrix[i][j] = 0
                        self.score[0]['result'] += 1
        for t in self.score:
            t['converted'] += t['result']
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                self.cell_list[i][j] = temporary_matrix[i][j]

    def start_game(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('LSD-Life')
        self.screen.fill(pygame.Color('white'))
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if (event.pos[0] > 340) and (event.pos[0] < 490) and (event.pos[1] > 170) and (
                                event.pos[1] < 220):
                            running = False
                            self.chosengame = 1
                            print(self.chosengame)
                        if (event.pos[0] > 340) and (event.pos[0] < 490) and (event.pos[1] > 260) and (
                                event.pos[1] < 310):
                            running = False
                            self.chosengame = 2
                            print(self.chosengame)
                        if (event.pos[0] > 340) and (event.pos[0] < 490) and (event.pos[1] > 350) and (
                                event.pos[1] < 400):
                            running = False
                            self.chosengame = 3
                            print(self.chosengame)

            myImage = pygame.image.load('images\\mainmenu_.jpg')
            myRect = (0, 0, 640, 480)
            self.screen.blit(myImage, myRect)

            pos = pygame.mouse.get_pos()

            if (pos[0] > 340) and (pos[0] < 560) and (pos[1] > 170) and (pos[1] < 220):
                myImage1 = pygame.image.load('images\\mainmenu1_.jpg')
                myRect1 = (0, 0, 640, 480)
                self.screen.blit(myImage1, myRect1)

            if (pos[0] > 340) and (pos[0] < 560) and (pos[1] > 260) and (pos[1] < 310):
                myImage2 = pygame.image.load('images\\mainmenu2_.jpg')
                myRect2 = (0, 0, 640, 480)
                self.screen.blit(myImage2, myRect2)

            if (pos[0] > 340) and (pos[0] < 560) and (pos[1] > 350) and (pos[1] < 400):
                myImage3 = pygame.image.load('images\\mainmenu3_.jpg')
                myRect3 = (0, 0, 640, 480)
                self.screen.blit(myImage3, myRect3)

            pygame.display.flip()

            clock.tick(self.speed)
        # pygame.quit()

    def run_war(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        rules = True
        while rules:
            myImage1 = pygame.image.load('images\\warrules.jpg')
            myRect1 = (0, 0, 640, 480)
            self.screen.blit(myImage1, myRect1)
            pygame.display.flip()
            clock.tick(self.speed)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    rules = False

        self.screen.fill(pygame.Color('white'))
        running = True
        self.draw_grid()
        self.draw_war_map()
        pygame.display.flip()
        self.create_cell_list()
        self.draw_cell_list()
        self.draw_grid()
        pygame.display.flip()
        clock.tick(self.speed)
        while running and self.counter < 50:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.counter += 1
            self.evolve()
            self.draw_cell_list()
            self.draw_grid()
            self.draw_war_map()
            pygame.display.flip()
            clock.tick(self.speed)
        points11 = 0
        points12 = 0
        points13 = 0
        points14 = 0
        points15 = 0
        points21 = 0
        points22 = 0
        points23 = 0
        points24 = 0
        points25 = 0

        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if i < 8 and j < 10:
                    if self.cell_list[i][j] % 2 == 0 and self.cell_list[i][j] > 0:
                        points11 += 1

                    if self.cell_list[i][j] % 2 == 1 and self.cell_list[i][j] > 0 and self.cell_list[i][j] != 1:
                        points21 += 1

                if i < 8 and j > 21:
                    if self.cell_list[i][j] % 2 == 0 and self.cell_list[i][j] > 0:
                        points12 += 1

                    if self.cell_list[i][j] % 2 == 1 and self.cell_list[i][j] > 0 and self.cell_list[i][j] != 1:
                        points22 += 1

                if i > 16 and j < 10:
                    if self.cell_list[i][j] % 2 == 0 and self.cell_list[i][j] > 0:
                        points13 += 1

                    if self.cell_list[i][j] % 2 == 1 and self.cell_list[i][j] > 0 and self.cell_list[i][j] != 1:
                        points23 += 1

                if i > 16 and j > 21:
                    if self.cell_list[i][j] % 2 == 0 and self.cell_list[i][j] > 0:
                        points14 += 1

                    if self.cell_list[i][j] % 2 == 1 and self.cell_list[i][j] > 0 and self.cell_list[i][j] != 1:
                        points24 += 1

                if (j < 20 and j > 13) and (i > 9 and i < 16):
                    if self.cell_list[i][j] % 2 == 0 and self.cell_list[i][j] > 0:
                        points15 += 1

                    if self.cell_list[i][j] % 2 == 1 and self.cell_list[i][j] > 0 and self.cell_list[i][j] != 1:
                        points25 += 1
        print(points11, points12, points13, points14, points15)
        print(points21, points22, points23, points24, points25)
        if points11 > 0 and points12 > 0 and points13 > 0 and points14 > 0 and points15 > 0:
            print('Player #1 win!')
        elif points21 > 0 and points22 > 0 and points23 > 0 and points24 > 0 and points25 > 0:
            print('Player #2 win!')
        else:
            print('War, war never changes')

    def run_economics(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        rules = True
        while rules:
            myImage1 = pygame.image.load('images\\economicsrules.jpg')
            myRect1 = (0, 0, 640, 480)
            self.screen.blit(myImage1, myRect1)
            pygame.display.flip()
            clock.tick(self.speed)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    rules = False

        self.screen.fill(pygame.Color('white'))
        running = True
        self.draw_grid()
        pygame.display.flip()
        self.create_cell_list()
        self.draw_cell_list()
        self.draw_grid()
        pygame.display.flip()
        clock.tick(self.speed)
        while running and self.counter < 40:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.evolve()
            self.counter += 1
            self.draw_cell_list()
            self.draw_grid()
            pygame.display.flip()
            clock.tick(self.speed)

        results = [i['converted'] for i in self.score[2:]]
        winner = results.index(max(results)) + 1
        print('Player #', winner, ' wins!')
        pygame.quit()

    def run_religion(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        rules = True
        while rules:
            myImage1 = pygame.image.load('images\\religionrules.jpg')
            myRect1 = (0, 0, 640, 480)
            self.screen.blit(myImage1, myRect1)
            pygame.display.flip()
            clock.tick(self.speed)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    rules = False

        self.screen.fill(pygame.Color('white'))
        running = True
        self.draw_grid()
        pygame.display.flip()
        self.create_cell_list()
        self.draw_cell_list()
        self.draw_grid()
        pygame.display.flip()
        clock.tick(self.speed)
        while running and self.counter < 30:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.evolve()
            self.counter += 1
            self.draw_cell_list()
            self.draw_grid()
            pygame.display.flip()
            clock.tick(self.speed)
        results = [i['result'] for i in self.score[2:]]
        winner = results.index(max(results)) + 1
        print('Player #', winner, ' wins!')
        pygame.quit()

    def create_cell_list(self, randomize=False):
        self.cell_list = [[0] * self.cell_width for i in range(self.cell_height)]
        if randomize:
            choicelist = [0] + list(range(2, self.n))
            for i in range(self.cell_height):
                for j in range(self.cell_width):
                    self.cell_list[i][j] = rand1(choicelist)
        else:
            count = 0
            while count < self.moves * (self.n - 2) ** 2:
                for i in pygame.event.get():
                    if i.type == pygame.MOUSEBUTTONDOWN:
                        if i.button == 1:
                            x = i.pos[0] // self.cell_size
                            y = i.pos[1] // self.cell_size
                            if self.cell_list[y][x] == 0:
                                self.cell_list[y][x] = 2 + ((count + 1) // 2) % (self.n - 2)
                                pygame.draw.rect(self.screen, pygame.Color(self.colors[self.cell_list[y][x]]),
                                                 pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size,
                                                             self.cell_size))
                                self.draw_grid()
                                pygame.display.flip()
                                count += 1
                    elif i.type == pygame.QUIT:
                        pygame.quit()
                pygame.time.delay(20)

    def draw_cell_list(self):
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                pygame.draw.rect(self.screen, pygame.Color(self.colors[self.cell_list[i][j]]),
                                 pygame.Rect(j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size))
        self.k = 1


if __name__ == '__main__':
    game = GameOfLife(640, 480, 20, 5)
    game.start_game()
    if game.chosengame == 1:
        game.run_war()

    if game.chosengame == 2:
        game.run_economics()

    if game.chosengame == 3:
        game.run_religion()
