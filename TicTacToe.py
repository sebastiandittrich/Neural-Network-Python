import sys
from random import randint
class Snake:
    def __init__(self, playground_height, playground_width):
        self.__playground = []
        for iter1 in range(playground_height):
            self.__playground.append([])
            for iter2 in range(playground_width):
                self.__playground[-1].append(0.5)

        self.__snake = [0,0]
        self.__playground[0][0] = 1
        self.__eat = [randint(0, playground_height-1), randint(0, playground_width-1)]
        self.__playground[self.__eat[0]][self.__eat[1]] = 0

    def out(self, var):
        sys.stdout.write(var)
    
    def print(self):
        self.out('\n-')
        for column in self.__playground[0]:
            self.out('-')
        self.out('-')
        for row in self.__playground:
            self.out('\n|')
            for column in row:
                if column == 0.5:
                    self.out(' ')
                elif column == 1:
                    self.out('#')
                elif column == 0:
                    self.out('+')
            self.out('|')
        self.out('\n-')
        for column in self.__playground[0]:
            self.out('-')
        self.out('-\n')

    def height_change(self):
        return self.__eat[0] - self.__snake[0]

    def width_change(self):
        return self.__eat[1] - self.__snake[1]

    def move(self, key):
        if key == 'up':
            self.__snake[0] = self.__snake[0] -1
        elif key == 'down':
            self.__snake[0] = self.__snake[0] +1
        elif key == 'right':
            self.__snake[1] = self.__snake[1] +1
        elif key == 'left':
            self.__snake[1] = self.__snake[1] -1
        self.normalize_snake()
        self.refresh_snake()

    def normalize_snake(self):
        if self.__snake[0] < 0:
            self.__snake[0] = len(self.__playground) -1
        if self.__snake[0] > len(self.__playground) -1:
            self.__snake[0] = 0
        if self.__snake[1] < 0:
            self.__snake[1] = len(self.__playground[0]) -1
        if self.__snake[1] < len(self.__playground[0]) -1:
            self.__snake[1] = 0

    def refresh_snake(self):
        self.__playground[self.__snake[0]][self.__snake[1]] = 1
