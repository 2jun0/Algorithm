import sys

def input(type_=str):
	return type_(sys.stdin.readline().rstrip())


def search(table, y, x, n):
    if n == 1:
        return table[y][x]
    
    nxt_n = n//2
    
    rs = [
        search(table, y, x, nxt_n),
        search(table, y, x+nxt_n, nxt_n),
        search(table, y+nxt_n, x, nxt_n),
        search(table, y+nxt_n, x+nxt_n, nxt_n)
    ]
    
    rs_str = '(' + ''.join(rs) + ')'
    
    if rs_str == '(0000)':
        return '0'
    if rs_str == '(1111)':
        return '1'
    
    return rs_str


N = input(int)
table = [input(str) for _ in range(N)]
print(search(table, 0, 0, N))