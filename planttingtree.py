n= int(input())
songay = list(map(int, input().split())) 
songay.sort(reverse=True)
res=0
songay.insert(0,res)
for i in range(1,n+1):
    res=max(res,i+songay[i]+1)
print(res)