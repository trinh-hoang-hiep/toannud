n, b = [int(x) for x in input().split()]
a=[]
a.append((0,0))
f=[[0]*(n+5) for i in range(b+1)]
for i in range(n):
    entries = tuple(map(int, input().split())) 
    a.append(entries)
for i in range(1,n+1):
    for j in range(b+1):
        f[i][j]=f[i-1][j]
        if(j >= a[i][0]):
            f[i][j] = max(f[i][j],f[i-1][j-a[i][0]]+a[i][1])
print (f)

##doc sau