n,m =[int(x) for x in input().split()]
dd = [0]*(n+5)
res=0
g=[['null'] for i in range(n+5)]
def DFS(u):
    dd[u]=1
    for i in range(len(g[u])) :
        if (type(g[u][i])!= type('str')):
            v=g[u][i]
            if( dd[v]==0):#đoạn nghiệp vụ của DFS
                DFS(v)
for i in range (m) :
    u, v = [int(x) for x in input().split()]
    if(g[u]=='null'): g[u].remove('null')
    g[u].append(v)
    if(g[v]=='null'): g[u].remove('null')
    g[v].append(u)
for i in range (1,n+1):
    if( dd[i] ==0 ):
        res+=1
        DFS(i)
# exit()
print(res)