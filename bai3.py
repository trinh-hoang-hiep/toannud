n, m,mm = [int(x) for x in input().split()]
# print(mm)
a = list(map(int, input().split()))
sum=0
dem=0
for i in range(n):
    # sum=0
    for j in range(i):
        # print(i,j)
        sum=0
        for k in range(j,i+1):
            sum+=a[k]
        # print(sum)
        if((sum<=mm) & (sum>=m)):
            dem+=1
for i in range(n):
    if((a[i]<=mm) & (a[i]>=m)):
        dem+=1
print(dem)

n, m,mm = [int(x) for x in input().split()]
# print(mm)
a = list(map(int, input().split()))
sum=0
dem=0
for i in range(n):
    sum=0
    for j in range(i,n):
        # print(i,j)
        # sum=0
        sum+=a[j]
        # print(sum)
        if((sum<(mm+1)) & (sum> (m-1))):
            dem+=1
# for i in range(n):
#     if((a[i]<(mm+1)) & (a[i]> (m-1))):
#         dem+=1
print(dem)




n, m,mm = [int(x) for x in input().split()]
# print(mm)
a = list(map(int, input().split()))
sum=0
dem=0
for i in range(n):
    sum=0
    for j in range(i,n):
        # # print(i,j)
        # sum=0
        # for k in range(j,i+1):
        #     sum+=a[k]
        # # print(sum)
        sum+=a[j]
        if((sum<=mm) & (sum>=m)):
            dem+=1
# for i in range(n):
#     if((a[i]<=mm) & (a[i]>=m)):
#         dem+=1
print(dem)



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