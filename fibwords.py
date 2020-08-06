dayfib=[""]*50
dayfib[0]="0"
dayfib[1]="1"

def preprocessing(i):
    if(dayfib[i]!=""):
        return dayfib[i]
    else:
        dayfib[i]=preprocessing(i-1)+preprocessing(i-2)
        return dayfib[i]
def dem(s,p):
    return s.count(p)
def demn(n,p):
    #với fn>p
    if(c[n]<0):
        c[n]=demn(n-1,p)+demn(n-2,p)+mc[n%2]
    return c[n]
def solution(n,p):
    lp = len(p)
    if (len(preprocessing(n)) < lp) : return 0
    # if(preprocessing(n))
    i=1
    while(len(preprocessing(i-1)) < lp): i+=1
    c[i - 1] = dem (dayfib[i - 1], p)
    # print(i)
    c[i] = dem (dayfib[i], p)
    x = dayfib[i][: (lp - 1)]
    a = dayfib[i-1][ (lp - 1):] #phần tử cuối
    b = dayfib[i][ (lp - 1):] #phần tử cuối
    mc[i % 2] = dem (a + x, p)
    mc[(i+1) % 2] = dem (b + x, p)
    return demn(n,p)
t=1

# k=0
# ketqua=[]
# inp = input().split()
# for i in range(len(inp)//2):
#     n, p = int(inp[2*i]), inp[2*i+1]
#     k+=1
#     c=[-1]*(n+1)#chú ý n+1 lỗi
#     mc=[-1,-1]
#     # ketqua.append(solution(n,p))
#     # ketqua.append(dem(preprocessing(n),p))
#     print("Case {0}: {1}".format(t,solution(n,p)))
#     t+=1
# # print (n)
# # for i in range(k):
# #     print("Case {0}: {1}".format(i+1, ketqua[i]))

k=0
ketqua=[]
while True:
    try:
        n=input()
        #do something
        n=int(n)
        p=input()
        # print(dem("10",p))
        # print(preprocessing(4))
        k+=1
        c=[-1]*(n+2)
        mc=[-1,-1]
        ketqua.append(solution(n,p))
        t+=1
    except EOFError:
        break
for i in range(k):
    print("Case {0}: {1}".format(i+1, ketqua[i]))

# while True:
#     try:
#         n=input()
#         #do something
#         n=int(n)
#         p=input()
#         # print(dem("10",p))
#         # print(preprocessing(4))
#         c=[-1]*(n+2)
#         mc=[-1,-1]
#         print("Case {0}: {1}".format(t,solution(n,p)))
#         t+=1
#     except EOFError:
#         break

    
# while True:
# # while(t==1):
#     n = input()
#     if not n:
#         break
#     n=int(n)
#     p=input()
#     # print(dem("10",p))
#     # print(preprocessing(4))
#     c=[-1]*(n+2)
#     mc=[-1,-1]
#     print("Case {0}: {1}".format(t,solution(n,p)))
#     t+=1


# k=0
# ketqua=[]
# while True:
# # while(t==1):
#     n = input()
#     if not n:
#         break
#     n=int(n)
#     p=input()
#     k+=1
#     # print(dem("10",p))
#     # print(preprocessing(4))
#     c=[-1]*(n+2)
#     mc=[-1,-1]
#     ketqua.append(solution(n,p))
#     t+=1
# for i in range(k):
#     print("Case {0}: {1}".format(i+1, ketqua[i]))


# k=0
# ketqua=[]
# while True:
#     try:
#         n=input()
#         #do something
#         n=int(n)
#         p=input()
#         # print(dem("10",p))
#         # print(preprocessing(4))
#         k+=1
#         c=[-1]*(n+2)
#         mc=[-1,-1]
#         # ketqua.append(dem(preprocessing(n),p))
#         # print(dem(preprocessing(n),p))
#         print("Case {0}: {1}".format(t,solution(n,p)))
#         t+=1
#     except EOFError:
#         break
# # for i in range(k):
# #     print("Case {0}: {1}".format(i+1, ketqua[i]))


# k=0
# ketqua=[]
# while True:
#     n=input()
#     if n:
        
#         #do something
#         n=int(n)
#         p=input()
#         # print(dem("10",p))
#         # print(preprocessing(4))
#         k+=1
#         c=[-1]*(n+2)
#         mc=[-1,-1]
#         ketqua.append(solution(n,p))
#         # print(dem(preprocessing(n),p))
#         # print("Case {0}: {1}".format(t,solution(n,p)))
#         t+=1
#     else:
#         break
# for i in range(k):
#     print("Case {0}: {1}".format(i+1, ketqua[i]))