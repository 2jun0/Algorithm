import sys
input = sys.stdin.readline

pattern = [
  (0,0), (0,1), (0,2),
  (1,0),        (1,2),
  (2,0), (2,1), (2,2)
]

N = int(input())
results = [[' ']*N for _ in range(N)]

def draw_pattern(y, x, width):
  if width == 3:
    for dy, dx in pattern: 
      results[y+dy][x+dx] = '*'

  else:
    width_nxt = width//3
    for dy, dx in pattern: 
      draw_pattern(y + dy*width_nxt, x + dx*width_nxt, width_nxt)

draw_pattern(0, 0, N)
print('\n'.join([''.join(a) for a in results]))