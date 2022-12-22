import sys 
 
def input(_type=str): 
  return _type(sys.stdin.readline().strip()) 
def input_n(_type=str): 
  return list(map(_type, input().split())) 

def get_groups(Ls: list, Xs: list):
  groups = [0]*len(Ls)
  group_d = [10000000]*len(Ls)
  visited = [False]*len(Xs)
  
  Ds = []
  
  for xidx, xpos in enumerate(Xs):
    y, x = xpos
    for lidx, lpos in enumerate(Ls):
      ly, lx = lpos
      d = (ly-y)**2 + (lx-x)**2
      Ds.append((d, lidx, xidx))
    
  Ds.sort()
  for d, lidx, xidx in Ds:
    if visited[xidx]:
      continue
    
    if group_d[lidx] == d:
      groups[lidx]+=1
      visited[xidx]=True
    elif group_d[lidx] > d:
      group_d[lidx] = d
      groups[lidx]=1
      visited[xidx]=True
  return groups

R, C = input_n(int)
table = [list(map(str, input())) for _ in range(R)]
Ls = []
Xs = []
for y in range(R):
  for x in range(C):
    if table[y][x] == 'L':
      Ls.append((y,x))
    if table[y][x] == 'X':
      Xs.append((y,x))
      
cnt = 0
g = get_groups(Ls, Xs)
for gg in g:
  if gg > 1:
    cnt += 1
print(cnt)