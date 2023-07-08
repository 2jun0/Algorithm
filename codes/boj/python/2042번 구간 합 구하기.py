import sys

def input(type_=str):
	return type_(sys.stdin.readline().rstrip())
def input_n(type_):
	return list(map(type_, input().split()))

def init_tree(tree, node, idx2node, arr, left, right):
    if left == right:
        tree[node] = arr[left]
        idx2node[left] = node
        return tree[node]
    
    mid = (left + right) // 2
    tree[node] = init_tree(tree, node*2, idx2node, arr, left, mid)\
               + init_tree(tree, node*2+1, idx2node, arr, mid+1, right)
    return tree[node]

def query_tree(tree, node, left, right, srt, end):
    if right < srt or end < left:
        return 0
    if srt <= left and right <= end:
        return tree[node]
    
    mid = (left + right) // 2
    return query_tree(tree, node*2, left, mid, srt, end)\
         + query_tree(tree, node*2+1, mid+1, right, srt, end) 
         
def update_tree(tree, node, v):
    diff = v - tree[node]
    
    while node > 0:
        tree[node] += diff
        node //= 2

N, M, K = input_n(int)
arr = [input(int) for _ in range(N)]

tree = [0]*(4*N)
idx2node = [0]*N
init_tree(tree, 1, idx2node, arr, 0, N-1)

for _ in range(M+K):
    a, b, c = input_n(int)
    
    if a == 1:
        update_tree(tree, idx2node[b-1], c)
    else:
        print(query_tree(tree, 1, 0, N-1, b-1, c-1))