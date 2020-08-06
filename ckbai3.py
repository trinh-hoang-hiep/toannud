string=input()
k=int(input())
lst=list(string)
num=list(map(ord, lst))
n=len(lst)


# ketqua=[]
# # print(num)
# F=[0]*n
# for i in range(n-1,-1,-1):
#     # if(F[i]==0):F[i]=num[i]
#     for j in range(n-i):
#         # print(i,j)
#         F[i] = max(num[i], num[j] )
#         # print(F)
dem=0
s=''
def laptimmax(x,y):
    num2=[0]*n
    global dem,s
    dem+=1
    if (dem>k): return
    # print(x,y)
    for i in range(x,y+1):
        # print(x,y)
        num2[i]=num[i]
    # print(num2)
    tmp=max(num2)
    s+=chr(tmp)
    # print(ind)
    laptimmax(num2.index(tmp)+1,y+1)
laptimmax(0,n-k)
print(s)

# tmp=0
# s=''
# for i in range(k+1):
#     # print(F)
#     if(max(F)==tmp):
#         id=F.index(tmp)
#         F.pop(id)
#     else:
#         tmp=max(F)
#         s+=chr(tmp)
#         # print(tmp)
#         id=F.index(tmp)
#         F.pop(id)


# print(s)























# # print(s)


# def laptimmax(x,y):
#     for i in range(x,y+1):
#         print(x,y)
#         num2[i]=num[i]
#     return(max(num2))
# # duyet=-1
# # for i in range(k-1,-1,-1):
# #     tmp= laptimmax(duyet+1,n-i-1-duyet)
# #     print(tmp)
# #     ketqua.append(tmp)
# #     duyet=num.index(tmp)
# #     print(duyet)

# # print(ketqua)