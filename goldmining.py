n, l1,l2 = [int(x) for x in input().split()]
sovang = list(map(int, input().split())) 

F=[0]*n
for i in range(0,n):
    F[i]=sovang[i]
    for j in range(max(0,i-l2),max(0,i-l1+1)):
        print(i,j)
        F[i] = max(F[i], F[j] + sovang[i])
        print(F)
print(F)
print(max(F))
