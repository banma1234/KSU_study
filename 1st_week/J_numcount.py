# 내코드

a = int(input())
b = int(input())
c = int(input())

res = list(str(a*b*c))
arr = [0,0,0,0,0,0,0,0,0,0]
for i in res[0:]:
    for j in range(10):
        if j==int(i):
            arr[j]+=1
for k in range(10):
    print(arr[k])
    
#===========================================

# 숏코딩
# a = int(input())
# b = int(input())
# c = int(input())

# result = list(str(a * b * c))
# for i in range(10):
#     print(result.count(str(i)))
