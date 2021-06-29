import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(str, sys.stdin.readline().split())))
arr.sort(key = lambda x : int(x[0]))    # 나이를 int형으로 바꿔줘야 정렬이 완벽히 된다.
for i in arr:
    print(i[0], i[1])