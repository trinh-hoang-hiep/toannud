# n=int(input())
# sum=0
# entries = list(map(int, input().split())) 
# for i in range(n):
#     sum+=entries[i]
# print(sum%int((1e9+7)))

#c2
# sum=0
# # x = [int(x) for x in input().split()] 
# for x in input().split():
#     sum+=int(x)
# print(sum)

# #tttttffffff chia de tri
# a, b = [int(x) for x in input().split()]
# mod=int((1e9+7))
# def sumo( x,y ):
#     # if(y==1): return  x % mod
#     if(y==0): return  1
    
#     # t=sumo(x, int(y/2))
#     # t=(t*t)% mod
#     # if(y%2): return (t*x)% mod
#     # return t

#     if (y%2): return (x*sumo(x, y-1))%mod
#     t=sumo(x, int(y/2))
#     return((t*t)% mod)
# print(sumo(a,b))

#subseq quy hoach dong kiem tra tk cuoi
mark=[0]*1000
mem=[0]*1000 #luu kq
n=int(input())
arr = list(map(int, input().split()))
def sumax(i):
    if(i==0):return arr[0]
    if(mark[i]): return mem[i]
    mem[i]=max(arr[i],arr[i]+sumax(i-1))
    mark[i]=1
    return mem[i]
ress=arr[0]
# for i in range(n):
ress=max(ress,sumax(n-1))
print(ress)



# # mem=[0]*1000 #luu kq
# n=int(input())
# arr = list(map(int, input().split()))
 
# def sumax(n, arr):
 
#     #mark la day luu cac subsequence lon nhat, voi dieu kien mark[i] la subsequence lon nhat co phan tu ket thuc la arr[i]
#  #cái kiểm tra là cái số tiếp theo trong dãy mà
# 	mark = [0 for _ in range(n)]
# 	res = mark[0] = arr[0]
# 	for i in range(1, n, 1):
# 		if mark[i-1] > 0:
# 			mark[i] = mark[i-1] + arr[i]
# 		else:
# 			mark[i] = arr[i]
# 		#print(mark[i])
# 		#res bang so lon nhat trong day mark
# 		if mark[i] > res:
# 			res = mark[i]
# 	return res
 
# res=sumax(n, arr)
 
# print(res)
'''
bai c
n, m, M = input().split()
n = int(n)
m = int(m)
M = int(M)
arr = list(map(int, input().split()))
def check_subseq(sum_array):
    if sum_array>=m and sum_array<=M:
        return True
    return False

def bound_subseq(arr):
    sum_array = 0
    count = 0
    for i in range(n-1):
        sum_array = arr[i]
        if check_subseq(sum_array):
            count += 1
        for j in range(i+1, n):
            sum_array += arr[j]
            if check_subseq(sum_array):
                count += 1
        
    if check_subseq(arr[-1]):
        count += 1
    return count
                    
print(bound_subseq(arr))
'''