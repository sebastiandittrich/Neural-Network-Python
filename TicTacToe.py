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


import random
import sys

N = 4

KEY_CODE = {'left': 37,
            'up': 38,
            'right': 39,
            'down': 40}
KEY_LEFT = 'left'
KEY_UP = 'up'
KEY_RIGHT = 'right'
KEY_DOWN = 'down'

class Board(object):
  def __init__(self):
    self.board = [[None] * N for i in range(N)]
    self.score = 0
    self.over = False

  def rotateLeft(self, grid):
    out = self.emptyGrid()
    for c in xrange(4):
      for r in xrange(4):
        out[r][3-c] = grid[c][r]
    return out

  def rotateRight(self, grid):
    out = self.emptyGrid()
    for c in xrange(4):
      for r in xrange(4):
        out[3-r][c] = grid[c][r]
    return out

  def emptyGrid(self):
    out = list()
    for x in xrange(4):
      col = list()
      for y in xrange(4):
        col.append(None)
      out.append(col)
    return out

  def to_move(self, grid, direction):
    out = self.emptyGrid()

    if direction == KEY_UP:
      rot = 1
    elif direction == KEY_RIGHT:
      rot = 2
    elif direction == KEY_DOWN:
      rot = 3
    else:
      rot = 0

    for i in xrange(rot):
      grid = self.rotateLeft(grid)

    score = 0
    for r in xrange(4):
      oc = 0
      ic = 0
      while ic < 4:
        if grid[ic][r] is None:
          ic += 1
          continue
        out[oc][r] = grid[ic][r]
        oc += 1
        ic += 1

      ic = 0
      oc = 0
      while ic < 4:
        if out[ic][r] is None:
          break
        if ic == 3:
          out[oc][r] = out[ic][r]
          oc += 1
          break
        if out[ic][r] == out[ic+1][r]:
          #out[oc][r] *= 2
          out[oc][r] = 2*out[ic][r]
          score += out[oc][r]
          ic += 1
        else:
          out[oc][r] = out[ic][r]
        ic += 1
        oc += 1
      while oc < 4:
        out[oc][r] = None
        oc += 1

    for i in xrange(rot):
      out = self.rotateRight(out)

    return out, score

  def move(self, direction):
    #print 'move', direction
    next_board, got_score = self.to_move(self.board, direction)
    moved = (next_board != self.board)

    self.board = next_board
    self.score += got_score

    if moved:
      if not self.randomTile():
        self.over = True

  def canMove(self, grid, direction):
    return grid != self.to_move(grid, direction)[0]

  def get_empty_cells(self):
    for i in range(N):
      for j in range(N):
        if self.board[i][j] is None:
          yield i, j

  def randomTile(self):
    cells = list(self.get_empty_cells())
    if not cells:
      return False
    #print 'cells', cells


    if random.random() < 0.9:
      v = 2
    else:
      v = 4

    cid = random.choice(cells)
    #print cid
    self.board[cid[0]][cid[1]] = v
    return True

  def show(self):
    for i in range(N):
      for j in range(N):
        if self.board[j][i]:
          print('%4d' % self.board[j][i]),
        else:
          print('   .'),
      print

def load_ai_module():
  if len(sys.argv) > 3:
    name = sys.argv[3]
  else:
    name = 'kcwu'
  fullpath = 'ai_modules.' + name
  print('load module', fullpath)
  ai = __import__(fullpath)
  return getattr(ai, name)
