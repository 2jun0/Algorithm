A,B=map(int,input().split())
a=[0]
for i in range(1, 55): a.append(2**(i-1) + 2*a[-1])
def g(n):
  b = bin(n)[2:]
  i = len(b)
  r = 0
  o = 0
  for c in b:
    if c == '1':
      r+=o*(2**(i-1))+(a[i-1]+1)
      o+=1
    i-=1
  return r
print(g(B)-g(A-1))