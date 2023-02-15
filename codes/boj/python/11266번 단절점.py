import sys
sys.setrecursionlimit(100001)
def inp(type=str):
    return type(sys.stdin.readline().strip())
def inp_n(type=str):
    return list(map(type, input().split()))

def dfs(r,x):
    global lc
    l[x] = lc
    lc+=1
    p[x]=l[x]
    c=0
    for n in g[x]:
        if l[n] != None:
            p[x] = min(p[x], l[n])
            continue
            
        c +=1
        cp=dfs(False,n)
        if not r and cp >= l[x]:
            a.add(x)
        
        p[x]=min(p[x],cp)
    if r and c >= 2:
        a.add(x)
    return p[x]

V,E =inp_n(int)
g=[[] for _ in range(V+1)]
for _ in range(E):
    a,b = inp_n(int)
    g[a].append(b)
    g[b].append(a)
l=[None]*(V+1)
p=[None]*(V+1)
lc=1
a=set()
for x in range(1,V+1):
    if l[x] == None:
        dfs(True,x)
a=sorted(a)
print(len(a))
print(*a)