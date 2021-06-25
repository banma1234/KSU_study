case = int(input())
for i in range(case):
    arr = list(map(int, input().split()))
    avg = sum(arr[1:])/arr[0]
    count = 0
    for j in arr[1:]:
        if j > avg:
            count+=1
    print("%.3f%%"%((count/arr[0])*100))