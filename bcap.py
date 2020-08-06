n, m = [int(x) for x in input().split()]
giatri=0
sotinchi = list(map(int, input().split())) 
sotinchi.insert(0, giatri)
# print(sotinchi)
A=[]
for i in range(n):
    rb = list(map(int, input().split())) 
    rb.insert(0,giatri)
    A.append(rb)
nhonhat=10000000000
# sotinmotky=[0 for _ in range(m+1)]
sotinmotky=[0]*(m+1)
chonkychomon=[0]*(n+1)
def check( v, k):#kỳ v môn k
    for i in range(1,k):
        if(A[i][k]== 1):#nếu môn i là tiên quyết của k
            if(chonkychomon[i]>=v): return False
    return True
def solution():
    global nhonhat
    # max_load = 0
    # for j in sotinmotky:
    #     if(max_load < j): max_load = j
    c=max(sotinmotky)
    if(c<nhonhat) : nhonhat = c


def TRY( k):
    for v in range(1,m+1):
        if(check(v,k)&(sotinmotky[v] + sotinchi[k] <nhonhat )):#check them
            chonkychomon[k]=v
            sotinmotky[v]+=sotinchi[k]
            if(k==n): solution()
            else:
                if (max(sotinmotky)<nhonhat):TRY(k+1) #nhánh cận
            sotinmotky[v]-=sotinchi[k]
TRY(1)
print(nhonhat)