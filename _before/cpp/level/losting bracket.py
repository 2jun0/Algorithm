/*
expr = input()
tokens_m = expr.split('-')

sum = 0

# first
tokens_p = tokens_m[0].split('+')
for token_p in tokens_p:
	sum = sum + int(token_p)

if len(tokens_m) > 1:
	for token_m in tokens_m[1:]:
		tokens_p = token_m.split('+')

		sum_of_toks_m = 0
		for token_p in tokens_p:
			sum_of_toks_m = sum_of_toks_m + int(token_p)

		sum = sum - sum_of_toks_m

print(sum)

*/