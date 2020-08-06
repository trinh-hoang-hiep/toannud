test=int(input())
o=test
ketqua=[]
# if(test==0):
#         print("0")
for _ in range(test):
    n=int(input())
    c=int(input())
    if(n % 1000):
        # print("0")
        ketqua.append(0)
        continue
    n //= 1000
    res = 0
    dem = 1

    temp = 5 * 10 ** c
    x = (n-temp)//temp
    if(x > 0):
        res += x
        n -= x * temp
    for i in range(c+1):
        t = n % 10
        n //= 10
        if(t == 1) or ( t == 2 ) or (t == 3 ) or (t == 5):
            res=res+1
        if( t == 4) or (t == 6):
            res += 2
            dem*=2
        if( t == 7) or (t == 8):
            res += 2
        if( t == 9):
            res += 3
            dem *= 3
    # print(str(res) + " " + str(dem) + '\n')
    tup=(res,dem)
    ketqua.append(tup)

# if(ketqua!=[]): c2
# if((not ketqua)==False):
for i in range(o):
    # print("Case #{0}: {1}".format(i+1, ketqua[i]))
    if(ketqua[i]==0):
        print(0)
    else:
        print(str(ketqua[i][0]) + " " + str(ketqua[i][1]))

# Yes: if not seq:
#      if seq:

# No:  if len(seq):
#      if not len(seq): 
#sai là do 
# 1
# 100000
# 1
# 2.0 1
#run time là đang chạy nó ra lỗi