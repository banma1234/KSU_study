import sys

tcase = int(sys.stdin.readline())
for i in range(tcase):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
