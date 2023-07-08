import sys

def input(type_=str):
	return type_(sys.stdin.readline().rstrip())
def input_n(type_):
	return list(map(type_, input().split()))

def init_tree(tree, node, arr, srt, end, func):
    if srt == end:
        tree[node] = arr[srt]
        return tree[node]
    
    mid = (srt + end) // 2
    tree[node] = func(
        init_tree(tree, node*2, arr, srt, mid, func),
        init_tree(tree, node*2+1, arr, mid+1, end, func))
    return tree[node]

def query_tree(tree, node, srt, end, left, right, func, t):
    if end < left or right < srt:
        return t
    if left <= srt and end <= right:
        return tree[node]
    
    mid = (srt + end) // 2
    return func(
        query_tree(tree, node*2, srt, mid, left, right, func, t),
        query_tree(tree, node*2+1, mid+1, end, left, right, func, t))

N, M = input_n(int)
arr = [input(int) for _ in range(N)]

min_tree = [-1]*(4*N)
max_tree = [-1]*(4*N)

init_tree(min_tree, 1, arr, 0, N-1, min)
init_tree(max_tree, 1, arr, 0, N-1, max)

for _ in range(M):
    a, b = input_n(int)
    a -= 1
    b -= 1
    
    min_v = query_tree(min_tree, 1, 0, N-1, a, b, min, 1e+9)
    max_v = query_tree(max_tree, 1, 0, N-1, a, b, max, 1)
    
    print(min_v, max_v)