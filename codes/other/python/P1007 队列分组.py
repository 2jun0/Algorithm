x = input()

def ck(s):
	if len(s) % 2 == 1: return False
	left, right = 0, 0
	for c in s[:len(s)//2]: left += int(c)
	for c in s[len(s)//2:]: right += int(c)
	if left == 0 and right == len(s)//2: return True
	if right == 0 and left == len(s)//2: return True
	return False

cnt = 0
for i in range(0, len(x)):
	for j in range(i, len(x)):
		if ck(x[i:j+1]):
			cnt+=1

print(cnt)
