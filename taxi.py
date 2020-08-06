n = int(input())
k=1
c=[[0]*23 for i in range(23)]
mark=[0 for i in range(23)]
soluongkhach, canhnhonhat, tong = 0, 1e9,0
best=1e9
sodinh= 2*n+1
for i in range(sodinh):
    entries = list(map(int, input().split())) 
    for j in range(sodinh):
        c[i][j]=entries[j]
        if(c[i][j]!=0): canhnhonhat=min(canhnhonhat,c[i][j])



def Duyet( x, y):#x số thành phố, y là tên thành phố
    global soluongkhach
    global tong
    global best
    for  i in range(1,2*n+1):# có thể tách thành 2 vòng for cho chạy nhanh
        if(i<=n):
            if((soluongkhach <k)):#bắt đầu đón khách
                if(mark[i]==0):
                    soluongkhach+=1
                    mark[i] = 1#khách lên xe
                    tong+=c[y][i]# đi từ y đến i
                    if(tong + (sodinh-x)*canhnhonhat < best):
                        Duyet(x+1,i)#di tiếp từ thành phố i
                    tong-=c[y][i]#bỏ đường; đi đường khác
                    mark[i] = 0
                    soluongkhach-=1
    
        else:#trả khách
            if((mark[i]==0) & (mark[i-n]==1)):#có khách và chưa trả
                soluongkhach-=1
                mark[i] = 1
                tong+=c[y][i]#đến trả khách
                if(x ==  2*n) :#điểm cuối
                    best = min(best,tong+c[i][0])#cập nhật
                
                if(tong + (sodinh-x)*canhnhonhat < best):
                    Duyet(x+1,i)
                tong-=c[y][i]
                mark[i] = 0
                soluongkhach+=1


Duyet(1,0)
print(best)

# print(canhnhonhat)