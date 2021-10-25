/*T = int(input())

for t in range(T):
	q = []
	cmds = input()
	n = int(input())
	nums = input()[1:-1].split(',')

	if n > 0:
		for num in nums:
			q.append(num)

	reverse = False
	is_error = False

	for cmd in cmds:
		if cmd is 'D':
			if len(q) > 0:
				if reverse:
					q.pop()
				else:
					q.pop(0)
			else:
				is_error = True
				break

		elif cmd is 'R':
			reverse = not reverse

	if is_error:
		print('error')
	else:
		if reverse:
			print('['+','.join(q[::-1])+']')
		else:
			print('['+','.join(q)+']')*/