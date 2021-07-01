import math
import sys

# def prime_3(n):
#     if n ==1 :
#         return False
    
#     num = int(math.sqrt(n))
#     for i in range(2, num+1):
#         if n % i == 0 :
#             return False
#     return True

# n, m = map(int, input().split())
# for i in range(n, m+1):
#     if prime_3(i):
#         print(i)

# ================================================================

m, n = map(int, sys.stdin.readline().split())

prime_list = [True] * (n + 1)
num = int(math.sqrt(n))

for i in range(2, num + 1):
    if prime_list[i]:
        for j in range(i*2, n + 1, i):
            prime_list[j] = False


arr = [i for i in range(2, n + 1) if prime_list[i] == True]

for i in range(len(arr)):
    if arr[i] >= m:
        print(arr[i])