import sys
sys.setrecursionlimit(100001)
def input(type=str):
  return type(sys.stdin.readline().strip())
def input_n(type=str):
  return list(map(type, input().split()))

def dfs(is_root, x):
  global label_counter
  
  labels[x] = label_counter
  label_counter += 1
  parents[x] = labels[x]
  
  child = 0
  
  for nxt in graph[x]:
    if labels[nxt] != None:
      parents[x] = min(parents[x], labels[nxt])
      continue
    
    child += 1
    ch_p = dfs(False, nxt)
    
    # x로 돌아오는 경우 + x로 돌아오지 않는 경우 => 단절점
    if not is_root and ch_p >= labels[x]:
      ans.add(x)
    
    parents[x] = min(parents[x], ch_p)
    
  if is_root and child >= 2:
    ans.add(x)
    
  return parents[x]

V, E = input_n(int)
graph = [[] for _ in range(V+1)]
for _ in range(E):
  a, b = input_n(int)
  graph[a].append(b)
  graph[b].append(a)
  
labels = [None]*(V+1)
parents = [None]*(V+1)
label_counter = 1

ans = set()
for x in range(1, V+1):
  if labels[x] != None:
    dfs(True, x)

ans = sorted(ans)
print(len(ans))
print(*ans)