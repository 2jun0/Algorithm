/*
T = int(input())
for t in range(T):
	N = int(input())

	if N == 0:
		print(0)
		continue

	clothes_cnt = {}
	for i in range(N):
		lines = input().split(' ')

		if lines[1] not in clothes_cnt:
			clothes_cnt[lines[1]] = 1
		else:
			clothes_cnt[lines[1]] = clothes_cnt[lines[1]] + 1
	
	result = 1
	for cnt in clothes_cnt.values():
		result = result * (cnt+1)
	result = result - 1
	print(result)
*/