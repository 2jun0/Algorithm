import sys
import math
input = sys.stdin.readline

N = int(input())

print(math.ceil((-3+(-3 + 12*N)**0.5)/6+1))
