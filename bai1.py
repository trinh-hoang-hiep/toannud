test=int(input())
o=test
ketqua=[]
while(test>0):
    n=int(input())
    a = list(map(int, input().split()))
    b=list(map(int, input().split()))
    a.sort()
    b.sort(reverse=True)
    summ=0
    for i in range(n):
        summ+=a[i]*b[i]
    ketqua.append(summ)
    test-=1

for i in range(o):
    print("Case #{0}: {1}".format(i+1, ketqua[i]))



test=int(input())
o=test
ketqua=[]
while(test>0):
    n=int(input())
    a = list(map(int, input().split()))
    b=list(map(int, input().split()))
    # print (b)
    d=[0]*n
    mini=100000000
    mang=[0]*n
    def Try( k) :
        global mini
        for i in range(n):
            if (d[i]==0):
                mang[k] = b[i]
                d[i] = 1
                if (k==n-1): 
                    # ab = [a[i]*mang[i] for i in range(n)]
                    # print(mang)
                    sum=0
                    for j in range(n):
                        sum+=a[j]*mang[j]
                    mini=min(sum, mini)
                    # print(mini)
                else: Try(k +1)
                d[i] = 0
            
    Try(0)
    # print(mini)
    ketqua.append(mini)
    test-=1

for i in range(o):
    print("Case #{0}: {1}".format(i+1, ketqua[i]))


# def msp(v1, v2):
#     return sum([x * y for x, y in zip(sorted(v1), sorted(v2, reverse=True))])
 
# if __name__=='__main__':
#     case = []
#     num_case = int(input())
 
#     for i in range(num_case):
#         input()
#         v1 = [int(k) for k in input().split()]
#         v2 = [int(k) for k in input().split()]
#         case.append([v1,v2])
#     result = [msp(v[0], v[1]) for v in case]
#     for i, r in zip(range(num_case), result):
#         print("Case #{}: {}".format(i+1,r))



def min_scalar_product(v1, v2):
    return sum([x * y for x, y in zip(sorted(v1), sorted(v2, reverse=True))])
def main():
    from sys import stdin, stdout
    T = int(stdin.readline())
    
    for t in range(T):
        n = int(stdin.readline())
        X = list(map(int, stdin.readline().split()))
        Y = list(map(int, stdin.readline().split()))
    
        tmp = min_scalar_product(X, Y)
        stdout.write("Case #" + str(t+1) + ": " + str(tmp) + "\n")
 
if __name__ == "__main__":
    main()
    

# #include<bits/stdc++.h>
# using namespace std;
# int T;
# int n;
# long long x[1000],y[1000];
 
 
# int main(){
# 	cin >> T;
# 	long long res[T];
# 	for(int i = 0; i<T; i++){
# 		cin >> n; 
# 		for(int j = 0; j<n; j++){
# 			cin >> x[j];
# 		}
# 		for(int j = 0; j<n; j++){
# 			cin >> y[j];
# 		}
# 		sort(x,x+n);
# 		sort(y,y+n);
# 		long long sum = 0;
# 		for(int k = 0; k<n; k++){
# 			sum += x[k]*y[n-1-k];
# 		}
# 		res[i] = sum;
		
# 	}
# 	for(int i = 0; i<T; i++){
# 		cout << "Case #" << (i+1) << ": " << res[i] << '\n';
# 	}
	
	
# 	return 0;
# }



# T = int(input())
 
# matrix = []
# for i in range(3 * T):
#     arr = list(map(int, input().split()))
#     matrix.append(arr)
 
# matrix = [matrix[3*i:(3*i+3)] for i in range(T)]
 
    
# def scalar(test):
#     min_value = 0
#     x_array = test[1]
#     y_array = test[2]
#     x_array.sort()
#     y_array.sort()
#     y_array = y_array[::-1]
#     for i in range(len(x_array)):
#         min_value += x_array[i] * y_array[i]
#     return min_value
         
# if __name__=='__main__':
#     for i in range(T):
#         print('Case #{}:'.format(i+1), scalar(matrix[i]))




# def compute_minimun_value(n, vector1, vector2):
#     min_val = 0
#     vector1.sort()
#     vector2.sort()
#     for i in range(n):
#         min_val += vector1[i] * vector2[n - i - 1]
#     return min_val
 
 
# if __name__ == '__main__':
#     number_test = int(input())
#     data_input = []
#     for i in range(number_test):
#         num_direction = int(input())
#         test = [num_direction]
#         vector1 = input()
#         vector2 = input()
#         vector_1 = [int(x) for x in vector1.split()]
#         vector_2 = [int(y) for y in vector2.split()]
#         test.append(vector_1)
#         test.append(vector_2)
#         data_input.append(test)
 
#     for i in range(number_test):
#         # print(data_input[i])
#         test = data_input[i]
#         print("Case #{index}: {value}".format(index=i + 1, value=compute_minimun_value(test[0], test[1], test[2])))



# def insertionSort(arr):
#     # Traverse through 1 to len(arr)
#     for i in range(1, len(arr)):
 
#         key = arr[i]
 
#         # Move elements of arr[0..i-1], that are
#         # greater than key, to one position ahead
#         # of their current position
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
 
# testCases = []
# test_number = int(input())
# for i in range (test_number):
#     testCase = []
#     n = int(input())
#     testCase.append(n)
#     A = input()
#     B = input()
#     arrayA = A.split(" ")
#     arrayB = B.split(" ")
#     intarrayA = []
#     intarrayb = []
#     for number in arrayA:
#         intarrayA.append(int(number))
#     for number in arrayB:
#         intarrayb.append(int(number))
#     testCase.append(intarrayA)
#     testCase.append(intarrayb)
#     testCases.append(testCase)
 
# for i in range(test_number):
#     n= testCases[i][0]
#     A = testCases[i][1]
#     B = testCases[i][2]
#     insertionSort(A)
#     insertionSort(B)
#     B.reverse()
#     sum = 0
#     for j in range(n):
#         sum = sum+A[j]*B[j]
#     print("Case #"+str(i+1)+": "+str(sum))

