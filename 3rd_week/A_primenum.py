import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
count = 0
for i in arr:
    flag = True
    if i > 1:
        for j in range(2, i):
            if i%j == 0:
                flag = False
                continue
        if flag:
            count += 1
print(count)
