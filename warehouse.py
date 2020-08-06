n, t,d = [int(x) for x in input().split()]
sovang = list(map(int, input().split())) 
thoigian=list(map(int, input().split())) 
# F=[0]*3
F=[[0]*t for i in range(n)]
for i in range(0,n):
    for  k in range(thoigian[i], t):

        F[i][k]=sovang[i]
        for j in range(i-d,i-1+1):
            print(i,j)
            F[i][k] = max(F[i][k], F[j][k] + sovang[i])
            print(F)
print(F)
print(max(max(x) for x in F))