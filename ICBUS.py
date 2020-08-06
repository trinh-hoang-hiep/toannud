n,k =[int(x) for x in input().split()]
dd = [0]*(n+5)
d = [0]*(n+5)
res=0
g=[['null'] for i in range(n+5)]
g2=[[0]*(n+5) for i in range(n+5)]
c = [0]*(n+5)


def BFS(u):
    q=[]
    q.append((u,d[u]))
    while(len(q)!=0):
        x = q[0]
        x.second-=1
        q.pop(0)
        # for(auto v: g1[x.F]){//đoạn nghiệp vụ của queue
        #     g2[u][v] = min(g2[u][v],c[u]);
        #     if(!dd[v] && x.S){
        #         dd[v] = 1;
        #         q.push(mp(v,x.S));

# n,m =[int(x) for x in input().split()]
# g = [[0]*(m+5) for i in range(m+5)]

# for i in range(m):
#     u,v,c = list(map(int, input().split()))
#     g[u][v]=c
#     g[v][u]=c
# k= int(input())
# path= list(map(int, input().split()))
# summ=0
# for i in range(k-1):
#     # print(g[path[i]][path[i+1]])
#     summ+=g[path[i]][path[i+1]]
# print(summ)