import sys

def centauri(x, y):
    distance = y - x
    count = 1
    while True:
        if count ** 2 <= distance < (count+1) ** 2:
            break
        count+=1
    if count ** 2 == distance:
        return count * 2 - 1
    elif count ** 2 < distance <= count ** 2 + count:
        return count * 2
    else:
        return count * 2 + 1
        

tcase = int(sys.stdin.readline())
for i in range(tcase):
    x, y = map(int, sys.stdin.readline().split())
    print(centauri(x, y))
