# import numpy as np
queue=[]
a, b, c = [int(x) for x in input().split()] 
dosau=0
# luuvet = np.zeros((200,200), dtype=int)
luuvet = [[0 for x in range(1000)] for y in range(1000)]
flag=0
class statewa:
    # nuoc=(0,0)
    # global dosau
    # nuoc=(0,0)
    def __init__(self,nuoc):
        self.nuoc=nuoc

    def state1(self) :#phai co ()
        # global dosau 
        # dosau+=1
        self.nuoc=(0,self.nuoc[1])#đổ nước bình 1 đi
    def state2(self):
        self.nuoc=(self.nuoc[0],0)
    def state3(self):
        self.nuoc=(a,self.nuoc[1])
    def state4(self):
        self.nuoc=(self.nuoc[0],b)
    def state5(self):
        self.nuoc=(self.nuoc[0]-min(self.nuoc[0],b-self.nuoc[1]),self.nuoc[1]+min(self.nuoc[0],b-self.nuoc[1]))
    def state6(self):
        self.nuoc=(self.nuoc[0]+min(a-self.nuoc[0],self.nuoc[1]), self.nuoc[1]-min(a-self.nuoc[0],self.nuoc[1]))

t=statewa((0,0))
luuvet[0][0]=0
# t.state3()
# print(t.nuoc)
# print(dosau)
queue.append(t.nuoc)
while(len(queue)!=0):
    temp=queue.pop(0)#temp=queue.pop() là dfs
    # print(temp)
    if((temp[0]==c)|(temp[1] ==c)):
        m=temp[0]
        n=temp[1]
        print(luuvet[m][n])
        # global flag
        flag=1
        # print("thay r")
        break
    
    # dosau+=1 k đc vì đi hết cây này sang cây khác độ sâu bị anh huong
    # dosau=luuvet[temp[0]][temp[1]]+1
    tt=statewa(temp)
    tt.state1()
    # print(1)
    next =tt.nuoc
    if ((luuvet[next[0]][next[1]]==0)&(next[0]+next[1]!=0)):
        queue.append(next)
        
        # luuvet[next[0]][next[1]]=dosau
        luuvet[next[0]][next[1]]=luuvet[temp[0]][temp[1]]+1
        # print(next)
    
    tt=statewa(temp)
    tt.state2()
    # print(2)
    next =tt.nuoc
    if ((luuvet[next[0]][next[1]]==0)&(next[0]+next[1]!=0)):
        queue.append(next)
        # luuvet[next[0]][next[1]]=dosau
        luuvet[next[0]][next[1]]=luuvet[temp[0]][temp[1]]+1
        # print(next)
    tt=statewa(temp)
    tt.state3()
    next =tt.nuoc
    # print(next)
    if ((luuvet[next[0]][next[1]]==0)&(next[0]+next[1]!=0)):
        queue.append(next)
        # luuvet[next[0]][next[1]]=dosau
        luuvet[next[0]][next[1]]=luuvet[temp[0]][temp[1]]+1
        # print(3)
        # print(next)
    tt=statewa(temp)
    tt.state4()
    next =tt.nuoc
    if ((luuvet[next[0]][next[1]]==0)&(next[0]+next[1]!=0)):
        queue.append(next)
        # luuvet[next[0]][next[1]]=dosau
        luuvet[next[0]][next[1]]=luuvet[temp[0]][temp[1]]+1
        # print(next)
    tt=statewa(temp)
    tt.state5()
    next =tt.nuoc
    if ((luuvet[next[0]][next[1]]==0)&(next[0]+next[1]!=0)):
        queue.append(next)
        # luuvet[next[0]][next[1]]=dosau
        luuvet[next[0]][next[1]]=luuvet[temp[0]][temp[1]]+1
        # print(next)
    tt=statewa(temp)
    tt.state6()
    next =tt.nuoc
    if ((luuvet[next[0]][next[1]]==0)&(next[0]+next[1]!=0)):
        queue.append(next)
        # luuvet[next[0]][next[1]]=dosau
        luuvet[next[0]][next[1]]=luuvet[temp[0]][temp[1]]+1
        # print(next)
    
if(flag==0): print("khong tim thay")
# print(temp)