import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]
def avg(l): return sum(l)/len(l)
###...#.###.###.#.#.###.###.###.###.###
#.#...#...#...#.#.#.#...#.....#.#.#.#.#
#.#...#.###.###.###.###.###...#.###.###
#.#...#.#.....#...#...#.#.#...#.#.#...#
###...#.###.###...#.###.###...#.###.###
NUMBERS = [
#0
'###\
 #.#\
 #.#\
 #.#\
 ###'.split(' '),
#1
'..#\
 ..#\
 ..#\
 ..#\
 ..#'.split(' '),
#2
'###\
 ..#\
 ###\
 #..\
 ###'.split(' '),
#3
'###\
 ..#\
 ###\
 ..#\
 ###'.split(' '),
#4
'#.#\
 #.#\
 ###\
 ..#\
 ..#'.split(' '),
#5
'###\
 #..\
 ###\
 ..#\
 ###'.split(' '),
#6
'###\
 #..\
 ###\
 #.#\
 ###'.split(' '),
#7
'###\
 ..#\
 ..#\
 ..#\
 ..#'.split(' '),
#8
'###\
 #.#\
 ###\
 #.#\
 ###'.split(' '),
#9
'###\
 #.#\
 ###\
 ..#\
 ###'.split(' '),
]

N = input(int)
S = [input() for _ in range(5)]

part_table = []

for i in range(0, N):
  x = i*4

  parts = []
  for part in range(10):
    flag = True
    for ny in range(5):
      for nx in range(3):
        if S[ny][nx+x] == '#' and NUMBERS[part][ny][nx] == '.':
          flag = False
          break

      if not flag: break
    
    if flag: parts.append(part)

  if len(parts) == 0:
    part_table = False
    break
  part_table = [parts]+part_table

if part_table:
  total_sum = 0
  for l_i in range(N): total_sum += avg(part_table[l_i]) * (10**l_i)
  print(total_sum)
else:
  print(-1)