import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
set_arr = sorted(list(set(arr)))
dic = {set_arr[i] : i for i in range(len(set_arr))}
# 리스트를 이용하면 각 과정마다 반복하며 탐색해야 딕셔너리를 사용해 시간초과를 방지한다.

for i in arr:
    print(dic[i], end = ' ')