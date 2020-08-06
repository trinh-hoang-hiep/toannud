n=int(input())
d= list(map(int, input().split()))
mark=[0]*n
day=0
d.sort(reverse=True)
# print(d)
# print(3)
for i in range(n):
    for j in range(i+1,n):
        if((mark[i]==0)&(mark[j]==0)&(d[i]+d[j]<=6)):    
            # print(i,0,j)
            # print((d[i],d[j]))
            day+=1
            mark[i]=1
            mark[j]=1
                #shift tab
    if(mark[i]==0):
        # print(d[i])
        day+=1
        mark[i]=1
           
print(day)
            
#chieesm maast thawfng bes nhaast