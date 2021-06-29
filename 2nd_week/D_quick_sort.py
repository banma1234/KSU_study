import sys

# 내 코드

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr)//2]
#     less_arr, equal_arr, greater_arr = [], [], []
#     for i in arr:
#         if i < pivot:
#             less_arr.append(i)
#         elif i > pivot:
#             greater_arr.append(i)
#         else:
#             equal_arr.append(i)
#     return quick_sort(less_arr) + equal_arr + quick_sort(greater_arr)



# n = int(sys.stdin.readline())
# arr = []
# for i in range(n):
#     arr.append(int(sys.stdin.readline()))
# for j in quick_sort(arr):
#     print(j)

# 숏코딩

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
for j in sorted(arr):
    print(j)