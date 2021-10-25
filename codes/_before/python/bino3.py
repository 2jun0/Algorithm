/*import sys
sys.setrecursionlimit(1000000)

def powMod(n, k, mod):
	if (k == 0):
		return 1

	temp = powMod(n, int(k / 2), mod)
	temp2 = (temp * temp) % mod

	if (k % 2 == 0):
		return temp2
	else:
		return (temp2 * (n % mod)) % mod

def factorialMod(a, mod):
	if(a==0): return 1

	result = a % mod

	for i in range(1,a):
		result = (result * i) % mod

	return result

nums = input().split(' ')
N = int(nums[0])
K = int(nums[1])
mod = 1000000007

a = factorialMod(N, mod)
b = factorialMod(K, mod)
c = factorialMod(N - K, mod)
print((((a * powMod(b, mod - 2, mod)) % mod) * powMod(c, mod - 2, mod)) % mod)*/