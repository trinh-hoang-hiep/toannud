import math  

matranx=[[191,131,53],[185,134,50],[200,137,52],[173,127,50],[171,128,49],[160,118,47],[188,134,54],[186,129,51]]
d=[[0]*8 for i in range(8)]
for i in range(8):
    for j in range (8):
        a=[0,0,0]
        for k in range(3):
            a[k]=matranx[i][k]-matranx[j][k]
        for m in range(3):
            d[i][j]+=a[m]*a[m] 
        d[i][j]= math.sqrt(d[i][j])
print(d)