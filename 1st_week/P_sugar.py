def deliver(num):
    count = 0
    while(True):
        if num%5 == 0:
            return count + num//5
        num-=3
        count+=1
        if num<0:
            return -1

num = int(input())
print(deliver(num))