import sys

def input(type_=str):
	return type_(sys.stdin.readline().rstrip())
def input_n(type_):
	return list(map(type_, input().split()))

rans = [set() for _ in range(11)]
visited = [False]*(1<<11)

Ls = []
for _ in range(2047):
  L = input_n(int)  
  Ls.append(L)
  
for L in Ls:
  for i, l in enumerate(L):
    rans[i].add(l)

for i in range(11):
  rans[i] = sorted(list(rans[i]))
    
for L in Ls:
  bits = 0
  for i, l in enumerate(L):
    if rans[i][1] == l:
      bits |= (1<<i)
      
  visited[bits] = True

found_bits = None
for bits in range(1<<11):
  if not visited[bits]:
    found_bits = bits
    
ans = []  
for i in range(11):
  if found_bits & (1 << i):
    ans.append(rans[i][1])
  else:
    ans.append(rans[i][0])

print(*ans)