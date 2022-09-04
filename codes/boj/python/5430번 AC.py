import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())

T = input(int)

for t in range(T):
	cmds = input()
	n = input(int)
	nums = input()[1:-1].split(',')
  
	if n == 0:
		nums = []

	reverse = False
	is_error = False

	for cmd in cmds:
		if cmd == 'D':
			if nums:
				if reverse: nums.pop()
				else: nums.pop(0)
			else:
				is_error = True
				break

		elif cmd == 'R':
			reverse = not reverse

	if is_error:
		print('error')
	else:
		if reverse:
			print('['+','.join(nums[::-1])+']')
		else:
			print('['+','.join(nums)+']')