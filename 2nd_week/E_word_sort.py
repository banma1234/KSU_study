import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(input())
arr = list(set(arr))
arr.sort(key = lambda x : (len(x), x))
for j in arr:
    print(j)
