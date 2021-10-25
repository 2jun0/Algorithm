/*
while True:
	s = input()

	if s == '.':
		break

	stk = []
	is_yes = True

	for c in s:
		if c in ['(', '[']:
			stk.append(c)
		elif c is ')':
			if len(stk) > 0 and stk[len(stk)-1] == '(':
				stk.pop()
			else:
				is_yes = False
				break
		elif c is ']':
			if len(stk) > 0 and stk[len(stk)-1] == '[':
				stk.pop()
			else:
				is_yes = False
				break

	if is_yes and len(stk) == 0:
		print('yes')
	else:
		print('no')
*/