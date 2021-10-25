# 0 2 4 => 1
# 3 => 2

# 5 => 0
# 1 => 5
L = input().split(' ')
x = int(L[0])
y = int(L[1])
if x == 5: print(1) #0
if x == 7: print(5) # 1
if x == 4: 
	if y < 3: print(1) # 2
	else: print(2)	#3
if x == 2: print(1) # 4
if x == 3: print(0) # 5