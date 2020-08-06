n, m = [int(x) for x in input().split()]
c=[[0]*21 for i in range(21)]
sum=0
mark=[0]*21
best=1000000000
canhnhonhat=1000000000
for i in range (m) :
    
    u, v, w = [int(x) for x in input().split()]
    c[u][v] = w
    if((w!=0)&(canhnhonhat>w)):#phải ngoặc lại
        canhnhonhat=w 
        # print(canhnhonhat)
mark[1]=1
# print(canhnhonhat)


def Duyet( x, u):

    global sum
    global best
    if (sum >= best): return #nhánh cận
    if(x == n) :
        if(c[u][1] != 0 & sum+c[u][1] < best):
            best = sum +c[u][1]
        return

    for i in range( 2,n+1):#nên thông minh hơn
        w=c[u][i]
        # print(w)
        if(mark[i]==0):
            mark[i] = 1
            sum += w
            if(sum+(n-x)*canhnhonhat<best):Duyet(x+1,i)#đi vào và duyệt tk tiếp
            mark[i] = 0
            sum -= w
Duyet(1,1)
print(best)

