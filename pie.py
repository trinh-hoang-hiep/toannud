test=int(input())
o=test
ketqua=[]
while (test>0):
    n, f = [int(x) for x in input().split()]
    rarr= list(map(int, input().split())) 
    rarr.sort()
    pi= 3.14159265358979323846264338327950288
    lo=0.0
    hi= pi*(rarr[n-1]**2)
    for j in range(50): #từ 30 thì sai test 2 đc 50; lên 50 thì đúng đc 100
        mi = (lo + hi) / 2
        count = 0

        for i in range(n-1,-1,-1):
            if (count <=f):
                count += int ( pi * rarr[i]*rarr[i] / mi )

        if( count > f): lo = mi
        else: hi = mi

    # print("{0:.6f}".format(mi))
    ketqua.append(mi)
    test-=1
for i in range(o):
    print("{0:.6f}".format( ketqua[i]))