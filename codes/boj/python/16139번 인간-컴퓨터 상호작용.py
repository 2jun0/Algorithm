import sys

def input(type_=str):
	return type_(sys.stdin.readline().rstrip())
def input_n(type_):
	return list(map(type_, input().split()))
    
ALPHAS = [chr(ord('a') + num) for num in range(26)]

S = input(str)
sums = {
    alpha: [0]*(len(S)+1) for alpha in ALPHAS
}

for alpha in ALPHAS:
    for idx in range(1, len(S)+1):
        c = S[idx-1]
        
        if alpha == c:
            sums[alpha][idx] = sums[alpha][idx-1] + 1
        else:
            sums[alpha][idx] = sums[alpha][idx-1]

q = input(int)
for _ in range(q):
    a, l, r = input_n(str)
    l, r = int(l), int(r)
    
    print(sums[a][r+1] - sums[a][l])