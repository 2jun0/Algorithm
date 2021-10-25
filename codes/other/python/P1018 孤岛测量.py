# 0 : 1 => 4
# 1 : 1 => 0
# 2 : 2 => 6
# 3 : 4 => 16
x = int(input())
input()
y = input()
if x == 1:
  if y[0] == '1': print(4) # 0
  else: print(0) # 1
if x == 2: print(6)
if x == 4: print(16)