import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr=[]

for i in range(n,m+1):
    if i==1:
        continue
    elif i==2:
        arr.append(i)
    else:
        for j in range(2, i):
            if i%j==0:
                break
            elif j==i-1:
                arr.append(i)
if len(arr)==0:
    print('-1')
else:
    print(sum(arr))
    print(min(arr))
