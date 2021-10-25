import sys

INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L):
  s = ''
  for l in L: s+='{} '.format(l)
  print(s[:-1])

T = input(int)
for _ in range(T):
  A, B = input_n(int)
  
  s2 = [(A, '')]
  s1 = []
  result = None

  visited = [False] * 10000

  while len(s2) > 0:
    s1, s2 = s2, s1
    while len(s1) > 0:
      n, rec = s1.pop()
      if visited[n]: continue
      visited[n] = True

      if n == B:
        s2 = []
        result = rec
        break

      n1=(2*n)%10000
      s2.append((n1, rec+'D'))

      n1=n-1 if n > 0 else 9999
      s2.append((n1, rec+'S'))
      
      tmp = 1000

      n1 = n%tmp*10 + n//tmp
      s2.append((n1, rec+'L'))
      
      n1 = n//10 + n%10*tmp
      s2.append((n1, rec+'R'))

  print(result)