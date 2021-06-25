arr = list(range(1,10001))
temp = []
for i in arr[0:]:
    for j in str(i):
        i+=int(j)
    if i<=10000:
        temp.append(i)

for num in arr[0:]:
    if num not in temp:
        print(num)