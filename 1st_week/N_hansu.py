def hansu(num):
    if num<100:
        return num
    elif 100<=num<=1000:
        count = 99
        for i in range(100,num+1):
            arr = list(map(int, str(i)))
            if arr[2] - arr[1] == arr[1] - arr[0]:
                count += 1
        return count

n = int(input())
print(hansu(n))