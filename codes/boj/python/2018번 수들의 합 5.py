N = int(input().strip())

a, b = 1, 1
s = 1
cnt = 0
while a <= b and b <= N:
  if s == N:
    cnt += 1
  
  if s <= N:
    b += 1
    s += b
  else:
    s -= a
    a += 1
    
print(cnt)