import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N = input(int)
A = [input(int) for _ in range(N)]

pA = [a for a in A if a > 0]
pA.sort(reverse=True)
nA = [a for a in A if a <= 0]
nA.sort()

sum_v = 0
pi = 0
while pi < len(pA):
  if pi+1 < len(pA) and pA[pi] * pA[pi+1] > pA[pi] + pA[pi+1]:
    sum_v += pA[pi] * pA[pi+1]
    pi+=2
  else:  
    sum_v += pA[pi]
    pi += 1

ni = 0
while ni < len(nA):
  if ni+1 < len(nA) and nA[ni] * nA[ni+1] > nA[ni] + nA[ni+1]:
    sum_v += nA[ni] * nA[ni+1]
    ni+=2
  else:  
    sum_v += nA[ni]
    ni += 1

  
print(sum_v)