from itertools import permutations
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

class Block:
  def __init__(self, color, value):
    self.color = color
    self.value = value
  def union(self, b):
    self.value = max(min(self.value + b.value, 9), 0)
    if b.color != 'W':
      self.color = b.color
  def clone(self):
    return Block(self.color, self.value)

def turn_right(ingredient):
  '''재료 돌리기'''
  new_ingredient = [[None]*4 for _ in range(4)]
  for y in range(4):
    for x in range(4):
      new_ingredient[x][3-y] = ingredient[y][x]
  return new_ingredient

def get_quality(table):
  '''품질 구하기'''
  R,B,G,Y = 0,0,0,0

  for y in range(5):
    for x in range(5):
      if table[y][x].color == 'R':
        R+=table[y][x].value
      if table[y][x].color == 'B':
        B+=table[y][x].value
      if table[y][x].color == 'G':
        G+=table[y][x].value
      if table[y][x].color == 'Y':
        Y+=table[y][x].value
  
  return 7*R + 5*B + 3*G + 2*Y

def union_ingredient(table, ingredient, y_srt, x_srt):
  for y in range(4):
    for x in range(4):
      table[y+y_srt][x+x_srt].union(ingredient[y][x])

def dfs(table, ingredients, i):
  global max_quality

  if i == len(ingredients):
    max_quality = max(max_quality, get_quality(table))
    return

  for _ in range(4):
    for y in range(2):
      for x in range(2):
        new_table = [[table[y][x].clone() for x in range(5)] for y in range(5)]
        union_ingredient(new_table, ingredients[i], y, x)
        dfs(new_table, ingredients, i+1)

    ingredients[i] = turn_right(ingredients[i])

n = input(int)
table = [[Block('W', 0) for _ in range(5)] for _ in range(5)]
ingredients = []

for _ in range(n):
  v_table = [input_n(int) for _ in range(4)]
  c_table = [input_n(str) for _ in range(4)]

  ingredients.append([
      [Block(c_table[y][x], v_table[y][x]) for x in range(4)]
    for y in range(4)
  ])

max_quality = 0
for sub_ingredients in permutations(ingredients, 3):
  dfs(table, list(sub_ingredients), 0)
    
print(max_quality)