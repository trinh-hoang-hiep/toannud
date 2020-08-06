# import functools
n, m = [int(x) for x in input().split()]
c=[[0]*21 for i in range(21)]
sum=0
mark=[0]*21
# g=[['null']]*21 sai do 1 đống đc khởi tạo
g=[['null'] for i in range(21)]
best=1e9
#c2 tạo arr add arr rồi add vào g[]
for i in range (m) :
    u, v, w = [int(x) for x in input().split()]
    # g[u].remove('null')#lần chạy thứ 2 k đc
    if(g[u][0]=='null'): g[u].remove('null')
    # g[u].clear() k dc 
    g[u].append((v,w))
    c[u][v] = w
    # print(u)
# print(m)
# print(g)
mark[1]=1
# def comp ( x,y):
#     return x[0] < y[0]
 
for i in range(1, n+1):
    # sort(g[i].begin(),g[i].end(),cmp)
    # g[i].sort(key=cmop)
    # sorted(g[i], cmp=comp) python 2
    # sorted(g[i], key=cmp_to_key(comp))# cần import
    g[i].sort(key=lambda x: x[1])
# print (g[1].remove('null'))
# print (g)
 
# x=(1,2)
# y=(0,3)
# print(cmp(x,y))
 
def Duyet(x, u):
    global sum
    global best
    if (sum >= best): return
    if(x == n) :
        if(c[u][1] != 0 & sum+c[u][1] < best):
            best = sum +c[u][1]
        return
    
    for i in range( len(g[u])):
        v = g[u][i][0]
        w = g[u][i][1]
        if(mark[v]==0):
            mark[v] = 1
            sum += w
            Duyet(x+1,v)
            mark[v] = 0
            sum -= w
 
Duyet(1,1)
print(best)
'''# import functools
n, m = [int(x) for x in input().split()]
c=[[0]*21 for i in range(21)]
sum=0
mark=[0]*21
# g=[['null']]*21 sai do 1 đống đc khởi tạo
# g=[['null'] for i in range(21)]
best=1e9
#c2 tạo arr add arr rồi add vào g[]
for i in range (m) :
    u, v, w = [int(x) for x in input().split()]
    # g[u].remove('null')#lần chạy thứ 2 k đc
    # if(g[u][0]=='null'): g[u].remove('null')
    # g[u].clear() k dc 
    # g[u].append((v,w))
    c[u][v] = w
    # print(u)
# print(m)
# print(g)
mark[1]=1
# def comp ( x,y):
#     return x[0] < y[0]
 
# for i in range(1, n+1):
    # sort(g[i].begin(),g[i].end(),cmp)
    # g[i].sort(key=cmop)
    # sorted(g[i], cmp=comp) python 2
    # sorted(g[i], key=cmp_to_key(comp))# cần import
    # g[i].sort(key=lambda x: x[1])
# print (g[1].remove('null'))
# print (g)
 
# x=(1,2)
# y=(0,3)
# print(cmp(x,y))
 
def Duyet(x, u):
    global sum
    global best
    if (sum >= best): return
    if(x == n) :
        if(c[u][1] != 0 & sum+c[u][1] < best):
            best = sum +c[u][1]
        return
    
    for i in range( 2,n+1):
        # v = g[u][i][0]
        # w = g[u][i][1]
        w=c[u][i]

        if(mark[i]==0):
            mark[i] = 1
            sum += w
            Duyet(x+1,i)
            mark[i] = 0
            sum -= w
 
Duyet(1,1)
print(best)
'''
'''
# import functools
n, m = [int(x) for x in input().split()]
# c=[[0]*21 for i in range(21)]
sum=0
mark=[0]*21
# g=[['null']]*21 sai do 1 đống đc khởi tạo
g=[['null'] for i in range(21)]
best=1e9
#c2 tạo arr add arr rồi add vào g[]
for i in range (m) :
    u, v, w = [int(x) for x in input().split()]
    # g[u].remove('null')#lần chạy thứ 2 k đc
    if(g[u][0]=='null'): g[u].remove('null')
    # g[u].clear() k dc 
    g[u].append((v,w))
    # c[u][v] = w
    # print(u)
# print(m)
# print(g)
mark[1]=1
# def comp ( x,y):
#     return x[0] < y[0]

for i in range(1, n+1):
    # sort(g[i].begin(),g[i].end(),cmp)
    # g[i].sort(key=cmop)
    # sorted(g[i], cmp=comp) python 2
    # sorted(g[i], key=cmp_to_key(comp))# cần import
    g[i].sort(key=lambda x: x[1])
# print (g[1].remove('null'))
# print (g)

# x=(1,2)
# y=(0,3)
# print(cmp(x,y))

def Duyet(x, u):
    global sum
    global best
    if (sum >= best): return
    
    if(x == n ) :
        # if(c[u][1] != 0 & sum+c[u][1] < best):
        for i in range(len(g[u])):
            if (g[u][i][0]==1): 
                a =g[u][i][1]
        # if(g[u][1][1] != 0 & sum+g[u][1][1] < best):
        #     # best = sum +c[u][1]
        #     best = sum +g[u][1][1]
        if(a != 0 & sum+ a < best):
            
            best = sum +a
            # print(a)
        return
    
    for i in range( len(g[u])):
        v = g[u][i][0]
        w = g[u][i][1]
        if(mark[v]==0):
            mark[v] = 1
            sum += w
            Duyet(x+1,v)
            mark[v] = 0
            sum -= w

Duyet(1,1)
print(best)
'''

'''
# import functools
n, m = [int(x) for x in input().split()]
# c=[[0]*21 for i in range(21)]
sum=0
mark=[0]*21
g=[['null']]*21
best=1e9
#c2 tạo arr add arr rồi add vào g[]
for i in range (m) :
    u, v, w = [int(x) for x in input().split()]
    # g[u].remove('null')#lần chạy thứ 2 k đc
    if(g[u][0]=='null'): g[u].remove('null')
    # g[u].clear() k dc 
    g[u].append((v,w))
    # c[u][v] = w

mark[1]=1
# def comp ( x,y):
#     return x[0] < y[0]

for i in range(1, n+1):
    # sort(g[i].begin(),g[i].end(),cmp)
    # g[i].sort(key=cmop)
    # sorted(g[i], cmp=comp) python 2
    # sorted(g[i], key=cmp_to_key(comp))# cần import
    g[i].sort(key=lambda x: x[1])
# print (g[1].remove('null'))

# x=(1,2)
# y=(0,3)
# print(cmp(x,y))

def Duyet(x, u):
    global sum
    global best
    if (sum >= best): return
    if(x == n) :
        if(g[u][1][1] != 0 & sum+g[u][1][1] < best):
            best = sum +g[u][1][1]
        return
    
    for i in range( len(g[u])):
        v = g[u][i][0]
        w = g[u][i][1]
        if(mark[v]==0):
            mark[v] = 1
            sum += w
            Duyet(x+1,v)
            mark[v] = 0
            sum -= w

Duyet(1,1)
print(best)
'''
