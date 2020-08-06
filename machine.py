n=int(input())
a=[]
# d=[0]*n
f=[-1]*n
# stack=[]
maxx=-1
for i in range(n):
    entries = tuple(map(int, input().split())) 
    a.append(entries)
# #cách 1 2 vòng for 20 điểm
# for i in range(n):
#     for j in range(i,n):
#         if(i!=j):
#             if((a[i][0]>a[j][1])|(a[i][1]<a[j][0])):
#                 c=a[i][1]-a[i][0]+a[j][1]-a[j][0]
#                 maxx=max(maxx,c)
# print(maxx)

# def Try(x):
#     if(x<0): return 0
    
#     if(f[x]<0):
#         tmp=0
#         for i in range(x,n):
#             if((a[i][0]>a[x][1])|(a[i][1]<a[x][0])):
                
                
#                 tmp=max(tmp,Try(i))
                
#         f[x]=tmp+a[x][1]-a[x][0]
#     return f[x]
# for i in range(n):
#     maxx=max(maxx,Try(i))
# print(maxx)


# l=[-1]*n
# for i in range(n):
#     l[i]=a[i][1]-a[i][0]
#     for j in range(0,i):      
#         if((a[i][0]>a[j][1])|(a[i][1]<a[j][0])):            
#             l[i]=max(l[i],l[j]+a[i][1]-a[i][0])
# print(max(l))

# def check(i,x):
#     if((a[i][0]>a[j][1])|(a[i][1]<a[j][0])):
#         return true
def Try(x):
    if(x ==0): 
        f[x]=a[0][1]-a[0][0]
        
    print(x)
    if(f[x]<0):
        tmp=a[x][1]-a[x][0]
        for i in range(x):
            if((a[i][0]>a[x][1])|(a[i][1]<a[x][0])):
                tmp=max(tmp,Try(i)+a[x][1]-a[x][0])
                
        f[x]=tmp
    return f[x]

Try(n-1)
print(max(f))