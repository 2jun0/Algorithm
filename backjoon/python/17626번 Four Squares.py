n=int(input())
t=[0]+[5]*(n+1)
for i in range(1,n+1):
 for j in range(1,int(i**.5)+1):t[i]=min(t[i],1+t[i-j*j])
print(t[n])