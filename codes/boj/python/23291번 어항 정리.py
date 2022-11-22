import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

class Fishbowls:
  def __init__(self, fishes):
    self.fishes = fishes

  def add_in_min_tiles(self):
    '''가장 적게 있는 물고기 칸에 1만큼 물고기를 넣어줌'''
    min_v = min(self.fishes)
    for i in range(len(self.fishes)):
      if self.fishes[i] == min_v:
        self.fishes[i] += 1

  def _flatten(self, table, line):
    h, w = len(table), len(table[0])
    idx = 0
    for x in range(w):
      for y in range(h-1, -1, -1):
        line[idx] = table[y][x]
        idx += 1

  def _turn_table_right(self, table, new_table):
    # rotate 90
    h, w = len(table), len(table[0])
    for y in range(h):
      for x in range(w):
        new_table[x][h-y-1] = table[y][x]

  def update_by_stack(self):
    '''칸 쌓기로 업데이트'''
    N = len(self.fishes)
    w, h = 1, 1

    # 위로 쌓을 칸들.
    stack_table = [[self.fishes[0]]]

    stack_size = w*h
    while len(self.fishes) - stack_size >= h:

      '''new stack'''
      new_h, new_w = w+1, h
      new_stack_table = [[None]*new_w for _ in range(new_h)]
      # rotate 90
      self._turn_table_right(stack_table, new_stack_table)

      # new tiles
      for i in range(new_w):
        remain_idx = stack_size + i
        new_stack_table[-1][i] = self.fishes[remain_idx]

      # update
      h, w = new_h, new_w
      stack_table = new_stack_table
      stack_size = h*w
    
    '''어항 정리'''
    # for stack
    add_stack_table = [[0]*w for _ in range(h)]
    for y in range(h):
      for x in range(w):

        for ny, nx in [(y-1,x), (y+1,x), (y,x-1), (y,x+1)]:
          if 0<=ny<h and 0<=nx<w and stack_table[y][x] > stack_table[ny][nx]:
            diff = stack_table[y][x] - stack_table[ny][nx]

            add_stack_table[ny][nx] += diff//5
            add_stack_table[y][x] -= diff//5
    # for fishes
    add_fishes = [0]*N
    srt, end = stack_size, N-1
    for i in range(srt, end+1):
      for ni in [i-1, i+1]:
        if srt<=ni<=end and self.fishes[i] > self.fishes[ni]:
          diff = self.fishes[i] - self.fishes[ni]

          add_fishes[ni] += diff//5
          add_fishes[i] -= diff//5

    # fishes and stack
    if srt < N:
      diff = stack_table[-1][-1] - self.fishes[srt]
      add_fishes[srt] += int(diff/5)
      add_stack_table[-1][-1] -= int(diff/5)

    # add 적용
    for y in range(h):
      for x in range(w):
        stack_table[y][x] += add_stack_table[y][x]
    for i in range(srt, end+1):
      self.fishes[i] += add_fishes[i]
    
    '''늘이기'''
    self._flatten(stack_table, self.fishes)

  def update_by_stack2(self):
    h, w = 2, len(self.fishes)//2
    stack_table = [self.fishes[:w][::-1], self.fishes[w:]]

    h, w = h*2, w//2
    stack_table = [stack_table[1][:w][::-1], stack_table[0][:w][::-1], stack_table[0][w:], stack_table[1][w:]]

    add_stack_table = [[0]*w for _ in range(h)]
    for y in range(h):
      for x in range(w):

        for ny, nx in [(y-1,x), (y+1,x), (y,x-1), (y,x+1)]:
          if 0<=ny<h and 0<=nx<w and stack_table[y][x] > stack_table[ny][nx]:
            diff = stack_table[y][x] - stack_table[ny][nx]

            add_stack_table[ny][nx] += diff//5
            add_stack_table[y][x] -= diff//5
    
    for y in range(h):
      for x in range(w):
        stack_table[y][x] += add_stack_table[y][x]

    self._flatten(stack_table, self.fishes)
  
  def is_finished(self, K):
    return max(self.fishes) - min(self.fishes) <= K

N, K = input_n(int)
fishes = input_n(int)
fishbowls = Fishbowls(fishes)
cnt = 0

while not fishbowls.is_finished(K):
  fishbowls.add_in_min_tiles()
  fishbowls.update_by_stack()
  fishbowls.update_by_stack2()
  cnt += 1

print(cnt)