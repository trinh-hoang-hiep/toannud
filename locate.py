
# import numpy as np
test=int(input())
 
# n, m = map(int, input().split())
# x, y = input(),  input() 
map1=[]
map2=[]
# dem = [[0 for x in range(20001)] for y in range(20001)]
# dem = [[0]*2001 for i in range(2001)]

while (test>0):
    n, m = [int(x) for x in input().split()] 
    dem = [[0]*(2*m+1) for i in range(2*n+1)]
    for i in range (n):
        entries = list(map(int, input().split())) #######
        for j in range(m):
            if(entries[j]==1): map1.append((i,j))
        #######
        # k=0
        # for x in input().split():
        #     if(x==1):map1.append((i,k))
        #     k+=1
        
    # if ((0*(1,2))==()): print ("ok") numpy reshape ......
    # print(map1)
    for i in range (n):
        entries = list(map(int, input().split())) 
        for j in range(m):
            if(entries[j]==1): map2.append((i,j))

    for i in range(len(map1)):
        for j in range(len(map2)):
            dem[map1[i][0]-map2[j][0]+m][map1[i][1]-map2[j][1]+m] +=1

    # print(count_nonzero(dem==1))
    # print(np.max(dem))
    print(max(max(x) for x in dem))
    # print(max(max(dem))) sai
    # map(max, dem)
    # list(map(max, dem))
    # print(max(map(max, dem)))
    test-=1

# so=int(input())
# entries = list(map(int, input().split())) 
# # for i in range (so):
# #     arr.append(entries[i])
# entries.sort()
# # print(entries)
# # arr=[]1
# # for i in range (so):1
# #     arr.append(entries[i])1
# # print(arr)1
# # arr[7][8]=2
# # print(max(max(x) for x in arr))
# for i in range (so):
#     print(entries[i], end=" ")